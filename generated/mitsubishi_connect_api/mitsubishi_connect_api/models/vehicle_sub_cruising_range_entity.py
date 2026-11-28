from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vsr_metric import VsrMetric


T = TypeVar("T", bound="VehicleSubCruisingRangeEntity")


@_attrs_define
class VehicleSubCruisingRangeEntity:
    """
    Attributes:
        engine_type (VsrMetric | Unset):
        range_2 (VsrMetric | Unset):
        range_3 (VsrMetric | Unset):
    """

    engine_type: VsrMetric | Unset = UNSET
    range_2: VsrMetric | Unset = UNSET
    range_3: VsrMetric | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        engine_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.engine_type, Unset):
            engine_type = self.engine_type.to_dict()

        range_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_2, Unset):
            range_2 = self.range_2.to_dict()

        range_3: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_3, Unset):
            range_3 = self.range_3.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if engine_type is not UNSET:
            field_dict["engineType"] = engine_type
        if range_2 is not UNSET:
            field_dict["range_2"] = range_2
        if range_3 is not UNSET:
            field_dict["range_3"] = range_3

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vsr_metric import VsrMetric  # noqa: PLC0415

        d = dict(src_dict)
        _engine_type = d.pop("engineType", UNSET)
        engine_type: VsrMetric | Unset
        if isinstance(_engine_type, Unset):
            engine_type = UNSET
        else:
            engine_type = VsrMetric.from_dict(_engine_type)

        _range_2 = d.pop("range_2", UNSET)
        range_2: VsrMetric | Unset
        if isinstance(_range_2, Unset):
            range_2 = UNSET
        else:
            range_2 = VsrMetric.from_dict(_range_2)

        _range_3 = d.pop("range_3", UNSET)
        range_3: VsrMetric | Unset
        if isinstance(_range_3, Unset):
            range_3 = UNSET
        else:
            range_3 = VsrMetric.from_dict(_range_3)

        vehicle_sub_cruising_range_entity = cls(
            engine_type=engine_type,
            range_2=range_2,
            range_3=range_3,
        )

        vehicle_sub_cruising_range_entity.additional_properties = d
        return vehicle_sub_cruising_range_entity

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
