from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generic_http_error import GenericHttpError
from ...models.unread_count_out import UnreadCountOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization_id: None | Unset | UUID = UNSET,
    dataspace_id: None | Unset | UUID = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_organization_id: None | str | Unset
    if isinstance(organization_id, Unset):
        json_organization_id = UNSET
    elif isinstance(organization_id, UUID):
        json_organization_id = str(organization_id)
    else:
        json_organization_id = organization_id
    params["organization_id"] = json_organization_id

    json_dataspace_id: None | str | Unset
    if isinstance(dataspace_id, Unset):
        json_dataspace_id = UNSET
    elif isinstance(dataspace_id, UUID):
        json_dataspace_id = str(dataspace_id)
    else:
        json_dataspace_id = dataspace_id
    params["dataspace_id"] = json_dataspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/notifications/unread-count/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenericHttpError | UnreadCountOut | None:
    if response.status_code == 200:
        response_200 = UnreadCountOut.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GenericHttpError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GenericHttpError.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GenericHttpError.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GenericHttpError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GenericHttpError.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GenericHttpError.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GenericHttpError.from_dict(response.json())

        return response_406

    if response.status_code == 407:
        response_407 = GenericHttpError.from_dict(response.json())

        return response_407

    if response.status_code == 408:
        response_408 = GenericHttpError.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = GenericHttpError.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = GenericHttpError.from_dict(response.json())

        return response_410

    if response.status_code == 411:
        response_411 = GenericHttpError.from_dict(response.json())

        return response_411

    if response.status_code == 412:
        response_412 = GenericHttpError.from_dict(response.json())

        return response_412

    if response.status_code == 416:
        response_416 = GenericHttpError.from_dict(response.json())

        return response_416

    if response.status_code == 418:
        response_418 = GenericHttpError.from_dict(response.json())

        return response_418

    if response.status_code == 425:
        response_425 = GenericHttpError.from_dict(response.json())

        return response_425

    if response.status_code == 429:
        response_429 = GenericHttpError.from_dict(response.json())

        return response_429

    if response.status_code == 451:
        response_451 = GenericHttpError.from_dict(response.json())

        return response_451

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GenericHttpError | UnreadCountOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    organization_id: None | Unset | UUID = UNSET,
    dataspace_id: None | Unset | UUID = UNSET,
) -> Response[GenericHttpError | UnreadCountOut]:
    """Return unread notification count

     m2KpL8vQ

    Get the count of unread notifications for the authenticated user.

    Supports filtering by organization and dataspace.

    Args:
        organization_id (None | Unset | UUID):
        dataspace_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericHttpError | UnreadCountOut]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        dataspace_id=dataspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    organization_id: None | Unset | UUID = UNSET,
    dataspace_id: None | Unset | UUID = UNSET,
) -> GenericHttpError | UnreadCountOut | None:
    """Return unread notification count

     m2KpL8vQ

    Get the count of unread notifications for the authenticated user.

    Supports filtering by organization and dataspace.

    Args:
        organization_id (None | Unset | UUID):
        dataspace_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericHttpError | UnreadCountOut
    """

    return sync_detailed(
        client=client,
        organization_id=organization_id,
        dataspace_id=dataspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    organization_id: None | Unset | UUID = UNSET,
    dataspace_id: None | Unset | UUID = UNSET,
) -> Response[GenericHttpError | UnreadCountOut]:
    """Return unread notification count

     m2KpL8vQ

    Get the count of unread notifications for the authenticated user.

    Supports filtering by organization and dataspace.

    Args:
        organization_id (None | Unset | UUID):
        dataspace_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericHttpError | UnreadCountOut]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        dataspace_id=dataspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    organization_id: None | Unset | UUID = UNSET,
    dataspace_id: None | Unset | UUID = UNSET,
) -> GenericHttpError | UnreadCountOut | None:
    """Return unread notification count

     m2KpL8vQ

    Get the count of unread notifications for the authenticated user.

    Supports filtering by organization and dataspace.

    Args:
        organization_id (None | Unset | UUID):
        dataspace_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericHttpError | UnreadCountOut
    """

    return (
        await asyncio_detailed(
            client=client,
            organization_id=organization_id,
            dataspace_id=dataspace_id,
        )
    ).parsed
