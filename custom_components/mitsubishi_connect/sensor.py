"""Sensor entities for Mitsubishi Connect."""

from __future__ import annotations

from datetime import datetime, timezone

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PERCENTAGE, UnitOfLength, UnitOfTemperature, UnitOfTime
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
    entities: list[SensorEntity] = []
    for vin, state in coordinator.data.items():
        entities.extend(
            [
                MitsubishiOdometerSensor(coordinator, vin),
                MitsubishiRangeSensor(coordinator, vin),
                MitsubishiTargetTempSensor(coordinator, vin),
                MitsubishiLastUpdateSensor(coordinator, vin),
            ]
        )
        if state.is_phev:
            entities.extend(
                [
                    MitsubishiBatterySensor(coordinator, vin),
                    MitsubishiChargeTimeSensor(coordinator, vin),
                ]
            )
    async_add_entities(entities)


def _distance_unit(diag: dict) -> str:
    msg = (diag.get("odos") or {}).get("displayMessage") or ""
    if msg.endswith("mi"):
        return UnitOfLength.MILES
    return UnitOfLength.KILOMETERS


class MitsubishiOdometerSensor(MitsubishiVehicleEntity, SensorEntity):
    _attr_name = "Odometer"
    _attr_translation_key = "odometer"
    _attr_device_class = SensorDeviceClass.DISTANCE
    _attr_state_class = SensorStateClass.TOTAL_INCREASING
    _attr_icon = "mdi:counter"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "odometer")

    @property
    def native_unit_of_measurement(self) -> str:
        diag = ((self.vehicle.vsr.get("data") or {}).get("diagnostic")) or {}
        return _distance_unit(diag)

    @property
    def native_value(self) -> float | None:
        diag = ((self.vehicle.vsr.get("data") or {}).get("diagnostic")) or {}
        raw = (diag.get("odo") or {}).get("value")
        try:
            return float(raw) if raw is not None else None
        except (TypeError, ValueError):
            return None


class MitsubishiRangeSensor(MitsubishiVehicleEntity, SensorEntity):
    _attr_name = "Fuel Range"
    _attr_translation_key = "fuel_range"
    _attr_device_class = SensorDeviceClass.DISTANCE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_icon = "mdi:gas-station"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "fuel_range")

    @property
    def native_unit_of_measurement(self) -> str:
        diag = ((self.vehicle.vsr.get("data") or {}).get("diagnostic")) or {}
        return _distance_unit(diag)

    @property
    def native_value(self) -> float | None:
        diag = ((self.vehicle.vsr.get("data") or {}).get("diagnostic")) or {}
        raw = (diag.get("availRange") or {}).get("value")
        try:
            return float(raw) if raw is not None else None
        except (TypeError, ValueError):
            return None


class MitsubishiTargetTempSensor(MitsubishiVehicleEntity, SensorEntity):
    _attr_name = "Target Cabin Temperature"
    _attr_translation_key = "target_cabin_temp"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "target_cabin_temp")

    @property
    def native_unit_of_measurement(self) -> str:
        unit = (self.vehicle.engine.get("temperatureUnit") or self.vehicle.temperature_unit).upper()
        return UnitOfTemperature.FAHRENHEIT if unit == "F" else UnitOfTemperature.CELSIUS

    @property
    def native_value(self) -> float | None:
        raw = self.vehicle.engine.get("targetTemperature")
        try:
            return float(raw) if raw is not None else None
        except (TypeError, ValueError):
            return None


class MitsubishiLastUpdateSensor(MitsubishiVehicleEntity, SensorEntity):
    _attr_name = "Last Telemetry Update"
    _attr_translation_key = "last_telemetry_update"
    _attr_device_class = SensorDeviceClass.TIMESTAMP
    _attr_icon = "mdi:clock-outline"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "last_telemetry_update")

    @property
    def native_value(self) -> datetime | None:
        raw = self.vehicle.vsr.get("timestamp")
        if raw is None:
            return None
        try:
            ts = int(str(raw))
            if ts > 10**12:
                ts = ts // 1000
            return datetime.fromtimestamp(ts, tz=timezone.utc)
        except (TypeError, ValueError, OSError):
            return None


class MitsubishiBatterySensor(MitsubishiVehicleEntity, SensorEntity):
    """High-voltage traction battery charge level (PHEV/EV only)."""

    _attr_name = "Battery"
    _attr_translation_key = "hv_battery"
    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = PERCENTAGE

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "hv_battery")

    @property
    def native_value(self) -> float | None:
        raw = self.vehicle.charge.get("hvBatteryLife")
        try:
            return float(raw) if raw is not None else None
        except (TypeError, ValueError):
            return None


class MitsubishiChargeTimeSensor(MitsubishiVehicleEntity, SensorEntity):
    """Estimated time remaining to a full charge (PHEV/EV only)."""

    _attr_name = "Time to Full Charge"
    _attr_translation_key = "time_to_full_charge"
    _attr_device_class = SensorDeviceClass.DURATION
    _attr_native_unit_of_measurement = UnitOfTime.MINUTES
    _attr_icon = "mdi:battery-clock"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "time_to_full_charge")

    @property
    def native_value(self) -> float | None:
        raw = self.vehicle.charge.get("hvTimeToFullCharge")
        try:
            return float(raw) if raw is not None else None
        except (TypeError, ValueError):
            return None
