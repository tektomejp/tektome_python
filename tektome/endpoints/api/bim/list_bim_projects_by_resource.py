from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_project_stats_response import BimProjectStatsResponse
from ...models.error_response_out import ErrorResponseOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    resource_id: UUID,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    json_resource_id = str(resource_id)
    params["resource_id"] = json_resource_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/bim/bim-project/by-resource/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponseOut | list[BimProjectStatsResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BimProjectStatsResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponseOut.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorResponseOut.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponseOut.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponseOut.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponseOut | list[BimProjectStatsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    resource_id: UUID,
) -> Response[ErrorResponseOut | list[BimProjectStatsResponse]]:
    """List BIM projects for a resource

     Retrieve paginated BIM projects linked to a specific resource, ordered by most recently updated.Each
    entry includes object, view, and sheet counts.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponseOut | list[BimProjectStatsResponse]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    resource_id: UUID,
) -> ErrorResponseOut | list[BimProjectStatsResponse] | None:
    """List BIM projects for a resource

     Retrieve paginated BIM projects linked to a specific resource, ordered by most recently updated.Each
    entry includes object, view, and sheet counts.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponseOut | list[BimProjectStatsResponse]
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        resource_id=resource_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    resource_id: UUID,
) -> Response[ErrorResponseOut | list[BimProjectStatsResponse]]:
    """List BIM projects for a resource

     Retrieve paginated BIM projects linked to a specific resource, ordered by most recently updated.Each
    entry includes object, view, and sheet counts.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponseOut | list[BimProjectStatsResponse]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    resource_id: UUID,
) -> ErrorResponseOut | list[BimProjectStatsResponse] | None:
    """List BIM projects for a resource

     Retrieve paginated BIM projects linked to a specific resource, ordered by most recently updated.Each
    entry includes object, view, and sheet counts.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponseOut | list[BimProjectStatsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            resource_id=resource_id,
        )
    ).parsed
