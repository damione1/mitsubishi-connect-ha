from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleDetailEntity")


@_attrs_define
class ScheduleDetailEntity:
    """
    Attributes:
        day_interval (int | None | Unset):
        end_date (None | str | Unset):
        end_time_of_day (None | str | Unset):
        every_friday (int | None | Unset):
        every_monday (int | None | Unset):
        every_saturday (int | None | Unset):
        every_sunday (int | None | Unset):
        every_thursday (int | None | Unset):
        every_tuesday (int | None | Unset):
        every_wednesday (int | None | Unset):
        is_schedule_with_local_time (bool | Unset):
        service_schedule_type (None | str | Unset):
        start_date (None | str | Unset):
        start_time_of_day (None | str | Unset):
    """

    day_interval: int | None | Unset = UNSET
    end_date: None | str | Unset = UNSET
    end_time_of_day: None | str | Unset = UNSET
    every_friday: int | None | Unset = UNSET
    every_monday: int | None | Unset = UNSET
    every_saturday: int | None | Unset = UNSET
    every_sunday: int | None | Unset = UNSET
    every_thursday: int | None | Unset = UNSET
    every_tuesday: int | None | Unset = UNSET
    every_wednesday: int | None | Unset = UNSET
    is_schedule_with_local_time: bool | Unset = UNSET
    service_schedule_type: None | str | Unset = UNSET
    start_date: None | str | Unset = UNSET
    start_time_of_day: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_interval: int | None | Unset
        if isinstance(self.day_interval, Unset):
            day_interval = UNSET
        else:
            day_interval = self.day_interval

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        end_time_of_day: None | str | Unset
        if isinstance(self.end_time_of_day, Unset):
            end_time_of_day = UNSET
        else:
            end_time_of_day = self.end_time_of_day

        every_friday: int | None | Unset
        if isinstance(self.every_friday, Unset):
            every_friday = UNSET
        else:
            every_friday = self.every_friday

        every_monday: int | None | Unset
        if isinstance(self.every_monday, Unset):
            every_monday = UNSET
        else:
            every_monday = self.every_monday

        every_saturday: int | None | Unset
        if isinstance(self.every_saturday, Unset):
            every_saturday = UNSET
        else:
            every_saturday = self.every_saturday

        every_sunday: int | None | Unset
        if isinstance(self.every_sunday, Unset):
            every_sunday = UNSET
        else:
            every_sunday = self.every_sunday

        every_thursday: int | None | Unset
        if isinstance(self.every_thursday, Unset):
            every_thursday = UNSET
        else:
            every_thursday = self.every_thursday

        every_tuesday: int | None | Unset
        if isinstance(self.every_tuesday, Unset):
            every_tuesday = UNSET
        else:
            every_tuesday = self.every_tuesday

        every_wednesday: int | None | Unset
        if isinstance(self.every_wednesday, Unset):
            every_wednesday = UNSET
        else:
            every_wednesday = self.every_wednesday

        is_schedule_with_local_time = self.is_schedule_with_local_time

        service_schedule_type: None | str | Unset
        if isinstance(self.service_schedule_type, Unset):
            service_schedule_type = UNSET
        else:
            service_schedule_type = self.service_schedule_type

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        start_time_of_day: None | str | Unset
        if isinstance(self.start_time_of_day, Unset):
            start_time_of_day = UNSET
        else:
            start_time_of_day = self.start_time_of_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day_interval is not UNSET:
            field_dict["dayInterval"] = day_interval
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if end_time_of_day is not UNSET:
            field_dict["endTimeOfDay"] = end_time_of_day
        if every_friday is not UNSET:
            field_dict["everyFriday"] = every_friday
        if every_monday is not UNSET:
            field_dict["everyMonday"] = every_monday
        if every_saturday is not UNSET:
            field_dict["everySaturday"] = every_saturday
        if every_sunday is not UNSET:
            field_dict["everySunday"] = every_sunday
        if every_thursday is not UNSET:
            field_dict["everyThursday"] = every_thursday
        if every_tuesday is not UNSET:
            field_dict["everyTuesday"] = every_tuesday
        if every_wednesday is not UNSET:
            field_dict["everyWednesday"] = every_wednesday
        if is_schedule_with_local_time is not UNSET:
            field_dict["isScheduleWithLocalTime"] = is_schedule_with_local_time
        if service_schedule_type is not UNSET:
            field_dict["serviceScheduleType"] = service_schedule_type
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if start_time_of_day is not UNSET:
            field_dict["startTimeOfDay"] = start_time_of_day

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_day_interval(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        day_interval = _parse_day_interval(d.pop("dayInterval", UNSET))

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        def _parse_end_time_of_day(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_time_of_day = _parse_end_time_of_day(d.pop("endTimeOfDay", UNSET))

        def _parse_every_friday(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        every_friday = _parse_every_friday(d.pop("everyFriday", UNSET))

        def _parse_every_monday(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        every_monday = _parse_every_monday(d.pop("everyMonday", UNSET))

        def _parse_every_saturday(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        every_saturday = _parse_every_saturday(d.pop("everySaturday", UNSET))

        def _parse_every_sunday(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        every_sunday = _parse_every_sunday(d.pop("everySunday", UNSET))

        def _parse_every_thursday(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        every_thursday = _parse_every_thursday(d.pop("everyThursday", UNSET))

        def _parse_every_tuesday(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        every_tuesday = _parse_every_tuesday(d.pop("everyTuesday", UNSET))

        def _parse_every_wednesday(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        every_wednesday = _parse_every_wednesday(d.pop("everyWednesday", UNSET))

        is_schedule_with_local_time = d.pop("isScheduleWithLocalTime", UNSET)

        def _parse_service_schedule_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_schedule_type = _parse_service_schedule_type(d.pop("serviceScheduleType", UNSET))

        def _parse_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_start_time_of_day(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_time_of_day = _parse_start_time_of_day(d.pop("startTimeOfDay", UNSET))

        schedule_detail_entity = cls(
            day_interval=day_interval,
            end_date=end_date,
            end_time_of_day=end_time_of_day,
            every_friday=every_friday,
            every_monday=every_monday,
            every_saturday=every_saturday,
            every_sunday=every_sunday,
            every_thursday=every_thursday,
            every_tuesday=every_tuesday,
            every_wednesday=every_wednesday,
            is_schedule_with_local_time=is_schedule_with_local_time,
            service_schedule_type=service_schedule_type,
            start_date=start_date,
            start_time_of_day=start_time_of_day,
        )

        schedule_detail_entity.additional_properties = d
        return schedule_detail_entity

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
