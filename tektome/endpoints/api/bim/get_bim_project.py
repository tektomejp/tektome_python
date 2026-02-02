from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_project_stats_get_out import BimProjectStatsGetOut
from ...types import UNSET, Response


def _get_kwargs(
    *,
    resource_id: UUID,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_resource_id = str(resource_id)
    params["resource_id"] = json_resource_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/bim/bim-project/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BimProjectStatsGetOut | None:
    if response.status_code == 200:
        response_200 = BimProjectStatsGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimProjectStatsGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    resource_id: UUID,
) -> Response[BimProjectStatsGetOut]:
    """Get Bim Project

     5PPx6mXb

    Get the latest BIM project data using a resource ID
    Returns: BIM project ID and BIM statistics (number of BIM objects, views, sheets)

    Args:
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimProjectStatsGetOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    resource_id: UUID,
) -> BimProjectStatsGetOut | None:
    """Get Bim Project

     5PPx6mXb

    Get the latest BIM project data using a resource ID
    Returns: BIM project ID and BIM statistics (number of BIM objects, views, sheets)

    Args:
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimProjectStatsGetOut
    """

    return sync_detailed(
        client=client,
        resource_id=resource_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    resource_id: UUID,
) -> Response[BimProjectStatsGetOut]:
    """Get Bim Project

     5PPx6mXb

    Get the latest BIM project data using a resource ID
    Returns: BIM project ID and BIM statistics (number of BIM objects, views, sheets)

    Args:
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimProjectStatsGetOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    resource_id: UUID,
) -> BimProjectStatsGetOut | None:
    """Get Bim Project

     5PPx6mXb

    Get the latest BIM project data using a resource ID
    Returns: BIM project ID and BIM statistics (number of BIM objects, views, sheets)

    Args:
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimProjectStatsGetOut
    """

    return (
        await asyncio_detailed(
            client=client,
            resource_id=resource_id,
        )
    ).parsed
