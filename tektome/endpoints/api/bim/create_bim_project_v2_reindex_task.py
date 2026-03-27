from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_project_v2_index_task_response import BimProjectV2IndexTaskResponse
from ...models.error_response_out import ErrorResponseOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bim_project_id: UUID,
    *,
    batch_size: int | Unset = 500,
    concurrency: int | Unset = 1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["batch_size"] = batch_size

    params["concurrency"] = concurrency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-project/{bim_project_id}/index-v2/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimProjectV2IndexTaskResponse | ErrorResponseOut | None:
    if response.status_code == 200:
        response_200 = BimProjectV2IndexTaskResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponseOut.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponseOut.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = ErrorResponseOut.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimProjectV2IndexTaskResponse | ErrorResponseOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    batch_size: int | Unset = 500,
    concurrency: int | Unset = 1,
) -> Response[BimProjectV2IndexTaskResponse | ErrorResponseOut]:
    """Start BIM project V2 reindex

     Trigger asynchronous V2 Elasticsearch reindexing for all BIM objects, views, and sheets in the
    specified BIM project. This endpoint is project-scoped and concurrency-safe: if an indexing task is
    already running for the same BIM project, the existing process ID is returned instead of scheduling
    a duplicate task. To retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/)
    endpoint with the task/process ID returned in this response.

    Args:
        bim_project_id (UUID):
        batch_size (int | Unset): Batch size for chunked indexing. Must be between 1 and 500.
            Default: 500.
        concurrency (int | Unset): Number of batches to process in parallel. Must be at least 1.
            Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimProjectV2IndexTaskResponse | ErrorResponseOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        batch_size=batch_size,
        concurrency=concurrency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    batch_size: int | Unset = 500,
    concurrency: int | Unset = 1,
) -> BimProjectV2IndexTaskResponse | ErrorResponseOut | None:
    """Start BIM project V2 reindex

     Trigger asynchronous V2 Elasticsearch reindexing for all BIM objects, views, and sheets in the
    specified BIM project. This endpoint is project-scoped and concurrency-safe: if an indexing task is
    already running for the same BIM project, the existing process ID is returned instead of scheduling
    a duplicate task. To retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/)
    endpoint with the task/process ID returned in this response.

    Args:
        bim_project_id (UUID):
        batch_size (int | Unset): Batch size for chunked indexing. Must be between 1 and 500.
            Default: 500.
        concurrency (int | Unset): Number of batches to process in parallel. Must be at least 1.
            Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimProjectV2IndexTaskResponse | ErrorResponseOut
    """

    return sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
        batch_size=batch_size,
        concurrency=concurrency,
    ).parsed


async def asyncio_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    batch_size: int | Unset = 500,
    concurrency: int | Unset = 1,
) -> Response[BimProjectV2IndexTaskResponse | ErrorResponseOut]:
    """Start BIM project V2 reindex

     Trigger asynchronous V2 Elasticsearch reindexing for all BIM objects, views, and sheets in the
    specified BIM project. This endpoint is project-scoped and concurrency-safe: if an indexing task is
    already running for the same BIM project, the existing process ID is returned instead of scheduling
    a duplicate task. To retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/)
    endpoint with the task/process ID returned in this response.

    Args:
        bim_project_id (UUID):
        batch_size (int | Unset): Batch size for chunked indexing. Must be between 1 and 500.
            Default: 500.
        concurrency (int | Unset): Number of batches to process in parallel. Must be at least 1.
            Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimProjectV2IndexTaskResponse | ErrorResponseOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        batch_size=batch_size,
        concurrency=concurrency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    batch_size: int | Unset = 500,
    concurrency: int | Unset = 1,
) -> BimProjectV2IndexTaskResponse | ErrorResponseOut | None:
    """Start BIM project V2 reindex

     Trigger asynchronous V2 Elasticsearch reindexing for all BIM objects, views, and sheets in the
    specified BIM project. This endpoint is project-scoped and concurrency-safe: if an indexing task is
    already running for the same BIM project, the existing process ID is returned instead of scheduling
    a duplicate task. To retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/)
    endpoint with the task/process ID returned in this response.

    Args:
        bim_project_id (UUID):
        batch_size (int | Unset): Batch size for chunked indexing. Must be between 1 and 500.
            Default: 500.
        concurrency (int | Unset): Number of batches to process in parallel. Must be at least 1.
            Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimProjectV2IndexTaskResponse | ErrorResponseOut
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            client=client,
            batch_size=batch_size,
            concurrency=concurrency,
        )
    ).parsed
