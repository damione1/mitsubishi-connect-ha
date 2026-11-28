"""Binary sensor entities for Mitsubishi Connect."""

from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import MitsubishiConnectCoordinator
from .entity import MitsubishiVehicleEntity

DOOR_POSITIONS: list[tuple[str, str, BinarySensorDeviceClass]] = [
    ("doorFrontLeft", "Front Left Door", BinarySensorDeviceClass.DOOR),
    ("doorFrontRight", "Front Right Door", BinarySensorDeviceClass.DOOR),
    ("doorRearLeft", "Rear Left Door", BinarySensorDeviceClass.DOOR),
    ("doorRearRight", "Rear Right Door", BinarySensorDeviceClass.DOOR),
    ("doorHood", "Hood", BinarySensorDeviceClass.OPENING),
    ("doorTrunk", "Trunk", BinarySensorDeviceClass.OPENING),
]

DOOR_TRANSLATION_KEYS: dict[str, str] = {
    "doorFrontLeft": "front_left_door",
    "doorFrontRight": "front_right_door",
    "doorRearLeft": "rear_left_door",
    "doorRearRight": "rear_right_door",
    "doorHood": "hood",
    "doorTrunk": "trunk",
}
WARNING_TRANSLATION_KEYS: dict[str, str] = {
    "breakWarn": "brake_warning",
    "engineOilWarn": "engine_oil_warning",
}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: MitsubishiConnectCoordinator = hass.data[DOMAIN][entry.entry_id]
    entities: list[BinarySensorEntity] = []
    for vin, state in coordinator.data.items():
        entities.append(MitsubishiEngineRunningSensor(coordinator, vin))
        entities.append(MitsubishiHeadlightsSensor(coordinator, vin))
        entities.append(MitsubishiWarningSensor(coordinator, vin, "breakWarn", "Brake Warning"))
        entities.append(
            MitsubishiWarningSensor(coordinator, vin, "engineOilWarn", "Engine Oil Warning")
        )
        for pos_key, label, dev_class in DOOR_POSITIONS:
            entities.append(MitsubishiDoorSensor(coordinator, vin, pos_key, label, dev_class))

        if state.is_phev:
            entities.append(MitsubishiPluggedInSensor(coordinator, vin))
            entities.append(MitsubishiChargingSensor(coordinator, vin))

        # Dynamically expose window sensors if the vehicle reports windowStatus in VSR
        vstatus = ((state.vsr.get("data") or {}).get("vehicleStatus")) or {}
        windows = ((vstatus.get("windowStatus") or {}).get("windows")) or []
        for idx, item in enumerate(windows):
            pos = (item.get("position") or {}).get("displayMessage") or f"window_{idx}"
            entities.append(MitsubishiWindowSensor(coordinator, vin, pos))

    async_add_entities(entities)


class MitsubishiEngineRunningSensor(MitsubishiVehicleEntity, BinarySensorEntity):
    _attr_name = "Engine"
    _attr_translation_key = "engine_running"
    _attr_device_class = BinarySensorDeviceClass.RUNNING
    _attr_icon = "mdi:engine"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "engine_running")

    @property
    def is_on(self) -> bool | None:
        val = self.vehicle.engine.get("isEngineOn")
        return bool(val) if val is not None else None


class MitsubishiDoorSensor(MitsubishiVehicleEntity, BinarySensorEntity):
    def __init__(
        self,
        coordinator: MitsubishiConnectCoordinator,
        vin: str,
        position_key: str,
        label: str,
        device_class: BinarySensorDeviceClass,
    ) -> None:
        super().__init__(coordinator, vin, f"door_{position_key}")
        self._pos_key = position_key
        self._attr_name = label
        self._attr_device_class = device_class
        self._attr_translation_key = DOOR_TRANSLATION_KEYS.get(position_key)

    @property
    def is_on(self) -> bool | None:
        vstatus = ((self.vehicle.vsr.get("data") or {}).get("vehicleStatus")) or {}
        doors = ((vstatus.get("doorStatus") or {}).get("doors")) or []
        for door in doors:
            pos = (door.get("position") or {}).get("displayMessage")
            if pos == self._pos_key:
                val = (door.get("state") or {}).get("value")
                if val is None:
                    return None
                return str(val) != "0"
        return None


class MitsubishiWindowSensor(MitsubishiVehicleEntity, BinarySensorEntity):
    _attr_device_class = BinarySensorDeviceClass.WINDOW

    def __init__(
        self, coordinator: MitsubishiConnectCoordinator, vin: str, position_key: str
    ) -> None:
        super().__init__(coordinator, vin, f"window_{position_key}")
        self._pos_key = position_key
        self._attr_name = position_key.replace("_", " ").title()
        self._attr_translation_key = "window"

    @property
    def is_on(self) -> bool | None:
        vstatus = ((self.vehicle.vsr.get("data") or {}).get("vehicleStatus")) or {}
        windows = ((vstatus.get("windowStatus") or {}).get("windows")) or []
        for win in windows:
            pos = (win.get("position") or {}).get("displayMessage")
            if pos == self._pos_key:
                val = (win.get("state") or {}).get("value")
                if val is None:
                    return None
                return str(val) != "0"
        return None


class MitsubishiHeadlightsSensor(MitsubishiVehicleEntity, BinarySensorEntity):
    _attr_name = "Headlights"
    _attr_translation_key = "headlights"
    _attr_device_class = BinarySensorDeviceClass.LIGHT
    _attr_icon = "mdi:car-light-high"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "headlights")

    @property
    def is_on(self) -> bool | None:
        vstatus = ((self.vehicle.vsr.get("data") or {}).get("vehicleStatus")) or {}
        lights = ((vstatus.get("lightStatus") or {}).get("lights")) or []
        for light in lights:
            state = light.get("state") or {}
            msg = str(state.get("displayMessage") or "").lower()
            if "off" in msg:
                return False
            if "on" in msg:
                return True
        return None


class MitsubishiWarningSensor(MitsubishiVehicleEntity, BinarySensorEntity):
    _attr_device_class = BinarySensorDeviceClass.PROBLEM

    def __init__(
        self,
        coordinator: MitsubishiConnectCoordinator,
        vin: str,
        diag_key: str,
        label: str,
    ) -> None:
        super().__init__(coordinator, vin, f"warning_{diag_key}")
        self._diag_key = diag_key
        self._attr_name = label
        self._attr_translation_key = WARNING_TRANSLATION_KEYS.get(diag_key)

    @property
    def is_on(self) -> bool | None:
        diag = ((self.vehicle.vsr.get("data") or {}).get("diagnostic")) or {}
        metric = diag.get(self._diag_key)
        if not isinstance(metric, dict):
            return None
        warn = metric.get("warning")
        if warn is not None:
            return str(warn).lower() == "true"
        val = metric.get("value")
        return str(val) != "0" if val is not None else None


class MitsubishiPluggedInSensor(MitsubishiVehicleEntity, BinarySensorEntity):
    """Charging cable connected (PHEV/EV only)."""

    _attr_name = "Charging Cable"
    _attr_translation_key = "charging_cable"
    _attr_device_class = BinarySensorDeviceClass.PLUG

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "charging_cable")

    @property
    def is_on(self) -> bool | None:
        value = self.vehicle.charge.get("isPluggedIn")
        return bool(value) if value is not None else None


class MitsubishiChargingSensor(MitsubishiVehicleEntity, BinarySensorEntity):
    """Traction battery actively charging (PHEV/EV only)."""

    _attr_name = "Charging"
    _attr_translation_key = "charging"
    _attr_device_class = BinarySensorDeviceClass.BATTERY_CHARGING

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "charging")

    @property
    def is_on(self) -> bool | None:
        value = self.vehicle.charge.get("isRealCharging")
        return bool(value) if value is not None else None
