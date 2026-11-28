from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.idm_login_request import IdmLoginRequest
from ...models.idm_tokens_response import IdmTokensResponse
from ...types import Response


def _get_kwargs(
    *,
    body: IdmLoginRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/login",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> IdmTokensResponse | None:
    if response.status_code == 200:
        response_200 = IdmTokensResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[IdmTokensResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IdmLoginRequest,
) -> Response[IdmTokensResponse]:
    """User login (email + RSA-encrypted password)

     IDM server endpoint. Format `password` as `<keyIndex>@<base64(RSA_PKCS1v15(password))>`.
    Omit `app-device-token` on this endpoint.


    Success is `code == "200"`; `code == "401"` means the access token is invalid (refresh it).

    Args:
        body (IdmLoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdmTokensResponse]
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
    body: IdmLoginRequest,
) -> IdmTokensResponse | None:
    """User login (email + RSA-encrypted password)

     IDM server endpoint. Format `password` as `<keyIndex>@<base64(RSA_PKCS1v15(password))>`.
    Omit `app-device-token` on this endpoint.


    Success is `code == "200"`; `code == "401"` means the access token is invalid (refresh it).

    Args:
        body (IdmLoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdmTokensResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IdmLoginRequest,
) -> Response[IdmTokensResponse]:
    """User login (email + RSA-encrypted password)

     IDM server endpoint. Format `password` as `<keyIndex>@<base64(RSA_PKCS1v15(password))>`.
    Omit `app-device-token` on this endpoint.


    Success is `code == "200"`; `code == "401"` means the access token is invalid (refresh it).

    Args:
        body (IdmLoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdmTokensResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: IdmLoginRequest,
) -> IdmTokensResponse | None:
    """User login (email + RSA-encrypted password)

     IDM server endpoint. Format `password` as `<keyIndex>@<base64(RSA_PKCS1v15(password))>`.
    Omit `app-device-token` on this endpoint.


    Success is `code == "200"`; `code == "401"` means the access token is invalid (refresh it).

    Args:
        body (IdmLoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdmTokensResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
