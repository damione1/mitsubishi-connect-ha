from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CheckVersionResponse")


@_attrs_define
class CheckVersionResponse:
    """
    Attributes:
        enc_key (str):
        sign_key (str):
    """

    enc_key: str
    sign_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enc_key = self.enc_key

        sign_key = self.sign_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encKey": enc_key,
                "signKey": sign_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enc_key = d.pop("encKey")

        sign_key = d.pop("signKey")

        check_version_response = cls(
            enc_key=enc_key,
            sign_key=sign_key,
        )

        check_version_response.additional_properties = d
        return check_version_response

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
