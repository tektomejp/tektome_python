from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    batch_size: int | Unset = 1000,
    max_workers: int | Unset = 8,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["batch_size"] = batch_size

    params["max_workers"] = max_workers

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/core/resource-groups/bim/bim-object/orphaned/",
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
    *,
    client: AuthenticatedClient,
    batch_size: int | Unset = 1000,
    max_workers: int | Unset = 8,
) -> Response[Any]:
    """Delete orphaned BIM objects

     Delete all BIM objects that are not linked to any project. This is an asynchronous operation. To
    retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the
    task/process ID returned in this response.

    Args:
        batch_size (int | Unset):  Default: 1000.
        max_workers (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        batch_size=batch_size,
        max_workers=max_workers,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    batch_size: int | Unset = 1000,
    max_workers: int | Unset = 8,
) -> Response[Any]:
    """Delete orphaned BIM objects

     Delete all BIM objects that are not linked to any project. This is an asynchronous operation. To
    retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the
    task/process ID returned in this response.

    Args:
        batch_size (int | Unset):  Default: 1000.
        max_workers (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        batch_size=batch_size,
        max_workers=max_workers,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
