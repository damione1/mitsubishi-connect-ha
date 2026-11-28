from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vehicle_location_item import VehicleLocationItem


T = TypeVar("T", bound="VehicleLocationResponse")


@_attrs_define
class VehicleLocationResponse:
    """
    Attributes:
        is_valid_pin (bool | None | Unset):  Default: True.
        location_latitude (VehicleLocationItem | Unset):
        location_longitude (VehicleLocationItem | Unset):
        timestamp (None | str | Unset):
    """

    is_valid_pin: bool | None | Unset = True
    location_latitude: VehicleLocationItem | Unset = UNSET
    location_longitude: VehicleLocationItem | Unset = UNSET
    timestamp: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_valid_pin: bool | None | Unset
        if isinstance(self.is_valid_pin, Unset):
            is_valid_pin = UNSET
        else:
            is_valid_pin = self.is_valid_pin

        location_latitude: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location_latitude, Unset):
            location_latitude = self.location_latitude.to_dict()

        location_longitude: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location_longitude, Unset):
            location_longitude = self.location_longitude.to_dict()

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_valid_pin is not UNSET:
            field_dict["isValidPIN"] = is_valid_pin
        if location_latitude is not UNSET:
            field_dict["locationLatitude"] = location_latitude
        if location_longitude is not UNSET:
            field_dict["locationLongitude"] = location_longitude
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vehicle_location_item import VehicleLocationItem  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_is_valid_pin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_valid_pin = _parse_is_valid_pin(d.pop("isValidPIN", UNSET))

        _location_latitude = d.pop("locationLatitude", UNSET)
        location_latitude: VehicleLocationItem | Unset
        if isinstance(_location_latitude, Unset):
            location_latitude = UNSET
        else:
            location_latitude = VehicleLocationItem.from_dict(_location_latitude)

        _location_longitude = d.pop("locationLongitude", UNSET)
        location_longitude: VehicleLocationItem | Unset
        if isinstance(_location_longitude, Unset):
            location_longitude = UNSET
        else:
            location_longitude = VehicleLocationItem.from_dict(_location_longitude)

        def _parse_timestamp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        vehicle_location_response = cls(
            is_valid_pin=is_valid_pin,
            location_latitude=location_latitude,
            location_longitude=location_longitude,
            timestamp=timestamp,
        )

        vehicle_location_response.additional_properties = d
        return vehicle_location_response

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
