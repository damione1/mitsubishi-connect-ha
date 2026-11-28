from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_curfew_alert_request_curfew_status import UpdateCurfewAlertRequestCurfewStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCurfewAlertRequest")


@_attrs_define
class UpdateCurfewAlertRequest:
    """
    Attributes:
        curfew_id (str):
        curfew_status (UpdateCurfewAlertRequestCurfewStatus): 0 disabled, 1 enabled.
        duration (float):
        is_schedule_with_local_time (bool):
        start_date_time (str):
        curfew_name (None | str | Unset):
        days (list[str] | Unset):
        direction (int | None | Unset):
        internal_vin (None | str | Unset): Internal VIN from `getVehicleList` (`vinList`), omitted when not provided.
            Example: JA4XXXXXXXXXXXXXX.
        support_polling_flag (bool | None | Unset): When `true`, the server returns a `requestId` to poll with
            `getBatchRequestStatus`.
        vin (None | str | Unset): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls.
            Example: JA4XXXXXXXXXXXXXX.
    """

    curfew_id: str
    curfew_status: UpdateCurfewAlertRequestCurfewStatus
    duration: float
    is_schedule_with_local_time: bool
    start_date_time: str
    curfew_name: None | str | Unset = UNSET
    days: list[str] | Unset = UNSET
    direction: int | None | Unset = UNSET
    internal_vin: None | str | Unset = UNSET
    support_polling_flag: bool | None | Unset = UNSET
    vin: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        curfew_id = self.curfew_id

        curfew_status = self.curfew_status.value

        duration = self.duration

        is_schedule_with_local_time = self.is_schedule_with_local_time

        start_date_time = self.start_date_time

        curfew_name: None | str | Unset
        if isinstance(self.curfew_name, Unset):
            curfew_name = UNSET
        else:
            curfew_name = self.curfew_name

        days: list[str] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = self.days

        direction: int | None | Unset
        if isinstance(self.direction, Unset):
            direction = UNSET
        else:
            direction = self.direction

        internal_vin: None | str | Unset
        if isinstance(self.internal_vin, Unset):
            internal_vin = UNSET
        else:
            internal_vin = self.internal_vin

        support_polling_flag: bool | None | Unset
        if isinstance(self.support_polling_flag, Unset):
            support_polling_flag = UNSET
        else:
            support_polling_flag = self.support_polling_flag

        vin: None | str | Unset
        if isinstance(self.vin, Unset):
            vin = UNSET
        else:
            vin = self.vin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "curfewId": curfew_id,
                "curfewStatus": curfew_status,
                "duration": duration,
                "isScheduleWithLocalTime": is_schedule_with_local_time,
                "startDateTime": start_date_time,
            }
        )
        if curfew_name is not UNSET:
            field_dict["curfewName"] = curfew_name
        if days is not UNSET:
            field_dict["days"] = days
        if direction is not UNSET:
            field_dict["direction"] = direction
        if internal_vin is not UNSET:
            field_dict["internalVin"] = internal_vin
        if support_polling_flag is not UNSET:
            field_dict["supportPollingFlag"] = support_polling_flag
        if vin is not UNSET:
            field_dict["vin"] = vin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        curfew_id = d.pop("curfewId")

        curfew_status = UpdateCurfewAlertRequestCurfewStatus(d.pop("curfewStatus"))

        duration = d.pop("duration")

        is_schedule_with_local_time = d.pop("isScheduleWithLocalTime")

        start_date_time = d.pop("startDateTime")

        def _parse_curfew_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        curfew_name = _parse_curfew_name(d.pop("curfewName", UNSET))

        days = cast(list[str], d.pop("days", UNSET))

        def _parse_direction(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        direction = _parse_direction(d.pop("direction", UNSET))

        def _parse_internal_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_vin = _parse_internal_vin(d.pop("internalVin", UNSET))

        def _parse_support_polling_flag(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        support_polling_flag = _parse_support_polling_flag(d.pop("supportPollingFlag", UNSET))

        def _parse_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vin = _parse_vin(d.pop("vin", UNSET))

        update_curfew_alert_request = cls(
            curfew_id=curfew_id,
            curfew_status=curfew_status,
            duration=duration,
            is_schedule_with_local_time=is_schedule_with_local_time,
            start_date_time=start_date_time,
            curfew_name=curfew_name,
            days=days,
            direction=direction,
            internal_vin=internal_vin,
            support_polling_flag=support_polling_flag,
            vin=vin,
        )

        update_curfew_alert_request.additional_properties = d
        return update_curfew_alert_request

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
