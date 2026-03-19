from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.search_payload_v4_response import SearchPayloadV4Response
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    *,
    query: str,
    keyword: None | str | Unset = UNSET,
    top_k: int | Unset = 30,
    skip: int | Unset = 0,
    sort_by_pages: bool | Unset = False,
    debug: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["query"] = query

    json_keyword: None | str | Unset
    if isinstance(keyword, Unset):
        json_keyword = UNSET
    else:
        json_keyword = keyword
    params["keyword"] = json_keyword

    params["top_k"] = top_k

    params["skip"] = skip

    params["sort_by_pages"] = sort_by_pages

    params["debug"] = debug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/projects/{project_id}/search-ocr-page/v4/".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SearchPayloadV4Response | None:
    if response.status_code == 200:
        response_200 = SearchPayloadV4Response.from_dict(response.json())

        return response_200

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | SearchPayloadV4Response]:
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
    query: str,
    keyword: None | str | Unset = UNSET,
    top_k: int | Unset = 30,
    skip: int | Unset = 0,
    sort_by_pages: bool | Unset = False,
    debug: bool | Unset = False,
) -> Response[ErrorResponse | SearchPayloadV4Response]:
    """Search project resource pages (v4)

     Search extracted pages in project resources using vector, exact, or hybrid search modes. Supports
    query-based semantic search and keyword-based exact matching.

    Args:
        project_id (UUID):
        query (str):
        keyword (None | str | Unset):
        top_k (int | Unset):  Default: 30.
        skip (int | Unset):  Default: 0.
        sort_by_pages (bool | Unset):  Default: False.
        debug (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SearchPayloadV4Response]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        query=query,
        keyword=keyword,
        top_k=top_k,
        skip=skip,
        sort_by_pages=sort_by_pages,
        debug=debug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    query: str,
    keyword: None | str | Unset = UNSET,
    top_k: int | Unset = 30,
    skip: int | Unset = 0,
    sort_by_pages: bool | Unset = False,
    debug: bool | Unset = False,
) -> ErrorResponse | SearchPayloadV4Response | None:
    """Search project resource pages (v4)

     Search extracted pages in project resources using vector, exact, or hybrid search modes. Supports
    query-based semantic search and keyword-based exact matching.

    Args:
        project_id (UUID):
        query (str):
        keyword (None | str | Unset):
        top_k (int | Unset):  Default: 30.
        skip (int | Unset):  Default: 0.
        sort_by_pages (bool | Unset):  Default: False.
        debug (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SearchPayloadV4Response
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        query=query,
        keyword=keyword,
        top_k=top_k,
        skip=skip,
        sort_by_pages=sort_by_pages,
        debug=debug,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    query: str,
    keyword: None | str | Unset = UNSET,
    top_k: int | Unset = 30,
    skip: int | Unset = 0,
    sort_by_pages: bool | Unset = False,
    debug: bool | Unset = False,
) -> Response[ErrorResponse | SearchPayloadV4Response]:
    """Search project resource pages (v4)

     Search extracted pages in project resources using vector, exact, or hybrid search modes. Supports
    query-based semantic search and keyword-based exact matching.

    Args:
        project_id (UUID):
        query (str):
        keyword (None | str | Unset):
        top_k (int | Unset):  Default: 30.
        skip (int | Unset):  Default: 0.
        sort_by_pages (bool | Unset):  Default: False.
        debug (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SearchPayloadV4Response]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        query=query,
        keyword=keyword,
        top_k=top_k,
        skip=skip,
        sort_by_pages=sort_by_pages,
        debug=debug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    query: str,
    keyword: None | str | Unset = UNSET,
    top_k: int | Unset = 30,
    skip: int | Unset = 0,
    sort_by_pages: bool | Unset = False,
    debug: bool | Unset = False,
) -> ErrorResponse | SearchPayloadV4Response | None:
    """Search project resource pages (v4)

     Search extracted pages in project resources using vector, exact, or hybrid search modes. Supports
    query-based semantic search and keyword-based exact matching.

    Args:
        project_id (UUID):
        query (str):
        keyword (None | str | Unset):
        top_k (int | Unset):  Default: 30.
        skip (int | Unset):  Default: 0.
        sort_by_pages (bool | Unset):  Default: False.
        debug (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SearchPayloadV4Response
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            query=query,
            keyword=keyword,
            top_k=top_k,
            skip=skip,
            sort_by_pages=sort_by_pages,
            debug=debug,
        )
    ).parsed
