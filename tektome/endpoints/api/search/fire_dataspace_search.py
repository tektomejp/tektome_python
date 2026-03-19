from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataspace_search_request_schema import DataspaceSearchRequestSchema
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    *,
    body: DataspaceSearchRequestSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/search/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | None:
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchRequestSchema,
) -> Response[ErrorResponse]:
    """Execute a new search

     Execute a new search request within a dataspace and return paginated results. Only the most recent
    unsaved requests per user are retained.

    Args:
        dataspace_id (UUID):
        body (DataspaceSearchRequestSchema): Base schema for search request fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchRequestSchema,
) -> ErrorResponse | None:
    """Execute a new search

     Execute a new search request within a dataspace and return paginated results. Only the most recent
    unsaved requests per user are retained.

    Args:
        dataspace_id (UUID):
        body (DataspaceSearchRequestSchema): Base schema for search request fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchRequestSchema,
) -> Response[ErrorResponse]:
    """Execute a new search

     Execute a new search request within a dataspace and return paginated results. Only the most recent
    unsaved requests per user are retained.

    Args:
        dataspace_id (UUID):
        body (DataspaceSearchRequestSchema): Base schema for search request fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchRequestSchema,
) -> ErrorResponse | None:
    """Execute a new search

     Execute a new search request within a dataspace and return paginated results. Only the most recent
    unsaved requests per user are retained.

    Args:
        dataspace_id (UUID):
        body (DataspaceSearchRequestSchema): Base schema for search request fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            client=client,
            body=body,
        )
    ).parsed
