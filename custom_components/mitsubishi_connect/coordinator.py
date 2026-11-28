"""DataUpdateCoordinator for Mitsubishi Connect."""

from __future__ import annotations

import asyncio
import logging
import random
import time
from dataclasses import dataclass, field
from datetime import timedelta
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed, HomeAssistantError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import MitsubishiApiClient, MitsubishiApiError, MitsubishiAuthError
from .const import (
    CONF_PIN,
    CONF_SCAN_INTERVAL,
    CONF_TEMP_UNIT,
    DEFAULT_SCAN_INTERVAL_MINUTES,
    DOMAIN,
    FORCE_REFRESH_COOLDOWN_SECONDS,
    MIN_SCAN_INTERVAL_MINUTES,
)

_LOGGER = logging.getLogger(__name__)


@dataclass
class VehicleState:
    """In-memory snapshot and control state for a single vehicle."""

    vin: str
    internal_vin: str | None
    info: dict[str, Any]
    vsr: dict[str, Any] = field(default_factory=dict)
    engine: dict[str, Any] = field(default_factory=dict)
    location: dict[str, Any] = field(default_factory=dict)
    # PHEV/EV charge state (empty for gas vehicles)
    is_phev: bool = False
    charge: dict[str, Any] = field(default_factory=dict)
    # Optimistic lock state when VSR does not expose lockStatus
    optimistic_locked: bool | None = None
    # User-selected pre-conditioning options for remote engine start
    target_temperature: float = 21.0
    temperature_unit: str = "C"
    front_defrost: bool = False
    rear_defrost: bool = False
    steering_heater: bool = False
    # Cooldown tracker for active vehicle wake (refreshVSR)
    last_force_refresh_monotonic: float = 0.0


# Powertrain hints from the vehicle list. Charge entities are created only when
# the vehicle is clearly electric, so gas vehicles are never queried for charge.
_EV_VEHICLE_TYPES = {"phev", "bev", "ev", "hev", "electric", "hybrid"}
_ICE_VEHICLE_TYPES = {"ice", "cv", "gas", "mpi", "diesel", "petrol"}


def _detect_phev(info: dict[str, Any]) -> bool:
    vehicle_type = str(info.get("vehicleType") or "").strip().lower()
    if vehicle_type in _EV_VEHICLE_TYPES:
        return True
    if vehicle_type in _ICE_VEHICLE_TYPES:
        return False
    # Unknown or missing: stay conservative and treat as non-PHEV
    return False


class MitsubishiConnectCoordinator(DataUpdateCoordinator[dict[str, VehicleState]]):
    """Conservative cloud-polling coordinator for Mitsubishi Connect.

    Only fetches server-cached VSR + engine status during scheduled polls (never wakes
    the vehicle automatically). Active wake (`refreshVSR`) is strictly manual and
    rate-limited to once every 10 minutes.
    """

    def __init__(
        self,
        hass: HomeAssistant,
        entry: ConfigEntry,
        api: MitsubishiApiClient,
    ) -> None:
        self.entry = entry
        self.api = api
        self._cmd_locks: dict[str, asyncio.Lock] = {}
        self._first_poll = True

        minutes = max(
            MIN_SCAN_INTERVAL_MINUTES,
            int(
                entry.options.get(
                    CONF_SCAN_INTERVAL,
                    entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL_MINUTES),
                )
            ),
        )
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_{entry.entry_id}",
            update_interval=timedelta(minutes=minutes),
        )

    @property
    def pin(self) -> str | None:
        val = self.entry.options.get(CONF_PIN, self.entry.data.get(CONF_PIN))
        return str(val).strip() if val else None

    @property
    def default_temp_unit(self) -> str:
        return str(
            self.entry.options.get(
                CONF_TEMP_UNIT, self.entry.data.get(CONF_TEMP_UNIT, "C")
            )
        ).upper()

    def _lock_for(self, vin: str) -> asyncio.Lock:
        if vin not in self._cmd_locks:
            self._cmd_locks[vin] = asyncio.Lock()
        return self._cmd_locks[vin]

    async def _async_update_data(self) -> dict[str, VehicleState]:
        # Small random jitter on background polls to avoid robotic exact-second spikes
        if not self._first_poll:
            await asyncio.sleep(random.uniform(1.0, 12.0))
        self._first_poll = False

        try:
            vehicles = await self.api.get_vehicles()
            prev_data = self.data or {}
            result: dict[str, VehicleState] = {}

            for v in vehicles:
                vin = v.get("vin")
                if not vin:
                    continue
                internal_vin = v.get("internalVin")
                vsr, engine = await asyncio.gather(
                    self.api.get_vsr(vin, internal_vin),
                    self.api.get_engine_details(vin, internal_vin),
                )
                is_phev = _detect_phev(v)
                charge: dict[str, Any] = {}
                if is_phev:
                    try:
                        charge = await self.api.get_charge_details(vin, internal_vin) or {}
                    except MitsubishiApiError:
                        charge = {}
                prev = prev_data.get(vin)
                if prev is not None:
                    state = prev
                    state.info = v
                    state.internal_vin = internal_vin
                    state.vsr = vsr or {}
                    state.engine = engine or {}
                    state.is_phev = is_phev
                    state.charge = charge
                else:
                    eng_temp = (engine or {}).get("targetTemperature")
                    eng_unit = (engine or {}).get("temperatureUnit") or self.default_temp_unit
                    hvac = (engine or {}).get("hvacSettings") or {}
                    state = VehicleState(
                        vin=vin,
                        internal_vin=internal_vin,
                        info=v,
                        vsr=vsr or {},
                        engine=engine or {},
                        target_temperature=float(eng_temp) if eng_temp is not None else 21.0,
                        temperature_unit=str(eng_unit).upper(),
                        front_defrost=bool(hvac.get("frontDefrostStatus")),
                        rear_defrost=bool(hvac.get("rearDefrostStatus")),
                        steering_heater=bool(hvac.get("steeringHeaterStatus")),
                        is_phev=is_phev,
                        charge=charge,
                    )
                result[vin] = state

            return result
        except MitsubishiAuthError as err:
            # Stop polling immediately and ask the user to reauthenticate
            raise ConfigEntryAuthFailed(str(err)) from err
        except MitsubishiApiError as err:
            raise UpdateFailed(f"Mitsubishi Connect API error: {err}") from err
        except Exception as err:  # noqa: BLE001
            raise UpdateFailed(f"Unexpected error communicating with Mitsubishi Connect: {err}") from err

    def _require_pin(self) -> str:
        if not self.pin:
            raise HomeAssistantError(
                "A 4-digit Mitsubishi Connect PIN is required for this action. "
                "Configure it in the Mitsubishi Connect integration options."
            )
        return self.pin

    # ------------------------------------------------------------------
    # Remote Commands (serialized per vehicle)
    # ------------------------------------------------------------------

    async def async_lock_doors(self, vin: str) -> None:
        state = self.data[vin]
        async with self._lock_for(vin):
            try:
                await self.api.lock_door(vin, pin=self.pin, internal_vin=state.internal_vin)
                state.optimistic_locked = True
                self.async_set_updated_data(self.data)
            except MitsubishiAuthError as err:
                raise ConfigEntryAuthFailed(str(err)) from err
            except MitsubishiApiError as err:
                raise HomeAssistantError(f"Failed to lock doors: {err}") from err

    async def async_unlock_doors(self, vin: str) -> None:
        state = self.data[vin]
        pin = self._require_pin()
        async with self._lock_for(vin):
            try:
                await self.api.unlock_door(vin, pin=pin, internal_vin=state.internal_vin)
                state.optimistic_locked = False
                self.async_set_updated_data(self.data)
            except MitsubishiAuthError as err:
                raise ConfigEntryAuthFailed(str(err)) from err
            except MitsubishiApiError as err:
                raise HomeAssistantError(f"Failed to unlock doors: {err}") from err

    async def async_start_engine(self, vin: str) -> None:
        state = self.data[vin]
        pin = self._require_pin()
        hvac = {
            "frontDefrostStatus": 1 if state.front_defrost else 0,
            "rearDefrostStatus": 1 if state.rear_defrost else 0,
            "steeringHeaterStatus": 1 if state.steering_heater else 0,
        }
        async with self._lock_for(vin):
            try:
                await self.api.start_engine(
                    vin,
                    pin=pin,
                    target_temperature=state.target_temperature,
                    temperature_unit=state.temperature_unit,
                    hvac_settings=hvac,
                    internal_vin=state.internal_vin,
                )
                state.engine["isEngineOn"] = True
                state.engine["targetTemperature"] = state.target_temperature
                state.engine["temperatureUnit"] = state.temperature_unit
                self.async_set_updated_data(self.data)
            except MitsubishiAuthError as err:
                raise ConfigEntryAuthFailed(str(err)) from err
            except MitsubishiApiError as err:
                raise HomeAssistantError(
                    f"Failed to start engine (make sure all doors/hood are closed and doors are locked): {err}"
                ) from err

    async def async_stop_engine(self, vin: str) -> None:
        state = self.data[vin]
        async with self._lock_for(vin):
            try:
                await self.api.stop_engine(vin, pin=None, internal_vin=state.internal_vin)
                state.engine["isEngineOn"] = False
                self.async_set_updated_data(self.data)
            except MitsubishiAuthError as err:
                raise ConfigEntryAuthFailed(str(err)) from err
            except MitsubishiApiError as err:
                raise HomeAssistantError(f"Failed to stop engine: {err}") from err

    async def async_flash_lights(self, vin: str) -> None:
        state = self.data[vin]
        async with self._lock_for(vin):
            try:
                await self.api.start_light(vin, pin=self.pin, internal_vin=state.internal_vin)
            except MitsubishiAuthError as err:
                raise ConfigEntryAuthFailed(str(err)) from err
            except MitsubishiApiError as err:
                raise HomeAssistantError(f"Failed to flash lights: {err}") from err

    async def async_sound_horn(self, vin: str) -> None:
        state = self.data[vin]
        async with self._lock_for(vin):
            try:
                await self.api.start_horn(vin, pin=self.pin, internal_vin=state.internal_vin)
            except MitsubishiAuthError as err:
                raise ConfigEntryAuthFailed(str(err)) from err
            except MitsubishiApiError as err:
                raise HomeAssistantError(f"Failed to sound horn: {err}") from err

    async def async_force_refresh(self, vin: str) -> None:
        state = self.data[vin]
        now = time.monotonic()
        elapsed = now - state.last_force_refresh_monotonic
        if state.last_force_refresh_monotonic > 0 and elapsed < FORCE_REFRESH_COOLDOWN_SECONDS:
            remaining = int(FORCE_REFRESH_COOLDOWN_SECONDS - elapsed)
            raise HomeAssistantError(
                f"Active vehicle refresh is rate-limited to protect your account and 12V battery. "
                f"Please wait {remaining}s."
            )
        async with self._lock_for(vin):
            try:
                await self.api.refresh_vsr(vin, internal_vin=state.internal_vin)
                state.last_force_refresh_monotonic = time.monotonic()
                vsr, engine = await asyncio.gather(
                    self.api.get_vsr(vin, state.internal_vin),
                    self.api.get_engine_details(vin, state.internal_vin),
                )
                state.vsr = vsr or {}
                state.engine = engine or {}
                self.async_set_updated_data(self.data)
            except MitsubishiAuthError as err:
                raise ConfigEntryAuthFailed(str(err)) from err
            except MitsubishiApiError as err:
                raise HomeAssistantError(f"Failed to refresh vehicle status: {err}") from err

    async def async_update_location(self, vin: str) -> None:
        state = self.data[vin]
        async with self._lock_for(vin):
            try:
                loc = await self.api.get_location(
                    vin, pin=self.pin, internal_vin=state.internal_vin
                )
                state.location = loc or {}
                self.async_set_updated_data(self.data)
            except MitsubishiAuthError as err:
                raise ConfigEntryAuthFailed(str(err)) from err
            except MitsubishiApiError as err:
                raise HomeAssistantError(f"Failed to fetch vehicle location: {err}") from err

    async def async_start_charge(self, vin: str) -> None:
        state = self.data[vin]
        async with self._lock_for(vin):
            try:
                await self.api.start_charge(vin, pin=self.pin, internal_vin=state.internal_vin)
                state.charge["isRealCharging"] = True
                self.async_set_updated_data(self.data)
            except MitsubishiAuthError as err:
                raise ConfigEntryAuthFailed(str(err)) from err
            except MitsubishiApiError as err:
                raise HomeAssistantError(f"Failed to start charging: {err}") from err

    async def async_stop_charge(self, vin: str) -> None:
        state = self.data[vin]
        async with self._lock_for(vin):
            try:
                await self.api.stop_charge(vin, pin=self.pin, internal_vin=state.internal_vin)
                state.charge["isRealCharging"] = False
                self.async_set_updated_data(self.data)
            except MitsubishiAuthError as err:
                raise ConfigEntryAuthFailed(str(err)) from err
            except MitsubishiApiError as err:
                raise HomeAssistantError(f"Failed to stop charging: {err}") from err
