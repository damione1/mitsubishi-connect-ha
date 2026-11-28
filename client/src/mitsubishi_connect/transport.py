"""Transparent `httpx2` transports implementing IDM & Kintaro encryption/signing.

These transports let the auto-generated `mitsubishi_connect_api` OpenAPI client
speak plaintext JSON logically while handling all application-layer AES
encryption, SHA-256/MD5 request signing, device JWTs, and session-key / token
auto-recovery transparently on the wire.
"""

from __future__ import annotations

import json
import time
import uuid
from collections.abc import Awaitable, Callable
from typing import Any
from urllib.parse import quote

import httpx2

from .config import RegionConfig, SessionState
from .crypto import (
    aes_cbc_decrypt,
    aes_cbc_encrypt,
    aes_ecb_decrypt,
    aes_ecb_encrypt,
    derive_kintaro_init_material,
    idm_signature,
    kintaro_init_sign,
    kintaro_normal_sign,
    make_device_jwt,
)


class MitsubishiConnectError(Exception):
    """Error raised when IDM or Kintaro returns a non-success status or code."""

    def __init__(
        self,
        message: str,
        *,
        code: str | int | None = None,
        payload: Any = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.payload = payload


def _strip_nulls(obj: Any) -> Any:
    """Recursively omit `None` keys in dicts (matches Android Gson serialization)."""
    if isinstance(obj, dict):
        return {k: _strip_nulls(v) for k, v in obj.items() if v is not None}
    if isinstance(obj, list):
        return [_strip_nulls(v) for v in obj]
    return obj


class IdmAsyncTransport(httpx2.AsyncBaseTransport):
    """`httpx2` async transport for the IDM authentication backend."""

    def __init__(
        self,
        config: RegionConfig,
        state: SessionState,
        inner: httpx2.AsyncBaseTransport | None = None,
    ) -> None:
        self._cfg = config
        self._state = state
        self._inner = inner or httpx2.AsyncHTTPTransport()
        self._aes_key = config.idm_aes_key.encode("utf-8")

    async def handle_async_request(self, request: httpx2.Request) -> httpx2.Response:
        raw_body = await request.aread()
        plain_str = raw_body.decode("utf-8") if raw_body else "{}"
        if raw_body:
            try:
                plain_str = json.dumps(
                    _strip_nulls(json.loads(plain_str)), separators=(",", ":")
                )
            except json.JSONDecodeError:
                pass

        enc_body = json.dumps(
            {"payload": aes_ecb_encrypt(plain_str, self._aes_key)},
            separators=(",", ":"),
        ).encode("utf-8")

        ts = str(int(time.time() * 1000))
        nonce = str(uuid.uuid4())
        headers = {
            "User-Agent": self._cfg.user_agent,
            "Content-Type": "application/json; charset=utf-8",
            "X-Device": self._cfg.device_model,
            "X-Device-Id": self._state.device_id,
            "X-Locale": self._cfg.locale,
            "X-Timezone": self._cfg.timezone_offset,
            "X-App-Name": self._cfg.app_name,
            "X-App-Version": self._cfg.app_version,
            "X-App-Unique-Id": self._cfg.package_name,
            "X-OS-Type": "ANDROID",
            "X-OS-Version": self._cfg.device_api_level,
            "X-Timestamp": ts,
            "X-Encrypt-Payload": "true",
            "X-Client-Id": self._cfg.idm_client_id,
            "X-Client-Secret": self._cfg.idm_client_secret,
            "X-Nonce": nonce,
            "X-Signature": idm_signature(self._cfg.idm_client_id, nonce, ts),
        }
        if request.url.path.endswith("/api/v1/init"):
            headers["app-device-token"] = make_device_jwt(self._cfg.jwt_sign_key)

        wire_req = httpx2.Request(
            method=request.method,
            url=request.url,
            headers=headers,
            content=enc_body,
        )
        wire_resp = await self._inner.handle_async_request(wire_req)
        resp_bytes = await wire_resp.aread()

        if wire_resp.status_code != 200:
            raise MitsubishiConnectError(
                f"IDM {request.url.path} failed with HTTP {wire_resp.status_code}: "
                f"{resp_bytes.decode('utf-8', errors='replace')[:300]}",
                code=wire_resp.status_code,
            )

        outer = json.loads(resp_bytes.decode("utf-8"))
        if isinstance(outer, dict) and isinstance(outer.get("payload"), str):
            decoded = json.loads(aes_ecb_decrypt(outer["payload"], self._aes_key))
        else:
            decoded = outer

        if isinstance(decoded, dict) and str(decoded.get("code")) != "200":
            raise MitsubishiConnectError(
                f"IDM {request.url.path} error {decoded.get('code')}: {decoded.get('message')}",
                code=decoded.get("code"),
                payload=decoded,
            )

        return httpx2.Response(
            status_code=200,
            headers={"content-type": "application/json"},
            content=json.dumps(decoded).encode("utf-8"),
            request=request,
        )

    async def aclose(self) -> None:
        await self._inner.aclose()


class KintaroAsyncTransport(httpx2.AsyncBaseTransport):
    """`httpx2` async transport for the Kintaro vehicle & remote API."""

    def __init__(
        self,
        config: RegionConfig,
        state: SessionState,
        *,
        on_refresh_token: Callable[[], Awaitable[None]] | None = None,
        inner: httpx2.AsyncBaseTransport | None = None,
    ) -> None:
        self._cfg = config
        self._state = state
        self._on_refresh_token = on_refresh_token
        self._inner = inner or httpx2.AsyncHTTPTransport()
        self._init_material = derive_kintaro_init_material(config)
        self._iv = config.kintaro_iv.encode("ascii")
        self.vehicle_meta: dict[str, Any] | None = None

    def _base_headers(self, ts: str, sign: str, *, is_init: bool) -> dict[str, str]:
        headers = {
            "User-Agent": self._cfg.user_agent,
            "Content-Type": "text/plain" if is_init else "text/plain; charset=utf-8",
            "knt-correlation-id": self._state.device_id,
            "knt-app-key": self._cfg.kintaro_app_code,
            "knt-app-os": "ANDROID",
            "knt-app-version": self._cfg.app_version,
            "knt-app-unique-id": self._cfg.package_name,
            "knt-region": self._cfg.region_tag,
            "knt-language": self._cfg.language,
            "knt-locale": self._cfg.locale,
            "knt-req-id": str(uuid.uuid4()),
            "knt-timestamp": ts,
            "knt-device-os-version": self._cfg.device_os_version,
            "knt-device-model": self._cfg.device_model,
            "knt-sign": sign,
        }
        if is_init:
            headers["knt-app-device-token"] = make_device_jwt(self._cfg.jwt_sign_key)
        else:
            headers["knt-app-version-code"] = self._cfg.app_version_code
            headers["knt-iso-locale"] = self._cfg.locale
            headers["knt-timezone"] = self._cfg.timezone
            headers["knt-user-country"] = self._cfg.country
            headers["knt-region-code"] = self._cfg.region_code
            headers["knt-app-guest-mode"] = "false"
            if self._state.access_token:
                headers["knt-access-token"] = self._state.access_token
            if self.vehicle_meta:
                self._attach_vehicle_headers(headers, self.vehicle_meta)
        return headers

    @staticmethod
    def _attach_vehicle_headers(headers: dict[str, str], v: dict[str, Any]) -> None:
        model_obj = v.get("model") or {}
        ext_color = v.get("exteriorColor") or {}
        mapping = {
            "knt-primaryflag": v.get("isPrimary"),
            "knt-vehicleyear": model_obj.get("modelYear") if isinstance(model_obj, dict) else None,
            "knt-vehiclemodel": v.get("modelCode"),
            "knt-vehiclecolor": ext_color.get("code") if isinstance(ext_color, dict) else None,
            "knt-vehicletype": v.get("vehicleType"),
            "knt-isxbadgeflag": v.get("isXbadgeFlag"),
        }
        for key, val in mapping.items():
            if val is not None:
                headers[key] = str(val).lower() if isinstance(val, bool) else str(val)

    async def _do_check_version(self, request: httpx2.Request) -> httpx2.Response:
        ts = str(int(time.time() * 1000))
        sign = kintaro_init_sign(ts, self._init_material.secret_part, self._cfg)
        wire_req = httpx2.Request(
            method="POST",
            url=f"{self._cfg.kintaro_base_url}/service/checkVersion",
            headers=self._base_headers(ts, sign, is_init=True),
            content=b"",
        )
        wire_resp = await self._inner.handle_async_request(wire_req)
        resp_bytes = await wire_resp.aread()
        if wire_resp.status_code != 200:
            raise MitsubishiConnectError(
                f"Kintaro checkVersion failed with HTTP {wire_resp.status_code}: "
                f"{resp_bytes.decode('utf-8', errors='replace')[:300]}",
                code=wire_resp.status_code,
            )
        outer = json.loads(resp_bytes.decode("utf-8"))
        if outer.get("state") != "S" or not outer.get("payload"):
            raise MitsubishiConnectError(
                f"Kintaro checkVersion error: {outer}",
                code=outer.get("errorCode"),
                payload=outer,
            )
        decrypted = json.loads(
            aes_cbc_decrypt(outer["payload"], self._init_material.init_key, self._iv)
        )
        self._state.enc_key = decrypted["encKey"]
        self._state.sign_key = decrypted["signKey"]
        return httpx2.Response(
            status_code=200,
            headers={"content-type": "application/json"},
            content=json.dumps(decrypted).encode("utf-8"),
            request=request,
        )

    async def handle_async_request(
        self, request: httpx2.Request, _retry: int = 0
    ) -> httpx2.Response:
        if request.url.path.endswith("/service/checkVersion"):
            return await self._do_check_version(request)

        if not self._state.enc_key or not self._state.sign_key:
            await self._do_check_version(request)

        enc_key = self._state.enc_key.encode("ascii")  # type: ignore[union-attr]
        sign_key = self._state.sign_key  # type: ignore[assignment]
        ts = str(int(time.time() * 1000))

        raw_body = await request.aread()
        raw_query = request.url.query.decode("utf-8") if request.url.query else ""
        base_url = str(request.url.copy_with(query=None))

        wire_url = base_url
        wire_content = b""

        if raw_query:
            enc_q = aes_cbc_encrypt(raw_query, enc_key, self._iv)
            sign = kintaro_normal_sign(enc_q, ts, sign_key, self._cfg)  # type: ignore[arg-type]
            wire_url = f"{base_url}?params={quote(enc_q, safe='')}"
        elif raw_body:
            body_text = raw_body.decode("utf-8")
            try:
                body_text = json.dumps(
                    _strip_nulls(json.loads(body_text)), separators=(",", ":")
                )
            except json.JSONDecodeError:
                pass
            enc_b = aes_cbc_encrypt(body_text, enc_key, self._iv)
            sign = kintaro_normal_sign(enc_b, ts, sign_key, self._cfg)  # type: ignore[arg-type]
            wire_content = enc_b.encode("utf-8")
        else:
            sign = kintaro_normal_sign("", ts, sign_key, self._cfg)  # type: ignore[arg-type]

        wire_req = httpx2.Request(
            method=request.method,
            url=wire_url,
            headers=self._base_headers(ts, sign, is_init=False),
            content=wire_content,
        )
        wire_resp = await self._inner.handle_async_request(wire_req)
        resp_bytes = await wire_resp.aread()

        if wire_resp.status_code != 200:
            raise MitsubishiConnectError(
                f"Kintaro {request.method} {request.url.path} failed with HTTP {wire_resp.status_code}: "
                f"{resp_bytes.decode('utf-8', errors='replace')[:300]}",
                code=wire_resp.status_code,
            )

        outer = json.loads(resp_bytes.decode("utf-8"))
        state_flag = outer.get("state")
        err_code = str(outer.get("errorCode", ""))

        if state_flag != "S" and _retry < 2:
            if err_code == "600001":
                await self._do_check_version(request)
                return await self.handle_async_request(request, _retry=_retry + 1)
            if err_code in ("600002", "600004") and self._on_refresh_token:
                await self._on_refresh_token()
                return await self.handle_async_request(request, _retry=_retry + 1)

        if state_flag != "S":
            raise MitsubishiConnectError(
                f"Kintaro {request.url.path} error {err_code}: {outer.get('errorMessage') or outer}",
                code=outer.get("errorCode"),
                payload=outer,
            )

        payload = outer.get("payload")
        if payload is None:
            decoded_bytes = b"{}"
        else:
            resp_mode = wire_resp.headers.get("knt-api-response-mode", "").upper()
            if resp_mode == "PLAINTEXT" or not isinstance(payload, str):
                decoded_bytes = json.dumps(payload).encode("utf-8")
            else:
                decoded_text = aes_cbc_decrypt(payload, enc_key, self._iv)
                decoded_bytes = decoded_text.encode("utf-8")

        return httpx2.Response(
            status_code=200,
            headers={"content-type": "application/json"},
            content=decoded_bytes,
            request=request,
        )

    async def aclose(self) -> None:
        await self._inner.aclose()
