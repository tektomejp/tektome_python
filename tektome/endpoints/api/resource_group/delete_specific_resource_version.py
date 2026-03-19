from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    resource_group_id: UUID,
    resource_vc_id: UUID,
    version_num: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/core/resource-groups/{resource_group_id}/resources/version-control/{resource_vc_id}/version/{version_num}/".format(
            resource_group_id=quote(str(resource_group_id), safe=""),
            resource_vc_id=quote(str(resource_vc_id), safe=""),
            version_num=quote(str(version_num), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = ErrorResponse.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = ErrorResponse.from_dict(response.json())

        return response_406

    if response.status_code == 407:
        response_407 = ErrorResponse.from_dict(response.json())

        return response_407

    if response.status_code == 408:
        response_408 = ErrorResponse.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 411:
        response_411 = ErrorResponse.from_dict(response.json())

        return response_411

    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412

    if response.status_code == 416:
        response_416 = ErrorResponse.from_dict(response.json())

        return response_416

    if response.status_code == 418:
        response_418 = ErrorResponse.from_dict(response.json())

        return response_418

    if response.status_code == 425:
        response_425 = ErrorResponse.from_dict(response.json())

        return response_425

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 451:
        response_451 = ErrorResponse.from_dict(response.json())

        return response_451

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_group_id: UUID,
    resource_vc_id: UUID,
    version_num: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ErrorResponse]:
    """Delete a specific resource version

     Delete a specific version of a resource by version number. Cannot delete if it is the only remaining
    version.

    Args:
        resource_group_id (UUID):
        resource_vc_id (UUID):
        version_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
        resource_vc_id=resource_vc_id,
        version_num=version_num,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_group_id: UUID,
    resource_vc_id: UUID,
    version_num: int,
    *,
    client: AuthenticatedClient,
) -> Any | ErrorResponse | None:
    """Delete a specific resource version

     Delete a specific version of a resource by version number. Cannot delete if it is the only remaining
    version.

    Args:
        resource_group_id (UUID):
        resource_vc_id (UUID):
        version_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return sync_detailed(
        resource_group_id=resource_group_id,
        resource_vc_id=resource_vc_id,
        version_num=version_num,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_group_id: UUID,
    resource_vc_id: UUID,
    version_num: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ErrorResponse]:
    """Delete a specific resource version

     Delete a specific version of a resource by version number. Cannot delete if it is the only remaining
    version.

    Args:
        resource_group_id (UUID):
        resource_vc_id (UUID):
        version_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
        resource_vc_id=resource_vc_id,
        version_num=version_num,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_group_id: UUID,
    resource_vc_id: UUID,
    version_num: int,
    *,
    client: AuthenticatedClient,
) -> Any | ErrorResponse | None:
    """Delete a specific resource version

     Delete a specific version of a resource by version number. Cannot delete if it is the only remaining
    version.

    Args:
        resource_group_id (UUID):
        resource_vc_id (UUID):
        version_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            resource_group_id=resource_group_id,
            resource_vc_id=resource_vc_id,
            version_num=version_num,
            client=client,
        )
    ).parsed
