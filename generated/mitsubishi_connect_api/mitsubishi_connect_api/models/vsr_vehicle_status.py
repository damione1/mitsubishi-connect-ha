from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vsr_door_status import VsrDoorStatus
    from ..models.vsr_light_status import VsrLightStatus
    from ..models.vsr_metric import VsrMetric
    from ..models.vsr_window_status import VsrWindowStatus


T = TypeVar("T", bound="VsrVehicleStatus")


@_attrs_define
class VsrVehicleStatus:
    """
    Attributes:
        door_status (VsrDoorStatus | Unset):
        light_status (VsrLightStatus | Unset):
        lock_status (VsrMetric | Unset):
        window_status (VsrWindowStatus | Unset):
    """

    door_status: VsrDoorStatus | Unset = UNSET
    light_status: VsrLightStatus | Unset = UNSET
    lock_status: VsrMetric | Unset = UNSET
    window_status: VsrWindowStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        door_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.door_status, Unset):
            door_status = self.door_status.to_dict()

        light_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.light_status, Unset):
            light_status = self.light_status.to_dict()

        lock_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lock_status, Unset):
            lock_status = self.lock_status.to_dict()

        window_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.window_status, Unset):
            window_status = self.window_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if door_status is not UNSET:
            field_dict["doorStatus"] = door_status
        if light_status is not UNSET:
            field_dict["lightStatus"] = light_status
        if lock_status is not UNSET:
            field_dict["lockStatus"] = lock_status
        if window_status is not UNSET:
            field_dict["windowStatus"] = window_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vsr_door_status import VsrDoorStatus  # noqa: PLC0415
        from ..models.vsr_light_status import VsrLightStatus  # noqa: PLC0415
        from ..models.vsr_metric import VsrMetric  # noqa: PLC0415
        from ..models.vsr_window_status import VsrWindowStatus  # noqa: PLC0415

        d = dict(src_dict)
        _door_status = d.pop("doorStatus", UNSET)
        door_status: VsrDoorStatus | Unset
        if isinstance(_door_status, Unset):
            door_status = UNSET
        else:
            door_status = VsrDoorStatus.from_dict(_door_status)

        _light_status = d.pop("lightStatus", UNSET)
        light_status: VsrLightStatus | Unset
        if isinstance(_light_status, Unset):
            light_status = UNSET
        else:
            light_status = VsrLightStatus.from_dict(_light_status)

        _lock_status = d.pop("lockStatus", UNSET)
        lock_status: VsrMetric | Unset
        if isinstance(_lock_status, Unset):
            lock_status = UNSET
        else:
            lock_status = VsrMetric.from_dict(_lock_status)

        _window_status = d.pop("windowStatus", UNSET)
        window_status: VsrWindowStatus | Unset
        if isinstance(_window_status, Unset):
            window_status = UNSET
        else:
            window_status = VsrWindowStatus.from_dict(_window_status)

        vsr_vehicle_status = cls(
            door_status=door_status,
            light_status=light_status,
            lock_status=lock_status,
            window_status=window_status,
        )

        vsr_vehicle_status.additional_properties = d
        return vsr_vehicle_status

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
