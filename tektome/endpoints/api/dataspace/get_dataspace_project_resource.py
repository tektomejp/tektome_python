from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataspace_project_resources_response import DataspaceProjectResourcesResponse
from ...types import Response


def _get_kwargs(
    resource_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/dataspaces/projects/resources/{resource_id}/".format(
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DataspaceProjectResourcesResponse | None:
    if response.status_code == 200:
        response_200 = DataspaceProjectResourcesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DataspaceProjectResourcesResponse]:
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
) -> Response[DataspaceProjectResourcesResponse]:
    """Get a dataspace project resource by ID

     Retrieve detailed information about a specific resource within a dataspace project, including its
    attributes.

    Args:
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceProjectResourcesResponse]
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
) -> DataspaceProjectResourcesResponse | None:
    """Get a dataspace project resource by ID

     Retrieve detailed information about a specific resource within a dataspace project, including its
    attributes.

    Args:
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceProjectResourcesResponse
    """

    return sync_detailed(
        resource_id=resource_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[DataspaceProjectResourcesResponse]:
    """Get a dataspace project resource by ID

     Retrieve detailed information about a specific resource within a dataspace project, including its
    attributes.

    Args:
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceProjectResourcesResponse]
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
) -> DataspaceProjectResourcesResponse | None:
    """Get a dataspace project resource by ID

     Retrieve detailed information about a specific resource within a dataspace project, including its
    attributes.

    Args:
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceProjectResourcesResponse
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            client=client,
        )
    ).parsed
