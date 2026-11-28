"""Switch entities for Mitsubishi Connect remote start HVAC presets."""

from __future__ import annotations

from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
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
    entities: list[SwitchEntity] = []
    for vin in coordinator.data:
        entities.extend(
            [
                MitsubishiHvacOptionSwitch(
                    coordinator,
                    vin,
                    "front_defrost",
                    "Remote Start Front Defrost",
                    "mdi:car-defrost-front",
                ),
                MitsubishiHvacOptionSwitch(
                    coordinator,
                    vin,
                    "rear_defrost",
                    "Remote Start Rear Defrost",
                    "mdi:car-defrost-rear",
                ),
                MitsubishiHvacOptionSwitch(
                    coordinator,
                    vin,
                    "steering_heater",
                    "Remote Start Steering Wheel Heater",
                    "mdi:steering",
                ),
            ]
        )
    async_add_entities(entities)


class MitsubishiHvacOptionSwitch(MitsubishiVehicleEntity, RestoreEntity, SwitchEntity):
    """Local pre-conditioning preset applied on the next remote engine start."""

    _attr_entity_category = EntityCategory.CONFIG

    def __init__(
        self,
        coordinator: MitsubishiConnectCoordinator,
        vin: str,
        attr_name: str,
        label: str,
        icon: str,
    ) -> None:
        super().__init__(coordinator, vin, f"hvac_{attr_name}")
        self._field = attr_name
        self._attr_name = label
        self._attr_icon = icon
        self._attr_translation_key = f"hvac_{attr_name}"

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        last = await self.async_get_last_state()
        if last is not None and last.state in ("on", "off"):
            setattr(self.vehicle, self._field, last.state == "on")

    @property
    def is_on(self) -> bool:
        return bool(getattr(self.vehicle, self._field))

    async def async_turn_on(self, **kwargs: Any) -> None:
        setattr(self.vehicle, self._field, True)
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs: Any) -> None:
        setattr(self.vehicle, self._field, False)
        self.async_write_ha_state()
