from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SOCEntity")


@_attrs_define
class SOCEntity:
    """
    Attributes:
        max_ (str | Unset):  Default: '100'.
        min_ (str | Unset):  Default: '60'.
        min_year (None | str | Unset):
        move_interval (str | Unset):  Default: '0'.
        ui_interval (str | Unset):  Default: '10'.
    """

    max_: str | Unset = "100"
    min_: str | Unset = "60"
    min_year: None | str | Unset = UNSET
    move_interval: str | Unset = "0"
    ui_interval: str | Unset = "10"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_ = self.max_

        min_ = self.min_

        min_year: None | str | Unset
        if isinstance(self.min_year, Unset):
            min_year = UNSET
        else:
            min_year = self.min_year

        move_interval = self.move_interval

        ui_interval = self.ui_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if min_year is not UNSET:
            field_dict["minYear"] = min_year
        if move_interval is not UNSET:
            field_dict["moveInterval"] = move_interval
        if ui_interval is not UNSET:
            field_dict["uiInterval"] = ui_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        def _parse_min_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        min_year = _parse_min_year(d.pop("minYear", UNSET))

        move_interval = d.pop("moveInterval", UNSET)

        ui_interval = d.pop("uiInterval", UNSET)

        soc_entity = cls(
            max_=max_,
            min_=min_,
            min_year=min_year,
            move_interval=move_interval,
            ui_interval=ui_interval,
        )

        soc_entity.additional_properties = d
        return soc_entity

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
