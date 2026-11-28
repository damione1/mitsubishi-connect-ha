from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_status_item import RequestStatusItem


T = TypeVar("T", bound="BatchRequestStatusResponse")


@_attrs_define
class BatchRequestStatusResponse:
    """App model `MMBatchRequestStatusEntity`.

    Attributes:
        request_status_list (list[RequestStatusItem] | Unset):
    """

    request_status_list: list[RequestStatusItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_status_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.request_status_list, Unset):
            request_status_list = []
            for request_status_list_item_data in self.request_status_list:
                request_status_list_item = request_status_list_item_data.to_dict()
                request_status_list.append(request_status_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_status_list is not UNSET:
            field_dict["requestStatusList"] = request_status_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_status_item import RequestStatusItem  # noqa: PLC0415

        d = dict(src_dict)
        _request_status_list = d.pop("requestStatusList", UNSET)
        request_status_list: list[RequestStatusItem] | Unset = UNSET
        if _request_status_list is not UNSET:
            request_status_list = []
            for request_status_list_item_data in _request_status_list:
                request_status_list_item = RequestStatusItem.from_dict(request_status_list_item_data)

                request_status_list.append(request_status_list_item)

        batch_request_status_response = cls(
            request_status_list=request_status_list,
        )

        batch_request_status_response.additional_properties = d
        return batch_request_status_response

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
