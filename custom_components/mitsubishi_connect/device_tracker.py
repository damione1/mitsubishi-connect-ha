"""Device tracker entity for Mitsubishi Connect GPS location."""

from __future__ import annotations

from homeassistant.components.device_tracker import SourceType
from homeassistant.components.device_tracker.config_entry import TrackerEntity
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
    async_add_entities(
        [MitsubishiLocationTracker(coordinator, vin) for vin in coordinator.data]
    )


class MitsubishiLocationTracker(MitsubishiVehicleEntity, TrackerEntity):
    """GPS tracker updated on demand via the Update GPS Location button."""

    _attr_name = "Location"
    _attr_translation_key = "location"
    _attr_icon = "mdi:car"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "location")

    @property
    def source_type(self) -> SourceType:
        return SourceType.GPS

    @property
    def latitude(self) -> float | None:
        item = self.vehicle.location.get("locationLatitude")
        val = item.get("value") if isinstance(item, dict) else None
        try:
            return float(val) if val is not None else None
        except (TypeError, ValueError):
            return None

    @property
    def longitude(self) -> float | None:
        item = self.vehicle.location.get("locationLongitude")
        val = item.get("value") if isinstance(item, dict) else None
        try:
            return float(val) if val is not None else None
        except (TypeError, ValueError):
            return None
