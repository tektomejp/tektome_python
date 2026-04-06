from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_key_response import GetAPIKeyResponse
from ...models.patch_api_key_request import PatchAPIKeyRequest
from ...types import Response


def _get_kwargs(
    api_key_id: UUID,
    *,
    body: PatchAPIKeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/account/access/api-keys/{api_key_id}/".format(
            api_key_id=quote(str(api_key_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAPIKeyResponse | None:
    if response.status_code == 200:
        response_200 = GetAPIKeyResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAPIKeyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    api_key_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchAPIKeyRequest,
) -> Response[GetAPIKeyResponse]:
    """Update an API key

     Update the name or expiration date of an existing API key owned by the authenticated user. Expired
    keys cannot be edited.

    Args:
        api_key_id (UUID):
        body (PatchAPIKeyRequest): Schema for updating an existing API key.
            Supports partial updates — only provided fields are applied.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAPIKeyResponse]
    """

    kwargs = _get_kwargs(
        api_key_id=api_key_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    api_key_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchAPIKeyRequest,
) -> GetAPIKeyResponse | None:
    """Update an API key

     Update the name or expiration date of an existing API key owned by the authenticated user. Expired
    keys cannot be edited.

    Args:
        api_key_id (UUID):
        body (PatchAPIKeyRequest): Schema for updating an existing API key.
            Supports partial updates — only provided fields are applied.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAPIKeyResponse
    """

    return sync_detailed(
        api_key_id=api_key_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    api_key_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchAPIKeyRequest,
) -> Response[GetAPIKeyResponse]:
    """Update an API key

     Update the name or expiration date of an existing API key owned by the authenticated user. Expired
    keys cannot be edited.

    Args:
        api_key_id (UUID):
        body (PatchAPIKeyRequest): Schema for updating an existing API key.
            Supports partial updates — only provided fields are applied.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAPIKeyResponse]
    """

    kwargs = _get_kwargs(
        api_key_id=api_key_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    api_key_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchAPIKeyRequest,
) -> GetAPIKeyResponse | None:
    """Update an API key

     Update the name or expiration date of an existing API key owned by the authenticated user. Expired
    keys cannot be edited.

    Args:
        api_key_id (UUID):
        body (PatchAPIKeyRequest): Schema for updating an existing API key.
            Supports partial updates — only provided fields are applied.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAPIKeyResponse
    """

    return (
        await asyncio_detailed(
            api_key_id=api_key_id,
            client=client,
            body=body,
        )
    ).parsed
