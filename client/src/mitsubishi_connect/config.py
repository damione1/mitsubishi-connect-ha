"""Region, backend, and session configuration loaders.

All region-specific settings (country, locale, timezone, IDM & Kintaro URLs,
and app parameters) are loaded from TOML configuration files and/or environment
variables — nothing personal or region-locked is hardcoded in the library.
"""

from __future__ import annotations

import base64
import json
import os
import tomllib
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


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

    Backend parameters are shared by every user (not personal data) and are
    stored lightly obfuscated, the way the official app ships them, so the files
    hold no high-entropy plaintext. This is not encryption and adds no security;
    a user override written in plain text is used as-is.
    """
    if not value.startswith("enc:"):
        return value
    raw = base64.b64decode(value[4:])
    return bytes(b ^ _OBF_KEY[i % len(_OBF_KEY)] for i, b in enumerate(raw)).decode("utf-8")


def _find_bundled_regions_file() -> Path | None:
    """Locate `config/regions.toml` relative to the repo or working directory."""
    candidates = [
        Path.cwd() / "config" / "regions.toml",
        Path(__file__).resolve().parents[3] / "config" / "regions.toml",
    ]
    for path in candidates:
        if path.is_file():
            return path
    return None


def default_config_dir() -> Path:
    """Return XDG-compliant user config directory (`~/.config/mitsubishi-connect`)."""
    base = Path(os.environ.get("XDG_CONFIG_HOME") or (Path.home() / ".config"))
    return base / "mitsubishi-connect"


def default_session_path() -> Path:
    """Return default session token file path."""
    env_path = os.environ.get("MITSUBISHI_SESSION")
    if env_path:
        return Path(env_path).expanduser()
    return default_config_dir() / "session.json"


def default_user_config_path() -> Path:
    """Return optional user config file (`~/.config/mitsubishi-connect/config.toml`)."""
    env_path = os.environ.get("MITSUBISHI_CONFIG")
    if env_path:
        return Path(env_path).expanduser()
    return default_config_dir() / "config.toml"


@dataclass(frozen=True)
class RegionConfig:
    """Regional endpoints, app identifiers, and locale settings."""

    name: str
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


def _merge_layer(merged: dict[str, Any], data: dict[str, Any]) -> None:
    if "default_region" in data:
        merged["default_region"] = data["default_region"]
    merged["app"].update(data.get("app", {}))
    for table in ("backends", "regions"):
        for name, values in data.get(table, {}).items():
            merged[table][name] = {**merged[table].get(name, {}), **values}


def _load_toml_data(config_path: Path | None = None) -> dict[str, Any]:
    merged: dict[str, Any] = {"app": {}, "backends": {}, "regions": {}}

    bundled = _find_bundled_regions_file()
    if bundled:
        _merge_layer(merged, tomllib.loads(bundled.read_text(encoding="utf-8")))

    user_cfg = config_path or default_user_config_path()
    if user_cfg and user_cfg.is_file():
        _merge_layer(merged, tomllib.loads(user_cfg.read_text(encoding="utf-8")))

    return merged


def _resolve_region(data: dict[str, Any], name: str) -> dict[str, Any]:
    """Flatten [app] + [backends.<backend>] + [regions.<name>] into one profile."""
    region = dict(data["regions"][name])
    backend = region.pop("backend", None)
    if backend is not None and backend not in data["backends"]:
        raise ValueError(f"Region '{name}' uses unknown backend '{backend}'.")
    return {**data["app"], **(data["backends"][backend] if backend else {}), **region}


def list_regions(config_path: Path | None = None) -> list[str]:
    """Return available region profile names from bundled + user TOML config."""
    data = _load_toml_data(config_path)
    return sorted(data.get("regions", {}).keys())


def load_region_config(
    region: str | None = None,
    *,
    config_path: Path | None = None,
    country: str | None = None,
    locale: str | None = None,
    timezone: str | None = None,
    timezone_offset: str | None = None,
    idm_base_url: str | None = None,
    kintaro_base_url: str | None = None,
) -> RegionConfig:
    """Load a `RegionConfig` with layered overrides: TOML -> env vars -> explicit args."""
    data = _load_toml_data(config_path)
    regions: dict[str, dict[str, Any]] = data.get("regions", {})

    selected = (
        region
        or os.environ.get("MITSUBISHI_REGION")
        or data.get("default_region")
        or "us"
    ).lower()

    if selected not in regions:
        available = ", ".join(sorted(regions)) or "(none)"
        raise ValueError(
            f"Unknown region '{selected}'. Available regions: {available}. "
            f"Add it to config/regions.toml or {default_user_config_path()}."
        )

    raw = _resolve_region(data, selected)

    for field_name in _SECRET_FIELDS:
        if field_name in raw:
            raw[field_name] = _decode_secret(str(raw[field_name]))

    for key in (
        "idm_client_id",
        "idm_client_secret",
        "idm_aes_key",
        "kintaro_app_code",
        "kintaro_app_hash",
        "kintaro_iv",
        "jwt_sign_key",
    ):
        val = str(raw.get(key, ""))
        if not val or (val.startswith("<") and val.endswith(">")):
            raise ValueError(
                f"Region '{selected}' is missing a configured value for '{key}'. "
                f"Set it in config/regions.toml or {default_user_config_path()}."
            )

    # Environment variable overrides
    env_map = {
        "country": "MITSUBISHI_COUNTRY",
        "locale": "MITSUBISHI_LOCALE",
        "region_code": "MITSUBISHI_REGION_CODE",
        "timezone": "MITSUBISHI_TIMEZONE",
        "timezone_offset": "MITSUBISHI_TIMEZONE_OFFSET",
        "idm_base_url": "MITSUBISHI_IDM_BASE_URL",
        "kintaro_base_url": "MITSUBISHI_KINTARO_BASE_URL",
    }
    for field_name, env_var in env_map.items():
        if os.environ.get(env_var):
            raw[field_name] = os.environ[env_var]

    # Explicit argument overrides
    explicit = {
        "country": country,
        "locale": locale,
        "timezone": timezone,
        "timezone_offset": timezone_offset,
        "idm_base_url": idm_base_url,
        "kintaro_base_url": kintaro_base_url,
    }
    for field_name, val in explicit.items():
        if val is not None:
            raw[field_name] = val

    return RegionConfig(
        name=selected,
        country=str(raw["country"]),
        locale=str(raw["locale"]),
        region_code=str(raw["region_code"]),
        timezone=str(raw["timezone"]),
        timezone_offset=str(raw["timezone_offset"]),
        package_name=str(raw["package_name"]),
        app_name=str(raw["app_name"]),
        app_version=str(raw["app_version"]),
        app_version_code=str(raw["app_version_code"]),
        user_agent=str(raw["user_agent"]),
        device_model=str(raw["device_model"]),
        device_os_version=str(raw["device_os_version"]),
        device_api_level=str(raw["device_api_level"]),
        idm_base_url=str(raw["idm_base_url"]).rstrip("/"),
        idm_client_id=str(raw["idm_client_id"]),
        idm_client_secret=str(raw["idm_client_secret"]),
        idm_aes_key=str(raw["idm_aes_key"]),
        kintaro_base_url=str(raw["kintaro_base_url"]).rstrip("/"),
        kintaro_app_code=str(raw["kintaro_app_code"]),
        kintaro_app_hash=str(raw["kintaro_app_hash"]),
        kintaro_iv=str(raw["kintaro_iv"]),
        kintaro_sec_cfg=tuple(int(x) for x in raw["kintaro_sec_cfg"]),
        jwt_sign_key=str(raw["jwt_sign_key"]),
    )


@dataclass
class SessionState:
    """Persisted authentication tokens and ephemeral Kintaro session keys."""

    device_id: str
    region: str = "us"
    access_token: str | None = None
    refresh_token: str | None = None
    token_expires_at: float | None = None
    enc_key: str | None = None
    sign_key: str | None = None
    default_vin: str | None = None

    @classmethod
    def create_new(cls, region: str = "us") -> SessionState:
        return cls(device_id=str(uuid.uuid4()), region=region)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".tmp")
        fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(asdict(self), fh, indent=2)
        os.replace(tmp, path)
        os.chmod(path, 0o600)

    @classmethod
    def load(cls, path: Path) -> SessionState:
        data = json.loads(path.read_text(encoding="utf-8"))
        known = {f for f in cls.__dataclass_fields__}
        filtered = {k: v for k, v in data.items() if k in known}
        return cls(**filtered)
