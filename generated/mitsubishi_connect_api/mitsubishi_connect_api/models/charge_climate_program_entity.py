from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChargeClimateProgramEntity")


@_attrs_define
class ChargeClimateProgramEntity:
    """
    Attributes:
        program_activation_friday (bool | None | Unset):
        program_activation_monday (bool | None | Unset):
        program_activation_saturday (bool | None | Unset):
        program_activation_status (bool | None | Unset):
        program_activation_sunday (bool | None | Unset):
        program_activation_thursday (bool | None | Unset):
        program_activation_tuesday (bool | None | Unset):
        program_activation_wednesday (bool | None | Unset):
        program_departure_time (None | str | Unset):
        program_type (None | str | Unset):
    """

    program_activation_friday: bool | None | Unset = UNSET
    program_activation_monday: bool | None | Unset = UNSET
    program_activation_saturday: bool | None | Unset = UNSET
    program_activation_status: bool | None | Unset = UNSET
    program_activation_sunday: bool | None | Unset = UNSET
    program_activation_thursday: bool | None | Unset = UNSET
    program_activation_tuesday: bool | None | Unset = UNSET
    program_activation_wednesday: bool | None | Unset = UNSET
    program_departure_time: None | str | Unset = UNSET
    program_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        program_activation_friday: bool | None | Unset
        if isinstance(self.program_activation_friday, Unset):
            program_activation_friday = UNSET
        else:
            program_activation_friday = self.program_activation_friday

        program_activation_monday: bool | None | Unset
        if isinstance(self.program_activation_monday, Unset):
            program_activation_monday = UNSET
        else:
            program_activation_monday = self.program_activation_monday

        program_activation_saturday: bool | None | Unset
        if isinstance(self.program_activation_saturday, Unset):
            program_activation_saturday = UNSET
        else:
            program_activation_saturday = self.program_activation_saturday

        program_activation_status: bool | None | Unset
        if isinstance(self.program_activation_status, Unset):
            program_activation_status = UNSET
        else:
            program_activation_status = self.program_activation_status

        program_activation_sunday: bool | None | Unset
        if isinstance(self.program_activation_sunday, Unset):
            program_activation_sunday = UNSET
        else:
            program_activation_sunday = self.program_activation_sunday

        program_activation_thursday: bool | None | Unset
        if isinstance(self.program_activation_thursday, Unset):
            program_activation_thursday = UNSET
        else:
            program_activation_thursday = self.program_activation_thursday

        program_activation_tuesday: bool | None | Unset
        if isinstance(self.program_activation_tuesday, Unset):
            program_activation_tuesday = UNSET
        else:
            program_activation_tuesday = self.program_activation_tuesday

        program_activation_wednesday: bool | None | Unset
        if isinstance(self.program_activation_wednesday, Unset):
            program_activation_wednesday = UNSET
        else:
            program_activation_wednesday = self.program_activation_wednesday

        program_departure_time: None | str | Unset
        if isinstance(self.program_departure_time, Unset):
            program_departure_time = UNSET
        else:
            program_departure_time = self.program_departure_time

        program_type: None | str | Unset
        if isinstance(self.program_type, Unset):
            program_type = UNSET
        else:
            program_type = self.program_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if program_activation_friday is not UNSET:
            field_dict["programActivationFriday"] = program_activation_friday
        if program_activation_monday is not UNSET:
            field_dict["programActivationMonday"] = program_activation_monday
        if program_activation_saturday is not UNSET:
            field_dict["programActivationSaturday"] = program_activation_saturday
        if program_activation_status is not UNSET:
            field_dict["programActivationStatus"] = program_activation_status
        if program_activation_sunday is not UNSET:
            field_dict["programActivationSunday"] = program_activation_sunday
        if program_activation_thursday is not UNSET:
            field_dict["programActivationThursday"] = program_activation_thursday
        if program_activation_tuesday is not UNSET:
            field_dict["programActivationTuesday"] = program_activation_tuesday
        if program_activation_wednesday is not UNSET:
            field_dict["programActivationWednesday"] = program_activation_wednesday
        if program_departure_time is not UNSET:
            field_dict["programDepartureTime"] = program_departure_time
        if program_type is not UNSET:
            field_dict["programType"] = program_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_program_activation_friday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        program_activation_friday = _parse_program_activation_friday(d.pop("programActivationFriday", UNSET))

        def _parse_program_activation_monday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        program_activation_monday = _parse_program_activation_monday(d.pop("programActivationMonday", UNSET))

        def _parse_program_activation_saturday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        program_activation_saturday = _parse_program_activation_saturday(d.pop("programActivationSaturday", UNSET))

        def _parse_program_activation_status(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        program_activation_status = _parse_program_activation_status(d.pop("programActivationStatus", UNSET))

        def _parse_program_activation_sunday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        program_activation_sunday = _parse_program_activation_sunday(d.pop("programActivationSunday", UNSET))

        def _parse_program_activation_thursday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        program_activation_thursday = _parse_program_activation_thursday(d.pop("programActivationThursday", UNSET))

        def _parse_program_activation_tuesday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        program_activation_tuesday = _parse_program_activation_tuesday(d.pop("programActivationTuesday", UNSET))

        def _parse_program_activation_wednesday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        program_activation_wednesday = _parse_program_activation_wednesday(d.pop("programActivationWednesday", UNSET))

        def _parse_program_departure_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        program_departure_time = _parse_program_departure_time(d.pop("programDepartureTime", UNSET))

        def _parse_program_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        program_type = _parse_program_type(d.pop("programType", UNSET))

        charge_climate_program_entity = cls(
            program_activation_friday=program_activation_friday,
            program_activation_monday=program_activation_monday,
            program_activation_saturday=program_activation_saturday,
            program_activation_status=program_activation_status,
            program_activation_sunday=program_activation_sunday,
            program_activation_thursday=program_activation_thursday,
            program_activation_tuesday=program_activation_tuesday,
            program_activation_wednesday=program_activation_wednesday,
            program_departure_time=program_departure_time,
            program_type=program_type,
        )

        charge_climate_program_entity.additional_properties = d
        return charge_climate_program_entity

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
