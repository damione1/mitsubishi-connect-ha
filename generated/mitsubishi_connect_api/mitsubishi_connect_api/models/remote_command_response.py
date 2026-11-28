from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditioning_definition_entity import ConditioningDefinitionEntity


T = TypeVar("T", bound="RemoteCommandResponse")


@_attrs_define
class RemoteCommandResponse:
    """
    Attributes:
        conditioning_definition (list[ConditioningDefinitionEntity] | Unset):
        duration (int | None | Unset):
        is_valid_pin (bool | None | Unset):  Default: True.
        keep_for_current_step (bool | Unset):  Default: False.
        keep_for_next_step (bool | Unset):  Default: False.
        polling_interval (int | None | Unset):  Default: 5.
        request_id (None | str | Unset): Asynchronous command id, poll it with `getBatchRequestStatus`. Example:
            REQ-00000000-0000-0000-0000-000000000000.
        vin (None | str | Unset): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls.
            Example: JA4XXXXXXXXXXXXXX.
    """

    conditioning_definition: list[ConditioningDefinitionEntity] | Unset = UNSET
    duration: int | None | Unset = UNSET
    is_valid_pin: bool | None | Unset = True
    keep_for_current_step: bool | Unset = False
    keep_for_next_step: bool | Unset = False
    polling_interval: int | None | Unset = 5
    request_id: None | str | Unset = UNSET
    vin: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditioning_definition: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditioning_definition, Unset):
            conditioning_definition = []
            for conditioning_definition_item_data in self.conditioning_definition:
                conditioning_definition_item = conditioning_definition_item_data.to_dict()
                conditioning_definition.append(conditioning_definition_item)

        duration: int | None | Unset
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        is_valid_pin: bool | None | Unset
        if isinstance(self.is_valid_pin, Unset):
            is_valid_pin = UNSET
        else:
            is_valid_pin = self.is_valid_pin

        keep_for_current_step = self.keep_for_current_step

        keep_for_next_step = self.keep_for_next_step

        polling_interval: int | None | Unset
        if isinstance(self.polling_interval, Unset):
            polling_interval = UNSET
        else:
            polling_interval = self.polling_interval

        request_id: None | str | Unset
        if isinstance(self.request_id, Unset):
            request_id = UNSET
        else:
            request_id = self.request_id

        vin: None | str | Unset
        if isinstance(self.vin, Unset):
            vin = UNSET
        else:
            vin = self.vin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conditioning_definition is not UNSET:
            field_dict["conditioningDefinition"] = conditioning_definition
        if duration is not UNSET:
            field_dict["duration"] = duration
        if is_valid_pin is not UNSET:
            field_dict["isValidPIN"] = is_valid_pin
        if keep_for_current_step is not UNSET:
            field_dict["keepForCurrentStep"] = keep_for_current_step
        if keep_for_next_step is not UNSET:
            field_dict["keepForNextStep"] = keep_for_next_step
        if polling_interval is not UNSET:
            field_dict["pollingInterval"] = polling_interval
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if vin is not UNSET:
            field_dict["vin"] = vin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditioning_definition_entity import ConditioningDefinitionEntity  # noqa: PLC0415

        d = dict(src_dict)
        _conditioning_definition = d.pop("conditioningDefinition", UNSET)
        conditioning_definition: list[ConditioningDefinitionEntity] | Unset = UNSET
        if _conditioning_definition is not UNSET:
            conditioning_definition = []
            for conditioning_definition_item_data in _conditioning_definition:
                conditioning_definition_item = ConditioningDefinitionEntity.from_dict(conditioning_definition_item_data)

                conditioning_definition.append(conditioning_definition_item)

        def _parse_duration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration = _parse_duration(d.pop("duration", UNSET))

        def _parse_is_valid_pin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_valid_pin = _parse_is_valid_pin(d.pop("isValidPIN", UNSET))

        keep_for_current_step = d.pop("keepForCurrentStep", UNSET)

        keep_for_next_step = d.pop("keepForNextStep", UNSET)

        def _parse_polling_interval(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        polling_interval = _parse_polling_interval(d.pop("pollingInterval", UNSET))

        def _parse_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_id = _parse_request_id(d.pop("requestId", UNSET))

        def _parse_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vin = _parse_vin(d.pop("vin", UNSET))

        remote_command_response = cls(
            conditioning_definition=conditioning_definition,
            duration=duration,
            is_valid_pin=is_valid_pin,
            keep_for_current_step=keep_for_current_step,
            keep_for_next_step=keep_for_next_step,
            polling_interval=polling_interval,
            request_id=request_id,
            vin=vin,
        )

        remote_command_response.additional_properties = d
        return remote_command_response

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
