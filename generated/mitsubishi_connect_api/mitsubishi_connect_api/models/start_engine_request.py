from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hvac_settings import HvacSettings


T = TypeVar("T", bound="StartEngineRequest")


@_attrs_define
class StartEngineRequest:
    """
    Attributes:
        pin_hash (str): PIN challenge hash (see PIN Challenge Protocol in the API description). Example:
            q83vEjRWeJA0Ehcm9kZkZw==.
        target_temperature (str): Target cabin temperature serialized as a decimal string (one decimal). Example: 21.0.
        temperature_unit (str): Temperature unit, `C` or `F`. Example: C.
        vin (str): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls. Example:
            JA4XXXXXXXXXXXXXX.
        action (None | str | Unset):
        hvac_settings (HvacSettings | Unset): Cabin comfort / winter HVAC options (0 = OFF, 1+ = ON / level)
        internal_vin (None | str | Unset): Internal VIN from `getVehicleList` (`vinList`), omitted when not provided.
            Example: JA4XXXXXXXXXXXXXX.
        pin_access_token (None | str | Unset): Short-lived PIN access token obtained through biometrics
            (`enableBiometricsForRemote` / `refreshBiometricsTokenForRemote`). Alternative to `pinHash`.
        start_flag (int | None | Unset): 0 IMMEDIATE_START_AC, 1 KEEP_AND_START_AC, 2 DELAY. Default: 0.
    """

    pin_hash: str
    target_temperature: str
    temperature_unit: str
    vin: str
    action: None | str | Unset = UNSET
    hvac_settings: HvacSettings | Unset = UNSET
    internal_vin: None | str | Unset = UNSET
    pin_access_token: None | str | Unset = UNSET
    start_flag: int | None | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pin_hash = self.pin_hash

        target_temperature = self.target_temperature

        temperature_unit = self.temperature_unit

        vin = self.vin

        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        else:
            action = self.action

        hvac_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hvac_settings, Unset):
            hvac_settings = self.hvac_settings.to_dict()

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

        start_flag: int | None | Unset
        if isinstance(self.start_flag, Unset):
            start_flag = UNSET
        else:
            start_flag = self.start_flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pinHash": pin_hash,
                "targetTemperature": target_temperature,
                "temperatureUnit": temperature_unit,
                "vin": vin,
            }
        )
        if action is not UNSET:
            field_dict["action"] = action
        if hvac_settings is not UNSET:
            field_dict["hvacSettings"] = hvac_settings
        if internal_vin is not UNSET:
            field_dict["internalVin"] = internal_vin
        if pin_access_token is not UNSET:
            field_dict["pinAccessToken"] = pin_access_token
        if start_flag is not UNSET:
            field_dict["startFlag"] = start_flag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hvac_settings import HvacSettings  # noqa: PLC0415

        d = dict(src_dict)
        pin_hash = d.pop("pinHash")

        target_temperature = d.pop("targetTemperature")

        temperature_unit = d.pop("temperatureUnit")

        vin = d.pop("vin")

        def _parse_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action = _parse_action(d.pop("action", UNSET))

        _hvac_settings = d.pop("hvacSettings", UNSET)
        hvac_settings: HvacSettings | Unset
        if isinstance(_hvac_settings, Unset):
            hvac_settings = UNSET
        else:
            hvac_settings = HvacSettings.from_dict(_hvac_settings)

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

        def _parse_start_flag(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_flag = _parse_start_flag(d.pop("startFlag", UNSET))

        start_engine_request = cls(
            pin_hash=pin_hash,
            target_temperature=target_temperature,
            temperature_unit=temperature_unit,
            vin=vin,
            action=action,
            hvac_settings=hvac_settings,
            internal_vin=internal_vin,
            pin_access_token=pin_access_token,
            start_flag=start_flag,
        )

        start_engine_request.additional_properties = d
        return start_engine_request

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
