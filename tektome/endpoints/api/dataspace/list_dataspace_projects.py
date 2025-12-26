from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_by import OrderBy
from ...models.paged_dataspace_projects_get_out import PagedDataspaceProjectsGetOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataspace_id: UUID,
    *,
    sort_by: str | Unset = "name",
    order_by: None | OrderBy | Unset = OrderBy.ASCENDING,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sort_by"] = sort_by

    json_order_by: None | str | Unset
    if isinstance(order_by, Unset):
        json_order_by = UNSET
    elif isinstance(order_by, OrderBy):
        json_order_by = order_by.value
    else:
        json_order_by = order_by
    params["order_by"] = json_order_by

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
        "url": "/api/core/dataspaces/{dataspace_id}/projects/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PagedDataspaceProjectsGetOut | None:
    if response.status_code == 200:
        response_200 = PagedDataspaceProjectsGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PagedDataspaceProjectsGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    sort_by: str | Unset = "name",
    order_by: None | OrderBy | Unset = OrderBy.ASCENDING,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedDataspaceProjectsGetOut]:
    """Get Dataspace Projects

     ttCTKUG4

    Retrieve all projects for the current dataspace.
    Filters and sorts projects based on query parameters.

    Args:
        dataspace_id (UUID):
        sort_by (str | Unset):  Default: 'name'.
        order_by (None | OrderBy | Unset):  Default: OrderBy.ASCENDING.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedDataspaceProjectsGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        sort_by=sort_by,
        order_by=order_by,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    sort_by: str | Unset = "name",
    order_by: None | OrderBy | Unset = OrderBy.ASCENDING,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedDataspaceProjectsGetOut | None:
    """Get Dataspace Projects

     ttCTKUG4

    Retrieve all projects for the current dataspace.
    Filters and sorts projects based on query parameters.

    Args:
        dataspace_id (UUID):
        sort_by (str | Unset):  Default: 'name'.
        order_by (None | OrderBy | Unset):  Default: OrderBy.ASCENDING.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedDataspaceProjectsGetOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        client=client,
        sort_by=sort_by,
        order_by=order_by,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    sort_by: str | Unset = "name",
    order_by: None | OrderBy | Unset = OrderBy.ASCENDING,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedDataspaceProjectsGetOut]:
    """Get Dataspace Projects

     ttCTKUG4

    Retrieve all projects for the current dataspace.
    Filters and sorts projects based on query parameters.

    Args:
        dataspace_id (UUID):
        sort_by (str | Unset):  Default: 'name'.
        order_by (None | OrderBy | Unset):  Default: OrderBy.ASCENDING.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedDataspaceProjectsGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        sort_by=sort_by,
        order_by=order_by,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    sort_by: str | Unset = "name",
    order_by: None | OrderBy | Unset = OrderBy.ASCENDING,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedDataspaceProjectsGetOut | None:
    """Get Dataspace Projects

     ttCTKUG4

    Retrieve all projects for the current dataspace.
    Filters and sorts projects based on query parameters.

    Args:
        dataspace_id (UUID):
        sort_by (str | Unset):  Default: 'name'.
        order_by (None | OrderBy | Unset):  Default: OrderBy.ASCENDING.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedDataspaceProjectsGetOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            client=client,
            sort_by=sort_by,
            order_by=order_by,
            page=page,
            page_size=page_size,
        )
    ).parsed
