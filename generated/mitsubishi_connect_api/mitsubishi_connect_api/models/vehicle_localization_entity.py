from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VehicleLocalizationEntity")


@_attrs_define
class VehicleLocalizationEntity:
    """
    Attributes:
        iso_2_delivery_country_code (None | str | Unset):
        iso_2_usage_country_code (None | str | Unset):
        region (None | str | Unset):
    """

    iso_2_delivery_country_code: None | str | Unset = UNSET
    iso_2_usage_country_code: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iso_2_delivery_country_code: None | str | Unset
        if isinstance(self.iso_2_delivery_country_code, Unset):
            iso_2_delivery_country_code = UNSET
        else:
            iso_2_delivery_country_code = self.iso_2_delivery_country_code

        iso_2_usage_country_code: None | str | Unset
        if isinstance(self.iso_2_usage_country_code, Unset):
            iso_2_usage_country_code = UNSET
        else:
            iso_2_usage_country_code = self.iso_2_usage_country_code

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if iso_2_delivery_country_code is not UNSET:
            field_dict["iso2DeliveryCountryCode"] = iso_2_delivery_country_code
        if iso_2_usage_country_code is not UNSET:
            field_dict["iso2UsageCountryCode"] = iso_2_usage_country_code
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_iso_2_delivery_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        iso_2_delivery_country_code = _parse_iso_2_delivery_country_code(d.pop("iso2DeliveryCountryCode", UNSET))

        def _parse_iso_2_usage_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        iso_2_usage_country_code = _parse_iso_2_usage_country_code(d.pop("iso2UsageCountryCode", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        vehicle_localization_entity = cls(
            iso_2_delivery_country_code=iso_2_delivery_country_code,
            iso_2_usage_country_code=iso_2_usage_country_code,
            region=region,
        )

        vehicle_localization_entity.additional_properties = d
        return vehicle_localization_entity

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
