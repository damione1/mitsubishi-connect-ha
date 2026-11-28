from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditioning_definition_entity import ConditioningDefinitionEntity


T = TypeVar("T", bound="ScheduleEntity")


@_attrs_define
class ScheduleEntity:
    """
    Attributes:
        action (None | str | Unset):
        conditioning_definition (list[ConditioningDefinitionEntity] | Unset):
        front_temperature (None | str | Unset):
        internal_vin (None | str | Unset): Internal VIN from `getVehicleList` (`vinList`), omitted when not provided.
            Example: JA4XXXXXXXXXXXXXX.
        is_climate_schedule (bool | None | Unset):
        support_charge_schedule_unique_id_flag (None | str | Unset):
        support_climate_schedule_unique_id_flag (None | str | Unset):
        support_polling_flag (bool | None | Unset): When `true`, the server returns a `requestId` to poll with
            `getBatchRequestStatus`.
        temperature_unit (None | str | Unset): Temperature unit, `C` or `F`. Example: C.
        timestamp (float | None | Unset):
        vin (None | str | Unset): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls.
            Example: JA4XXXXXXXXXXXXXX.
    """

    action: None | str | Unset = UNSET
    conditioning_definition: list[ConditioningDefinitionEntity] | Unset = UNSET
    front_temperature: None | str | Unset = UNSET
    internal_vin: None | str | Unset = UNSET
    is_climate_schedule: bool | None | Unset = UNSET
    support_charge_schedule_unique_id_flag: None | str | Unset = UNSET
    support_climate_schedule_unique_id_flag: None | str | Unset = UNSET
    support_polling_flag: bool | None | Unset = UNSET
    temperature_unit: None | str | Unset = UNSET
    timestamp: float | None | Unset = UNSET
    vin: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        else:
            action = self.action

        conditioning_definition: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditioning_definition, Unset):
            conditioning_definition = []
            for conditioning_definition_item_data in self.conditioning_definition:
                conditioning_definition_item = conditioning_definition_item_data.to_dict()
                conditioning_definition.append(conditioning_definition_item)

        front_temperature: None | str | Unset
        if isinstance(self.front_temperature, Unset):
            front_temperature = UNSET
        else:
            front_temperature = self.front_temperature

        internal_vin: None | str | Unset
        if isinstance(self.internal_vin, Unset):
            internal_vin = UNSET
        else:
            internal_vin = self.internal_vin

        is_climate_schedule: bool | None | Unset
        if isinstance(self.is_climate_schedule, Unset):
            is_climate_schedule = UNSET
        else:
            is_climate_schedule = self.is_climate_schedule

        support_charge_schedule_unique_id_flag: None | str | Unset
        if isinstance(self.support_charge_schedule_unique_id_flag, Unset):
            support_charge_schedule_unique_id_flag = UNSET
        else:
            support_charge_schedule_unique_id_flag = self.support_charge_schedule_unique_id_flag

        support_climate_schedule_unique_id_flag: None | str | Unset
        if isinstance(self.support_climate_schedule_unique_id_flag, Unset):
            support_climate_schedule_unique_id_flag = UNSET
        else:
            support_climate_schedule_unique_id_flag = self.support_climate_schedule_unique_id_flag

        support_polling_flag: bool | None | Unset
        if isinstance(self.support_polling_flag, Unset):
            support_polling_flag = UNSET
        else:
            support_polling_flag = self.support_polling_flag

        temperature_unit: None | str | Unset
        if isinstance(self.temperature_unit, Unset):
            temperature_unit = UNSET
        else:
            temperature_unit = self.temperature_unit

        timestamp: float | None | Unset
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
        if conditioning_definition is not UNSET:
            field_dict["conditioningDefinition"] = conditioning_definition
        if front_temperature is not UNSET:
            field_dict["frontTemperature"] = front_temperature
        if internal_vin is not UNSET:
            field_dict["internalVin"] = internal_vin
        if is_climate_schedule is not UNSET:
            field_dict["isClimateSchedule"] = is_climate_schedule
        if support_charge_schedule_unique_id_flag is not UNSET:
            field_dict["supportChargeScheduleUniqueIdFlag"] = support_charge_schedule_unique_id_flag
        if support_climate_schedule_unique_id_flag is not UNSET:
            field_dict["supportClimateScheduleUniqueIdFlag"] = support_climate_schedule_unique_id_flag
        if support_polling_flag is not UNSET:
            field_dict["supportPollingFlag"] = support_polling_flag
        if temperature_unit is not UNSET:
            field_dict["temperatureUnit"] = temperature_unit
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if vin is not UNSET:
            field_dict["vin"] = vin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditioning_definition_entity import ConditioningDefinitionEntity  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action = _parse_action(d.pop("action", UNSET))

        _conditioning_definition = d.pop("conditioningDefinition", UNSET)
        conditioning_definition: list[ConditioningDefinitionEntity] | Unset = UNSET
        if _conditioning_definition is not UNSET:
            conditioning_definition = []
            for conditioning_definition_item_data in _conditioning_definition:
                conditioning_definition_item = ConditioningDefinitionEntity.from_dict(conditioning_definition_item_data)

                conditioning_definition.append(conditioning_definition_item)

        def _parse_front_temperature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        front_temperature = _parse_front_temperature(d.pop("frontTemperature", UNSET))

        def _parse_internal_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_vin = _parse_internal_vin(d.pop("internalVin", UNSET))

        def _parse_is_climate_schedule(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_climate_schedule = _parse_is_climate_schedule(d.pop("isClimateSchedule", UNSET))

        def _parse_support_charge_schedule_unique_id_flag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_charge_schedule_unique_id_flag = _parse_support_charge_schedule_unique_id_flag(
            d.pop("supportChargeScheduleUniqueIdFlag", UNSET)
        )

        def _parse_support_climate_schedule_unique_id_flag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_climate_schedule_unique_id_flag = _parse_support_climate_schedule_unique_id_flag(
            d.pop("supportClimateScheduleUniqueIdFlag", UNSET)
        )

        def _parse_support_polling_flag(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        support_polling_flag = _parse_support_polling_flag(d.pop("supportPollingFlag", UNSET))

        def _parse_temperature_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        temperature_unit = _parse_temperature_unit(d.pop("temperatureUnit", UNSET))

        def _parse_timestamp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        def _parse_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vin = _parse_vin(d.pop("vin", UNSET))

        schedule_entity = cls(
            action=action,
            conditioning_definition=conditioning_definition,
            front_temperature=front_temperature,
            internal_vin=internal_vin,
            is_climate_schedule=is_climate_schedule,
            support_charge_schedule_unique_id_flag=support_charge_schedule_unique_id_flag,
            support_climate_schedule_unique_id_flag=support_climate_schedule_unique_id_flag,
            support_polling_flag=support_polling_flag,
            temperature_unit=temperature_unit,
            timestamp=timestamp,
            vin=vin,
        )

        schedule_entity.additional_properties = d
        return schedule_entity

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
