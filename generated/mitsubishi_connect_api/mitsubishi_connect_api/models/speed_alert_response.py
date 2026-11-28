from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpeedAlertResponse")


@_attrs_define
class SpeedAlertResponse:
    """
    Attributes:
        speed (int | None | Unset):
        speed_status (int | None | Unset):
        speed_unit (None | str | Unset):
        timestamp (None | str | Unset):
    """

    speed: int | None | Unset = UNSET
    speed_status: int | None | Unset = UNSET
    speed_unit: None | str | Unset = UNSET
    timestamp: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        speed: int | None | Unset
        if isinstance(self.speed, Unset):
            speed = UNSET
        else:
            speed = self.speed

        speed_status: int | None | Unset
        if isinstance(self.speed_status, Unset):
            speed_status = UNSET
        else:
            speed_status = self.speed_status

        speed_unit: None | str | Unset
        if isinstance(self.speed_unit, Unset):
            speed_unit = UNSET
        else:
            speed_unit = self.speed_unit

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if speed is not UNSET:
            field_dict["speed"] = speed
        if speed_status is not UNSET:
            field_dict["speedStatus"] = speed_status
        if speed_unit is not UNSET:
            field_dict["speedUnit"] = speed_unit
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_speed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        speed = _parse_speed(d.pop("speed", UNSET))

        def _parse_speed_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        speed_status = _parse_speed_status(d.pop("speedStatus", UNSET))

        def _parse_speed_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        speed_unit = _parse_speed_unit(d.pop("speedUnit", UNSET))

        def _parse_timestamp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        speed_alert_response = cls(
            speed=speed,
            speed_status=speed_status,
            speed_unit=speed_unit,
            timestamp=timestamp,
        )

        speed_alert_response.additional_properties = d
        return speed_alert_response

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
