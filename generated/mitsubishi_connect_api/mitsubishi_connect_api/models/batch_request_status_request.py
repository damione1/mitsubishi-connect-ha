from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.request_id_item import RequestIdItem


T = TypeVar("T", bound="BatchRequestStatusRequest")


@_attrs_define
class BatchRequestStatusRequest:
    """
    Attributes:
        request_id_list (list[RequestIdItem]):
    """

    request_id_list: list[RequestIdItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_id_list = []
        for request_id_list_item_data in self.request_id_list:
            request_id_list_item = request_id_list_item_data.to_dict()
            request_id_list.append(request_id_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestIdList": request_id_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_id_item import RequestIdItem  # noqa: PLC0415

        d = dict(src_dict)
        request_id_list = []
        _request_id_list = d.pop("requestIdList")
        for request_id_list_item_data in _request_id_list:
            request_id_list_item = RequestIdItem.from_dict(request_id_list_item_data)

            request_id_list.append(request_id_list_item)

        batch_request_status_request = cls(
            request_id_list=request_id_list,
        )

        batch_request_status_request.additional_properties = d
        return batch_request_status_request

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
