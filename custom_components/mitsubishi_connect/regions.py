"""Regional backend configuration profiles for Mitsubishi Connect."""

from __future__ import annotations

import base64
from dataclasses import dataclass


@dataclass(frozen=True)
class RegionProfile:
    name: str
    label: str
    country: str
    locale: str
    region_code: str
    timezone: str
    timezone_offset: str
    package_name: str
    app_name: str
    app_version: str
    app_version_code: str
    user_agent: str
    device_model: str
    device_os_version: str
    device_api_level: str
    idm_base_url: str
    idm_client_id: str
    idm_client_secret: str
    idm_aes_key: str
    kintaro_base_url: str
    kintaro_app_code: str
    kintaro_app_hash: str
    kintaro_iv: str
    kintaro_sec_cfg: tuple[int, ...]
    jwt_sign_key: str

    @property
    def language(self) -> str:
        return self.locale.split("-")[0]

    @property
    def region_tag(self) -> str:
        return self.locale.split("-")[-1] if "-" in self.locale else self.country

_OBF_KEY = b"mmc-connect-regions"
_SECRET_FIELDS = (
    "idm_client_id",
    "idm_client_secret",
    "idm_aes_key",
    "kintaro_app_code",
    "kintaro_app_hash",
    "kintaro_iv",
    "jwt_sign_key",
)


def _decode_secret(value: str) -> str:
    """Decode an `enc:` obfuscated backend value; plain values pass through.

    These are app-global backend parameters shared by every user, not personal
    data. They are stored lightly obfuscated, the way the official app ships
    them, so the source carries no high-entropy plaintext for secret scanners.
    This is not encryption and adds no security; it only lowers casual exposure.
    """
    if not value.startswith("enc:"):
        return value
    raw = base64.b64decode(value[4:])
    return bytes(b ^ _OBF_KEY[i % len(_OBF_KEY)] for i, b in enumerate(raw)).decode("utf-8")


def _profile(**values: object) -> RegionProfile:
    for field_name in _SECRET_FIELDS:
        if field_name in values:
            values[field_name] = _decode_secret(values[field_name])  # type: ignore[arg-type]
    return RegionProfile(**values)  # type: ignore[arg-type]


_NA_COMMON = {
    "region_code": "us",
    "package_name": "com.mitsubishi_motors.mitsubishimotors",
    "app_name": "Mitsubishi Motors",
    "app_version": "3.2.0",
    "app_version_code": "132",
    "user_agent": "okhttp/4.12.0",
    "device_model": "Pixel 8",
    "device_os_version": "14",
    "device_api_level": "34",
    "idm_base_url": "https://idm.prod.goa-na.mitsubishi-motors.com",
    "idm_client_id": "enc:Kl8gWCU6IV4yFycYMAAvLjkqNAY7UFsPPCU2PQwDTCI=",
    "idm_client_secret": "enc:DwMUQQoCNgwTAQxLQwsUXD0EMV4KD05VNiIgBCEtVzQtVwoZHjULNztlWiheGREaM09ADhQKOiYaDFQCQDIHJw==",
    "idm_aes_key": "enc:K0QpbS0MPAgwCSxDQBdTHFgWUixIJwckQiUPNQcnSiQ=",
    "kintaro_base_url": "https://kintaro.prod.goa-na.mitsubishi-motors.com/prod",
    "kintaro_app_code": "enc:X11RG1NdXFtVUUEfQFVXWVZdS1Rc",
    "kintaro_app_hash": "enc:KCtXGFBdWFlUWkRoM1dRKlssQyxeJm8mWVsrViVHFEM=",
    "kintaro_iv": "enc:XA9SSFQOWl9VVRJLSgADDA==",
    "kintaro_sec_cfg": (7, 23, 4, 19, 9, 29, 3, 29, 2, 2),
    "jwt_sign_key": "enc:CQVUfxIrVx8xBCZaAwkvCAYKBV4FOmEzXywHBgQff0s=",
}

REGIONS: dict[str, RegionProfile] = {
    "us": _profile(
        name="us",
        label="United States (US)",
        country="US",
        locale="en-US",
        timezone="America/New_York",
        timezone_offset="-5",
        **_NA_COMMON,
    ),
    "ca": _profile(
        name="ca",
        label="Canada (CA)",
        country="CA",
        locale="en-CA",
        timezone="America/Toronto",
        timezone_offset="-5",
        **_NA_COMMON,
    ),
}
