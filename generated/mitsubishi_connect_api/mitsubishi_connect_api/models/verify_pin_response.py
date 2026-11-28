from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyPinResponse")


@_attrs_define
class VerifyPinResponse:
    """
    Attributes:
        is_valid_pin (bool | None | Unset):  Default: True.
    """

    is_valid_pin: bool | None | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_valid_pin: bool | None | Unset
        if isinstance(self.is_valid_pin, Unset):
            is_valid_pin = UNSET
        else:
            is_valid_pin = self.is_valid_pin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_valid_pin is not UNSET:
            field_dict["isValidPIN"] = is_valid_pin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_is_valid_pin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_valid_pin = _parse_is_valid_pin(d.pop("isValidPIN", UNSET))

        verify_pin_response = cls(
            is_valid_pin=is_valid_pin,
        )

        verify_pin_response.additional_properties = d
        return verify_pin_response

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
