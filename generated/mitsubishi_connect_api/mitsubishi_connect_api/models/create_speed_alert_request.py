from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_speed_alert_request_speed_status import CreateSpeedAlertRequestSpeedStatus
from ..models.create_speed_alert_request_speed_unit import CreateSpeedAlertRequestSpeedUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSpeedAlertRequest")


@_attrs_define
class CreateSpeedAlertRequest:
    """
    Attributes:
        speed (int):
        speed_status (CreateSpeedAlertRequestSpeedStatus): 0 disabled, 1 enabled.
        speed_unit (CreateSpeedAlertRequestSpeedUnit):  Example: KMH.
        internal_vin (None | str | Unset): Internal VIN from `getVehicleList` (`vinList`), omitted when not provided.
            Example: JA4XXXXXXXXXXXXXX.
        vin (None | str | Unset): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls.
            Example: JA4XXXXXXXXXXXXXX.
    """

    speed: int
    speed_status: CreateSpeedAlertRequestSpeedStatus
    speed_unit: CreateSpeedAlertRequestSpeedUnit
    internal_vin: None | str | Unset = UNSET
    vin: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        speed = self.speed

        speed_status = self.speed_status.value

        speed_unit = self.speed_unit.value

        internal_vin: None | str | Unset
        if isinstance(self.internal_vin, Unset):
            internal_vin = UNSET
        else:
            internal_vin = self.internal_vin

        vin: None | str | Unset
        if isinstance(self.vin, Unset):
            vin = UNSET
        else:
            vin = self.vin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "speed": speed,
                "speedStatus": speed_status,
                "speedUnit": speed_unit,
            }
        )
        if internal_vin is not UNSET:
            field_dict["internalVin"] = internal_vin
        if vin is not UNSET:
            field_dict["vin"] = vin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        speed = d.pop("speed")

        speed_status = CreateSpeedAlertRequestSpeedStatus(d.pop("speedStatus"))

        speed_unit = CreateSpeedAlertRequestSpeedUnit(d.pop("speedUnit"))

        def _parse_internal_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_vin = _parse_internal_vin(d.pop("internalVin", UNSET))

        def _parse_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vin = _parse_vin(d.pop("vin", UNSET))

        create_speed_alert_request = cls(
            speed=speed,
            speed_status=speed_status,
            speed_unit=speed_unit,
            internal_vin=internal_vin,
            vin=vin,
        )

        create_speed_alert_request.additional_properties = d
        return create_speed_alert_request

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
