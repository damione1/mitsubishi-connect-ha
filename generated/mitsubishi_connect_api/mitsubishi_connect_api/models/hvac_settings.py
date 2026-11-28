from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HvacSettings")


@_attrs_define
class HvacSettings:
    """Cabin comfort / winter HVAC options (0 = OFF, 1+ = ON / level)

    Attributes:
        fan_status (int | None | Unset):
        front_defrost_status (int | None | Unset):
        front_left_seat_status (int | None | Unset):
        front_right_seat_status (int | None | Unset):
        max_defrost_status (int | None | Unset):
        rear_center_seat_status (int | None | Unset):
        rear_defrost_status (int | None | Unset):
        rear_left_seat_status (int | None | Unset):
        rear_right_seat_status (int | None | Unset):
        start_date_time (None | str | Unset):
        steering_heater_status (int | None | Unset):
    """

    fan_status: int | None | Unset = UNSET
    front_defrost_status: int | None | Unset = UNSET
    front_left_seat_status: int | None | Unset = UNSET
    front_right_seat_status: int | None | Unset = UNSET
    max_defrost_status: int | None | Unset = UNSET
    rear_center_seat_status: int | None | Unset = UNSET
    rear_defrost_status: int | None | Unset = UNSET
    rear_left_seat_status: int | None | Unset = UNSET
    rear_right_seat_status: int | None | Unset = UNSET
    start_date_time: None | str | Unset = UNSET
    steering_heater_status: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fan_status: int | None | Unset
        if isinstance(self.fan_status, Unset):
            fan_status = UNSET
        else:
            fan_status = self.fan_status

        front_defrost_status: int | None | Unset
        if isinstance(self.front_defrost_status, Unset):
            front_defrost_status = UNSET
        else:
            front_defrost_status = self.front_defrost_status

        front_left_seat_status: int | None | Unset
        if isinstance(self.front_left_seat_status, Unset):
            front_left_seat_status = UNSET
        else:
            front_left_seat_status = self.front_left_seat_status

        front_right_seat_status: int | None | Unset
        if isinstance(self.front_right_seat_status, Unset):
            front_right_seat_status = UNSET
        else:
            front_right_seat_status = self.front_right_seat_status

        max_defrost_status: int | None | Unset
        if isinstance(self.max_defrost_status, Unset):
            max_defrost_status = UNSET
        else:
            max_defrost_status = self.max_defrost_status

        rear_center_seat_status: int | None | Unset
        if isinstance(self.rear_center_seat_status, Unset):
            rear_center_seat_status = UNSET
        else:
            rear_center_seat_status = self.rear_center_seat_status

        rear_defrost_status: int | None | Unset
        if isinstance(self.rear_defrost_status, Unset):
            rear_defrost_status = UNSET
        else:
            rear_defrost_status = self.rear_defrost_status

        rear_left_seat_status: int | None | Unset
        if isinstance(self.rear_left_seat_status, Unset):
            rear_left_seat_status = UNSET
        else:
            rear_left_seat_status = self.rear_left_seat_status

        rear_right_seat_status: int | None | Unset
        if isinstance(self.rear_right_seat_status, Unset):
            rear_right_seat_status = UNSET
        else:
            rear_right_seat_status = self.rear_right_seat_status

        start_date_time: None | str | Unset
        if isinstance(self.start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = self.start_date_time

        steering_heater_status: int | None | Unset
        if isinstance(self.steering_heater_status, Unset):
            steering_heater_status = UNSET
        else:
            steering_heater_status = self.steering_heater_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fan_status is not UNSET:
            field_dict["fanStatus"] = fan_status
        if front_defrost_status is not UNSET:
            field_dict["frontDefrostStatus"] = front_defrost_status
        if front_left_seat_status is not UNSET:
            field_dict["frontLeftSeatStatus"] = front_left_seat_status
        if front_right_seat_status is not UNSET:
            field_dict["frontRightSeatStatus"] = front_right_seat_status
        if max_defrost_status is not UNSET:
            field_dict["maxDefrostStatus"] = max_defrost_status
        if rear_center_seat_status is not UNSET:
            field_dict["rearCenterSeatStatus"] = rear_center_seat_status
        if rear_defrost_status is not UNSET:
            field_dict["rearDefrostStatus"] = rear_defrost_status
        if rear_left_seat_status is not UNSET:
            field_dict["rearLeftSeatStatus"] = rear_left_seat_status
        if rear_right_seat_status is not UNSET:
            field_dict["rearRightSeatStatus"] = rear_right_seat_status
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if steering_heater_status is not UNSET:
            field_dict["steeringHeaterStatus"] = steering_heater_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_fan_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fan_status = _parse_fan_status(d.pop("fanStatus", UNSET))

        def _parse_front_defrost_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        front_defrost_status = _parse_front_defrost_status(d.pop("frontDefrostStatus", UNSET))

        def _parse_front_left_seat_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        front_left_seat_status = _parse_front_left_seat_status(d.pop("frontLeftSeatStatus", UNSET))

        def _parse_front_right_seat_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        front_right_seat_status = _parse_front_right_seat_status(d.pop("frontRightSeatStatus", UNSET))

        def _parse_max_defrost_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_defrost_status = _parse_max_defrost_status(d.pop("maxDefrostStatus", UNSET))

        def _parse_rear_center_seat_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rear_center_seat_status = _parse_rear_center_seat_status(d.pop("rearCenterSeatStatus", UNSET))

        def _parse_rear_defrost_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rear_defrost_status = _parse_rear_defrost_status(d.pop("rearDefrostStatus", UNSET))

        def _parse_rear_left_seat_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rear_left_seat_status = _parse_rear_left_seat_status(d.pop("rearLeftSeatStatus", UNSET))

        def _parse_rear_right_seat_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rear_right_seat_status = _parse_rear_right_seat_status(d.pop("rearRightSeatStatus", UNSET))

        def _parse_start_date_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date_time = _parse_start_date_time(d.pop("startDateTime", UNSET))

        def _parse_steering_heater_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        steering_heater_status = _parse_steering_heater_status(d.pop("steeringHeaterStatus", UNSET))

        hvac_settings = cls(
            fan_status=fan_status,
            front_defrost_status=front_defrost_status,
            front_left_seat_status=front_left_seat_status,
            front_right_seat_status=front_right_seat_status,
            max_defrost_status=max_defrost_status,
            rear_center_seat_status=rear_center_seat_status,
            rear_defrost_status=rear_defrost_status,
            rear_left_seat_status=rear_left_seat_status,
            rear_right_seat_status=rear_right_seat_status,
            start_date_time=start_date_time,
            steering_heater_status=steering_heater_status,
        )

        hvac_settings.additional_properties = d
        return hvac_settings

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
