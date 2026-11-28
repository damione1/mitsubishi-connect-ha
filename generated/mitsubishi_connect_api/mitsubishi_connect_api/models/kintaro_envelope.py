from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kintaro_envelope_state import KintaroEnvelopeState
from ..types import UNSET, Unset

T = TypeVar("T", bound="KintaroEnvelope")


@_attrs_define
class KintaroEnvelope:
    """Raw Kintaro HTTP body before decryption. HTTP status is 200 for business errors too: check `state`. The operations
    in this document describe the decrypted `payload` only.

        Attributes:
            state (KintaroEnvelopeState): `S` success, `F` failure.
            payload (None | str | Unset): AES-128-CBC + Base64 encrypted JSON payload (plain JSON when `knt-api-response-
                mode: PLAINTEXT`).
            error_code (None | str | Unset): See `ErrorCode`.
            error (None | str | Unset):
            error_for_display (None | str | Unset):
            error_title (None | str | Unset):
            extra_code (None | str | Unset):
            extra_message (None | str | Unset):
    """

    state: KintaroEnvelopeState
    payload: None | str | Unset = UNSET
    error_code: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    error_for_display: None | str | Unset = UNSET
    error_title: None | str | Unset = UNSET
    extra_code: None | str | Unset = UNSET
    extra_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        payload: None | str | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        else:
            payload = self.payload

        error_code: None | str | Unset
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        error_for_display: None | str | Unset
        if isinstance(self.error_for_display, Unset):
            error_for_display = UNSET
        else:
            error_for_display = self.error_for_display

        error_title: None | str | Unset
        if isinstance(self.error_title, Unset):
            error_title = UNSET
        else:
            error_title = self.error_title

        extra_code: None | str | Unset
        if isinstance(self.extra_code, Unset):
            extra_code = UNSET
        else:
            extra_code = self.extra_code

        extra_message: None | str | Unset
        if isinstance(self.extra_message, Unset):
            extra_message = UNSET
        else:
            extra_message = self.extra_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if payload is not UNSET:
            field_dict["payload"] = payload
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error is not UNSET:
            field_dict["error"] = error
        if error_for_display is not UNSET:
            field_dict["errorForDisplay"] = error_for_display
        if error_title is not UNSET:
            field_dict["errorTitle"] = error_title
        if extra_code is not UNSET:
            field_dict["extraCode"] = extra_code
        if extra_message is not UNSET:
            field_dict["extraMessage"] = extra_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = KintaroEnvelopeState(d.pop("state"))

        def _parse_payload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))

        def _parse_error_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_code = _parse_error_code(d.pop("errorCode", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_error_for_display(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_for_display = _parse_error_for_display(d.pop("errorForDisplay", UNSET))

        def _parse_error_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_title = _parse_error_title(d.pop("errorTitle", UNSET))

        def _parse_extra_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extra_code = _parse_extra_code(d.pop("extraCode", UNSET))

        def _parse_extra_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extra_message = _parse_extra_message(d.pop("extraMessage", UNSET))

        kintaro_envelope = cls(
            state=state,
            payload=payload,
            error_code=error_code,
            error=error,
            error_for_display=error_for_display,
            error_title=error_title,
            extra_code=extra_code,
            extra_message=extra_message,
        )

        kintaro_envelope.additional_properties = d
        return kintaro_envelope

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
