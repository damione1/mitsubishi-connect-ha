from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.charge_detail_entity import ChargeDetailEntity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    vin: str,
    internal_vin: str | Unset = UNSET,
    refresh_type: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["vin"] = vin

    params["internalVin"] = internal_vin

    params["refreshType"] = refresh_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/status/getChargeDetails/v1",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> ChargeDetailEntity | None:
    if response.status_code == 200:
        response_200 = ChargeDetailEntity.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[ChargeDetailEntity]:
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
    refresh_type: int | Unset = UNSET,
) -> Response[ChargeDetailEntity]:
    """Get battery and charging status (PHEV/EV only)

     PHEV/EV only.

    Args:
        vin (str):  Example: JA4XXXXXXXXXXXXXX.
        internal_vin (str | Unset):
        refresh_type (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChargeDetailEntity]
    """

    kwargs = _get_kwargs(
        vin=vin,
        internal_vin=internal_vin,
        refresh_type=refresh_type,
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
    refresh_type: int | Unset = UNSET,
) -> ChargeDetailEntity | None:
    """Get battery and charging status (PHEV/EV only)

     PHEV/EV only.

    Args:
        vin (str):  Example: JA4XXXXXXXXXXXXXX.
        internal_vin (str | Unset):
        refresh_type (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChargeDetailEntity
    """

    return sync_detailed(
        client=client,
        vin=vin,
        internal_vin=internal_vin,
        refresh_type=refresh_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    vin: str,
    internal_vin: str | Unset = UNSET,
    refresh_type: int | Unset = UNSET,
) -> Response[ChargeDetailEntity]:
    """Get battery and charging status (PHEV/EV only)

     PHEV/EV only.

    Args:
        vin (str):  Example: JA4XXXXXXXXXXXXXX.
        internal_vin (str | Unset):
        refresh_type (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChargeDetailEntity]
    """

    kwargs = _get_kwargs(
        vin=vin,
        internal_vin=internal_vin,
        refresh_type=refresh_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    vin: str,
    internal_vin: str | Unset = UNSET,
    refresh_type: int | Unset = UNSET,
) -> ChargeDetailEntity | None:
    """Get battery and charging status (PHEV/EV only)

     PHEV/EV only.

    Args:
        vin (str):  Example: JA4XXXXXXXXXXXXXX.
        internal_vin (str | Unset):
        refresh_type (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChargeDetailEntity
    """

    return (
        await asyncio_detailed(
            client=client,
            vin=vin,
            internal_vin=internal_vin,
            refresh_type=refresh_type,
        )
    ).parsed
