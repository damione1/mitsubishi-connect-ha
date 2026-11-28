from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IdmLoginRequest")


@_attrs_define
class IdmLoginRequest:
    """
    Attributes:
        client_id (str): IDM client id from the regional configuration. Example: example-client-id.
        device_id (str): Random per-install device UUID. Example: 00000000-0000-4000-8000-000000000000.
        password (str): For `/api/v1/login`: `<keyIndex>@<base64(RSA_PKCS1v15(password))>`. Example:
            1@BASE64CIPHERTEXT==.
        username (str):  Example: owner@example.com.
    """

    client_id: str
    device_id: str
    password: str
    username: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        device_id = self.device_id

        password = self.password

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientId": client_id,
                "deviceId": device_id,
                "password": password,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("clientId")

        device_id = d.pop("deviceId")

        password = d.pop("password")

        username = d.pop("username")

        idm_login_request = cls(
            client_id=client_id,
            device_id=device_id,
            password=password,
            username=username,
        )

        idm_login_request.additional_properties = d
        return idm_login_request

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
