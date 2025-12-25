from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paged_dataspace_list_get_out import PagedDataspaceListGetOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
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

    params["page"] = page

    json_page_size: int | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["page_size"] = json_page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/dataspaces/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PagedDataspaceListGetOut | None:
    if response.status_code == 200:
        response_200 = PagedDataspaceListGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PagedDataspaceListGetOut]:
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
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedDataspaceListGetOut]:
    """Get Dataspaces

     rvCLTwry

    Retrieve all dataspaces that the user is a member of.
    if organization_id is provided, filter dataspaces by organization ID.

    Args:
        organization_id (None | Unset | UUID): Filter dataspaces by organization ID.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedDataspaceListGetOut]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    organization_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedDataspaceListGetOut | None:
    """Get Dataspaces

     rvCLTwry

    Retrieve all dataspaces that the user is a member of.
    if organization_id is provided, filter dataspaces by organization ID.

    Args:
        organization_id (None | Unset | UUID): Filter dataspaces by organization ID.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedDataspaceListGetOut
    """

    return sync_detailed(
        client=client,
        organization_id=organization_id,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    organization_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedDataspaceListGetOut]:
    """Get Dataspaces

     rvCLTwry

    Retrieve all dataspaces that the user is a member of.
    if organization_id is provided, filter dataspaces by organization ID.

    Args:
        organization_id (None | Unset | UUID): Filter dataspaces by organization ID.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedDataspaceListGetOut]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    organization_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedDataspaceListGetOut | None:
    """Get Dataspaces

     rvCLTwry

    Retrieve all dataspaces that the user is a member of.
    if organization_id is provided, filter dataspaces by organization ID.

    Args:
        organization_id (None | Unset | UUID): Filter dataspaces by organization ID.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedDataspaceListGetOut
    """

    return (
        await asyncio_detailed(
            client=client,
            organization_id=organization_id,
            page=page,
            page_size=page_size,
        )
    ).parsed
