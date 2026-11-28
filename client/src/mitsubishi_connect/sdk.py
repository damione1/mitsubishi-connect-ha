"""High-level async SDK built on top of the OpenAPI-generated client."""

from __future__ import annotations

import asyncio
import time
from typing import Any

import httpx2
from mitsubishi_connect_api import Client as GeneratedApiClient
from mitsubishi_connect_api.api.auth import idm_init, idm_login, idm_refresh_token
from mitsubishi_connect_api.api.phev import (
    get_charge_details,
    get_climate_details,
    get_soc_setting,
    set_soc_setting,
    start_charge,
    start_climate,
    stop_charge,
    stop_climate,
)
from mitsubishi_connect_api.api.schedules import (
    get_charge_climate_schedule,
    get_charge_schedule,
    get_climate_schedule,
)
from mitsubishi_connect_api.api.polling import (
    generate_server_nonce,
    get_available_service,
    get_batch_request_status,
)
from mitsubishi_connect_api.api.remote import (
    get_vehicle_location,
    lock_door,
    start_engine,
    start_horn,
    start_light,
    stop_engine,
    unlock_door,
)
from mitsubishi_connect_api.api.session import kintaro_check_version
from mitsubishi_connect_api.api.status import (
    get_engine_details,
    get_vsr,
    refresh_vsr,
)
from mitsubishi_connect_api.api.vehicle import (
    get_curfew_alert,
    get_geofence_alert,
    get_speed_alert,
    get_vehicle_list,
    verify_pin,
)
from mitsubishi_connect_api.models import (
    BatchRequestStatusRequest,
    GetAvailableServiceIsSecondaryVehicle,
    HvacSettings,
    IdmInitRequest,
    IdmLoginRequest,
    IdmRefreshTokenRequest,
    PinCommandRequest,
    RefreshVsrRequest,
    RemoteCommandResponse,
    RequestIdItem,
    ServerNonceRequest,
    SOCSettingEntity,
    StartEngineRequest,
    StopEngineRequest,
    Vehicle,
    VerifyPinRequest,
)
from mitsubishi_connect_api.types import UNSET

from .config import RegionConfig, SessionState
from .crypto import compute_pin_hash, generate_client_nonce, rsa_encrypt_password
from .transport import IdmAsyncTransport, KintaroAsyncTransport, MitsubishiConnectError


def _unset(val: Any) -> Any:
    return UNSET if val is None else val


class MitsubishiConnectSDK:
    """Async SDK orchestrating the generated OpenAPI client + encrypted transports."""

    def __init__(
        self,
        config: RegionConfig,
        state: SessionState | None = None,
        *,
        timeout: float = 30.0,
    ) -> None:
        self.config = config
        self.state = state or SessionState.create_new(region=config.name)
        self._timeout = httpx2.Timeout(timeout)
        self._idm_transport = IdmAsyncTransport(self.config, self.state)
        self._kintaro_transport = KintaroAsyncTransport(
            self.config,
            self.state,
            on_refresh_token=self.refresh_token,
        )
        self.idm_client = GeneratedApiClient(
            base_url=self.config.idm_base_url,
            timeout=self._timeout,
            httpx_args={"transport": self._idm_transport},
            raise_on_unexpected_status=True,
        )
        self.kintaro_client = GeneratedApiClient(
            base_url=self.config.kintaro_base_url,
            timeout=self._timeout,
            httpx_args={"transport": self._kintaro_transport},
            raise_on_unexpected_status=True,
        )

    async def __aenter__(self) -> MitsubishiConnectSDK:
        await self.idm_client.__aenter__()
        await self.kintaro_client.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.kintaro_client.__aexit__(*args)
        await self.idm_client.__aexit__(*args)

    def set_vehicle_context(self, vehicle: Vehicle | dict[str, Any] | None) -> None:
        if vehicle is None:
            self._kintaro_transport.vehicle_meta = None
        elif isinstance(vehicle, dict):
            self._kintaro_transport.vehicle_meta = vehicle
        else:
            self._kintaro_transport.vehicle_meta = vehicle.to_dict()

    # ------------------------------------------------------------------
    # Auth & Session
    # ------------------------------------------------------------------

    async def idm_init(self) -> tuple[str, str]:
        res = await idm_init.asyncio(
            client=self.idm_client,
            body=IdmInitRequest(
                device_id=self.state.device_id,
                client_id=self.config.idm_client_id,
            ),
        )
        if not res or not res.data or res.data is UNSET:
            raise MitsubishiConnectError("Empty response from IDM /api/v1/init")
        return res.data.key_index, res.data.public_key

    async def handshake(self) -> tuple[str, str]:
        res = await kintaro_check_version.asyncio(client=self.kintaro_client)
        if not res:
            raise MitsubishiConnectError("Empty response from Kintaro /service/checkVersion")
        return res.enc_key, res.sign_key

    async def login(self, username: str, password: str) -> dict[str, Any]:
        key_index, public_key = await self.idm_init()
        encrypted_pw = rsa_encrypt_password(password, key_index, public_key)
        res = await idm_login.asyncio(
            client=self.idm_client,
            body=IdmLoginRequest(
                username=username,
                password=encrypted_pw,
                client_id=self.config.idm_client_id,
                device_id=self.state.device_id,
            ),
        )
        if not res or not res.data or res.data is UNSET:
            raise MitsubishiConnectError("Empty response from IDM /api/v1/login")
        data = res.data.to_dict()
        self._store_tokens(data)
        await self.handshake()
        return data

    async def refresh_token(self) -> None:
        if not self.state.refresh_token:
            raise MitsubishiConnectError("No refresh_token stored; please log in again.")
        res = await idm_refresh_token.asyncio(
            client=self.idm_client,
            body=IdmRefreshTokenRequest(
                refresh_token=self.state.refresh_token,
                client_id=self.config.idm_client_id,
                client_secret=self.config.idm_client_secret,
            ),
        )
        if not res or not res.data or res.data is UNSET:
            raise MitsubishiConnectError("Empty response from IDM /api/v1/refreshToken")
        self._store_tokens(res.data.to_dict())

    def _store_tokens(self, data: dict[str, Any]) -> None:
        if data.get("accessToken"):
            self.state.access_token = data["accessToken"]
        if data.get("refreshToken"):
            self.state.refresh_token = data["refreshToken"]
        expires_in = data.get("expiresIn")
        if isinstance(expires_in, (int, float)):
            self.state.token_expires_at = time.time() + float(expires_in)

    # ------------------------------------------------------------------
    # PIN & Polling Helpers
    # ------------------------------------------------------------------

    async def compute_pin_hash(
        self, vin: str, pin: str, internal_vin: str | None = None
    ) -> str:
        client_nonce = generate_client_nonce()
        res = await generate_server_nonce.asyncio(
            client=self.kintaro_client,
            body=ServerNonceRequest(
                vin=vin,
                internal_vin=_unset(internal_vin),
                client_nonce=client_nonce,
            ),
        )
        if not res:
            raise MitsubishiConnectError("Empty response from generateServerNonce")
        return compute_pin_hash(pin, client_nonce, res.server_nonce)

    async def poll_request(
        self,
        request_id: str,
        *,
        interval: float = 5.0,
        timeout: float = 90.0,
    ) -> dict[str, Any]:
        deadline = time.monotonic() + timeout
        last: dict[str, Any] = {"requestId": request_id, "status": 1}
        while time.monotonic() < deadline:
            res = await get_batch_request_status.asyncio(
                client=self.kintaro_client,
                body=BatchRequestStatusRequest(
                    request_id_list=[RequestIdItem(request_id=request_id)]
                ),
            )
            if res and res.request_status_list and res.request_status_list is not UNSET:
                item = res.request_status_list[0].to_dict()
                last = item
                if item.get("status") != 1:
                    return item
            await asyncio.sleep(interval)
        raise MitsubishiConnectError(
            f"Timed out waiting for request {request_id}", payload=last
        )

    async def _maybe_poll(
        self, res: RemoteCommandResponse | None, *, wait: bool
    ) -> dict[str, Any]:
        if not res:
            return {}
        data = res.to_dict()
        req_id = data.get("requestId")
        if wait and isinstance(req_id, str) and req_id:
            return await self.poll_request(
                req_id,
                interval=float(data.get("pollingInterval") or 5),
                timeout=float(data.get("duration") or 90),
            )
        return data

    # ------------------------------------------------------------------
    # Vehicle Endpoints
    # ------------------------------------------------------------------

    async def get_vehicles(self) -> list[Vehicle]:
        res = await get_vehicle_list.asyncio(client=self.kintaro_client)
        if not res or not res.vehicles or res.vehicles is UNSET:
            return []
        return list(res.vehicles)
    async def verify_pin(
        self, vin: str, pin: str, internal_vin: str | None = None
    ) -> dict[str, Any]:
        pin_hash = await self.compute_pin_hash(vin, pin, internal_vin)
        res = await verify_pin.asyncio(
            client=self.kintaro_client,
            body=VerifyPinRequest(
                vin=vin, internal_vin=_unset(internal_vin), pin_hash=pin_hash
            ),
        )
        return res.to_dict() if res else {}

    async def get_curfew_alert(self, vin: str, internal_vin: str | None = None) -> dict[str, Any]:
        res = await get_curfew_alert.asyncio(
            client=self.kintaro_client, vin=vin, internal_vin=_unset(internal_vin)
        )
        return res.to_dict() if res else {}

    async def get_geofence_alert(self, vin: str, internal_vin: str | None = None) -> dict[str, Any]:
        res = await get_geofence_alert.asyncio(
            client=self.kintaro_client, vin=vin, internal_vin=_unset(internal_vin)
        )
        return res.to_dict() if res else {}

    async def get_speed_alert(self, vin: str, internal_vin: str | None = None) -> dict[str, Any]:
        res = await get_speed_alert.asyncio(
            client=self.kintaro_client, vin=vin, internal_vin=_unset(internal_vin)
        )
        return res.to_dict() if res else {}
    # ------------------------------------------------------------------
    # Status & Telemetry
    # ------------------------------------------------------------------

    async def get_vsr(self, vin: str, internal_vin: str | None = None) -> dict[str, Any]:
        res = await get_vsr.asyncio(
            client=self.kintaro_client, vin=vin, internal_vin=_unset(internal_vin)
        )
        return res.to_dict() if res else {}

    async def refresh_vsr(
        self,
        vin: str,
        *,
        internal_vin: str | None = None,
        refresh_type: int = 1,
        wait: bool = True,
    ) -> dict[str, Any]:
        res = await refresh_vsr.asyncio(
            client=self.kintaro_client,
            body=RefreshVsrRequest(
                vin=vin,
                internal_vin=_unset(internal_vin),
                refresh_type=refresh_type,
            ),
        )
        return await self._maybe_poll(res, wait=wait)

    async def get_engine_details(
        self, vin: str, internal_vin: str | None = None
    ) -> dict[str, Any]:
        res = await get_engine_details.asyncio(
            client=self.kintaro_client, vin=vin, internal_vin=_unset(internal_vin)
        )
        return res.to_dict() if res else {}
    async def get_available_services(
        self,
        vin: str,
        *,
        internal_vin: str | None = None,
        is_secondary: bool = False,
    ) -> dict[str, Any]:
        res = await get_available_service.asyncio(
            client=self.kintaro_client,
            vin=vin,
            internal_vin=_unset(internal_vin),
            is_secondary_vehicle=(
                GetAvailableServiceIsSecondaryVehicle.TRUE
                if is_secondary
                else GetAvailableServiceIsSecondaryVehicle.FALSE
            ),
        )
        return res.to_dict() if res else {}

    # ------------------------------------------------------------------
    # Remote Commands
    # ------------------------------------------------------------------

    async def get_location(
        self, vin: str, *, pin: str | None = None, internal_vin: str | None = None
    ) -> dict[str, Any]:
        pin_hash = await self.compute_pin_hash(vin, pin, internal_vin) if pin else None
        res = await get_vehicle_location.asyncio(
            client=self.kintaro_client,
            body=PinCommandRequest(
                vin=vin, internal_vin=_unset(internal_vin), pin_hash=_unset(pin_hash)
            ),
        )
        return res.to_dict() if res else {}

    async def lock_door(
        self,
        vin: str,
        *,
        pin: str | None = None,
        internal_vin: str | None = None,
        wait: bool = True,
    ) -> dict[str, Any]:
        pin_hash = await self.compute_pin_hash(vin, pin, internal_vin) if pin else None
        res = await lock_door.asyncio(
            client=self.kintaro_client,
            body=PinCommandRequest(
                vin=vin, internal_vin=_unset(internal_vin), pin_hash=_unset(pin_hash)
            ),
        )
        return await self._maybe_poll(res, wait=wait)

    async def unlock_door(
        self,
        vin: str,
        *,
        pin: str,
        internal_vin: str | None = None,
        wait: bool = True,
    ) -> dict[str, Any]:
        pin_hash = await self.compute_pin_hash(vin, pin, internal_vin)
        res = await unlock_door.asyncio(
            client=self.kintaro_client,
            body=PinCommandRequest(
                vin=vin, internal_vin=_unset(internal_vin), pin_hash=pin_hash
            ),
        )
        return await self._maybe_poll(res, wait=wait)

    async def start_engine(
        self,
        vin: str,
        *,
        pin: str,
        target_temperature: float = 21.0,
        temperature_unit: str = "C",
        hvac_settings: HvacSettings | None = None,
        start_flag: int = 0,
        internal_vin: str | None = None,
        wait: bool = True,
    ) -> dict[str, Any]:
        pin_hash = await self.compute_pin_hash(vin, pin, internal_vin)
        res = await start_engine.asyncio(
            client=self.kintaro_client,
            body=StartEngineRequest(
                vin=vin,
                internal_vin=_unset(internal_vin),
                pin_hash=pin_hash,
                target_temperature=f"{target_temperature:.1f}",
                temperature_unit=temperature_unit.upper(),
                start_flag=start_flag,
                hvac_settings=_unset(hvac_settings),
            ),
        )
        return await self._maybe_poll(res, wait=wait)

    async def stop_engine(
        self,
        vin: str,
        *,
        pin: str | None = None,
        cancel_flag: int = 0,
        internal_vin: str | None = None,
        wait: bool = True,
    ) -> dict[str, Any]:
        pin_hash = await self.compute_pin_hash(vin, pin, internal_vin) if pin else None
        res = await stop_engine.asyncio(
            client=self.kintaro_client,
            body=StopEngineRequest(
                vin=vin,
                internal_vin=_unset(internal_vin),
                pin_hash=_unset(pin_hash),
                cancel_flag=cancel_flag,
            ),
        )
        return await self._maybe_poll(res, wait=wait)

    async def start_horn(
        self,
        vin: str,
        *,
        pin: str | None = None,
        internal_vin: str | None = None,
        wait: bool = True,
    ) -> dict[str, Any]:
        pin_hash = await self.compute_pin_hash(vin, pin, internal_vin) if pin else None
        res = await start_horn.asyncio(
            client=self.kintaro_client,
            body=PinCommandRequest(
                vin=vin, internal_vin=_unset(internal_vin), pin_hash=_unset(pin_hash)
            ),
        )
        return await self._maybe_poll(res, wait=wait)

    async def start_light(
        self,
        vin: str,
        *,
        pin: str | None = None,
        internal_vin: str | None = None,
        wait: bool = True,
    ) -> dict[str, Any]:
        pin_hash = await self.compute_pin_hash(vin, pin, internal_vin) if pin else None
        res = await start_light.asyncio(
            client=self.kintaro_client,
            body=PinCommandRequest(
                vin=vin, internal_vin=_unset(internal_vin), pin_hash=_unset(pin_hash)
            ),
        )
        return await self._maybe_poll(res, wait=wait)
    # ------------------------------------------------------------------
    # PHEV / EV Commands
    # ------------------------------------------------------------------

    async def start_climate(
        self,
        vin: str,
        *,
        pin: str,
        target_temperature: float = 21.0,
        temperature_unit: str = "C",
        hvac_settings: HvacSettings | None = None,
        internal_vin: str | None = None,
        wait: bool = True,
    ) -> dict[str, Any]:
        pin_hash = await self.compute_pin_hash(vin, pin, internal_vin)
        res = await start_climate.asyncio(
            client=self.kintaro_client,
            body=StartEngineRequest(
                vin=vin,
                internal_vin=_unset(internal_vin),
                pin_hash=pin_hash,
                target_temperature=f"{target_temperature:.1f}",
                temperature_unit=temperature_unit.upper(),
                start_flag=0,
                hvac_settings=_unset(hvac_settings),
            ),
        )
        return await self._maybe_poll(res, wait=wait)

    async def stop_climate(
        self,
        vin: str,
        *,
        pin: str | None = None,
        internal_vin: str | None = None,
        wait: bool = True,
    ) -> dict[str, Any]:
        pin_hash = await self.compute_pin_hash(vin, pin, internal_vin) if pin else None
        res = await stop_climate.asyncio(
            client=self.kintaro_client,
            body=StopEngineRequest(
                vin=vin,
                internal_vin=_unset(internal_vin),
                pin_hash=_unset(pin_hash),
                cancel_flag=0,
            ),
        )
        return await self._maybe_poll(res, wait=wait)

    async def start_charge(
        self,
        vin: str,
        *,
        pin: str | None = None,
        internal_vin: str | None = None,
        wait: bool = True,
    ) -> dict[str, Any]:
        pin_hash = await self.compute_pin_hash(vin, pin, internal_vin) if pin else None
        res = await start_charge.asyncio(
            client=self.kintaro_client,
            body=PinCommandRequest(
                vin=vin, internal_vin=_unset(internal_vin), pin_hash=_unset(pin_hash)
            ),
        )
        return await self._maybe_poll(res, wait=wait)

    async def stop_charge(
        self,
        vin: str,
        *,
        pin: str | None = None,
        internal_vin: str | None = None,
        wait: bool = True,
    ) -> dict[str, Any]:
        pin_hash = await self.compute_pin_hash(vin, pin, internal_vin) if pin else None
        res = await stop_charge.asyncio(
            client=self.kintaro_client,
            body=PinCommandRequest(
                vin=vin, internal_vin=_unset(internal_vin), pin_hash=_unset(pin_hash)
            ),
        )
        return await self._maybe_poll(res, wait=wait)

    async def get_charge_details(
        self,
        vin: str,
        *,
        refresh_type: int | None = None,
        internal_vin: str | None = None,
    ) -> dict[str, Any]:
        res = await get_charge_details.asyncio(
            client=self.kintaro_client,
            vin=vin,
            internal_vin=_unset(internal_vin),
            refresh_type=_unset(refresh_type),
        )
        return res.to_dict() if res else {}

    async def get_climate_details(self, vin: str, internal_vin: str | None = None) -> dict[str, Any]:
        res = await get_climate_details.asyncio(
            client=self.kintaro_client, vin=vin, internal_vin=_unset(internal_vin)
        )
        return res.to_dict() if res else {}

    async def get_soc_setting(self, vin: str, internal_vin: str | None = None) -> dict[str, Any]:
        res = await get_soc_setting.asyncio(
            client=self.kintaro_client, vin=vin, internal_vin=_unset(internal_vin)
        )
        return res.to_dict() if res else {}

    async def set_soc_setting(
        self,
        vin: str,
        *,
        charging_limit: str | None = None,
        charging_notification: str | None = None,
        internal_vin: str | None = None,
    ) -> dict[str, Any]:
        res = await set_soc_setting.asyncio(
            client=self.kintaro_client,
            body=SOCSettingEntity(
                vin=vin,
                internal_vin=_unset(internal_vin),
                charging_limit_threshold=_unset(charging_limit),
                charging_notification_threshold=_unset(charging_notification),
            ),
        )
        return res.to_dict() if res else {}

    async def get_charge_schedule(self, vin: str, internal_vin: str | None = None) -> dict[str, Any]:
        res = await get_charge_schedule.asyncio(
            client=self.kintaro_client, vin=vin, internal_vin=_unset(internal_vin)
        )
        return res.to_dict() if res else {}

    async def get_climate_schedule(self, vin: str, internal_vin: str | None = None) -> dict[str, Any]:
        res = await get_climate_schedule.asyncio(
            client=self.kintaro_client, vin=vin, internal_vin=_unset(internal_vin)
        )
        return res.to_dict() if res else {}

    async def get_charge_climate_schedule(
        self, vin: str, internal_vin: str | None = None
    ) -> dict[str, Any]:
        res = await get_charge_climate_schedule.asyncio(
            client=self.kintaro_client, vin=vin, internal_vin=_unset(internal_vin)
        )
        return res.to_dict() if res else {}
