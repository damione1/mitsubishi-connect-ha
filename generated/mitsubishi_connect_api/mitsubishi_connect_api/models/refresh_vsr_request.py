from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RefreshVsrRequest")


@_attrs_define
class RefreshVsrRequest:
    """
    Attributes:
        refresh_type (int): Refresh trigger: 0 HomeEnter, 1 HomePullDown, 2 Push, 3 StatusEnter, 4 StatusPullDown, 8
            AwakeFromBackground. Default: 1. Example: 1.
        vin (str): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls. Example:
            JA4XXXXXXXXXXXXXX.
        internal_vin (None | str | Unset): Internal VIN from `getVehicleList` (`vinList`), omitted when not provided.
            Example: JA4XXXXXXXXXXXXXX.
    """

    vin: str
    refresh_type: int = 1
    internal_vin: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        refresh_type = self.refresh_type

        vin = self.vin

        internal_vin: None | str | Unset
        if isinstance(self.internal_vin, Unset):
            internal_vin = UNSET
        else:
            internal_vin = self.internal_vin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refreshType": refresh_type,
                "vin": vin,
            }
        )
        if internal_vin is not UNSET:
            field_dict["internalVin"] = internal_vin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        refresh_type = d.pop("refreshType")

        vin = d.pop("vin")

        def _parse_internal_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_vin = _parse_internal_vin(d.pop("internalVin", UNSET))

        refresh_vsr_request = cls(
            refresh_type=refresh_type,
            vin=vin,
            internal_vin=internal_vin,
        )

        refresh_vsr_request.additional_properties = d
        return refresh_vsr_request

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
