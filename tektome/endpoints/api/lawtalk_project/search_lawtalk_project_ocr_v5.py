from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_out import ErrorOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    *,
    query: str,
    keywords: list[str] | Unset = UNSET,
    resource_group_ids: list[UUID] | Unset = UNSET,
    top_k: int | Unset = 30,
    skip: int | Unset = 0,
    sort_by_pages: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["query"] = query

    json_keywords: list[str] | Unset = UNSET
    if not isinstance(keywords, Unset):
        json_keywords = keywords

    params["keywords"] = json_keywords

    json_resource_group_ids: list[str] | Unset = UNSET
    if not isinstance(resource_group_ids, Unset):
        json_resource_group_ids = []
        for resource_group_ids_item_data in resource_group_ids:
            resource_group_ids_item = str(resource_group_ids_item_data)
            json_resource_group_ids.append(resource_group_ids_item)

    params["resource_group_ids"] = json_resource_group_ids

    params["top_k"] = top_k

    params["skip"] = skip

    params["sort_by_pages"] = sort_by_pages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/projects/{project_id}/search-ocr-page/v5/".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorOut | None:
    if response.status_code == 200:
        response_200 = response.json()
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

    if response.status_code == 500:
        response_500 = ErrorOut.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorOut]:
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
    keywords: list[str] | Unset = UNSET,
    resource_group_ids: list[UUID] | Unset = UNSET,
    top_k: int | Unset = 30,
    skip: int | Unset = 0,
    sort_by_pages: bool | Unset = False,
) -> Response[Any | ErrorOut]:
    """Search Ocr Page V5

     Wp_rJkTS

    Searching for OCR result from the given query and keywords.

    Logic:

        - If only query is provided, will perform vector search
            (Score is based on cosine similarity)

            PS. Current embedding model is Azure Text Embedding ADA002
            Will change to 003 - Large once re-embedding is done

        - If only keyword is provided, will perform exact search
            (Score is based on BM25)

        - If both query and keyword are provided, will perform hybrid search
            (Score is based on RRF - Reciprocal Rank Fusion)

    Results:
        # TBD

    Noted:
        if sort_by_pages is True, the list result will be sorted by (page number ascending, score
    descending)
        else, the list result will be sorted by (score descending, page number ascending)

    Args:
        project_id (UUID):
        query (str):
        keywords (list[str] | Unset):
        resource_group_ids (list[UUID] | Unset):
        top_k (int | Unset):  Default: 30.
        skip (int | Unset):  Default: 0.
        sort_by_pages (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        query=query,
        keywords=keywords,
        resource_group_ids=resource_group_ids,
        top_k=top_k,
        skip=skip,
        sort_by_pages=sort_by_pages,
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
    keywords: list[str] | Unset = UNSET,
    resource_group_ids: list[UUID] | Unset = UNSET,
    top_k: int | Unset = 30,
    skip: int | Unset = 0,
    sort_by_pages: bool | Unset = False,
) -> Any | ErrorOut | None:
    """Search Ocr Page V5

     Wp_rJkTS

    Searching for OCR result from the given query and keywords.

    Logic:

        - If only query is provided, will perform vector search
            (Score is based on cosine similarity)

            PS. Current embedding model is Azure Text Embedding ADA002
            Will change to 003 - Large once re-embedding is done

        - If only keyword is provided, will perform exact search
            (Score is based on BM25)

        - If both query and keyword are provided, will perform hybrid search
            (Score is based on RRF - Reciprocal Rank Fusion)

    Results:
        # TBD

    Noted:
        if sort_by_pages is True, the list result will be sorted by (page number ascending, score
    descending)
        else, the list result will be sorted by (score descending, page number ascending)

    Args:
        project_id (UUID):
        query (str):
        keywords (list[str] | Unset):
        resource_group_ids (list[UUID] | Unset):
        top_k (int | Unset):  Default: 30.
        skip (int | Unset):  Default: 0.
        sort_by_pages (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorOut
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        query=query,
        keywords=keywords,
        resource_group_ids=resource_group_ids,
        top_k=top_k,
        skip=skip,
        sort_by_pages=sort_by_pages,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    query: str,
    keywords: list[str] | Unset = UNSET,
    resource_group_ids: list[UUID] | Unset = UNSET,
    top_k: int | Unset = 30,
    skip: int | Unset = 0,
    sort_by_pages: bool | Unset = False,
) -> Response[Any | ErrorOut]:
    """Search Ocr Page V5

     Wp_rJkTS

    Searching for OCR result from the given query and keywords.

    Logic:

        - If only query is provided, will perform vector search
            (Score is based on cosine similarity)

            PS. Current embedding model is Azure Text Embedding ADA002
            Will change to 003 - Large once re-embedding is done

        - If only keyword is provided, will perform exact search
            (Score is based on BM25)

        - If both query and keyword are provided, will perform hybrid search
            (Score is based on RRF - Reciprocal Rank Fusion)

    Results:
        # TBD

    Noted:
        if sort_by_pages is True, the list result will be sorted by (page number ascending, score
    descending)
        else, the list result will be sorted by (score descending, page number ascending)

    Args:
        project_id (UUID):
        query (str):
        keywords (list[str] | Unset):
        resource_group_ids (list[UUID] | Unset):
        top_k (int | Unset):  Default: 30.
        skip (int | Unset):  Default: 0.
        sort_by_pages (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        query=query,
        keywords=keywords,
        resource_group_ids=resource_group_ids,
        top_k=top_k,
        skip=skip,
        sort_by_pages=sort_by_pages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    query: str,
    keywords: list[str] | Unset = UNSET,
    resource_group_ids: list[UUID] | Unset = UNSET,
    top_k: int | Unset = 30,
    skip: int | Unset = 0,
    sort_by_pages: bool | Unset = False,
) -> Any | ErrorOut | None:
    """Search Ocr Page V5

     Wp_rJkTS

    Searching for OCR result from the given query and keywords.

    Logic:

        - If only query is provided, will perform vector search
            (Score is based on cosine similarity)

            PS. Current embedding model is Azure Text Embedding ADA002
            Will change to 003 - Large once re-embedding is done

        - If only keyword is provided, will perform exact search
            (Score is based on BM25)

        - If both query and keyword are provided, will perform hybrid search
            (Score is based on RRF - Reciprocal Rank Fusion)

    Results:
        # TBD

    Noted:
        if sort_by_pages is True, the list result will be sorted by (page number ascending, score
    descending)
        else, the list result will be sorted by (score descending, page number ascending)

    Args:
        project_id (UUID):
        query (str):
        keywords (list[str] | Unset):
        resource_group_ids (list[UUID] | Unset):
        top_k (int | Unset):  Default: 30.
        skip (int | Unset):  Default: 0.
        sort_by_pages (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorOut
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            query=query,
            keywords=keywords,
            resource_group_ids=resource_group_ids,
            top_k=top_k,
            skip=skip,
            sort_by_pages=sort_by_pages,
        )
    ).parsed
