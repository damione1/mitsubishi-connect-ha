from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.idm_init_request import IdmInitRequest
from ...models.idm_init_response import IdmInitResponse
from ...types import Response


def _get_kwargs(
    *,
    body: IdmInitRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/init",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> IdmInitResponse | None:
    if response.status_code == 200:
        response_200 = IdmInitResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[IdmInitResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IdmInitRequest,
) -> Response[IdmInitResponse]:
    """Initialize IDM session and fetch RSA public key

     IDM server endpoint. Requires `app-device-token` header (HS256 JWT).
    Returns `keyIndex` and `publicKey` (Base64 DER X.509 RSA public key)
    used to encrypt the password for `/api/v1/login`.


    Success is `code == "200"`; `code == "401"` means the access token is invalid (refresh it).

    Args:
        body (IdmInitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdmInitResponse]
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
    body: IdmInitRequest,
) -> IdmInitResponse | None:
    """Initialize IDM session and fetch RSA public key

     IDM server endpoint. Requires `app-device-token` header (HS256 JWT).
    Returns `keyIndex` and `publicKey` (Base64 DER X.509 RSA public key)
    used to encrypt the password for `/api/v1/login`.


    Success is `code == "200"`; `code == "401"` means the access token is invalid (refresh it).

    Args:
        body (IdmInitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdmInitResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IdmInitRequest,
) -> Response[IdmInitResponse]:
    """Initialize IDM session and fetch RSA public key

     IDM server endpoint. Requires `app-device-token` header (HS256 JWT).
    Returns `keyIndex` and `publicKey` (Base64 DER X.509 RSA public key)
    used to encrypt the password for `/api/v1/login`.


    Success is `code == "200"`; `code == "401"` means the access token is invalid (refresh it).

    Args:
        body (IdmInitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdmInitResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: IdmInitRequest,
) -> IdmInitResponse | None:
    """Initialize IDM session and fetch RSA public key

     IDM server endpoint. Requires `app-device-token` header (HS256 JWT).
    Returns `keyIndex` and `publicKey` (Base64 DER X.509 RSA public key)
    used to encrypt the password for `/api/v1/login`.


    Success is `code == "200"`; `code == "401"` means the access token is invalid (refresh it).

    Args:
        body (IdmInitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdmInitResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
