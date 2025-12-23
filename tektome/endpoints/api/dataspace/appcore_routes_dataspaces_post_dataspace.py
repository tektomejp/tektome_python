from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appcore_routes_dataspaces_post_dataspace_response import AppcoreRoutesDataspacesPostDataspaceResponse
from ...models.dataspace_post_in import DataspacePostIn
from ...models.dataspace_post_out import DataspacePostOut
from ...types import Response


def _get_kwargs(
    *,
    body: DataspacePostIn,
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
) -> AppcoreRoutesDataspacesPostDataspaceResponse | DataspacePostOut | None:
    if response.status_code == 201:
        response_201 = DataspacePostOut.from_dict(response.json())

        return response_201

    if response.status_code == 416:
        response_416 = AppcoreRoutesDataspacesPostDataspaceResponse.from_dict(response.json())

        return response_416

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppcoreRoutesDataspacesPostDataspaceResponse | DataspacePostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DataspacePostIn,
) -> Response[AppcoreRoutesDataspacesPostDataspaceResponse | DataspacePostOut]:
    """Post Dataspace

     x16N0f5v

    Create a new dataspace, if organization_id is not provided, will use the user's current
    organization.
    WARN:
        id in the payload is ONLY intended to be used for syncing DS from storage. DO NOT USE IT
    OTHERWISE.

    Args:
        body (DataspacePostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppcoreRoutesDataspacesPostDataspaceResponse | DataspacePostOut]
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
    body: DataspacePostIn,
) -> AppcoreRoutesDataspacesPostDataspaceResponse | DataspacePostOut | None:
    """Post Dataspace

     x16N0f5v

    Create a new dataspace, if organization_id is not provided, will use the user's current
    organization.
    WARN:
        id in the payload is ONLY intended to be used for syncing DS from storage. DO NOT USE IT
    OTHERWISE.

    Args:
        body (DataspacePostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppcoreRoutesDataspacesPostDataspaceResponse | DataspacePostOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DataspacePostIn,
) -> Response[AppcoreRoutesDataspacesPostDataspaceResponse | DataspacePostOut]:
    """Post Dataspace

     x16N0f5v

    Create a new dataspace, if organization_id is not provided, will use the user's current
    organization.
    WARN:
        id in the payload is ONLY intended to be used for syncing DS from storage. DO NOT USE IT
    OTHERWISE.

    Args:
        body (DataspacePostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppcoreRoutesDataspacesPostDataspaceResponse | DataspacePostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DataspacePostIn,
) -> AppcoreRoutesDataspacesPostDataspaceResponse | DataspacePostOut | None:
    """Post Dataspace

     x16N0f5v

    Create a new dataspace, if organization_id is not provided, will use the user's current
    organization.
    WARN:
        id in the payload is ONLY intended to be used for syncing DS from storage. DO NOT USE IT
    OTHERWISE.

    Args:
        body (DataspacePostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppcoreRoutesDataspacesPostDataspaceResponse | DataspacePostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
