from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SOCSettingEntity")


@_attrs_define
class SOCSettingEntity:
    """
    Attributes:
        charging_limit_threshold (None | str | Unset):
        charging_notification_threshold (None | str | Unset):
        internal_vin (None | str | Unset): Internal VIN from `getVehicleList` (`vinList`), omitted when not provided.
            Example: JA4XXXXXXXXXXXXXX.
        vin (None | str | Unset): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls.
            Example: JA4XXXXXXXXXXXXXX.
    """

    charging_limit_threshold: None | str | Unset = UNSET
    charging_notification_threshold: None | str | Unset = UNSET
    internal_vin: None | str | Unset = UNSET
    vin: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charging_limit_threshold: None | str | Unset
        if isinstance(self.charging_limit_threshold, Unset):
            charging_limit_threshold = UNSET
        else:
            charging_limit_threshold = self.charging_limit_threshold

        charging_notification_threshold: None | str | Unset
        if isinstance(self.charging_notification_threshold, Unset):
            charging_notification_threshold = UNSET
        else:
            charging_notification_threshold = self.charging_notification_threshold

        internal_vin: None | str | Unset
        if isinstance(self.internal_vin, Unset):
            internal_vin = UNSET
        else:
            internal_vin = self.internal_vin

        vin: None | str | Unset
        if isinstance(self.vin, Unset):
            vin = UNSET
        else:
            vin = self.vin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charging_limit_threshold is not UNSET:
            field_dict["chargingLimitThreshold"] = charging_limit_threshold
        if charging_notification_threshold is not UNSET:
            field_dict["chargingNotificationThreshold"] = charging_notification_threshold
        if internal_vin is not UNSET:
            field_dict["internalVin"] = internal_vin
        if vin is not UNSET:
            field_dict["vin"] = vin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_charging_limit_threshold(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        charging_limit_threshold = _parse_charging_limit_threshold(d.pop("chargingLimitThreshold", UNSET))

        def _parse_charging_notification_threshold(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        charging_notification_threshold = _parse_charging_notification_threshold(
            d.pop("chargingNotificationThreshold", UNSET)
        )

        def _parse_internal_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_vin = _parse_internal_vin(d.pop("internalVin", UNSET))

        def _parse_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vin = _parse_vin(d.pop("vin", UNSET))

        soc_setting_entity = cls(
            charging_limit_threshold=charging_limit_threshold,
            charging_notification_threshold=charging_notification_threshold,
            internal_vin=internal_vin,
            vin=vin,
        )

        soc_setting_entity.additional_properties = d
        return soc_setting_entity

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
