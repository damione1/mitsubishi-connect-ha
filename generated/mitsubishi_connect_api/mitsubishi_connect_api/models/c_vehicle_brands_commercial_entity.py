from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CVehicleBrandsCommercialEntity")


@_attrs_define
class CVehicleBrandsCommercialEntity:
    """
    Attributes:
        brand_code (None | str | Unset):
        brand_name (None | str | Unset):
        master_brand_name (None | str | Unset):
    """

    brand_code: None | str | Unset = UNSET
    brand_name: None | str | Unset = UNSET
    master_brand_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_code: None | str | Unset
        if isinstance(self.brand_code, Unset):
            brand_code = UNSET
        else:
            brand_code = self.brand_code

        brand_name: None | str | Unset
        if isinstance(self.brand_name, Unset):
            brand_name = UNSET
        else:
            brand_name = self.brand_name

        master_brand_name: None | str | Unset
        if isinstance(self.master_brand_name, Unset):
            master_brand_name = UNSET
        else:
            master_brand_name = self.master_brand_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brand_code is not UNSET:
            field_dict["brandCode"] = brand_code
        if brand_name is not UNSET:
            field_dict["brandName"] = brand_name
        if master_brand_name is not UNSET:
            field_dict["masterBrandName"] = master_brand_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_brand_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        brand_code = _parse_brand_code(d.pop("brandCode", UNSET))

        def _parse_brand_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        brand_name = _parse_brand_name(d.pop("brandName", UNSET))

        def _parse_master_brand_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        master_brand_name = _parse_master_brand_name(d.pop("masterBrandName", UNSET))

        c_vehicle_brands_commercial_entity = cls(
            brand_code=brand_code,
            brand_name=brand_name,
            master_brand_name=master_brand_name,
        )

        c_vehicle_brands_commercial_entity.additional_properties = d
        return c_vehicle_brands_commercial_entity

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
