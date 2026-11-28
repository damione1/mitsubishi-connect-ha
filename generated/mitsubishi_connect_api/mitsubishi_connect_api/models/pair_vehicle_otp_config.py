from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PairVehicleOtpConfig")


@_attrs_define
class PairVehicleOtpConfig:
    """
    Attributes:
        expire_seconds (None | str | Unset):
        length (None | str | Unset):
        lock_seconds (None | str | Unset):
        max_wrong_times (None | str | Unset):
    """

    expire_seconds: None | str | Unset = UNSET
    length: None | str | Unset = UNSET
    lock_seconds: None | str | Unset = UNSET
    max_wrong_times: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expire_seconds: None | str | Unset
        if isinstance(self.expire_seconds, Unset):
            expire_seconds = UNSET
        else:
            expire_seconds = self.expire_seconds

        length: None | str | Unset
        if isinstance(self.length, Unset):
            length = UNSET
        else:
            length = self.length

        lock_seconds: None | str | Unset
        if isinstance(self.lock_seconds, Unset):
            lock_seconds = UNSET
        else:
            lock_seconds = self.lock_seconds

        max_wrong_times: None | str | Unset
        if isinstance(self.max_wrong_times, Unset):
            max_wrong_times = UNSET
        else:
            max_wrong_times = self.max_wrong_times

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expire_seconds is not UNSET:
            field_dict["expireSeconds"] = expire_seconds
        if length is not UNSET:
            field_dict["length"] = length
        if lock_seconds is not UNSET:
            field_dict["lockSeconds"] = lock_seconds
        if max_wrong_times is not UNSET:
            field_dict["maxWrongTimes"] = max_wrong_times

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expire_seconds(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expire_seconds = _parse_expire_seconds(d.pop("expireSeconds", UNSET))

        def _parse_length(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        length = _parse_length(d.pop("length", UNSET))

        def _parse_lock_seconds(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lock_seconds = _parse_lock_seconds(d.pop("lockSeconds", UNSET))

        def _parse_max_wrong_times(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_wrong_times = _parse_max_wrong_times(d.pop("maxWrongTimes", UNSET))

        pair_vehicle_otp_config = cls(
            expire_seconds=expire_seconds,
            length=length,
            lock_seconds=lock_seconds,
            max_wrong_times=max_wrong_times,
        )

        pair_vehicle_otp_config.additional_properties = d
        return pair_vehicle_otp_config

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
