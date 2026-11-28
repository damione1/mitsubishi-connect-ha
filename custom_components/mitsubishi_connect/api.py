"""Async aiohttp API client for the Mitsubishi Connect Home Assistant integration.

Designed for permanent, low-noise operation:
- Persists a stable `device_id` and token bundle via callback
- Proactively refreshes `access_token` before expiry without re-logging in
- Auto-recovers once on Kintaro `600001` (expired session key) and `600002`/`600004`
- Raises `MitsubishiAuthError` immediately on permanent auth failures so HA triggers
  Reauth instead of hammering the login endpoint
"""

from __future__ import annotations

import asyncio
import json
import time
import uuid
from collections.abc import Awaitable, Callable
from dataclasses import asdict, dataclass
from typing import Any
from urllib.parse import quote, urlencode

import aiohttp

from .const import TOKEN_REFRESH_MARGIN_SECONDS
from .crypto import (
    aes_cbc_decrypt,
    aes_cbc_encrypt,
    aes_ecb_decrypt,
    aes_ecb_encrypt,
    compute_pin_hash,
    derive_kintaro_init_material,
    generate_client_nonce,
    idm_signature,
    kintaro_init_sign,
    kintaro_normal_sign,
    make_device_jwt,
    rsa_encrypt_password,
)
from .regions import RegionProfile


class MitsubishiApiError(Exception):
    """Generic API error returned by IDM or Kintaro."""

    def __init__(self, message: str, *, code: str | int | None = None) -> None:
        super().__init__(message)
        self.code = code


class MitsubishiAuthError(MitsubishiApiError):
    """Authentication / session failure requiring user reauthentication."""


@dataclass
class TokenBundle:
    device_id: str
    access_token: str | None = None
    refresh_token: str | None = None
    token_expires_at: float | None = None
    enc_key: str | None = None
    sign_key: str | None = None

    @classmethod
    def new(cls) -> TokenBundle:
        return cls(device_id=str(uuid.uuid4()))

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TokenBundle:
        known = set(cls.__dataclass_fields__)
        filtered = {k: v for k, v in data.items() if k in known}
        if not filtered.get("device_id"):
            filtered["device_id"] = str(uuid.uuid4())
        return cls(**filtered)


def _strip_nulls(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: _strip_nulls(v) for k, v in obj.items() if v is not None}
    if isinstance(obj, list):
        return [_strip_nulls(v) for v in obj]
    return obj


class MitsubishiApiClient:
    """Async aiohttp client tailored for Home Assistant."""

    def __init__(
        self,
        session: aiohttp.ClientSession,
        profile: RegionProfile,
        tokens: TokenBundle | None = None,
        *,
        on_tokens_updated: Callable[[TokenBundle], Awaitable[None]] | None = None,
    ) -> None:
        self._http = session
        self.profile = profile
        self.tokens = tokens or TokenBundle.new()
        self._on_tokens_updated = on_tokens_updated
        self._init_material = derive_kintaro_init_material(profile)
        self._idm_key = profile.idm_aes_key.encode("utf-8")
        self._knt_iv = profile.kintaro_iv.encode("ascii")
        self._auth_lock = asyncio.Lock()
        self._vehicle_headers_cache: dict[str, dict[str, str]] = {}

    async def _persist(self) -> None:
        if self._on_tokens_updated:
            await self._on_tokens_updated(self.tokens)

    def register_vehicle_meta(self, vehicle: dict[str, Any]) -> None:
        vin = vehicle.get("vin")
        if not vin:
            return
        model_obj = vehicle.get("model") or {}
        ext_color = vehicle.get("exteriorColor") or {}
        mapping = {
            "knt-primaryflag": vehicle.get("isPrimary"),
            "knt-vehicleyear": model_obj.get("modelYear") if isinstance(model_obj, dict) else None,
            "knt-vehiclemodel": vehicle.get("modelCode"),
            "knt-vehiclecolor": ext_color.get("code") if isinstance(ext_color, dict) else None,
            "knt-vehicletype": vehicle.get("vehicleType"),
            "knt-isxbadgeflag": vehicle.get("isXbadgeFlag"),
        }
        self._vehicle_headers_cache[vin] = {
            k: (str(v).lower() if isinstance(v, bool) else str(v))
            for k, v in mapping.items()
            if v is not None
        }

    # ------------------------------------------------------------------
    # IDM Auth
    # ------------------------------------------------------------------

    def _idm_headers(self, *, include_device_token: bool) -> dict[str, str]:
        ts = str(int(time.time() * 1000))
        nonce = str(uuid.uuid4())
        headers = {
            "User-Agent": self.profile.user_agent,
            "Content-Type": "application/json; charset=utf-8",
            "X-Device": self.profile.device_model,
            "X-Device-Id": self.tokens.device_id,
            "X-Locale": self.profile.locale,
            "X-Timezone": self.profile.timezone_offset,
            "X-App-Name": self.profile.app_name,
            "X-App-Version": self.profile.app_version,
            "X-App-Unique-Id": self.profile.package_name,
            "X-OS-Type": "ANDROID",
            "X-OS-Version": self.profile.device_api_level,
            "X-Timestamp": ts,
            "X-Encrypt-Payload": "true",
            "X-Client-Id": self.profile.idm_client_id,
            "X-Client-Secret": self.profile.idm_client_secret,
            "X-Nonce": nonce,
            "X-Signature": idm_signature(self.profile.idm_client_id, nonce, ts),
        }
        if include_device_token:
            headers["app-device-token"] = make_device_jwt(self.profile.jwt_sign_key)
        return headers

    async def _idm_post(
        self, path: str, body: dict[str, Any], *, include_device_token: bool
    ) -> dict[str, Any]:
        url = f"{self.profile.idm_base_url}{path}"
        enc_body = {
            "payload": aes_ecb_encrypt(
                json.dumps(_strip_nulls(body), separators=(",", ":")),
                self._idm_key,
            )
        }
        async with self._http.post(
            url,
            json=enc_body,
            headers=self._idm_headers(include_device_token=include_device_token),
            timeout=aiohttp.ClientTimeout(total=30),
        ) as resp:
            text = await resp.text()
            if resp.status in (401, 403):
                raise MitsubishiAuthError(f"IDM {path} rejected (HTTP {resp.status})", code=resp.status)
            if resp.status != 200:
                raise MitsubishiApiError(f"IDM {path} HTTP {resp.status}: {text[:200]}", code=resp.status)
            outer = json.loads(text)
            decoded = (
                json.loads(aes_ecb_decrypt(outer["payload"], self._idm_key))
                if isinstance(outer, dict) and isinstance(outer.get("payload"), str)
                else outer
            )
            code = str(decoded.get("code", ""))
            if code != "200":
                msg = decoded.get("message") or str(decoded)
                if path in ("/api/v1/login", "/api/v1/refreshToken"):
                    raise MitsubishiAuthError(f"IDM {path} error {code}: {msg}", code=code)
                raise MitsubishiApiError(f"IDM {path} error {code}: {msg}", code=code)
            return decoded

    async def login(self, email: str, password: str) -> None:
        """Perform full IDM login + Kintaro handshake and persist tokens."""
        async with self._auth_lock:
            init_res = await self._idm_post(
                "/api/v1/init",
                {"deviceId": self.tokens.device_id, "clientId": self.profile.idm_client_id},
                include_device_token=True,
            )
            data = init_res.get("data") or {}
            enc_pw = rsa_encrypt_password(password, data["keyIndex"], data["publicKey"])
            login_res = await self._idm_post(
                "/api/v1/login",
                {
                    "username": email,
                    "password": enc_pw,
                    "clientId": self.profile.idm_client_id,
                    "deviceId": self.tokens.device_id,
                },
                include_device_token=False,
            )
            self._apply_tokens(login_res.get("data") or {})
            await self._kintaro_handshake_unlocked()
            await self._persist()

    async def refresh_access_token(self) -> None:
        """Refresh IDM access token; raises MitsubishiAuthError if refresh fails."""
        async with self._auth_lock:
            if not self.tokens.refresh_token:
                raise MitsubishiAuthError("No refresh token available; reauthentication required.")
            res = await self._idm_post(
                "/api/v1/refreshToken",
                {
                    "refreshToken": self.tokens.refresh_token,
                    "clientId": self.profile.idm_client_id,
                    "clientSecret": self.profile.idm_client_secret,
                },
                include_device_token=False,
            )
            self._apply_tokens(res.get("data") or {})
            await self._persist()

    def _apply_tokens(self, data: dict[str, Any]) -> None:
        if data.get("accessToken"):
            self.tokens.access_token = data["accessToken"]
        if data.get("refreshToken"):
            self.tokens.refresh_token = data["refreshToken"]
        expires_in = data.get("expiresIn")
        if isinstance(expires_in, (int, float)):
            self.tokens.token_expires_at = time.time() + float(expires_in)

    async def ensure_valid_session(self) -> None:
        """Proactively refresh expiring access tokens and ensure Kintaro keys exist."""
        if not self.tokens.access_token:
            if self.tokens.refresh_token:
                await self.refresh_access_token()
            else:
                raise MitsubishiAuthError("Missing access token; reauthentication required.")
        elif (
            self.tokens.token_expires_at is not None
            and time.time() >= self.tokens.token_expires_at - TOKEN_REFRESH_MARGIN_SECONDS
            and self.tokens.refresh_token
        ):
            await self.refresh_access_token()

        if not self.tokens.enc_key or not self.tokens.sign_key:
            async with self._auth_lock:
                if not self.tokens.enc_key or not self.tokens.sign_key:
                    await self._kintaro_handshake_unlocked()
                    await self._persist()

    # ------------------------------------------------------------------
    # Kintaro Transport
    # ------------------------------------------------------------------

    def _kintaro_headers(
        self, ts: str, sign: str, *, is_init: bool, vin: str | None = None
    ) -> dict[str, str]:
        headers = {
            "User-Agent": self.profile.user_agent,
            "Content-Type": "text/plain" if is_init else "text/plain; charset=utf-8",
            "knt-correlation-id": self.tokens.device_id,
            "knt-app-key": self.profile.kintaro_app_code,
            "knt-app-os": "ANDROID",
            "knt-app-version": self.profile.app_version,
            "knt-app-unique-id": self.profile.package_name,
            "knt-region": self.profile.region_tag,
            "knt-language": self.profile.language,
            "knt-locale": self.profile.locale,
            "knt-req-id": str(uuid.uuid4()),
            "knt-timestamp": ts,
            "knt-device-os-version": self.profile.device_os_version,
            "knt-device-model": self.profile.device_model,
            "knt-sign": sign,
        }
        if is_init:
            headers["knt-app-device-token"] = make_device_jwt(self.profile.jwt_sign_key)
        else:
            headers["knt-app-version-code"] = self.profile.app_version_code
            headers["knt-iso-locale"] = self.profile.locale
            headers["knt-timezone"] = self.profile.timezone
            headers["knt-user-country"] = self.profile.country
            headers["knt-region-code"] = self.profile.region_code
            headers["knt-app-guest-mode"] = "false"
            if self.tokens.access_token:
                headers["knt-access-token"] = self.tokens.access_token
            if vin and vin in self._vehicle_headers_cache:
                headers.update(self._vehicle_headers_cache[vin])
        return headers

    async def _kintaro_handshake_unlocked(self) -> None:
        ts = str(int(time.time() * 1000))
        sign = kintaro_init_sign(ts, self._init_material.secret_part, self.profile)
        url = f"{self.profile.kintaro_base_url}/service/checkVersion"
        async with self._http.post(
            url,
            data=b"",
            headers=self._kintaro_headers(ts, sign, is_init=True),
            timeout=aiohttp.ClientTimeout(total=30),
        ) as resp:
            text = await resp.text()
            if resp.status != 200:
                raise MitsubishiApiError(
                    f"Kintaro checkVersion HTTP {resp.status}: {text[:200]}", code=resp.status
                )
            outer = json.loads(text)
            if outer.get("state") != "S" or not outer.get("payload"):
                raise MitsubishiApiError(
                    f"Kintaro checkVersion error: {outer}", code=outer.get("errorCode")
                )
            decoded = json.loads(
                aes_cbc_decrypt(outer["payload"], self._init_material.init_key, self._knt_iv)
            )
            self.tokens.enc_key = decoded["encKey"]
            self.tokens.sign_key = decoded["signKey"]

    async def kintaro_request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
        vin: str | None = None,
        _retry: int = 0,
    ) -> Any:
        await self.ensure_valid_session()

        enc_key = self.tokens.enc_key.encode("ascii")  # type: ignore[union-attr]
        sign_key = self.tokens.sign_key  # type: ignore[assignment]
        ts = str(int(time.time() * 1000))

        url = f"{self.profile.kintaro_base_url}/{path.lstrip('/')}"
        body_bytes: bytes | None = None

        if params:
            filtered = {k: v for k, v in params.items() if v is not None}
            enc_q = aes_cbc_encrypt(urlencode(filtered), enc_key, self._knt_iv)
            sign = kintaro_normal_sign(enc_q, ts, sign_key, self.profile)  # type: ignore[arg-type]
            url = f"{url}?params={quote(enc_q, safe='')}"
        elif json_body is not None:
            raw_json = json.dumps(_strip_nulls(json_body), separators=(",", ":"))
            enc_b = aes_cbc_encrypt(raw_json, enc_key, self._knt_iv)
            sign = kintaro_normal_sign(enc_b, ts, sign_key, self.profile)  # type: ignore[arg-type]
            body_bytes = enc_b.encode("utf-8")
        else:
            sign = kintaro_normal_sign("", ts, sign_key, self.profile)  # type: ignore[arg-type]

        async with self._http.request(
            method.upper(),
            url,
            data=body_bytes,
            headers=self._kintaro_headers(ts, sign, is_init=False, vin=vin),
            timeout=aiohttp.ClientTimeout(total=30),
        ) as resp:
            text = await resp.text()
            if resp.status in (401, 403):
                raise MitsubishiAuthError(f"Kintaro {path} HTTP {resp.status}", code=resp.status)
            if resp.status != 200:
                raise MitsubishiApiError(
                    f"Kintaro {path} HTTP {resp.status}: {text[:200]}", code=resp.status
                )
            outer = json.loads(text)
            state_flag = outer.get("state")
            err_code = str(outer.get("errorCode", ""))

            if state_flag != "S" and _retry < 2:
                if err_code == "600001":
                    async with self._auth_lock:
                        await self._kintaro_handshake_unlocked()
                        await self._persist()
                    return await self.kintaro_request(
                        method, path, params=params, json_body=json_body, vin=vin, _retry=_retry + 1
                    )
                if err_code in ("600002", "600004"):
                    await self.refresh_access_token()
                    return await self.kintaro_request(
                        method, path, params=params, json_body=json_body, vin=vin, _retry=_retry + 1
                    )

            if state_flag != "S":
                if err_code in ("600002", "600004", "401005"):
                    raise MitsubishiAuthError(f"Session expired ({err_code})", code=err_code)
                raise MitsubishiApiError(
                    f"Kintaro {path} error {err_code}: {outer.get('errorMessage') or outer}",
                    code=err_code,
                )

            payload = outer.get("payload")
            if payload is None:
                return {}
            if resp.headers.get("knt-api-response-mode", "").upper() == "PLAINTEXT" or not isinstance(
                payload, str
            ):
                return payload
            decrypted = aes_cbc_decrypt(payload, enc_key, self._knt_iv)
            try:
                return json.loads(decrypted)
            except json.JSONDecodeError:
                return decrypted

    # ------------------------------------------------------------------
    # High-level Vehicle & Remote Operations
    # ------------------------------------------------------------------

    async def get_vehicles(self) -> list[dict[str, Any]]:
        data = await self.kintaro_request("GET", "/vehicle/getVehicleList/v1")
        vehicles = (data or {}).get("vehicles") or (data or {}).get("vehicleList") or []
        for v in vehicles:
            self.register_vehicle_meta(v)
        return vehicles

    async def get_vsr(self, vin: str, internal_vin: str | None = None) -> dict[str, Any]:
        return await self.kintaro_request(
            "GET", "/status/getVSR/v1", params={"vin": vin, "internalVin": internal_vin}, vin=vin
        )

    async def get_engine_details(
        self, vin: str, internal_vin: str | None = None
    ) -> dict[str, Any]:
        return await self.kintaro_request(
            "GET",
            "/status/getEngineDetails/v1",
            params={"vin": vin, "internalVin": internal_vin},
            vin=vin,
        )

    async def _pin_hash(self, vin: str, pin: str, internal_vin: str | None = None) -> str:
        client_nonce = generate_client_nonce()
        res = await self.kintaro_request(
            "POST",
            "/remote/generateServerNonce/v1",
            json_body={"vin": vin, "internalVin": internal_vin, "clientNonce": client_nonce},
            vin=vin,
        )
        return compute_pin_hash(pin, client_nonce, res["serverNonce"])

    async def poll_request(
        self, request_id: str, *, vin: str | None = None, interval: float = 5.0, timeout: float = 90.0
    ) -> dict[str, Any]:
        deadline = time.monotonic() + timeout
        last: dict[str, Any] = {"requestId": request_id, "status": 1}
        while time.monotonic() < deadline:
            res = await self.kintaro_request(
                "POST",
                "/remote/getBatchRequestStatus/v1",
                json_body={"requestIdList": [{"requestId": request_id}]},
                vin=vin,
            )
            items = (res or {}).get("requestStatusList") or []
            if items:
                last = items[0]
                if last.get("status") != 1:
                    return last
            await asyncio.sleep(interval)
        raise MitsubishiApiError(f"Remote command {request_id} timed out")

    async def _poll_if_async(self, res: dict[str, Any], *, vin: str) -> dict[str, Any]:
        req_id = (res or {}).get("requestId")
        if req_id:
            result = await self.poll_request(
                req_id,
                vin=vin,
                interval=float(res.get("pollingInterval") or 5),
                timeout=float(res.get("duration") or 90),
            )
            if result.get("status") != 2:
                raise MitsubishiApiError(f"Remote command failed (status={result.get('status')})")
            return result
        return res

    async def refresh_vsr(self, vin: str, internal_vin: str | None = None) -> dict[str, Any]:
        res = await self.kintaro_request(
            "POST",
            "/status/refreshVSR/v1",
            json_body={"vin": vin, "internalVin": internal_vin, "refreshType": 1},
            vin=vin,
        )
        return await self._poll_if_async(res, vin=vin)

    async def get_location(
        self, vin: str, *, pin: str | None = None, internal_vin: str | None = None
    ) -> dict[str, Any]:
        body: dict[str, Any] = {"vin": vin, "internalVin": internal_vin}
        if pin:
            body["pinHash"] = await self._pin_hash(vin, pin, internal_vin)
        return await self.kintaro_request(
            "POST", "/remote/getVehicleLocation/v1", json_body=body, vin=vin
        )

    async def lock_door(
        self, vin: str, *, pin: str | None = None, internal_vin: str | None = None
    ) -> dict[str, Any]:
        body: dict[str, Any] = {"vin": vin, "internalVin": internal_vin}
        if pin:
            body["pinHash"] = await self._pin_hash(vin, pin, internal_vin)
        res = await self.kintaro_request("POST", "/remote/lockDoor/v1", json_body=body, vin=vin)
        return await self._poll_if_async(res, vin=vin)

    async def unlock_door(
        self, vin: str, *, pin: str, internal_vin: str | None = None
    ) -> dict[str, Any]:
        pin_hash = await self._pin_hash(vin, pin, internal_vin)
        res = await self.kintaro_request(
            "POST",
            "/remote/unlockDoor/v1",
            json_body={"vin": vin, "internalVin": internal_vin, "pinHash": pin_hash},
            vin=vin,
        )
        return await self._poll_if_async(res, vin=vin)

    async def start_engine(
        self,
        vin: str,
        *,
        pin: str,
        target_temperature: float = 21.0,
        temperature_unit: str = "C",
        hvac_settings: dict[str, Any] | None = None,
        internal_vin: str | None = None,
    ) -> dict[str, Any]:
        pin_hash = await self._pin_hash(vin, pin, internal_vin)
        body: dict[str, Any] = {
            "vin": vin,
            "internalVin": internal_vin,
            "pinHash": pin_hash,
            "targetTemperature": f"{target_temperature:.1f}",
            "temperatureUnit": temperature_unit.upper(),
            "startFlag": 0,
        }
        if hvac_settings:
            body["hvacSettings"] = hvac_settings
        res = await self.kintaro_request("POST", "/remote/startEngine/v1", json_body=body, vin=vin)
        return await self._poll_if_async(res, vin=vin)

    async def stop_engine(
        self, vin: str, *, pin: str | None = None, internal_vin: str | None = None
    ) -> dict[str, Any]:
        body: dict[str, Any] = {"vin": vin, "internalVin": internal_vin, "cancelFlag": 0}
        if pin:
            body["pinHash"] = await self._pin_hash(vin, pin, internal_vin)
        res = await self.kintaro_request("POST", "/remote/stopEngine/v1", json_body=body, vin=vin)
        return await self._poll_if_async(res, vin=vin)

    async def start_light(
        self, vin: str, *, pin: str | None = None, internal_vin: str | None = None
    ) -> dict[str, Any]:
        body: dict[str, Any] = {"vin": vin, "internalVin": internal_vin}
        if pin:
            body["pinHash"] = await self._pin_hash(vin, pin, internal_vin)
        res = await self.kintaro_request("POST", "/remote/startLight/v1", json_body=body, vin=vin)
        return await self._poll_if_async(res, vin=vin)

    async def start_horn(
        self, vin: str, *, pin: str | None = None, internal_vin: str | None = None
    ) -> dict[str, Any]:
        body: dict[str, Any] = {"vin": vin, "internalVin": internal_vin}
        if pin:
            body["pinHash"] = await self._pin_hash(vin, pin, internal_vin)
        res = await self.kintaro_request("POST", "/remote/startHorn/v1", json_body=body, vin=vin)
        return await self._poll_if_async(res, vin=vin)

    async def get_charge_details(
        self, vin: str, internal_vin: str | None = None
    ) -> dict[str, Any]:
        return await self.kintaro_request(
            "GET",
            "/status/getChargeDetails/v1",
            params={"vin": vin, "internalVin": internal_vin},
            vin=vin,
        )

    async def start_charge(
        self, vin: str, *, pin: str | None = None, internal_vin: str | None = None
    ) -> dict[str, Any]:
        body: dict[str, Any] = {"vin": vin, "internalVin": internal_vin}
        if pin:
            body["pinHash"] = await self._pin_hash(vin, pin, internal_vin)
        res = await self.kintaro_request("POST", "/remote/startCharge/v1", json_body=body, vin=vin)
        return await self._poll_if_async(res, vin=vin)

    async def stop_charge(
        self, vin: str, *, pin: str | None = None, internal_vin: str | None = None
    ) -> dict[str, Any]:
        body: dict[str, Any] = {"vin": vin, "internalVin": internal_vin}
        if pin:
            body["pinHash"] = await self._pin_hash(vin, pin, internal_vin)
        res = await self.kintaro_request("POST", "/remote/stopCharge/v1", json_body=body, vin=vin)
        return await self._poll_if_async(res, vin=vin)
