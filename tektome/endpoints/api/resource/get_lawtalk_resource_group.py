from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lawtalk_resource_group_schema import LawtalkResourceGroupSchema
from ...types import Response


def _get_kwargs(
    resource_group_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/resources/groups/{resource_group_id}/".format(
            resource_group_id=quote(str(resource_group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LawtalkResourceGroupSchema | None:
    if response.status_code == 200:
        response_200 = LawtalkResourceGroupSchema.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LawtalkResourceGroupSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[LawtalkResourceGroupSchema]:
    """Get resource group details

     Retrieve detailed information about a specific resource group by its ID.

    Args:
        resource_group_id (UUID): Resource group ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LawtalkResourceGroupSchema]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> LawtalkResourceGroupSchema | None:
    """Get resource group details

     Retrieve detailed information about a specific resource group by its ID.

    Args:
        resource_group_id (UUID): Resource group ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LawtalkResourceGroupSchema
    """

    return sync_detailed(
        resource_group_id=resource_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[LawtalkResourceGroupSchema]:
    """Get resource group details

     Retrieve detailed information about a specific resource group by its ID.

    Args:
        resource_group_id (UUID): Resource group ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LawtalkResourceGroupSchema]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> LawtalkResourceGroupSchema | None:
    """Get resource group details

     Retrieve detailed information about a specific resource group by its ID.

    Args:
        resource_group_id (UUID): Resource group ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LawtalkResourceGroupSchema
    """

    return (
        await asyncio_detailed(
            resource_group_id=resource_group_id,
            client=client,
        )
    ).parsed
