from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_code import ErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="KintaroError")


@_attrs_define
class KintaroError:
    """Error fields of a failed Kintaro envelope.

    Attributes:
        error_code (ErrorCode): Kintaro `errorCode` values. `600001`, `600002`, `600004`, `600005`, `600044`, `700000`
            and `401005` can be returned by any Kintaro endpoint; the other server codes are endpoint specific (see
            `x-error-codes`). `4`, `5` and `-1` to `-7` are produced on the device and never sent by the server.

            | Code | App name | Meaning |
            |---|---|---|
            | `600001` | (transport, / `p017b`) | Kintaro session key (`encKey`/`signKey`) expired or unknown. Re-run `POST
            /service/checkVersion` and retry. |
            | `600002` | ForceLogout | IDM access token expired or revoked. Refresh it with `/api/v1/refreshToken`,
            otherwise log in again. |
            | `600004` | ReLogin | session invalidated (for example the account logged in on another device; one session per
            account). Refresh the token or log in again. |
            | `600005` | ForceUpdate | the app version sent in the headers is no longer supported. |
            | `600006` | PinAccessTokenExpired | the biometrics `pinAccessToken` expired. Retry with a `pinHash` or refresh
            it with `refreshBiometricsTokenForRemote`. |
            | `600007` | PinRefreshTokenExpired | the biometrics PIN refresh token expired. Re-enable biometrics
            (`enableBiometricsForRemote`). |
            | `600044` | AccessTokenRequired | `knt-access-token` missing for an authenticated endpoint. |
            | `700000` | AppMaintenance | backend under maintenance. |
            | `401005` | RequestTimeValidFailed | request timestamp rejected (clock skew or replay). Clients should treat it
            as a forced logout. |
            | `956000` | PinVerifyFailed | wrong security PIN (`pinHash` mismatch). |
            | `956002` | MyQTokenRequired | no myQ account linked or its token is missing. |
            | `956003` | CheckUserResidence | residence country check required (getProfile with `checkResidenceFlag`). |
            | `956005` | MigrationFailed | payment / account migration failed. |
            | `956006` | PurchaseFailed | the purchase failed. |
            | `956007` | PurchaseSucceed | purchase completed (status code reported through the error channel). |
            | `956008` | PurchaseTimeout | purchase still pending after the timeout. |
            | `956011` | InvalidZipCode | address validation rejected the postal code. |
            | `956012` | InvalidAddressLine | address validation rejected the street line. |
            | `956013` | InvalidState | address validation rejected the state / province. |
            | `956014` | InvalidCity | address validation rejected the city. |
            | `956017` | ChargingInProgress | Plug & Charge operation refused while a charging session is in progress. |
            | `956018` | MyQRefreshTokenExpired | myQ refresh token expired; relink the myQ account. |
            | `957000` | PairVehicleRequestIdExpired | pairing `requestId` expired; restart pairing. |
            | `958000` | PairVehicleOtpCodeWrong | wrong pairing OTP code (attempts are limited by
            `otpConfig.maxWrongTimes`). |
            | `4` | StripeUnknownFailed | client-side code for Stripe failures, never returned by the server. |
            | `5` | FindMyCarUnknownFailed | client-side code for Find My Car failures, never returned by the server. |
            | `-1` | INTERNAL_SERVER_ERROR | Client-side transport error, produced on the device for transport failures,
            never returned by the server. |
            | `-2` | NETWORK_ERROR | Client-side transport error, produced on the device for transport failures, never
            returned by the server. |
            | `-3` | INVALID_DATA_FORMAT_ERROR | Client-side transport error, produced on the device for transport failures,
            never returned by the server. |
            | `-4` | CONFIG_SETUP_ERROR | Client-side transport error, produced on the device for transport failures, never
            returned by the server. |
            | `-5` | TIMEOUT_ERROR | Client-side transport error, produced on the device for transport failures, never
            returned by the server. |
            | `-6` | UNKNOWN_ERROR | Client-side transport error, produced on the device for transport failures, never
            returned by the server. |
            | `-7` | CONFIG_NOT_INITIALIZED | Client-side transport error, produced on the device for transport failures,
            never returned by the server. |
        error_title (None | str | Unset): Localized dialog title.
        error (None | str | Unset): Localized error message (`errorMessage` in ).
        error_for_display (None | str | Unset):
        extra_code (None | str | Unset):
        extra_message (None | str | Unset):
    """

    error_code: ErrorCode
    error_title: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    error_for_display: None | str | Unset = UNSET
    extra_code: None | str | Unset = UNSET
    extra_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code.value

        error_title: None | str | Unset
        if isinstance(self.error_title, Unset):
            error_title = UNSET
        else:
            error_title = self.error_title

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
                "errorCode": error_code,
            }
        )
        if error_title is not UNSET:
            field_dict["errorTitle"] = error_title
        if error is not UNSET:
            field_dict["error"] = error
        if error_for_display is not UNSET:
            field_dict["errorForDisplay"] = error_for_display
        if extra_code is not UNSET:
            field_dict["extraCode"] = extra_code
        if extra_message is not UNSET:
            field_dict["extraMessage"] = extra_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_code = ErrorCode(d.pop("errorCode"))

        def _parse_error_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_title = _parse_error_title(d.pop("errorTitle", UNSET))

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

        kintaro_error = cls(
            error_code=error_code,
            error_title=error_title,
            error=error,
            error_for_display=error_for_display,
            extra_code=extra_code,
            extra_message=extra_message,
        )

        kintaro_error.additional_properties = d
        return kintaro_error

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
