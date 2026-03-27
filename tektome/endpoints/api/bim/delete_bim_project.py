from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    bim_project_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/core/resource-groups/bim/bim-project/{bim_project_id}/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[str]:
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
) -> Response[str]:
    """Delete a BIM project

     Delete a BIM project and all its associated elements. This is an asynchronous operation. To retrieve
    the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the task/process ID
    returned in this response.

    Args:
        bim_project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
) -> str | None:
    """Delete a BIM project

     Delete a BIM project and all its associated elements. This is an asynchronous operation. To retrieve
    the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the task/process ID
    returned in this response.

    Args:
        bim_project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[str]:
    """Delete a BIM project

     Delete a BIM project and all its associated elements. This is an asynchronous operation. To retrieve
    the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the task/process ID
    returned in this response.

    Args:
        bim_project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
) -> str | None:
    """Delete a BIM project

     Delete a BIM project and all its associated elements. This is an asynchronous operation. To retrieve
    the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the task/process ID
    returned in this response.

    Args:
        bim_project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            client=client,
        )
    ).parsed
