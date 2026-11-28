from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VehicleModel")


@_attrs_define
class VehicleModel:
    """
    Attributes:
        body_work (None | str | Unset):
        family (None | str | Unset):
        model_year (None | str | Unset):
        phase (None | str | Unset):
    """

    body_work: None | str | Unset = UNSET
    family: None | str | Unset = UNSET
    model_year: None | str | Unset = UNSET
    phase: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_work: None | str | Unset
        if isinstance(self.body_work, Unset):
            body_work = UNSET
        else:
            body_work = self.body_work

        family: None | str | Unset
        if isinstance(self.family, Unset):
            family = UNSET
        else:
            family = self.family

        model_year: None | str | Unset
        if isinstance(self.model_year, Unset):
            model_year = UNSET
        else:
            model_year = self.model_year

        phase: None | str | Unset
        if isinstance(self.phase, Unset):
            phase = UNSET
        else:
            phase = self.phase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body_work is not UNSET:
            field_dict["bodyWork"] = body_work
        if family is not UNSET:
            field_dict["family"] = family
        if model_year is not UNSET:
            field_dict["modelYear"] = model_year
        if phase is not UNSET:
            field_dict["phase"] = phase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_body_work(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body_work = _parse_body_work(d.pop("bodyWork", UNSET))

        def _parse_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family = _parse_family(d.pop("family", UNSET))

        def _parse_model_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_year = _parse_model_year(d.pop("modelYear", UNSET))

        def _parse_phase(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phase = _parse_phase(d.pop("phase", UNSET))

        vehicle_model = cls(
            body_work=body_work,
            family=family,
            model_year=model_year,
            phase=phase,
        )

        vehicle_model.additional_properties = d
        return vehicle_model

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
