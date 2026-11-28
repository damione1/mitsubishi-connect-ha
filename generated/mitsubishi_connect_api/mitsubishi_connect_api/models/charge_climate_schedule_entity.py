from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_climate_program_entity import ChargeClimateProgramEntity
    from ..models.hvac_settings import HvacSettings


T = TypeVar("T", bound="ChargeClimateScheduleEntity")


@_attrs_define
class ChargeClimateScheduleEntity:
    """
    Attributes:
        charge_duration (int | None | Unset):
        charge_mode_rq (None | str | Unset):
        charge_time_start (None | str | Unset):
        delegated_activated (bool | None | Unset):
        hvac_settings (HvacSettings | Unset): Cabin comfort / winter HVAC options (0 = OFF, 1+ = ON / level)
        is_schedule_with_local_time (bool | Unset):  Default: False.
        last_settings_update_timestamp (None | str | Unset):
        preconditioning_temperature (None | str | Unset):
        programs (list[ChargeClimateProgramEntity] | Unset):
        temperature_unit (None | str | Unset): Temperature unit, `C` or `F`. Example: C.
    """

    charge_duration: int | None | Unset = UNSET
    charge_mode_rq: None | str | Unset = UNSET
    charge_time_start: None | str | Unset = UNSET
    delegated_activated: bool | None | Unset = UNSET
    hvac_settings: HvacSettings | Unset = UNSET
    is_schedule_with_local_time: bool | Unset = False
    last_settings_update_timestamp: None | str | Unset = UNSET
    preconditioning_temperature: None | str | Unset = UNSET
    programs: list[ChargeClimateProgramEntity] | Unset = UNSET
    temperature_unit: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_duration: int | None | Unset
        if isinstance(self.charge_duration, Unset):
            charge_duration = UNSET
        else:
            charge_duration = self.charge_duration

        charge_mode_rq: None | str | Unset
        if isinstance(self.charge_mode_rq, Unset):
            charge_mode_rq = UNSET
        else:
            charge_mode_rq = self.charge_mode_rq

        charge_time_start: None | str | Unset
        if isinstance(self.charge_time_start, Unset):
            charge_time_start = UNSET
        else:
            charge_time_start = self.charge_time_start

        delegated_activated: bool | None | Unset
        if isinstance(self.delegated_activated, Unset):
            delegated_activated = UNSET
        else:
            delegated_activated = self.delegated_activated

        hvac_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hvac_settings, Unset):
            hvac_settings = self.hvac_settings.to_dict()

        is_schedule_with_local_time = self.is_schedule_with_local_time

        last_settings_update_timestamp: None | str | Unset
        if isinstance(self.last_settings_update_timestamp, Unset):
            last_settings_update_timestamp = UNSET
        else:
            last_settings_update_timestamp = self.last_settings_update_timestamp

        preconditioning_temperature: None | str | Unset
        if isinstance(self.preconditioning_temperature, Unset):
            preconditioning_temperature = UNSET
        else:
            preconditioning_temperature = self.preconditioning_temperature

        programs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.programs, Unset):
            programs = []
            for programs_item_data in self.programs:
                programs_item = programs_item_data.to_dict()
                programs.append(programs_item)

        temperature_unit: None | str | Unset
        if isinstance(self.temperature_unit, Unset):
            temperature_unit = UNSET
        else:
            temperature_unit = self.temperature_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_duration is not UNSET:
            field_dict["chargeDuration"] = charge_duration
        if charge_mode_rq is not UNSET:
            field_dict["chargeModeRq"] = charge_mode_rq
        if charge_time_start is not UNSET:
            field_dict["chargeTimeStart"] = charge_time_start
        if delegated_activated is not UNSET:
            field_dict["delegatedActivated"] = delegated_activated
        if hvac_settings is not UNSET:
            field_dict["hvacSettings"] = hvac_settings
        if is_schedule_with_local_time is not UNSET:
            field_dict["isScheduleWithLocalTime"] = is_schedule_with_local_time
        if last_settings_update_timestamp is not UNSET:
            field_dict["lastSettingsUpdateTimestamp"] = last_settings_update_timestamp
        if preconditioning_temperature is not UNSET:
            field_dict["preconditioningTemperature"] = preconditioning_temperature
        if programs is not UNSET:
            field_dict["programs"] = programs
        if temperature_unit is not UNSET:
            field_dict["temperatureUnit"] = temperature_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.charge_climate_program_entity import ChargeClimateProgramEntity  # noqa: PLC0415
        from ..models.hvac_settings import HvacSettings  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_charge_duration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        charge_duration = _parse_charge_duration(d.pop("chargeDuration", UNSET))

        def _parse_charge_mode_rq(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        charge_mode_rq = _parse_charge_mode_rq(d.pop("chargeModeRq", UNSET))

        def _parse_charge_time_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        charge_time_start = _parse_charge_time_start(d.pop("chargeTimeStart", UNSET))

        def _parse_delegated_activated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delegated_activated = _parse_delegated_activated(d.pop("delegatedActivated", UNSET))

        _hvac_settings = d.pop("hvacSettings", UNSET)
        hvac_settings: HvacSettings | Unset
        if isinstance(_hvac_settings, Unset):
            hvac_settings = UNSET
        else:
            hvac_settings = HvacSettings.from_dict(_hvac_settings)

        is_schedule_with_local_time = d.pop("isScheduleWithLocalTime", UNSET)

        def _parse_last_settings_update_timestamp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_settings_update_timestamp = _parse_last_settings_update_timestamp(
            d.pop("lastSettingsUpdateTimestamp", UNSET)
        )

        def _parse_preconditioning_temperature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preconditioning_temperature = _parse_preconditioning_temperature(d.pop("preconditioningTemperature", UNSET))

        _programs = d.pop("programs", UNSET)
        programs: list[ChargeClimateProgramEntity] | Unset = UNSET
        if _programs is not UNSET:
            programs = []
            for programs_item_data in _programs:
                programs_item = ChargeClimateProgramEntity.from_dict(programs_item_data)

                programs.append(programs_item)

        def _parse_temperature_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        temperature_unit = _parse_temperature_unit(d.pop("temperatureUnit", UNSET))

        charge_climate_schedule_entity = cls(
            charge_duration=charge_duration,
            charge_mode_rq=charge_mode_rq,
            charge_time_start=charge_time_start,
            delegated_activated=delegated_activated,
            hvac_settings=hvac_settings,
            is_schedule_with_local_time=is_schedule_with_local_time,
            last_settings_update_timestamp=last_settings_update_timestamp,
            preconditioning_temperature=preconditioning_temperature,
            programs=programs,
            temperature_unit=temperature_unit,
        )

        charge_climate_schedule_entity.additional_properties = d
        return charge_climate_schedule_entity

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
