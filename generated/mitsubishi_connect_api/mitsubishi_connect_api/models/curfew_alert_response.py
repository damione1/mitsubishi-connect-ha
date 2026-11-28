from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.curfew_alert_item import CurfewAlertItem


T = TypeVar("T", bound="CurfewAlertResponse")


@_attrs_define
class CurfewAlertResponse:
    """
    Attributes:
        data (list[CurfewAlertItem] | Unset):
        support_start_time_with_offset (bool | None | Unset):
        timestamp (None | str | Unset):
        vin (None | str | Unset): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls.
            Example: JA4XXXXXXXXXXXXXX.
    """

    data: list[CurfewAlertItem] | Unset = UNSET
    support_start_time_with_offset: bool | None | Unset = UNSET
    timestamp: None | str | Unset = UNSET
    vin: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        support_start_time_with_offset: bool | None | Unset
        if isinstance(self.support_start_time_with_offset, Unset):
            support_start_time_with_offset = UNSET
        else:
            support_start_time_with_offset = self.support_start_time_with_offset

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
        if data is not UNSET:
            field_dict["data"] = data
        if support_start_time_with_offset is not UNSET:
            field_dict["supportStartTimeWithOffset"] = support_start_time_with_offset
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if vin is not UNSET:
            field_dict["vin"] = vin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.curfew_alert_item import CurfewAlertItem  # noqa: PLC0415

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[CurfewAlertItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = CurfewAlertItem.from_dict(data_item_data)

                data.append(data_item)

        def _parse_support_start_time_with_offset(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        support_start_time_with_offset = _parse_support_start_time_with_offset(
            d.pop("supportStartTimeWithOffset", UNSET)
        )

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

        curfew_alert_response = cls(
            data=data,
            support_start_time_with_offset=support_start_time_with_offset,
            timestamp=timestamp,
            vin=vin,
        )

        curfew_alert_response.additional_properties = d
        return curfew_alert_response

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
