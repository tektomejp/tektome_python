import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paged_dataspace_search_request_get_out import PagedDataspaceSearchRequestGetOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataspace_id: UUID,
    *,
    user_ids: list[UUID] | Unset = UNSET,
    date_from: datetime.date | None | Unset = UNSET,
    date_to: datetime.date | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_user_ids: list[str] | Unset = UNSET
    if not isinstance(user_ids, Unset):
        json_user_ids = []
        for user_ids_item_data in user_ids:
            user_ids_item = str(user_ids_item_data)
            json_user_ids.append(user_ids_item)

    params["user_ids"] = json_user_ids

    json_date_from: None | str | Unset
    if isinstance(date_from, Unset):
        json_date_from = UNSET
    elif isinstance(date_from, datetime.date):
        json_date_from = date_from.isoformat()
    else:
        json_date_from = date_from
    params["date_from"] = json_date_from

    json_date_to: None | str | Unset
    if isinstance(date_to, Unset):
        json_date_to = UNSET
    elif isinstance(date_to, datetime.date):
        json_date_to = date_to.isoformat()
    else:
        json_date_to = date_to
    params["date_to"] = json_date_to

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

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
        "url": "/api/core/dataspaces/{dataspace_id}/search/requests/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PagedDataspaceSearchRequestGetOut | None:
    if response.status_code == 200:
        response_200 = PagedDataspaceSearchRequestGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PagedDataspaceSearchRequestGetOut]:
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
    user_ids: list[UUID] | Unset = UNSET,
    date_from: datetime.date | None | Unset = UNSET,
    date_to: datetime.date | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedDataspaceSearchRequestGetOut]:
    """List search requests

     Retrieve all search requests for the current user in this dataspace, ordered by creation date with
    the newest first.

    Args:
        dataspace_id (UUID):
        user_ids (list[UUID] | Unset): Filter by creator user IDs.
        date_from (datetime.date | None | Unset): Filter search requests created on or after this
            date (inclusive).
        date_to (datetime.date | None | Unset): Filter search requests created on or before this
            date (inclusive, end of day).
        search (None | str | Unset): Keyword search across snapshot tag name, keywords, highlight
            keywords, and snapshot filter configuration names.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedDataspaceSearchRequestGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        user_ids=user_ids,
        date_from=date_from,
        date_to=date_to,
        search=search,
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
    user_ids: list[UUID] | Unset = UNSET,
    date_from: datetime.date | None | Unset = UNSET,
    date_to: datetime.date | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedDataspaceSearchRequestGetOut | None:
    """List search requests

     Retrieve all search requests for the current user in this dataspace, ordered by creation date with
    the newest first.

    Args:
        dataspace_id (UUID):
        user_ids (list[UUID] | Unset): Filter by creator user IDs.
        date_from (datetime.date | None | Unset): Filter search requests created on or after this
            date (inclusive).
        date_to (datetime.date | None | Unset): Filter search requests created on or before this
            date (inclusive, end of day).
        search (None | str | Unset): Keyword search across snapshot tag name, keywords, highlight
            keywords, and snapshot filter configuration names.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedDataspaceSearchRequestGetOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        client=client,
        user_ids=user_ids,
        date_from=date_from,
        date_to=date_to,
        search=search,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    user_ids: list[UUID] | Unset = UNSET,
    date_from: datetime.date | None | Unset = UNSET,
    date_to: datetime.date | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedDataspaceSearchRequestGetOut]:
    """List search requests

     Retrieve all search requests for the current user in this dataspace, ordered by creation date with
    the newest first.

    Args:
        dataspace_id (UUID):
        user_ids (list[UUID] | Unset): Filter by creator user IDs.
        date_from (datetime.date | None | Unset): Filter search requests created on or after this
            date (inclusive).
        date_to (datetime.date | None | Unset): Filter search requests created on or before this
            date (inclusive, end of day).
        search (None | str | Unset): Keyword search across snapshot tag name, keywords, highlight
            keywords, and snapshot filter configuration names.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedDataspaceSearchRequestGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        user_ids=user_ids,
        date_from=date_from,
        date_to=date_to,
        search=search,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    user_ids: list[UUID] | Unset = UNSET,
    date_from: datetime.date | None | Unset = UNSET,
    date_to: datetime.date | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedDataspaceSearchRequestGetOut | None:
    """List search requests

     Retrieve all search requests for the current user in this dataspace, ordered by creation date with
    the newest first.

    Args:
        dataspace_id (UUID):
        user_ids (list[UUID] | Unset): Filter by creator user IDs.
        date_from (datetime.date | None | Unset): Filter search requests created on or after this
            date (inclusive).
        date_to (datetime.date | None | Unset): Filter search requests created on or before this
            date (inclusive, end of day).
        search (None | str | Unset): Keyword search across snapshot tag name, keywords, highlight
            keywords, and snapshot filter configuration names.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedDataspaceSearchRequestGetOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            client=client,
            user_ids=user_ids,
            date_from=date_from,
            date_to=date_to,
            search=search,
            page=page,
            page_size=page_size,
        )
    ).parsed
