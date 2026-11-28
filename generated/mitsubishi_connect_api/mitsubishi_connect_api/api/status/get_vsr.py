from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.vsr_payload import VsrPayload
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    vin: str,
    internal_vin: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["vin"] = vin

    params["internalVin"] = internal_vin

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/status/getVSR/v1",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> VsrPayload | None:
    if response.status_code == 200:
        response_200 = VsrPayload.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[VsrPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    vin: str,
    internal_vin: str | Unset = UNSET,
) -> Response[VsrPayload]:
    """Get latest cached Vehicle Status Report (VSR)

     Returns the latest server-cached snapshot (~1-2 s, does not wake the vehicle):
    odometer, fuel range, individual door/hood/trunk states, headlights,
    brake/oil/TPMS warnings, and ignition status.

    Args:
        vin (str):  Example: JA4XXXXXXXXXXXXXX.
        internal_vin (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VsrPayload]
    """

    kwargs = _get_kwargs(
        vin=vin,
        internal_vin=internal_vin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    vin: str,
    internal_vin: str | Unset = UNSET,
) -> VsrPayload | None:
    """Get latest cached Vehicle Status Report (VSR)

     Returns the latest server-cached snapshot (~1-2 s, does not wake the vehicle):
    odometer, fuel range, individual door/hood/trunk states, headlights,
    brake/oil/TPMS warnings, and ignition status.

    Args:
        vin (str):  Example: JA4XXXXXXXXXXXXXX.
        internal_vin (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VsrPayload
    """

    return sync_detailed(
        client=client,
        vin=vin,
        internal_vin=internal_vin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    vin: str,
    internal_vin: str | Unset = UNSET,
) -> Response[VsrPayload]:
    """Get latest cached Vehicle Status Report (VSR)

     Returns the latest server-cached snapshot (~1-2 s, does not wake the vehicle):
    odometer, fuel range, individual door/hood/trunk states, headlights,
    brake/oil/TPMS warnings, and ignition status.

    Args:
        vin (str):  Example: JA4XXXXXXXXXXXXXX.
        internal_vin (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VsrPayload]
    """

    kwargs = _get_kwargs(
        vin=vin,
        internal_vin=internal_vin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    vin: str,
    internal_vin: str | Unset = UNSET,
) -> VsrPayload | None:
    """Get latest cached Vehicle Status Report (VSR)

     Returns the latest server-cached snapshot (~1-2 s, does not wake the vehicle):
    odometer, fuel range, individual door/hood/trunk states, headlights,
    brake/oil/TPMS warnings, and ignition status.

    Args:
        vin (str):  Example: JA4XXXXXXXXXXXXXX.
        internal_vin (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VsrPayload
    """

    return (
        await asyncio_detailed(
            client=client,
            vin=vin,
            internal_vin=internal_vin,
        )
    ).parsed
