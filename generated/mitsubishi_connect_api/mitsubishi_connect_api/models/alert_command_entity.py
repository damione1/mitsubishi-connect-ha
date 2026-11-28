from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertCommandEntity")


@_attrs_define
class AlertCommandEntity:
    """
    Attributes:
        command_id (None | str | Unset):
        curfew_id (None | str | Unset):
        geofence_id (None | str | Unset):
    """

    command_id: None | str | Unset = UNSET
    curfew_id: None | str | Unset = UNSET
    geofence_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command_id: None | str | Unset
        if isinstance(self.command_id, Unset):
            command_id = UNSET
        else:
            command_id = self.command_id

        curfew_id: None | str | Unset
        if isinstance(self.curfew_id, Unset):
            curfew_id = UNSET
        else:
            curfew_id = self.curfew_id

        geofence_id: None | str | Unset
        if isinstance(self.geofence_id, Unset):
            geofence_id = UNSET
        else:
            geofence_id = self.geofence_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command_id is not UNSET:
            field_dict["commandId"] = command_id
        if curfew_id is not UNSET:
            field_dict["curfewId"] = curfew_id
        if geofence_id is not UNSET:
            field_dict["geofenceId"] = geofence_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_command_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        command_id = _parse_command_id(d.pop("commandId", UNSET))

        def _parse_curfew_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        curfew_id = _parse_curfew_id(d.pop("curfewId", UNSET))

        def _parse_geofence_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geofence_id = _parse_geofence_id(d.pop("geofenceId", UNSET))

        alert_command_entity = cls(
            command_id=command_id,
            curfew_id=curfew_id,
            geofence_id=geofence_id,
        )

        alert_command_entity.additional_properties = d
        return alert_command_entity

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
