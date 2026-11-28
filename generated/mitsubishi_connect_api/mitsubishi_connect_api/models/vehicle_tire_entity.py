from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vsr_metric import VsrMetric


T = TypeVar("T", bound="VehicleTireEntity")


@_attrs_define
class VehicleTireEntity:
    """
    Attributes:
        position (VsrMetric | Unset):
        pressure (VsrMetric | Unset):
        pressure_value (VsrMetric | Unset):
    """

    position: VsrMetric | Unset = UNSET
    pressure: VsrMetric | Unset = UNSET
    pressure_value: VsrMetric | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        pressure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pressure, Unset):
            pressure = self.pressure.to_dict()

        pressure_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pressure_value, Unset):
            pressure_value = self.pressure_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if pressure is not UNSET:
            field_dict["pressure"] = pressure
        if pressure_value is not UNSET:
            field_dict["pressureValue"] = pressure_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vsr_metric import VsrMetric  # noqa: PLC0415

        d = dict(src_dict)
        _position = d.pop("position", UNSET)
        position: VsrMetric | Unset
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = VsrMetric.from_dict(_position)

        _pressure = d.pop("pressure", UNSET)
        pressure: VsrMetric | Unset
        if isinstance(_pressure, Unset):
            pressure = UNSET
        else:
            pressure = VsrMetric.from_dict(_pressure)

        _pressure_value = d.pop("pressureValue", UNSET)
        pressure_value: VsrMetric | Unset
        if isinstance(_pressure_value, Unset):
            pressure_value = UNSET
        else:
            pressure_value = VsrMetric.from_dict(_pressure_value)

        vehicle_tire_entity = cls(
            position=position,
            pressure=pressure,
            pressure_value=pressure_value,
        )

        vehicle_tire_entity.additional_properties = d
        return vehicle_tire_entity

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
