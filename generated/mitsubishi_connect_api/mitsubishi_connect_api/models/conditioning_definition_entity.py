from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hvac_settings import HvacSettings
    from ..models.schedule_detail_entity import ScheduleDetailEntity


T = TypeVar("T", bound="ConditioningDefinitionEntity")


@_attrs_define
class ConditioningDefinitionEntity:
    """
    Attributes:
        conditioning_action (None | str | Unset):
        conditioning_id (None | str | Unset):
        conditioning_name (None | str | Unset):
        conditioning_status (None | str | Unset):
        front_temperature (None | str | Unset):
        hvac_settings (HvacSettings | Unset): Cabin comfort / winter HVAC options (0 = OFF, 1+ = ON / level)
        is_add_manually (bool | Unset):
        schedule (ScheduleDetailEntity | Unset):
        temperature_unit (None | str | Unset): Temperature unit, `C` or `F`. Example: C.
    """

    conditioning_action: None | str | Unset = UNSET
    conditioning_id: None | str | Unset = UNSET
    conditioning_name: None | str | Unset = UNSET
    conditioning_status: None | str | Unset = UNSET
    front_temperature: None | str | Unset = UNSET
    hvac_settings: HvacSettings | Unset = UNSET
    is_add_manually: bool | Unset = UNSET
    schedule: ScheduleDetailEntity | Unset = UNSET
    temperature_unit: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditioning_action: None | str | Unset
        if isinstance(self.conditioning_action, Unset):
            conditioning_action = UNSET
        else:
            conditioning_action = self.conditioning_action

        conditioning_id: None | str | Unset
        if isinstance(self.conditioning_id, Unset):
            conditioning_id = UNSET
        else:
            conditioning_id = self.conditioning_id

        conditioning_name: None | str | Unset
        if isinstance(self.conditioning_name, Unset):
            conditioning_name = UNSET
        else:
            conditioning_name = self.conditioning_name

        conditioning_status: None | str | Unset
        if isinstance(self.conditioning_status, Unset):
            conditioning_status = UNSET
        else:
            conditioning_status = self.conditioning_status

        front_temperature: None | str | Unset
        if isinstance(self.front_temperature, Unset):
            front_temperature = UNSET
        else:
            front_temperature = self.front_temperature

        hvac_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hvac_settings, Unset):
            hvac_settings = self.hvac_settings.to_dict()

        is_add_manually = self.is_add_manually

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        temperature_unit: None | str | Unset
        if isinstance(self.temperature_unit, Unset):
            temperature_unit = UNSET
        else:
            temperature_unit = self.temperature_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conditioning_action is not UNSET:
            field_dict["conditioningAction"] = conditioning_action
        if conditioning_id is not UNSET:
            field_dict["conditioningId"] = conditioning_id
        if conditioning_name is not UNSET:
            field_dict["conditioningName"] = conditioning_name
        if conditioning_status is not UNSET:
            field_dict["conditioningStatus"] = conditioning_status
        if front_temperature is not UNSET:
            field_dict["frontTemperature"] = front_temperature
        if hvac_settings is not UNSET:
            field_dict["hvacSettings"] = hvac_settings
        if is_add_manually is not UNSET:
            field_dict["isAddManually"] = is_add_manually
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if temperature_unit is not UNSET:
            field_dict["temperatureUnit"] = temperature_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hvac_settings import HvacSettings  # noqa: PLC0415
        from ..models.schedule_detail_entity import ScheduleDetailEntity  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_conditioning_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conditioning_action = _parse_conditioning_action(d.pop("conditioningAction", UNSET))

        def _parse_conditioning_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conditioning_id = _parse_conditioning_id(d.pop("conditioningId", UNSET))

        def _parse_conditioning_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conditioning_name = _parse_conditioning_name(d.pop("conditioningName", UNSET))

        def _parse_conditioning_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conditioning_status = _parse_conditioning_status(d.pop("conditioningStatus", UNSET))

        def _parse_front_temperature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        front_temperature = _parse_front_temperature(d.pop("frontTemperature", UNSET))

        _hvac_settings = d.pop("hvacSettings", UNSET)
        hvac_settings: HvacSettings | Unset
        if isinstance(_hvac_settings, Unset):
            hvac_settings = UNSET
        else:
            hvac_settings = HvacSettings.from_dict(_hvac_settings)

        is_add_manually = d.pop("isAddManually", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: ScheduleDetailEntity | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = ScheduleDetailEntity.from_dict(_schedule)

        def _parse_temperature_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        temperature_unit = _parse_temperature_unit(d.pop("temperatureUnit", UNSET))

        conditioning_definition_entity = cls(
            conditioning_action=conditioning_action,
            conditioning_id=conditioning_id,
            conditioning_name=conditioning_name,
            conditioning_status=conditioning_status,
            front_temperature=front_temperature,
            hvac_settings=hvac_settings,
            is_add_manually=is_add_manually,
            schedule=schedule,
            temperature_unit=temperature_unit,
        )

        conditioning_definition_entity.additional_properties = d
        return conditioning_definition_entity

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
