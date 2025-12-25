from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appresource_routers_resource_version_control_router_upload_new_version_resource_file_params import (
    AppresourceRoutersResourceVersionControlRouterUploadNewVersionResourceFileParams,
)
from ...models.error_out import ErrorOut
from ...models.resource_schema_post_out import ResourceSchemaPostOut
from ...types import Response


def _get_kwargs(
    resource_group_id: UUID,
    resource_vc_id: UUID,
    *,
    body: AppresourceRoutersResourceVersionControlRouterUploadNewVersionResourceFileParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/{resource_group_id}/resources/version-control/{resource_vc_id}/".format(
            resource_group_id=quote(str(resource_group_id), safe=""),
            resource_vc_id=quote(str(resource_vc_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorOut | ResourceSchemaPostOut | None:
    if response.status_code == 200:
        response_200 = ResourceSchemaPostOut.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorOut.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorOut.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorOut.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorOut.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorOut.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = ErrorOut.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = ErrorOut.from_dict(response.json())

        return response_406

    if response.status_code == 407:
        response_407 = ErrorOut.from_dict(response.json())

        return response_407

    if response.status_code == 408:
        response_408 = ErrorOut.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = ErrorOut.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorOut.from_dict(response.json())

        return response_410

    if response.status_code == 411:
        response_411 = ErrorOut.from_dict(response.json())

        return response_411

    if response.status_code == 412:
        response_412 = ErrorOut.from_dict(response.json())

        return response_412

    if response.status_code == 416:
        response_416 = ErrorOut.from_dict(response.json())

        return response_416

    if response.status_code == 418:
        response_418 = ErrorOut.from_dict(response.json())

        return response_418

    if response.status_code == 425:
        response_425 = ErrorOut.from_dict(response.json())

        return response_425

    if response.status_code == 429:
        response_429 = ErrorOut.from_dict(response.json())

        return response_429

    if response.status_code == 451:
        response_451 = ErrorOut.from_dict(response.json())

        return response_451

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorOut | ResourceSchemaPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_group_id: UUID,
    resource_vc_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AppresourceRoutersResourceVersionControlRouterUploadNewVersionResourceFileParams,
) -> Response[ErrorOut | ResourceSchemaPostOut]:
    """Upload New Version Resource

     3wnuzkXm

    Upload file as a new version of resource

    Note: can add ResourceAllowEdit in body later

    Args:
        resource_group_id (UUID):
        resource_vc_id (UUID):
        body (AppresourceRoutersResourceVersionControlRouterUploadNewVersionResourceFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOut | ResourceSchemaPostOut]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
        resource_vc_id=resource_vc_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_group_id: UUID,
    resource_vc_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AppresourceRoutersResourceVersionControlRouterUploadNewVersionResourceFileParams,
) -> ErrorOut | ResourceSchemaPostOut | None:
    """Upload New Version Resource

     3wnuzkXm

    Upload file as a new version of resource

    Note: can add ResourceAllowEdit in body later

    Args:
        resource_group_id (UUID):
        resource_vc_id (UUID):
        body (AppresourceRoutersResourceVersionControlRouterUploadNewVersionResourceFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOut | ResourceSchemaPostOut
    """

    return sync_detailed(
        resource_group_id=resource_group_id,
        resource_vc_id=resource_vc_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    resource_group_id: UUID,
    resource_vc_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AppresourceRoutersResourceVersionControlRouterUploadNewVersionResourceFileParams,
) -> Response[ErrorOut | ResourceSchemaPostOut]:
    """Upload New Version Resource

     3wnuzkXm

    Upload file as a new version of resource

    Note: can add ResourceAllowEdit in body later

    Args:
        resource_group_id (UUID):
        resource_vc_id (UUID):
        body (AppresourceRoutersResourceVersionControlRouterUploadNewVersionResourceFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOut | ResourceSchemaPostOut]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
        resource_vc_id=resource_vc_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_group_id: UUID,
    resource_vc_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AppresourceRoutersResourceVersionControlRouterUploadNewVersionResourceFileParams,
) -> ErrorOut | ResourceSchemaPostOut | None:
    """Upload New Version Resource

     3wnuzkXm

    Upload file as a new version of resource

    Note: can add ResourceAllowEdit in body later

    Args:
        resource_group_id (UUID):
        resource_vc_id (UUID):
        body (AppresourceRoutersResourceVersionControlRouterUploadNewVersionResourceFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOut | ResourceSchemaPostOut
    """

    return (
        await asyncio_detailed(
            resource_group_id=resource_group_id,
            resource_vc_id=resource_vc_id,
            client=client,
            body=body,
        )
    ).parsed
