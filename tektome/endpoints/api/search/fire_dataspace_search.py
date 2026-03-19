from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataspace_search_request_schema import DataspaceSearchRequestSchema
from ...models.dataspace_search_result_out import DataspaceSearchResultOut
from ...models.error_out import ErrorOut
from ...models.fire_dataspace_search_target_entity import FireDataspaceSearchTargetEntity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataspace_id: UUID,
    *,
    body: DataspaceSearchRequestSchema,
    target_entity: FireDataspaceSearchTargetEntity | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 30,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_target_entity: dict[str, Any] | Unset = UNSET
    if not isinstance(target_entity, Unset):
        json_target_entity = target_entity.to_dict()
    if not isinstance(json_target_entity, Unset):
        params.update(json_target_entity)

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/search/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DataspaceSearchResultOut | ErrorOut | None:
    if response.status_code == 200:
        response_200 = DataspaceSearchResultOut.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorOut.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DataspaceSearchResultOut | ErrorOut]:
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
    target_entity: FireDataspaceSearchTargetEntity | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 30,
) -> Response[DataspaceSearchResultOut | ErrorOut]:
    """Post Fire Search

     sR8Kj2Lm

    Fire a new search request.

    Creates a new search request, executes the search with caching,
    and returns paginated results along with the search request info.

    Only keeps the latest 8 (configurable) unsaved requests per user.

    Args:
        dataspace_id (UUID):
        target_entity (FireDataspaceSearchTargetEntity | Unset): Target entity type to search
            (project or resource)
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Page size for pagination Default: 30.
        body (DataspaceSearchRequestSchema): Base schema for search request fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceSearchResultOut | ErrorOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        body=body,
        target_entity=target_entity,
        page=page,
        page_size=page_size,
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
    target_entity: FireDataspaceSearchTargetEntity | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 30,
) -> DataspaceSearchResultOut | ErrorOut | None:
    """Post Fire Search

     sR8Kj2Lm

    Fire a new search request.

    Creates a new search request, executes the search with caching,
    and returns paginated results along with the search request info.

    Only keeps the latest 8 (configurable) unsaved requests per user.

    Args:
        dataspace_id (UUID):
        target_entity (FireDataspaceSearchTargetEntity | Unset): Target entity type to search
            (project or resource)
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Page size for pagination Default: 30.
        body (DataspaceSearchRequestSchema): Base schema for search request fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceSearchResultOut | ErrorOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        client=client,
        body=body,
        target_entity=target_entity,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchRequestSchema,
    target_entity: FireDataspaceSearchTargetEntity | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 30,
) -> Response[DataspaceSearchResultOut | ErrorOut]:
    """Post Fire Search

     sR8Kj2Lm

    Fire a new search request.

    Creates a new search request, executes the search with caching,
    and returns paginated results along with the search request info.

    Only keeps the latest 8 (configurable) unsaved requests per user.

    Args:
        dataspace_id (UUID):
        target_entity (FireDataspaceSearchTargetEntity | Unset): Target entity type to search
            (project or resource)
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Page size for pagination Default: 30.
        body (DataspaceSearchRequestSchema): Base schema for search request fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceSearchResultOut | ErrorOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        body=body,
        target_entity=target_entity,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchRequestSchema,
    target_entity: FireDataspaceSearchTargetEntity | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 30,
) -> DataspaceSearchResultOut | ErrorOut | None:
    """Post Fire Search

     sR8Kj2Lm

    Fire a new search request.

    Creates a new search request, executes the search with caching,
    and returns paginated results along with the search request info.

    Only keeps the latest 8 (configurable) unsaved requests per user.

    Args:
        dataspace_id (UUID):
        target_entity (FireDataspaceSearchTargetEntity | Unset): Target entity type to search
            (project or resource)
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Page size for pagination Default: 30.
        body (DataspaceSearchRequestSchema): Base schema for search request fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceSearchResultOut | ErrorOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            client=client,
            body=body,
            target_entity=target_entity,
            page=page,
            page_size=page_size,
        )
    ).parsed
