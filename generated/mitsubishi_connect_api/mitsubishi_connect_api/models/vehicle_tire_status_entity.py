from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vehicle_tire_entity import VehicleTireEntity


T = TypeVar("T", bound="VehicleTireStatusEntity")


@_attrs_define
class VehicleTireStatusEntity:
    """
    Attributes:
        id (None | str | Unset):
        name (None | str | Unset):
        tires (list[VehicleTireEntity] | Unset):
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    tires: list[VehicleTireEntity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        tires: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tires, Unset):
            tires = []
            for tires_item_data in self.tires:
                tires_item = tires_item_data.to_dict()
                tires.append(tires_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if tires is not UNSET:
            field_dict["tires"] = tires

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vehicle_tire_entity import VehicleTireEntity  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _tires = d.pop("tires", UNSET)
        tires: list[VehicleTireEntity] | Unset = UNSET
        if _tires is not UNSET:
            tires = []
            for tires_item_data in _tires:
                tires_item = VehicleTireEntity.from_dict(tires_item_data)

                tires.append(tires_item)

        vehicle_tire_status_entity = cls(
            id=id,
            name=name,
            tires=tires,
        )

        vehicle_tire_status_entity.additional_properties = d
        return vehicle_tire_status_entity

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
