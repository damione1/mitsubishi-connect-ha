from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vsr_metric import VsrMetric


T = TypeVar("T", bound="VsrStateItem")


@_attrs_define
class VsrStateItem:
    """
    Attributes:
        position (VsrMetric | Unset):
        state (VsrMetric | Unset):
    """

    position: VsrMetric | Unset = UNSET
    state: VsrMetric | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vsr_metric import VsrMetric  # noqa: PLC0415

        d = dict(src_dict)
        _position = d.pop("position", UNSET)
        position: VsrMetric | Unset
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = VsrMetric.from_dict(_position)

        _state = d.pop("state", UNSET)
        state: VsrMetric | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = VsrMetric.from_dict(_state)

        vsr_state_item = cls(
            position=position,
            state=state,
        )

        vsr_state_item.additional_properties = d
        return vsr_state_item

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
