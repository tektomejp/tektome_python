from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity_search_request_schema_get_out import EntitySearchRequestSchemaGetOut
from ...types import Response


def _get_kwargs(
    request_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/search/entities/requests/{request_id}/".format(
            request_id=quote(str(request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EntitySearchRequestSchemaGetOut | None:
    if response.status_code == 200:
        response_200 = EntitySearchRequestSchemaGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EntitySearchRequestSchemaGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    request_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[EntitySearchRequestSchemaGetOut]:
    """Get Request

     2g7H8f9J

    Retrieve a specific search request by its ID.

    Args:
        request_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntitySearchRequestSchemaGetOut]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    request_id: UUID,
    *,
    client: AuthenticatedClient,
) -> EntitySearchRequestSchemaGetOut | None:
    """Get Request

     2g7H8f9J

    Retrieve a specific search request by its ID.

    Args:
        request_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntitySearchRequestSchemaGetOut
    """

    return sync_detailed(
        request_id=request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    request_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[EntitySearchRequestSchemaGetOut]:
    """Get Request

     2g7H8f9J

    Retrieve a specific search request by its ID.

    Args:
        request_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntitySearchRequestSchemaGetOut]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    request_id: UUID,
    *,
    client: AuthenticatedClient,
) -> EntitySearchRequestSchemaGetOut | None:
    """Get Request

     2g7H8f9J

    Retrieve a specific search request by its ID.

    Args:
        request_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntitySearchRequestSchemaGetOut
    """

    return (
        await asyncio_detailed(
            request_id=request_id,
            client=client,
        )
    ).parsed
