from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generic_response import GenericResponse


T = TypeVar("T", bound="GeofenceAlertData")


@_attrs_define
class GeofenceAlertData:
    """
    Attributes:
        default_rad (float | None | Unset):
        geofence_conf (list[GenericResponse] | Unset):
        max_rad (float | None | Unset):  Default: 20000.0.
        min_rad (float | None | Unset):  Default: 1000.0.
    """

    default_rad: float | None | Unset = UNSET
    geofence_conf: list[GenericResponse] | Unset = UNSET
    max_rad: float | None | Unset = 20000.0
    min_rad: float | None | Unset = 1000.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_rad: float | None | Unset
        if isinstance(self.default_rad, Unset):
            default_rad = UNSET
        else:
            default_rad = self.default_rad

        geofence_conf: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.geofence_conf, Unset):
            geofence_conf = []
            for geofence_conf_item_data in self.geofence_conf:
                geofence_conf_item = geofence_conf_item_data.to_dict()
                geofence_conf.append(geofence_conf_item)

        max_rad: float | None | Unset
        if isinstance(self.max_rad, Unset):
            max_rad = UNSET
        else:
            max_rad = self.max_rad

        min_rad: float | None | Unset
        if isinstance(self.min_rad, Unset):
            min_rad = UNSET
        else:
            min_rad = self.min_rad

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_rad is not UNSET:
            field_dict["defaultRad"] = default_rad
        if geofence_conf is not UNSET:
            field_dict["geofenceConf"] = geofence_conf
        if max_rad is not UNSET:
            field_dict["maxRad"] = max_rad
        if min_rad is not UNSET:
            field_dict["minRad"] = min_rad

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generic_response import GenericResponse  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_default_rad(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        default_rad = _parse_default_rad(d.pop("defaultRad", UNSET))

        _geofence_conf = d.pop("geofenceConf", UNSET)
        geofence_conf: list[GenericResponse] | Unset = UNSET
        if _geofence_conf is not UNSET:
            geofence_conf = []
            for geofence_conf_item_data in _geofence_conf:
                geofence_conf_item = GenericResponse.from_dict(geofence_conf_item_data)

                geofence_conf.append(geofence_conf_item)

        def _parse_max_rad(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_rad = _parse_max_rad(d.pop("maxRad", UNSET))

        def _parse_min_rad(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_rad = _parse_min_rad(d.pop("minRad", UNSET))

        geofence_alert_data = cls(
            default_rad=default_rad,
            geofence_conf=geofence_conf,
            max_rad=max_rad,
            min_rad=min_rad,
        )

        geofence_alert_data.additional_properties = d
        return geofence_alert_data

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
