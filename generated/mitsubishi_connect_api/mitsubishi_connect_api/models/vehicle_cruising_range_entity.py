from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vehicle_sub_cruising_range_entity import VehicleSubCruisingRangeEntity


T = TypeVar("T", bound="VehicleCruisingRangeEntity")


@_attrs_define
class VehicleCruisingRangeEntity:
    """
    Attributes:
        cruising_range (list[VehicleSubCruisingRangeEntity] | Unset):
        id (None | str | Unset):
        name (None | str | Unset):
    """

    cruising_range: list[VehicleSubCruisingRangeEntity] | Unset = UNSET
    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cruising_range: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cruising_range, Unset):
            cruising_range = []
            for cruising_range_item_data in self.cruising_range:
                cruising_range_item = cruising_range_item_data.to_dict()
                cruising_range.append(cruising_range_item)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cruising_range is not UNSET:
            field_dict["cruisingRange"] = cruising_range
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vehicle_sub_cruising_range_entity import VehicleSubCruisingRangeEntity  # noqa: PLC0415

        d = dict(src_dict)
        _cruising_range = d.pop("cruisingRange", UNSET)
        cruising_range: list[VehicleSubCruisingRangeEntity] | Unset = UNSET
        if _cruising_range is not UNSET:
            cruising_range = []
            for cruising_range_item_data in _cruising_range:
                cruising_range_item = VehicleSubCruisingRangeEntity.from_dict(cruising_range_item_data)

                cruising_range.append(cruising_range_item)

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

        vehicle_cruising_range_entity = cls(
            cruising_range=cruising_range,
            id=id,
            name=name,
        )

        vehicle_cruising_range_entity.additional_properties = d
        return vehicle_cruising_range_entity

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
