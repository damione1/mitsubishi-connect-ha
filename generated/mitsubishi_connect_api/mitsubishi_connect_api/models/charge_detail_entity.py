from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChargeDetailEntity")


@_attrs_define
class ChargeDetailEntity:
    """
    Attributes:
        hv_battery_life (None | str | Unset):
        hv_charging_ready (None | str | Unset):
        hv_time_to_full_charge (None | str | Unset):
        is_disable_start (bool | Unset):  Default: False.
        is_plugged_in (bool | Unset):  Default: False.
        is_real_charging (bool | Unset):  Default: False.
        polling_interval (int | None | Unset):
        timestamp (None | str | Unset):
        vin (None | str | Unset): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls.
            Example: JA4XXXXXXXXXXXXXX.
    """

    hv_battery_life: None | str | Unset = UNSET
    hv_charging_ready: None | str | Unset = UNSET
    hv_time_to_full_charge: None | str | Unset = UNSET
    is_disable_start: bool | Unset = False
    is_plugged_in: bool | Unset = False
    is_real_charging: bool | Unset = False
    polling_interval: int | None | Unset = UNSET
    timestamp: None | str | Unset = UNSET
    vin: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hv_battery_life: None | str | Unset
        if isinstance(self.hv_battery_life, Unset):
            hv_battery_life = UNSET
        else:
            hv_battery_life = self.hv_battery_life

        hv_charging_ready: None | str | Unset
        if isinstance(self.hv_charging_ready, Unset):
            hv_charging_ready = UNSET
        else:
            hv_charging_ready = self.hv_charging_ready

        hv_time_to_full_charge: None | str | Unset
        if isinstance(self.hv_time_to_full_charge, Unset):
            hv_time_to_full_charge = UNSET
        else:
            hv_time_to_full_charge = self.hv_time_to_full_charge

        is_disable_start = self.is_disable_start

        is_plugged_in = self.is_plugged_in

        is_real_charging = self.is_real_charging

        polling_interval: int | None | Unset
        if isinstance(self.polling_interval, Unset):
            polling_interval = UNSET
        else:
            polling_interval = self.polling_interval

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = self.timestamp

        vin: None | str | Unset
        if isinstance(self.vin, Unset):
            vin = UNSET
        else:
            vin = self.vin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hv_battery_life is not UNSET:
            field_dict["hvBatteryLife"] = hv_battery_life
        if hv_charging_ready is not UNSET:
            field_dict["hvChargingReady"] = hv_charging_ready
        if hv_time_to_full_charge is not UNSET:
            field_dict["hvTimeToFullCharge"] = hv_time_to_full_charge
        if is_disable_start is not UNSET:
            field_dict["isDisableStart"] = is_disable_start
        if is_plugged_in is not UNSET:
            field_dict["isPluggedIn"] = is_plugged_in
        if is_real_charging is not UNSET:
            field_dict["isRealCharging"] = is_real_charging
        if polling_interval is not UNSET:
            field_dict["pollingInterval"] = polling_interval
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if vin is not UNSET:
            field_dict["vin"] = vin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_hv_battery_life(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hv_battery_life = _parse_hv_battery_life(d.pop("hvBatteryLife", UNSET))

        def _parse_hv_charging_ready(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hv_charging_ready = _parse_hv_charging_ready(d.pop("hvChargingReady", UNSET))

        def _parse_hv_time_to_full_charge(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hv_time_to_full_charge = _parse_hv_time_to_full_charge(d.pop("hvTimeToFullCharge", UNSET))

        is_disable_start = d.pop("isDisableStart", UNSET)

        is_plugged_in = d.pop("isPluggedIn", UNSET)

        is_real_charging = d.pop("isRealCharging", UNSET)

        def _parse_polling_interval(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        polling_interval = _parse_polling_interval(d.pop("pollingInterval", UNSET))

        def _parse_timestamp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        def _parse_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vin = _parse_vin(d.pop("vin", UNSET))

        charge_detail_entity = cls(
            hv_battery_life=hv_battery_life,
            hv_charging_ready=hv_charging_ready,
            hv_time_to_full_charge=hv_time_to_full_charge,
            is_disable_start=is_disable_start,
            is_plugged_in=is_plugged_in,
            is_real_charging=is_real_charging,
            polling_interval=polling_interval,
            timestamp=timestamp,
            vin=vin,
        )

        charge_detail_entity.additional_properties = d
        return charge_detail_entity

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
