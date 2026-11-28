"""Number entity for remote engine target cabin temperature."""

from __future__ import annotations

from homeassistant.components.number import NumberDeviceClass, NumberEntity, NumberMode
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory, UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity

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
        [MitsubishiTargetTempNumber(coordinator, vin) for vin in coordinator.data]
    )


class MitsubishiTargetTempNumber(MitsubishiVehicleEntity, RestoreEntity, NumberEntity):
    """Target cabin temperature preset used when remote-starting the engine."""

    _attr_name = "Remote Start Temperature"
    _attr_translation_key = "remote_start_temp"
    _attr_device_class = NumberDeviceClass.TEMPERATURE
    _attr_entity_category = EntityCategory.CONFIG
    _attr_mode = NumberMode.BOX
    _attr_icon = "mdi:thermometer"

    def __init__(self, coordinator: MitsubishiConnectCoordinator, vin: str) -> None:
        super().__init__(coordinator, vin, "remote_start_temp")

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        last = await self.async_get_last_state()
        if last is not None:
            try:
                self.vehicle.target_temperature = float(last.state)
            except (TypeError, ValueError):
                pass

    @property
    def native_unit_of_measurement(self) -> str:
        return (
            UnitOfTemperature.FAHRENHEIT
            if self.vehicle.temperature_unit == "F"
            else UnitOfTemperature.CELSIUS
        )

    @property
    def native_min_value(self) -> float:
        return 60.0 if self.vehicle.temperature_unit == "F" else 16.0

    @property
    def native_max_value(self) -> float:
        return 86.0 if self.vehicle.temperature_unit == "F" else 30.0

    @property
    def native_step(self) -> float:
        return 1.0 if self.vehicle.temperature_unit == "F" else 0.5

    @property
    def native_value(self) -> float:
        return self.vehicle.target_temperature

    async def async_set_native_value(self, value: float) -> None:
        self.vehicle.target_temperature = float(value)
        self.async_write_ha_state()
