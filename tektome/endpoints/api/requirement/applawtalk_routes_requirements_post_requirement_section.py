from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resource_section_schema import ResourceSectionSchema
from ...types import Response


def _get_kwargs(
    requirement_id: UUID,
    resource_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/requirements/{requirement_id}/resource/{resource_id}/sections/".format(
            requirement_id=quote(str(requirement_id), safe=""),
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ResourceSectionSchema | None:
    if response.status_code == 201:
        response_201 = ResourceSectionSchema.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResourceSectionSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    requirement_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ResourceSectionSchema]:
    """Post Requirement Section

     Al_9UtBt
    Create a Section object

    Args:
        request: Request object
        path_params: path params of type CreateResourceSectionPath

    Returns: 201, ResourceSectionSchema

    Args:
        requirement_id (UUID):
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceSectionSchema]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ResourceSectionSchema | None:
    """Post Requirement Section

     Al_9UtBt
    Create a Section object

    Args:
        request: Request object
        path_params: path params of type CreateResourceSectionPath

    Returns: 201, ResourceSectionSchema

    Args:
        requirement_id (UUID):
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceSectionSchema
    """

    return sync_detailed(
        requirement_id=requirement_id,
        resource_id=resource_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    requirement_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ResourceSectionSchema]:
    """Post Requirement Section

     Al_9UtBt
    Create a Section object

    Args:
        request: Request object
        path_params: path params of type CreateResourceSectionPath

    Returns: 201, ResourceSectionSchema

    Args:
        requirement_id (UUID):
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceSectionSchema]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ResourceSectionSchema | None:
    """Post Requirement Section

     Al_9UtBt
    Create a Section object

    Args:
        request: Request object
        path_params: path params of type CreateResourceSectionPath

    Returns: 201, ResourceSectionSchema

    Args:
        requirement_id (UUID):
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceSectionSchema
    """

    return (
        await asyncio_detailed(
            requirement_id=requirement_id,
            resource_id=resource_id,
            client=client,
        )
    ).parsed
