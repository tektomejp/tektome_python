from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_task_response import BimTaskResponse
from ...types import Response


def _get_kwargs(
    bim_task_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/bim/bim-tasks/{bim_task_id}/".format(
            bim_task_id=quote(str(bim_task_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BimTaskResponse | None:
    if response.status_code == 200:
        response_200 = BimTaskResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BimTaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_task_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[BimTaskResponse]:
    """Get BIM task status

     Retrieve the current status and full details of a BIM task by its DB ID. The task ID is returned by
    endpoints that create BIM tasks, such as the V2 reindex endpoint. The status field reflects the
    processing state: PENDING, PROCESSING, COMPLETED, or FAILED.

    Args:
        bim_task_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimTaskResponse]
    """

    kwargs = _get_kwargs(
        bim_task_id=bim_task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_task_id: UUID,
    *,
    client: AuthenticatedClient,
) -> BimTaskResponse | None:
    """Get BIM task status

     Retrieve the current status and full details of a BIM task by its DB ID. The task ID is returned by
    endpoints that create BIM tasks, such as the V2 reindex endpoint. The status field reflects the
    processing state: PENDING, PROCESSING, COMPLETED, or FAILED.

    Args:
        bim_task_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimTaskResponse
    """

    return sync_detailed(
        bim_task_id=bim_task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bim_task_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[BimTaskResponse]:
    """Get BIM task status

     Retrieve the current status and full details of a BIM task by its DB ID. The task ID is returned by
    endpoints that create BIM tasks, such as the V2 reindex endpoint. The status field reflects the
    processing state: PENDING, PROCESSING, COMPLETED, or FAILED.

    Args:
        bim_task_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimTaskResponse]
    """

    kwargs = _get_kwargs(
        bim_task_id=bim_task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_task_id: UUID,
    *,
    client: AuthenticatedClient,
) -> BimTaskResponse | None:
    """Get BIM task status

     Retrieve the current status and full details of a BIM task by its DB ID. The task ID is returned by
    endpoints that create BIM tasks, such as the V2 reindex endpoint. The status field reflects the
    processing state: PENDING, PROCESSING, COMPLETED, or FAILED.

    Args:
        bim_task_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimTaskResponse
    """

    return (
        await asyncio_detailed(
            bim_task_id=bim_task_id,
            client=client,
        )
    ).parsed
