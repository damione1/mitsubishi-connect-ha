from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.available_services_response import AvailableServicesResponse
from ...models.get_available_service_is_secondary_vehicle import GetAvailableServiceIsSecondaryVehicle
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    vin: str,
    internal_vin: str | Unset = UNSET,
    is_secondary_vehicle: GetAvailableServiceIsSecondaryVehicle | Unset = GetAvailableServiceIsSecondaryVehicle.FALSE,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["vin"] = vin

    params["internalVin"] = internal_vin

    json_is_secondary_vehicle: str | Unset = UNSET
    if not isinstance(is_secondary_vehicle, Unset):
        json_is_secondary_vehicle = is_secondary_vehicle.value

    params["isSecondaryVehicle"] = json_is_secondary_vehicle

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/remote/getAvailableService/v1",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AvailableServicesResponse | None:
    if response.status_code == 200:
        response_200 = AvailableServicesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[AvailableServicesResponse]:
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
    is_secondary_vehicle: GetAvailableServiceIsSecondaryVehicle | Unset = GetAvailableServiceIsSecondaryVehicle.FALSE,
) -> Response[AvailableServicesResponse]:
    """List active remote services for the vehicle subscription

    Args:
        vin (str):  Example: JA4XXXXXXXXXXXXXX.
        internal_vin (str | Unset):
        is_secondary_vehicle (GetAvailableServiceIsSecondaryVehicle | Unset):  Default:
            GetAvailableServiceIsSecondaryVehicle.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableServicesResponse]
    """

    kwargs = _get_kwargs(
        vin=vin,
        internal_vin=internal_vin,
        is_secondary_vehicle=is_secondary_vehicle,
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
    is_secondary_vehicle: GetAvailableServiceIsSecondaryVehicle | Unset = GetAvailableServiceIsSecondaryVehicle.FALSE,
) -> AvailableServicesResponse | None:
    """List active remote services for the vehicle subscription

    Args:
        vin (str):  Example: JA4XXXXXXXXXXXXXX.
        internal_vin (str | Unset):
        is_secondary_vehicle (GetAvailableServiceIsSecondaryVehicle | Unset):  Default:
            GetAvailableServiceIsSecondaryVehicle.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailableServicesResponse
    """

    return sync_detailed(
        client=client,
        vin=vin,
        internal_vin=internal_vin,
        is_secondary_vehicle=is_secondary_vehicle,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    vin: str,
    internal_vin: str | Unset = UNSET,
    is_secondary_vehicle: GetAvailableServiceIsSecondaryVehicle | Unset = GetAvailableServiceIsSecondaryVehicle.FALSE,
) -> Response[AvailableServicesResponse]:
    """List active remote services for the vehicle subscription

    Args:
        vin (str):  Example: JA4XXXXXXXXXXXXXX.
        internal_vin (str | Unset):
        is_secondary_vehicle (GetAvailableServiceIsSecondaryVehicle | Unset):  Default:
            GetAvailableServiceIsSecondaryVehicle.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableServicesResponse]
    """

    kwargs = _get_kwargs(
        vin=vin,
        internal_vin=internal_vin,
        is_secondary_vehicle=is_secondary_vehicle,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    vin: str,
    internal_vin: str | Unset = UNSET,
    is_secondary_vehicle: GetAvailableServiceIsSecondaryVehicle | Unset = GetAvailableServiceIsSecondaryVehicle.FALSE,
) -> AvailableServicesResponse | None:
    """List active remote services for the vehicle subscription

    Args:
        vin (str):  Example: JA4XXXXXXXXXXXXXX.
        internal_vin (str | Unset):
        is_secondary_vehicle (GetAvailableServiceIsSecondaryVehicle | Unset):  Default:
            GetAvailableServiceIsSecondaryVehicle.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailableServicesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            vin=vin,
            internal_vin=internal_vin,
            is_secondary_vehicle=is_secondary_vehicle,
        )
    ).parsed
