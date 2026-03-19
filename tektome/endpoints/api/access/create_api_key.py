from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_api_key_request import CreateAPIKeyRequest
from ...models.create_api_key_response import CreateAPIKeyResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateAPIKeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/account/access/api-keys/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateAPIKeyResponse | None:
    if response.status_code == 201:
        response_201 = CreateAPIKeyResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateAPIKeyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateAPIKeyRequest,
) -> Response[CreateAPIKeyResponse]:
    """Create an API key

     Create a new API key for the authenticated user. API keys can be used in the Authorization header as
    'Bearer sk-xxxx' to authenticate requests. Keys can be valid for up to one year. A maximum of 100
    keys per user is enforced.

    Args:
        body (CreateAPIKeyRequest): Schema for creating a new API key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAPIKeyResponse]
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
    client: AuthenticatedClient,
    body: CreateAPIKeyRequest,
) -> CreateAPIKeyResponse | None:
    """Create an API key

     Create a new API key for the authenticated user. API keys can be used in the Authorization header as
    'Bearer sk-xxxx' to authenticate requests. Keys can be valid for up to one year. A maximum of 100
    keys per user is enforced.

    Args:
        body (CreateAPIKeyRequest): Schema for creating a new API key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAPIKeyResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateAPIKeyRequest,
) -> Response[CreateAPIKeyResponse]:
    """Create an API key

     Create a new API key for the authenticated user. API keys can be used in the Authorization header as
    'Bearer sk-xxxx' to authenticate requests. Keys can be valid for up to one year. A maximum of 100
    keys per user is enforced.

    Args:
        body (CreateAPIKeyRequest): Schema for creating a new API key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAPIKeyResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateAPIKeyRequest,
) -> CreateAPIKeyResponse | None:
    """Create an API key

     Create a new API key for the authenticated user. API keys can be used in the Authorization header as
    'Bearer sk-xxxx' to authenticate requests. Keys can be valid for up to one year. A maximum of 100
    keys per user is enforced.

    Args:
        body (CreateAPIKeyRequest): Schema for creating a new API key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAPIKeyResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
