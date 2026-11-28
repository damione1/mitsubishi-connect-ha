from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PinCommandRequest")


@_attrs_define
class PinCommandRequest:
    """
    Attributes:
        vin (str): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls. Example:
            JA4XXXXXXXXXXXXXX.
        cancel_flag (int | None | Unset): For stopEngine/stopClimate: 0 IMMEDIATE_STOP_AC, 1 CANCEL_DELAY.
        internal_vin (None | str | Unset): Internal VIN from `getVehicleList` (`vinList`), omitted when not provided.
            Example: JA4XXXXXXXXXXXXXX.
        pin_access_token (None | str | Unset): Short-lived PIN access token obtained through biometrics
            (`enableBiometricsForRemote` / `refreshBiometricsTokenForRemote`). Alternative to `pinHash`.
        pin_hash (None | str | Unset): PIN challenge hash (see PIN Challenge Protocol in the API description). Example:
            q83vEjRWeJA0Ehcm9kZkZw==.
    """

    vin: str
    cancel_flag: int | None | Unset = UNSET
    internal_vin: None | str | Unset = UNSET
    pin_access_token: None | str | Unset = UNSET
    pin_hash: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vin = self.vin

        cancel_flag: int | None | Unset
        if isinstance(self.cancel_flag, Unset):
            cancel_flag = UNSET
        else:
            cancel_flag = self.cancel_flag

        internal_vin: None | str | Unset
        if isinstance(self.internal_vin, Unset):
            internal_vin = UNSET
        else:
            internal_vin = self.internal_vin

        pin_access_token: None | str | Unset
        if isinstance(self.pin_access_token, Unset):
            pin_access_token = UNSET
        else:
            pin_access_token = self.pin_access_token

        pin_hash: None | str | Unset
        if isinstance(self.pin_hash, Unset):
            pin_hash = UNSET
        else:
            pin_hash = self.pin_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vin": vin,
            }
        )
        if cancel_flag is not UNSET:
            field_dict["cancelFlag"] = cancel_flag
        if internal_vin is not UNSET:
            field_dict["internalVin"] = internal_vin
        if pin_access_token is not UNSET:
            field_dict["pinAccessToken"] = pin_access_token
        if pin_hash is not UNSET:
            field_dict["pinHash"] = pin_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vin = d.pop("vin")

        def _parse_cancel_flag(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cancel_flag = _parse_cancel_flag(d.pop("cancelFlag", UNSET))

        def _parse_internal_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_vin = _parse_internal_vin(d.pop("internalVin", UNSET))

        def _parse_pin_access_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pin_access_token = _parse_pin_access_token(d.pop("pinAccessToken", UNSET))

        def _parse_pin_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pin_hash = _parse_pin_hash(d.pop("pinHash", UNSET))

        pin_command_request = cls(
            vin=vin,
            cancel_flag=cancel_flag,
            internal_vin=internal_vin,
            pin_access_token=pin_access_token,
            pin_hash=pin_hash,
        )

        pin_command_request.additional_properties = d
        return pin_command_request

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
