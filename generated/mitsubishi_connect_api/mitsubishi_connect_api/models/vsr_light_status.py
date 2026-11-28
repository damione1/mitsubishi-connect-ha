from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vsr_state_item import VsrStateItem


T = TypeVar("T", bound="VsrLightStatus")


@_attrs_define
class VsrLightStatus:
    """
    Attributes:
        id (None | str | Unset):
        lights (list[VsrStateItem] | Unset):
        name (None | str | Unset):
    """

    id: None | str | Unset = UNSET
    lights: list[VsrStateItem] | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        lights: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lights, Unset):
            lights = []
            for lights_item_data in self.lights:
                lights_item = lights_item_data.to_dict()
                lights.append(lights_item)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if lights is not UNSET:
            field_dict["lights"] = lights
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vsr_state_item import VsrStateItem  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _lights = d.pop("lights", UNSET)
        lights: list[VsrStateItem] | Unset = UNSET
        if _lights is not UNSET:
            lights = []
            for lights_item_data in _lights:
                lights_item = VsrStateItem.from_dict(lights_item_data)

                lights.append(lights_item)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        vsr_light_status = cls(
            id=id,
            lights=lights,
            name=name,
        )

        vsr_light_status.additional_properties = d
        return vsr_light_status

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
