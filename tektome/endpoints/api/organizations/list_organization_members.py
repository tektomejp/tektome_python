from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generic_http_error import GenericHttpError
from ...models.organization_members_schema_response import OrganizationMembersSchemaResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: UUID,
    *,
    ids: list[UUID] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | None | Unset
    if isinstance(ids, Unset):
        json_ids = UNSET
    elif isinstance(ids, list):
        json_ids = []
        for ids_type_0_item_data in ids:
            ids_type_0_item = str(ids_type_0_item_data)
            json_ids.append(ids_type_0_item)

    else:
        json_ids = ids
    params["ids"] = json_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/account/organizations/{organization_id}/members/".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenericHttpError | list[OrganizationMembersSchemaResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OrganizationMembersSchemaResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[GenericHttpError | list[OrganizationMembersSchemaResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    ids: list[UUID] | None | Unset = UNSET,
) -> Response[GenericHttpError | list[OrganizationMembersSchemaResponse]]:
    """List organization members

     Retrieve all members of an organization along with their roles. Optionally filter by user IDs via
    the ids query parameter.

    Args:
        organization_id (UUID):
        ids (list[UUID] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericHttpError | list[OrganizationMembersSchemaResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    ids: list[UUID] | None | Unset = UNSET,
) -> GenericHttpError | list[OrganizationMembersSchemaResponse] | None:
    """List organization members

     Retrieve all members of an organization along with their roles. Optionally filter by user IDs via
    the ids query parameter.

    Args:
        organization_id (UUID):
        ids (list[UUID] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericHttpError | list[OrganizationMembersSchemaResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    ids: list[UUID] | None | Unset = UNSET,
) -> Response[GenericHttpError | list[OrganizationMembersSchemaResponse]]:
    """List organization members

     Retrieve all members of an organization along with their roles. Optionally filter by user IDs via
    the ids query parameter.

    Args:
        organization_id (UUID):
        ids (list[UUID] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericHttpError | list[OrganizationMembersSchemaResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    ids: list[UUID] | None | Unset = UNSET,
) -> GenericHttpError | list[OrganizationMembersSchemaResponse] | None:
    """List organization members

     Retrieve all members of an organization along with their roles. Optionally filter by user IDs via
    the ids query parameter.

    Args:
        organization_id (UUID):
        ids (list[UUID] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericHttpError | list[OrganizationMembersSchemaResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            ids=ids,
        )
    ).parsed
