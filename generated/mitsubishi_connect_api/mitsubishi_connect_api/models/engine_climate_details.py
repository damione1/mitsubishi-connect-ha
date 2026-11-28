from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hvac_settings import HvacSettings


T = TypeVar("T", bound="EngineClimateDetails")


@_attrs_define
class EngineClimateDetails:
    """
    Attributes:
        action (None | str | Unset):
        hvac_settings (HvacSettings | Unset): Cabin comfort / winter HVAC options (0 = OFF, 1+ = ON / level)
        is_ac_on (bool | None | Unset):  Default: False.
        is_engine_on (bool | None | Unset):  Default: False.
        target_temperature (float | None | Unset): Target cabin temperature serialized as a decimal string (one
            decimal). Example: 21.0.
        temperature_unit (None | str | Unset): Temperature unit, `C` or `F`. Example: C.
        timestamp (None | str | Unset):
        vin (None | str | Unset): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls.
            Example: JA4XXXXXXXXXXXXXX.
    """

    action: None | str | Unset = UNSET
    hvac_settings: HvacSettings | Unset = UNSET
    is_ac_on: bool | None | Unset = False
    is_engine_on: bool | None | Unset = False
    target_temperature: float | None | Unset = UNSET
    temperature_unit: None | str | Unset = UNSET
    timestamp: None | str | Unset = UNSET
    vin: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        else:
            action = self.action

        hvac_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hvac_settings, Unset):
            hvac_settings = self.hvac_settings.to_dict()

        is_ac_on: bool | None | Unset
        if isinstance(self.is_ac_on, Unset):
            is_ac_on = UNSET
        else:
            is_ac_on = self.is_ac_on

        is_engine_on: bool | None | Unset
        if isinstance(self.is_engine_on, Unset):
            is_engine_on = UNSET
        else:
            is_engine_on = self.is_engine_on

        target_temperature: float | None | Unset
        if isinstance(self.target_temperature, Unset):
            target_temperature = UNSET
        else:
            target_temperature = self.target_temperature

        temperature_unit: None | str | Unset
        if isinstance(self.temperature_unit, Unset):
            temperature_unit = UNSET
        else:
            temperature_unit = self.temperature_unit

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
        if action is not UNSET:
            field_dict["action"] = action
        if hvac_settings is not UNSET:
            field_dict["hvacSettings"] = hvac_settings
        if is_ac_on is not UNSET:
            field_dict["isACOn"] = is_ac_on
        if is_engine_on is not UNSET:
            field_dict["isEngineOn"] = is_engine_on
        if target_temperature is not UNSET:
            field_dict["targetTemperature"] = target_temperature
        if temperature_unit is not UNSET:
            field_dict["temperatureUnit"] = temperature_unit
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if vin is not UNSET:
            field_dict["vin"] = vin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hvac_settings import HvacSettings  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action = _parse_action(d.pop("action", UNSET))

        _hvac_settings = d.pop("hvacSettings", UNSET)
        hvac_settings: HvacSettings | Unset
        if isinstance(_hvac_settings, Unset):
            hvac_settings = UNSET
        else:
            hvac_settings = HvacSettings.from_dict(_hvac_settings)

        def _parse_is_ac_on(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_ac_on = _parse_is_ac_on(d.pop("isACOn", UNSET))

        def _parse_is_engine_on(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_engine_on = _parse_is_engine_on(d.pop("isEngineOn", UNSET))

        def _parse_target_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        target_temperature = _parse_target_temperature(d.pop("targetTemperature", UNSET))

        def _parse_temperature_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        temperature_unit = _parse_temperature_unit(d.pop("temperatureUnit", UNSET))

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

        engine_climate_details = cls(
            action=action,
            hvac_settings=hvac_settings,
            is_ac_on=is_ac_on,
            is_engine_on=is_engine_on,
            target_temperature=target_temperature,
            temperature_unit=temperature_unit,
            timestamp=timestamp,
            vin=vin,
        )

        engine_climate_details.additional_properties = d
        return engine_climate_details

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
