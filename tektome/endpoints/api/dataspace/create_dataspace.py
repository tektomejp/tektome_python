from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_dataspace_request import CreateDataspaceRequest
from ...models.create_dataspace_response import CreateDataspaceResponse
from ...models.dataspace_response import DataspaceResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateDataspaceRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateDataspaceResponse | DataspaceResponse | None:
    if response.status_code == 201:
        response_201 = DataspaceResponse.from_dict(response.json())

        return response_201

    if response.status_code == 416:
        response_416 = CreateDataspaceResponse.from_dict(response.json())

        return response_416

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateDataspaceResponse | DataspaceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateDataspaceRequest,
) -> Response[CreateDataspaceResponse | DataspaceResponse]:
    """Create a new dataspace

     Create a new dataspace within an organization. If no organization ID is provided, the user's current
    organization is used.

    Args:
        body (CreateDataspaceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateDataspaceResponse | DataspaceResponse]
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
    body: CreateDataspaceRequest,
) -> CreateDataspaceResponse | DataspaceResponse | None:
    """Create a new dataspace

     Create a new dataspace within an organization. If no organization ID is provided, the user's current
    organization is used.

    Args:
        body (CreateDataspaceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateDataspaceResponse | DataspaceResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateDataspaceRequest,
) -> Response[CreateDataspaceResponse | DataspaceResponse]:
    """Create a new dataspace

     Create a new dataspace within an organization. If no organization ID is provided, the user's current
    organization is used.

    Args:
        body (CreateDataspaceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateDataspaceResponse | DataspaceResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateDataspaceRequest,
) -> CreateDataspaceResponse | DataspaceResponse | None:
    """Create a new dataspace

     Create a new dataspace within an organization. If no organization ID is provided, the user's current
    organization is used.

    Args:
        body (CreateDataspaceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateDataspaceResponse | DataspaceResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
