from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IdmRefreshTokenRequest")


@_attrs_define
class IdmRefreshTokenRequest:
    """
    Attributes:
        client_id (str): IDM client id from the regional configuration. Example: example-client-id.
        client_secret (str): IDM client secret from the regional configuration. Example: example-client-secret.
        refresh_token (str):  Example: eyJhbGciOiJIUzI1NiJ9.example.refresh.
    """

    client_id: str
    client_secret: str
    refresh_token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        client_secret = self.client_secret

        refresh_token = self.refresh_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientId": client_id,
                "clientSecret": client_secret,
                "refreshToken": refresh_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("clientId")

        client_secret = d.pop("clientSecret")

        refresh_token = d.pop("refreshToken")

        idm_refresh_token_request = cls(
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
        )

        idm_refresh_token_request.additional_properties = d
        return idm_refresh_token_request

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
