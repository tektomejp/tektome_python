from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity_search_request_schema_patch_in import EntitySearchRequestSchemaPatchIn
from ...models.entity_search_request_schema_patch_out import EntitySearchRequestSchemaPatchOut
from ...types import Response


def _get_kwargs(
    request_id: UUID,
    *,
    body: EntitySearchRequestSchemaPatchIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/search/entities/requests/{request_id}/".format(
            request_id=quote(str(request_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EntitySearchRequestSchemaPatchOut | None:
    if response.status_code == 201:
        response_201 = EntitySearchRequestSchemaPatchOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EntitySearchRequestSchemaPatchOut]:
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
    body: EntitySearchRequestSchemaPatchIn,
) -> Response[EntitySearchRequestSchemaPatchOut]:
    """Update Request

     Medykvlc

    Update the given entity search request.

    Args:
        request_id (UUID):
        body (EntitySearchRequestSchemaPatchIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntitySearchRequestSchemaPatchOut]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: EntitySearchRequestSchemaPatchIn,
) -> EntitySearchRequestSchemaPatchOut | None:
    """Update Request

     Medykvlc

    Update the given entity search request.

    Args:
        request_id (UUID):
        body (EntitySearchRequestSchemaPatchIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntitySearchRequestSchemaPatchOut
    """

    return sync_detailed(
        request_id=request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: EntitySearchRequestSchemaPatchIn,
) -> Response[EntitySearchRequestSchemaPatchOut]:
    """Update Request

     Medykvlc

    Update the given entity search request.

    Args:
        request_id (UUID):
        body (EntitySearchRequestSchemaPatchIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntitySearchRequestSchemaPatchOut]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: EntitySearchRequestSchemaPatchIn,
) -> EntitySearchRequestSchemaPatchOut | None:
    """Update Request

     Medykvlc

    Update the given entity search request.

    Args:
        request_id (UUID):
        body (EntitySearchRequestSchemaPatchIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntitySearchRequestSchemaPatchOut
    """

    return (
        await asyncio_detailed(
            request_id=request_id,
            client=client,
            body=body,
        )
    ).parsed
