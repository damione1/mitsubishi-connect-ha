"""Base entity for Mitsubishi Connect devices."""

from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import MitsubishiConnectCoordinator, VehicleState


class MitsubishiVehicleEntity(CoordinatorEntity[MitsubishiConnectCoordinator]):
    """Shared base class for all entities belonging to a Mitsubishi vehicle."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: MitsubishiConnectCoordinator,
        vin: str,
        unique_suffix: str,
    ) -> None:
        super().__init__(coordinator)
        self._vin = vin
        self._attr_unique_id = f"{vin}_{unique_suffix}"

    @property
    def vehicle(self) -> VehicleState:
        return self.coordinator.data[self._vin]

    @property
    def available(self) -> bool:
        return super().available and self._vin in (self.coordinator.data or {})

    @property
    def device_info(self) -> DeviceInfo:
        info = self.vehicle.info
        model_obj = info.get("model") or {}
        year = model_obj.get("modelYear") or ""
        body = model_obj.get("bodyWork") or "Vehicle"
        nickname = info.get("nickName")
        name = nickname or f"Mitsubishi {body} {year}".strip()
        model_str = f"{body} ({year})" if year else body
        return DeviceInfo(
            identifiers={(DOMAIN, self._vin)},
            manufacturer="Mitsubishi Motors",
            name=name,
            model=model_str,
            serial_number=self._vin,
        )
