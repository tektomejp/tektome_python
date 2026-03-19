from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    *,
    search_query: None | str | Unset = UNSET,
    keywords: list[str] | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_search_query: None | str | Unset
    if isinstance(search_query, Unset):
        json_search_query = UNSET
    else:
        json_search_query = search_query
    params["search_query"] = json_search_query

    json_keywords: list[str] | None | Unset
    if isinstance(keywords, Unset):
        json_keywords = UNSET
    elif isinstance(keywords, list):
        json_keywords = keywords

    else:
        json_keywords = keywords
    params["keywords"] = json_keywords

    json_is_public: bool | None | Unset
    if isinstance(is_public, Unset):
        json_is_public = UNSET
    else:
        json_is_public = is_public
    params["is_public"] = json_is_public

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
        "url": "/api/app/lawtalk/projects/{project_id}/resources/".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    search_query: None | str | Unset = UNSET,
    keywords: list[str] | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[Any]:
    """List project resources

     Retrieve a paginated list of all resources under a project. Supports filtering by search query,
    keywords, and public visibility.

    Args:
        project_id (UUID):
        search_query (None | str | Unset):
        keywords (list[str] | None | Unset):
        is_public (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        search_query=search_query,
        keywords=keywords,
        is_public=is_public,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    search_query: None | str | Unset = UNSET,
    keywords: list[str] | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[Any]:
    """List project resources

     Retrieve a paginated list of all resources under a project. Supports filtering by search query,
    keywords, and public visibility.

    Args:
        project_id (UUID):
        search_query (None | str | Unset):
        keywords (list[str] | None | Unset):
        is_public (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        search_query=search_query,
        keywords=keywords,
        is_public=is_public,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
