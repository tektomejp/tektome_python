from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chunk_group_component_schema_get_out import ChunkGroupComponentSchemaGetOut
from ...types import Response


def _get_kwargs(
    resource_id: UUID,
    chunk_group_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/resources/{resource_id}/chunk-groups/{chunk_group_id}/".format(
            resource_id=quote(str(resource_id), safe=""),
            chunk_group_id=quote(str(chunk_group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChunkGroupComponentSchemaGetOut | None:
    if response.status_code == 200:
        response_200 = ChunkGroupComponentSchemaGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ChunkGroupComponentSchemaGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_id: UUID,
    chunk_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ChunkGroupComponentSchemaGetOut]:
    """Get Resource Chunk Group

     NMm0DmZE

    Retrieve a specific chunk group of a resource.

    Args:
        resource_id (UUID):
        chunk_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChunkGroupComponentSchemaGetOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        chunk_group_id=chunk_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_id: UUID,
    chunk_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ChunkGroupComponentSchemaGetOut | None:
    """Get Resource Chunk Group

     NMm0DmZE

    Retrieve a specific chunk group of a resource.

    Args:
        resource_id (UUID):
        chunk_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChunkGroupComponentSchemaGetOut
    """

    return sync_detailed(
        resource_id=resource_id,
        chunk_group_id=chunk_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_id: UUID,
    chunk_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ChunkGroupComponentSchemaGetOut]:
    """Get Resource Chunk Group

     NMm0DmZE

    Retrieve a specific chunk group of a resource.

    Args:
        resource_id (UUID):
        chunk_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChunkGroupComponentSchemaGetOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        chunk_group_id=chunk_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_id: UUID,
    chunk_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ChunkGroupComponentSchemaGetOut | None:
    """Get Resource Chunk Group

     NMm0DmZE

    Retrieve a specific chunk group of a resource.

    Args:
        resource_id (UUID):
        chunk_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChunkGroupComponentSchemaGetOut
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            chunk_group_id=chunk_group_id,
            client=client,
        )
    ).parsed
