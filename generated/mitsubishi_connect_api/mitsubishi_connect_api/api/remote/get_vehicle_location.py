from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pin_command_request import PinCommandRequest
from ...models.vehicle_location_response import VehicleLocationResponse
from ...types import Response


def _get_kwargs(
    *,
    body: PinCommandRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/remote/getVehicleLocation/v1",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> VehicleLocationResponse | None:
    if response.status_code == 200:
        response_200 = VehicleLocationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[VehicleLocationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PinCommandRequest,
) -> Response[VehicleLocationResponse]:
    """Get vehicle GPS coordinates (Find My Car)

     Requires an active connected-services subscription; check `getAvailableService`.

    Known error codes: `600006`, `600007`, `956000` (see `ErrorCode`).

    Args:
        body (PinCommandRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VehicleLocationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PinCommandRequest,
) -> VehicleLocationResponse | None:
    """Get vehicle GPS coordinates (Find My Car)

     Requires an active connected-services subscription; check `getAvailableService`.

    Known error codes: `600006`, `600007`, `956000` (see `ErrorCode`).

    Args:
        body (PinCommandRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VehicleLocationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PinCommandRequest,
) -> Response[VehicleLocationResponse]:
    """Get vehicle GPS coordinates (Find My Car)

     Requires an active connected-services subscription; check `getAvailableService`.

    Known error codes: `600006`, `600007`, `956000` (see `ErrorCode`).

    Args:
        body (PinCommandRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VehicleLocationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PinCommandRequest,
) -> VehicleLocationResponse | None:
    """Get vehicle GPS coordinates (Find My Car)

     Requires an active connected-services subscription; check `getAvailableService`.

    Known error codes: `600006`, `600007`, `956000` (see `ErrorCode`).

    Args:
        body (PinCommandRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VehicleLocationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
