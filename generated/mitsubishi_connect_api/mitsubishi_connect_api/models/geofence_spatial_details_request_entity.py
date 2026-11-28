from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeofenceSpatialDetailsRequestEntity")


@_attrs_define
class GeofenceSpatialDetailsRequestEntity:
    """
    Attributes:
        lat (str):  Default: '0'.
        lon (str):  Default: '0'.
        rad (None | str | Unset):
    """

    lat: str = "0"
    lon: str = "0"
    rad: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lat = self.lat

        lon = self.lon

        rad: None | str | Unset
        if isinstance(self.rad, Unset):
            rad = UNSET
        else:
            rad = self.rad

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lat": lat,
                "lon": lon,
            }
        )
        if rad is not UNSET:
            field_dict["rad"] = rad

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lat = d.pop("lat")

        lon = d.pop("lon")

        def _parse_rad(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rad = _parse_rad(d.pop("rad", UNSET))

        geofence_spatial_details_request_entity = cls(
            lat=lat,
            lon=lon,
            rad=rad,
        )

        geofence_spatial_details_request_entity.additional_properties = d
        return geofence_spatial_details_request_entity

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
