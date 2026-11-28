from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.idm_tokens_data import IdmTokensData


T = TypeVar("T", bound="IdmTokensResponse")


@_attrs_define
class IdmTokensResponse:
    """
    Attributes:
        code (str | Unset):
        error (None | str | Unset):
        error_description (None | str | Unset):
        message (str | Unset):
        data (IdmTokensData | Unset):
    """

    code: str | Unset = UNSET
    error: None | str | Unset = UNSET
    error_description: None | str | Unset = UNSET
    message: str | Unset = UNSET
    data: IdmTokensData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        error_description: None | str | Unset
        if isinstance(self.error_description, Unset):
            error_description = UNSET
        else:
            error_description = self.error_description

        message = self.message

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if error is not UNSET:
            field_dict["error"] = error
        if error_description is not UNSET:
            field_dict["error_description"] = error_description
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.idm_tokens_data import IdmTokensData  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_error_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_description = _parse_error_description(d.pop("error_description", UNSET))

        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: IdmTokensData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = IdmTokensData.from_dict(_data)

        idm_tokens_response = cls(
            code=code,
            error=error,
            error_description=error_description,
            message=message,
            data=data,
        )

        idm_tokens_response.additional_properties = d
        return idm_tokens_response

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
