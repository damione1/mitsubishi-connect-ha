from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vsr_diagnostic import VsrDiagnostic
    from ..models.vsr_vehicle_status import VsrVehicleStatus


T = TypeVar("T", bound="VsrData")


@_attrs_define
class VsrData:
    """
    Attributes:
        diagnostic (VsrDiagnostic | Unset):
        message (None | str | Unset):
        vehicle_status (VsrVehicleStatus | Unset):
    """

    diagnostic: VsrDiagnostic | Unset = UNSET
    message: None | str | Unset = UNSET
    vehicle_status: VsrVehicleStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        diagnostic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diagnostic, Unset):
            diagnostic = self.diagnostic.to_dict()

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        vehicle_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vehicle_status, Unset):
            vehicle_status = self.vehicle_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if diagnostic is not UNSET:
            field_dict["diagnostic"] = diagnostic
        if message is not UNSET:
            field_dict["message"] = message
        if vehicle_status is not UNSET:
            field_dict["vehicleStatus"] = vehicle_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vsr_diagnostic import VsrDiagnostic  # noqa: PLC0415
        from ..models.vsr_vehicle_status import VsrVehicleStatus  # noqa: PLC0415

        d = dict(src_dict)
        _diagnostic = d.pop("diagnostic", UNSET)
        diagnostic: VsrDiagnostic | Unset
        if isinstance(_diagnostic, Unset):
            diagnostic = UNSET
        else:
            diagnostic = VsrDiagnostic.from_dict(_diagnostic)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        _vehicle_status = d.pop("vehicleStatus", UNSET)
        vehicle_status: VsrVehicleStatus | Unset
        if isinstance(_vehicle_status, Unset):
            vehicle_status = UNSET
        else:
            vehicle_status = VsrVehicleStatus.from_dict(_vehicle_status)

        vsr_data = cls(
            diagnostic=diagnostic,
            message=message,
            vehicle_status=vehicle_status,
        )

        vsr_data.additional_properties = d
        return vsr_data

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
