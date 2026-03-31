from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.lawtalk_resource_schema import LawtalkResourceSchema
from ...models.wrap_core_resource_post_in import WrapCoreResourcePostIn
from ...types import Response


def _get_kwargs(
    resource_group_id: UUID,
    *,
    body: WrapCoreResourcePostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/resources/groups/{resource_group_id}/wrap-core-resource/".format(
            resource_group_id=quote(str(resource_group_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | LawtalkResourceSchema | None:
    if response.status_code == 201:
        response_201 = LawtalkResourceSchema.from_dict(response.json())

        return response_201

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | LawtalkResourceSchema]:
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
    body: WrapCoreResourcePostIn,
) -> Response[ErrorResponse | LawtalkResourceSchema]:
    """Wrap a core resource with LawtalkResource

     Create a LawtalkResource wrapper for an existing core resource identified by its
    ResourceVersionControl ID. Used when resources are created via core path-based APIs and need to be
    accessible through lawtalk endpoints.

    Args:
        resource_group_id (UUID): Resource group ID
        body (WrapCoreResourcePostIn): Input for wrapping a core resource with a LawtalkResource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | LawtalkResourceSchema]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: WrapCoreResourcePostIn,
) -> ErrorResponse | LawtalkResourceSchema | None:
    """Wrap a core resource with LawtalkResource

     Create a LawtalkResource wrapper for an existing core resource identified by its
    ResourceVersionControl ID. Used when resources are created via core path-based APIs and need to be
    accessible through lawtalk endpoints.

    Args:
        resource_group_id (UUID): Resource group ID
        body (WrapCoreResourcePostIn): Input for wrapping a core resource with a LawtalkResource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | LawtalkResourceSchema
    """

    return sync_detailed(
        resource_group_id=resource_group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: WrapCoreResourcePostIn,
) -> Response[ErrorResponse | LawtalkResourceSchema]:
    """Wrap a core resource with LawtalkResource

     Create a LawtalkResource wrapper for an existing core resource identified by its
    ResourceVersionControl ID. Used when resources are created via core path-based APIs and need to be
    accessible through lawtalk endpoints.

    Args:
        resource_group_id (UUID): Resource group ID
        body (WrapCoreResourcePostIn): Input for wrapping a core resource with a LawtalkResource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | LawtalkResourceSchema]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: WrapCoreResourcePostIn,
) -> ErrorResponse | LawtalkResourceSchema | None:
    """Wrap a core resource with LawtalkResource

     Create a LawtalkResource wrapper for an existing core resource identified by its
    ResourceVersionControl ID. Used when resources are created via core path-based APIs and need to be
    accessible through lawtalk endpoints.

    Args:
        resource_group_id (UUID): Resource group ID
        body (WrapCoreResourcePostIn): Input for wrapping a core resource with a LawtalkResource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | LawtalkResourceSchema
    """

    return (
        await asyncio_detailed(
            resource_group_id=resource_group_id,
            client=client,
            body=body,
        )
    ).parsed
