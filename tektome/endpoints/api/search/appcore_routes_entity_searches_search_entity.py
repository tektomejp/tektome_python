from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appcore_routes_entity_searches_search_entity_response import (
    AppcoreRoutesEntitySearchesSearchEntityResponse,
)
from ...models.entity_search_request_schema_post_in import EntitySearchRequestSchemaPostIn
from ...models.entity_search_result import EntitySearchResult
from ...types import Response


def _get_kwargs(
    *,
    body: EntitySearchRequestSchemaPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/search/entities/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppcoreRoutesEntitySearchesSearchEntityResponse | EntitySearchResult | None:
    if response.status_code == 200:
        response_200 = EntitySearchResult.from_dict(response.json())

        return response_200

    if response.status_code == 416:
        response_416 = AppcoreRoutesEntitySearchesSearchEntityResponse.from_dict(response.json())

        return response_416

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppcoreRoutesEntitySearchesSearchEntityResponse | EntitySearchResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EntitySearchRequestSchemaPostIn,
) -> Response[AppcoreRoutesEntitySearchesSearchEntityResponse | EntitySearchResult]:
    """Search Entity

     Z3qNgwYf

    Search for entities based on the provided conditions

    Args:
        body (EntitySearchRequestSchemaPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppcoreRoutesEntitySearchesSearchEntityResponse | EntitySearchResult]
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
    body: EntitySearchRequestSchemaPostIn,
) -> AppcoreRoutesEntitySearchesSearchEntityResponse | EntitySearchResult | None:
    """Search Entity

     Z3qNgwYf

    Search for entities based on the provided conditions

    Args:
        body (EntitySearchRequestSchemaPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppcoreRoutesEntitySearchesSearchEntityResponse | EntitySearchResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EntitySearchRequestSchemaPostIn,
) -> Response[AppcoreRoutesEntitySearchesSearchEntityResponse | EntitySearchResult]:
    """Search Entity

     Z3qNgwYf

    Search for entities based on the provided conditions

    Args:
        body (EntitySearchRequestSchemaPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppcoreRoutesEntitySearchesSearchEntityResponse | EntitySearchResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EntitySearchRequestSchemaPostIn,
) -> AppcoreRoutesEntitySearchesSearchEntityResponse | EntitySearchResult | None:
    """Search Entity

     Z3qNgwYf

    Search for entities based on the provided conditions

    Args:
        body (EntitySearchRequestSchemaPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppcoreRoutesEntitySearchesSearchEntityResponse | EntitySearchResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
