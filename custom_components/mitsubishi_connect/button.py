"""Button entities for Mitsubishi Connect remote actions."""

from __future__ import annotations

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import MitsubishiConnectCoordinator
from .entity import MitsubishiVehicleEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: MitsubishiConnectCoordinator = hass.data[DOMAIN][entry.entry_id]
    entities: list[ButtonEntity] = []
    for vin, state in coordinator.data.items():
        entities.extend(
            [
                MitsubishiStartEngineButton(coordinator, vin),
                MitsubishiStopEngineButton(coordinator, vin),
                MitsubishiLockDoorsButton(coordinator, vin),
                MitsubishiUnlockDoorsButton(coordinator, vin),
                MitsubishiFlashLightsButton(coordinator, vin),
                MitsubishiSoundHornButton(coordinator, vin),
                MitsubishiForceRefreshButton(coordinator, vin),
                MitsubishiUpdateLocationButton(coordinator, vin),
            ]
        )
        if state.is_phev:
            entities.extend(
                [
                    MitsubishiStartChargeButton(coordinator, vin),
                    MitsubishiStopChargeButton(coordinator, vin),
                ]
            )
    async_add_entities(entities)


class MitsubishiStartEngineButton(MitsubishiVehicleEntity, ButtonEntity):
    _attr_name = "Start Engine"
    _attr_translation_key = "start_engine"
    _attr_icon = "mdi:engine"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "start_engine")

    async def async_press(self) -> None:
        await self.coordinator.async_start_engine(self._vin)


class MitsubishiStopEngineButton(MitsubishiVehicleEntity, ButtonEntity):
    _attr_name = "Stop Engine"
    _attr_translation_key = "stop_engine"
    _attr_icon = "mdi:engine-off"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "stop_engine")

    async def async_press(self) -> None:
        await self.coordinator.async_stop_engine(self._vin)


class MitsubishiLockDoorsButton(MitsubishiVehicleEntity, ButtonEntity):
    _attr_name = "Lock Doors"
    _attr_translation_key = "lock_doors"
    _attr_icon = "mdi:car-door-lock"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "lock_doors")

    async def async_press(self) -> None:
        await self.coordinator.async_lock_doors(self._vin)


class MitsubishiUnlockDoorsButton(MitsubishiVehicleEntity, ButtonEntity):
    _attr_name = "Unlock Doors"
    _attr_translation_key = "unlock_doors"
    _attr_icon = "mdi:car-door-lock-open"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "unlock_doors")

    async def async_press(self) -> None:
        await self.coordinator.async_unlock_doors(self._vin)


class MitsubishiFlashLightsButton(MitsubishiVehicleEntity, ButtonEntity):
    _attr_name = "Flash Lights"
    _attr_translation_key = "flash_lights"
    _attr_icon = "mdi:car-light-high"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "flash_lights")

    async def async_press(self) -> None:
        await self.coordinator.async_flash_lights(self._vin)


class MitsubishiSoundHornButton(MitsubishiVehicleEntity, ButtonEntity):
    _attr_name = "Sound Horn"
    _attr_translation_key = "sound_horn"
    _attr_icon = "mdi:bugle"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "sound_horn")

    async def async_press(self) -> None:
        await self.coordinator.async_sound_horn(self._vin)


class MitsubishiForceRefreshButton(MitsubishiVehicleEntity, ButtonEntity):
    """Manually wake the vehicle for fresh VSR telemetry (10-min cooldown)."""

    _attr_name = "Refresh Vehicle Status"
    _attr_translation_key = "force_refresh"
    _attr_icon = "mdi:refresh"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "force_refresh")

    async def async_press(self) -> None:
        await self.coordinator.async_force_refresh(self._vin)


class MitsubishiUpdateLocationButton(MitsubishiVehicleEntity, ButtonEntity):
    """Manually request vehicle GPS coordinates (Find My Car)."""

    _attr_name = "Update GPS Location"
    _attr_translation_key = "update_location"
    _attr_icon = "mdi:crosshairs-gps"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "update_location")

    async def async_press(self) -> None:
        await self.coordinator.async_update_location(self._vin)


class MitsubishiStartChargeButton(MitsubishiVehicleEntity, ButtonEntity):
    """Start charging the traction battery (PHEV/EV only)."""

    _attr_name = "Start Charging"
    _attr_translation_key = "start_charge"
    _attr_icon = "mdi:battery-charging"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "start_charge")

    async def async_press(self) -> None:
        await self.coordinator.async_start_charge(self._vin)


class MitsubishiStopChargeButton(MitsubishiVehicleEntity, ButtonEntity):
    """Stop charging the traction battery (PHEV/EV only)."""

    _attr_name = "Stop Charging"
    _attr_translation_key = "stop_charge"
    _attr_icon = "mdi:battery-off"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "stop_charge")

    async def async_press(self) -> None:
        await self.coordinator.async_stop_charge(self._vin)
