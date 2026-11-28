from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurfewAlertItem")


@_attrs_define
class CurfewAlertItem:
    """
    Attributes:
        curfew_id (None | str | Unset):
        curfew_name (None | str | Unset):
        curfew_status (int | None | Unset):
        days (list[str] | Unset):
        direction (int | None | Unset):
        duration (float | None | Unset):
        is_delete_check (bool | None | Unset):  Default: False.
        is_schedule_with_local_time (bool | None | Unset):  Default: False.
        start_date_time (None | str | Unset):
    """

    curfew_id: None | str | Unset = UNSET
    curfew_name: None | str | Unset = UNSET
    curfew_status: int | None | Unset = UNSET
    days: list[str] | Unset = UNSET
    direction: int | None | Unset = UNSET
    duration: float | None | Unset = UNSET
    is_delete_check: bool | None | Unset = False
    is_schedule_with_local_time: bool | None | Unset = False
    start_date_time: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        curfew_id: None | str | Unset
        if isinstance(self.curfew_id, Unset):
            curfew_id = UNSET
        else:
            curfew_id = self.curfew_id

        curfew_name: None | str | Unset
        if isinstance(self.curfew_name, Unset):
            curfew_name = UNSET
        else:
            curfew_name = self.curfew_name

        curfew_status: int | None | Unset
        if isinstance(self.curfew_status, Unset):
            curfew_status = UNSET
        else:
            curfew_status = self.curfew_status

        days: list[str] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = self.days

        direction: int | None | Unset
        if isinstance(self.direction, Unset):
            direction = UNSET
        else:
            direction = self.direction

        duration: float | None | Unset
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        is_delete_check: bool | None | Unset
        if isinstance(self.is_delete_check, Unset):
            is_delete_check = UNSET
        else:
            is_delete_check = self.is_delete_check

        is_schedule_with_local_time: bool | None | Unset
        if isinstance(self.is_schedule_with_local_time, Unset):
            is_schedule_with_local_time = UNSET
        else:
            is_schedule_with_local_time = self.is_schedule_with_local_time

        start_date_time: None | str | Unset
        if isinstance(self.start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = self.start_date_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if curfew_id is not UNSET:
            field_dict["curfewId"] = curfew_id
        if curfew_name is not UNSET:
            field_dict["curfewName"] = curfew_name
        if curfew_status is not UNSET:
            field_dict["curfewStatus"] = curfew_status
        if days is not UNSET:
            field_dict["days"] = days
        if direction is not UNSET:
            field_dict["direction"] = direction
        if duration is not UNSET:
            field_dict["duration"] = duration
        if is_delete_check is not UNSET:
            field_dict["isDeleteCheck"] = is_delete_check
        if is_schedule_with_local_time is not UNSET:
            field_dict["isScheduleWithLocalTime"] = is_schedule_with_local_time
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_curfew_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        curfew_id = _parse_curfew_id(d.pop("curfewId", UNSET))

        def _parse_curfew_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        curfew_name = _parse_curfew_name(d.pop("curfewName", UNSET))

        def _parse_curfew_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        curfew_status = _parse_curfew_status(d.pop("curfewStatus", UNSET))

        days = cast(list[str], d.pop("days", UNSET))

        def _parse_direction(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        direction = _parse_direction(d.pop("direction", UNSET))

        def _parse_duration(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration = _parse_duration(d.pop("duration", UNSET))

        def _parse_is_delete_check(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_delete_check = _parse_is_delete_check(d.pop("isDeleteCheck", UNSET))

        def _parse_is_schedule_with_local_time(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_schedule_with_local_time = _parse_is_schedule_with_local_time(d.pop("isScheduleWithLocalTime", UNSET))

        def _parse_start_date_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date_time = _parse_start_date_time(d.pop("startDateTime", UNSET))

        curfew_alert_item = cls(
            curfew_id=curfew_id,
            curfew_name=curfew_name,
            curfew_status=curfew_status,
            days=days,
            direction=direction,
            duration=duration,
            is_delete_check=is_delete_check,
            is_schedule_with_local_time=is_schedule_with_local_time,
            start_date_time=start_date_time,
        )

        curfew_alert_item.additional_properties = d
        return curfew_alert_item

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
