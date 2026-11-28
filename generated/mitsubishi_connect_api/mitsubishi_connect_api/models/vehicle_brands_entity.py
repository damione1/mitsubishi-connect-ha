from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.c_vehicle_brands_commercial_entity import CVehicleBrandsCommercialEntity


T = TypeVar("T", bound="VehicleBrandsEntity")


@_attrs_define
class VehicleBrandsEntity:
    """
    Attributes:
        commercial (CVehicleBrandsCommercialEntity | Unset):
    """

    commercial: CVehicleBrandsCommercialEntity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commercial: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commercial, Unset):
            commercial = self.commercial.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commercial is not UNSET:
            field_dict["commercial"] = commercial

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.c_vehicle_brands_commercial_entity import CVehicleBrandsCommercialEntity  # noqa: PLC0415

        d = dict(src_dict)
        _commercial = d.pop("commercial", UNSET)
        commercial: CVehicleBrandsCommercialEntity | Unset
        if isinstance(_commercial, Unset):
            commercial = UNSET
        else:
            commercial = CVehicleBrandsCommercialEntity.from_dict(_commercial)

        vehicle_brands_entity = cls(
            commercial=commercial,
        )

        vehicle_brands_entity.additional_properties = d
        return vehicle_brands_entity

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
