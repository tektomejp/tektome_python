from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.applawtalk_routes_projects_search_ocr_page_v3_azure_embedding_model import (
    ApplawtalkRoutesProjectsSearchOcrPageV3AzureEmbeddingModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    *,
    embedding_model: ApplawtalkRoutesProjectsSearchOcrPageV3AzureEmbeddingModel,
    query: None | str | Unset = UNSET,
    keyword: None | str | Unset = UNSET,
    top_k: int | Unset = 10,
    sort_by_pages: bool | Unset = False,
    vector_project: None | str | Unset = UNSET,
    vector_data_space: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_embedding_model = embedding_model.value
    params["embedding_model"] = json_embedding_model

    json_query: None | str | Unset
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    json_keyword: None | str | Unset
    if isinstance(keyword, Unset):
        json_keyword = UNSET
    else:
        json_keyword = keyword
    params["keyword"] = json_keyword

    params["top_k"] = top_k

    params["sort_by_pages"] = sort_by_pages

    json_vector_project: None | str | Unset
    if isinstance(vector_project, Unset):
        json_vector_project = UNSET
    else:
        json_vector_project = vector_project
    params["vector_project"] = json_vector_project

    json_vector_data_space: None | str | Unset
    if isinstance(vector_data_space, Unset):
        json_vector_data_space = UNSET
    else:
        json_vector_data_space = vector_data_space
    params["vector_data_space"] = json_vector_data_space

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/projects/{project_id}/search-ocr-page/v3/".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

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
    embedding_model: ApplawtalkRoutesProjectsSearchOcrPageV3AzureEmbeddingModel,
    query: None | str | Unset = UNSET,
    keyword: None | str | Unset = UNSET,
    top_k: int | Unset = 10,
    sort_by_pages: bool | Unset = False,
    vector_project: None | str | Unset = UNSET,
    vector_data_space: None | str | Unset = UNSET,
) -> Response[Any]:
    """Search Ocr Page V3

     rMqXpEPr

    Search pages in a given resources on specific keywords and/or query
    - also returns original tektome response

    Args:
        project_id (UUID):
        embedding_model (ApplawtalkRoutesProjectsSearchOcrPageV3AzureEmbeddingModel): List of
            available embedding models which compatible with litellm

            the exahustive list of models can be found at https://models.litellm.ai/
        query (None | str | Unset):
        keyword (None | str | Unset):
        top_k (int | Unset):  Default: 10.
        sort_by_pages (bool | Unset):  Default: False.
        vector_project (None | str | Unset):
        vector_data_space (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        embedding_model=embedding_model,
        query=query,
        keyword=keyword,
        top_k=top_k,
        sort_by_pages=sort_by_pages,
        vector_project=vector_project,
        vector_data_space=vector_data_space,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    embedding_model: ApplawtalkRoutesProjectsSearchOcrPageV3AzureEmbeddingModel,
    query: None | str | Unset = UNSET,
    keyword: None | str | Unset = UNSET,
    top_k: int | Unset = 10,
    sort_by_pages: bool | Unset = False,
    vector_project: None | str | Unset = UNSET,
    vector_data_space: None | str | Unset = UNSET,
) -> Response[Any]:
    """Search Ocr Page V3

     rMqXpEPr

    Search pages in a given resources on specific keywords and/or query
    - also returns original tektome response

    Args:
        project_id (UUID):
        embedding_model (ApplawtalkRoutesProjectsSearchOcrPageV3AzureEmbeddingModel): List of
            available embedding models which compatible with litellm

            the exahustive list of models can be found at https://models.litellm.ai/
        query (None | str | Unset):
        keyword (None | str | Unset):
        top_k (int | Unset):  Default: 10.
        sort_by_pages (bool | Unset):  Default: False.
        vector_project (None | str | Unset):
        vector_data_space (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        embedding_model=embedding_model,
        query=query,
        keyword=keyword,
        top_k=top_k,
        sort_by_pages=sort_by_pages,
        vector_project=vector_project,
        vector_data_space=vector_data_space,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
