from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vsr_state_item import VsrStateItem


T = TypeVar("T", bound="VsrDoorStatus")


@_attrs_define
class VsrDoorStatus:
    """
    Attributes:
        doors (list[VsrStateItem] | Unset):
        id (None | str | Unset):
        name (None | str | Unset):
    """

    doors: list[VsrStateItem] | Unset = UNSET
    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        doors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.doors, Unset):
            doors = []
            for doors_item_data in self.doors:
                doors_item = doors_item_data.to_dict()
                doors.append(doors_item)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doors is not UNSET:
            field_dict["doors"] = doors
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vsr_state_item import VsrStateItem  # noqa: PLC0415

        d = dict(src_dict)
        _doors = d.pop("doors", UNSET)
        doors: list[VsrStateItem] | Unset = UNSET
        if _doors is not UNSET:
            doors = []
            for doors_item_data in _doors:
                doors_item = VsrStateItem.from_dict(doors_item_data)

                doors.append(doors_item)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        vsr_door_status = cls(
            doors=doors,
            id=id,
            name=name,
        )

        vsr_door_status.additional_properties = d
        return vsr_door_status

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
