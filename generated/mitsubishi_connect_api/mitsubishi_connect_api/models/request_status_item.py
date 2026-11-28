from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestStatusItem")


@_attrs_define
class RequestStatusItem:
    """
    Attributes:
        request_id (str | Unset): Asynchronous command id, poll it with `getBatchRequestStatus`. Example:
            REQ-00000000-0000-0000-0000-000000000000.
        status (int | Unset): 1 in progress, 2 success, any other value failed. Default: 0.
    """

    request_id: str | Unset = UNSET
    status: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_id = self.request_id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        request_id = d.pop("requestId", UNSET)

        status = d.pop("status", UNSET)

        request_status_item = cls(
            request_id=request_id,
            status=status,
        )

        request_status_item.additional_properties = d
        return request_status_item

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
