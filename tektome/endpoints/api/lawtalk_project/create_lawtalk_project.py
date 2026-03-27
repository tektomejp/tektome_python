from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_lawtalk_project_request import CreateLawtalkProjectRequest
from ...models.error_response import ErrorResponse
from ...models.lawtalk_project_schema import LawtalkProjectSchema
from ...types import Response


def _get_kwargs(
    *,
    body: CreateLawtalkProjectRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/projects/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | LawtalkProjectSchema | None:
    if response.status_code == 201:
        response_201 = LawtalkProjectSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | LawtalkProjectSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateLawtalkProjectRequest,
) -> Response[ErrorResponse | LawtalkProjectSchema]:
    """Create a project with attributes

     Create a new project with country-specific attributes such as structures, site area, floors, height,
    and building area. The creator is assigned as project owner.

    Args:
        body (CreateLawtalkProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | LawtalkProjectSchema]
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
    body: CreateLawtalkProjectRequest,
) -> ErrorResponse | LawtalkProjectSchema | None:
    """Create a project with attributes

     Create a new project with country-specific attributes such as structures, site area, floors, height,
    and building area. The creator is assigned as project owner.

    Args:
        body (CreateLawtalkProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | LawtalkProjectSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateLawtalkProjectRequest,
) -> Response[ErrorResponse | LawtalkProjectSchema]:
    """Create a project with attributes

     Create a new project with country-specific attributes such as structures, site area, floors, height,
    and building area. The creator is assigned as project owner.

    Args:
        body (CreateLawtalkProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | LawtalkProjectSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateLawtalkProjectRequest,
) -> ErrorResponse | LawtalkProjectSchema | None:
    """Create a project with attributes

     Create a new project with country-specific attributes such as structures, site area, floors, height,
    and building area. The creator is assigned as project owner.

    Args:
        body (CreateLawtalkProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | LawtalkProjectSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
