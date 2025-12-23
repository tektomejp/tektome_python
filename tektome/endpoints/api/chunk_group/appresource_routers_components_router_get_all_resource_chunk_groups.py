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
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/resources/{resource_id}/chunk-groups/".format(
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ChunkGroupComponentSchemaGetOut] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChunkGroupComponentSchemaGetOut.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ChunkGroupComponentSchemaGetOut]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[list[ChunkGroupComponentSchemaGetOut]]:
    """Get All Resource Chunk Groups

     hcWBxv70

    Retrieve all chunk groups of a resource.

    Args:
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ChunkGroupComponentSchemaGetOut]]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> list[ChunkGroupComponentSchemaGetOut] | None:
    """Get All Resource Chunk Groups

     hcWBxv70

    Retrieve all chunk groups of a resource.

    Args:
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ChunkGroupComponentSchemaGetOut]
    """

    return sync_detailed(
        resource_id=resource_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[list[ChunkGroupComponentSchemaGetOut]]:
    """Get All Resource Chunk Groups

     hcWBxv70

    Retrieve all chunk groups of a resource.

    Args:
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ChunkGroupComponentSchemaGetOut]]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> list[ChunkGroupComponentSchemaGetOut] | None:
    """Get All Resource Chunk Groups

     hcWBxv70

    Retrieve all chunk groups of a resource.

    Args:
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ChunkGroupComponentSchemaGetOut]
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            client=client,
        )
    ).parsed
