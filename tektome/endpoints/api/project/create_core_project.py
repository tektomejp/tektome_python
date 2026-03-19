from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.core_project_post_in import CoreProjectPostIn
from ...models.core_project_schema import CoreProjectSchema
from ...models.create_core_project_response import CreateCoreProjectResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CoreProjectPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/projects/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CoreProjectSchema | CreateCoreProjectResponse | None:
    if response.status_code == 201:
        response_201 = CoreProjectSchema.from_dict(response.json())

        return response_201

    if response.status_code == 416:
        response_416 = CreateCoreProjectResponse.from_dict(response.json())

        return response_416

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CoreProjectSchema | CreateCoreProjectResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CoreProjectPostIn,
) -> Response[CoreProjectSchema | CreateCoreProjectResponse]:
    """Post Project

     awdssts1

    Create a new core project in user's current organization
    Create a core project.

    Args:
        body (CoreProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CoreProjectSchema | CreateCoreProjectResponse]
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
    body: CoreProjectPostIn,
) -> CoreProjectSchema | CreateCoreProjectResponse | None:
    """Post Project

     awdssts1

    Create a new core project in user's current organization
    Create a core project.

    Args:
        body (CoreProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CoreProjectSchema | CreateCoreProjectResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CoreProjectPostIn,
) -> Response[CoreProjectSchema | CreateCoreProjectResponse]:
    """Post Project

     awdssts1

    Create a new core project in user's current organization
    Create a core project.

    Args:
        body (CoreProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CoreProjectSchema | CreateCoreProjectResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CoreProjectPostIn,
) -> CoreProjectSchema | CreateCoreProjectResponse | None:
    """Post Project

     awdssts1

    Create a new core project in user's current organization
    Create a core project.

    Args:
        body (CoreProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CoreProjectSchema | CreateCoreProjectResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
