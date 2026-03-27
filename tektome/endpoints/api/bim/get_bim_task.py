from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_task_response import BimTaskResponse
from ...models.error_response_out import ErrorResponseOut
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


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimTaskResponse | ErrorResponseOut | None:
    if response.status_code == 200:
        response_200 = BimTaskResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponseOut.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponseOut.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponseOut.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponseOut.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponseOut.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = ErrorResponseOut.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = ErrorResponseOut.from_dict(response.json())

        return response_406

    if response.status_code == 407:
        response_407 = ErrorResponseOut.from_dict(response.json())

        return response_407

    if response.status_code == 408:
        response_408 = ErrorResponseOut.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = ErrorResponseOut.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponseOut.from_dict(response.json())

        return response_410

    if response.status_code == 411:
        response_411 = ErrorResponseOut.from_dict(response.json())

        return response_411

    if response.status_code == 412:
        response_412 = ErrorResponseOut.from_dict(response.json())

        return response_412

    if response.status_code == 416:
        response_416 = ErrorResponseOut.from_dict(response.json())

        return response_416

    if response.status_code == 418:
        response_418 = ErrorResponseOut.from_dict(response.json())

        return response_418

    if response.status_code == 425:
        response_425 = ErrorResponseOut.from_dict(response.json())

        return response_425

    if response.status_code == 429:
        response_429 = ErrorResponseOut.from_dict(response.json())

        return response_429

    if response.status_code == 451:
        response_451 = ErrorResponseOut.from_dict(response.json())

        return response_451

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimTaskResponse | ErrorResponseOut]:
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
) -> Response[BimTaskResponse | ErrorResponseOut]:
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
        Response[BimTaskResponse | ErrorResponseOut]
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
) -> BimTaskResponse | ErrorResponseOut | None:
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
        BimTaskResponse | ErrorResponseOut
    """

    return sync_detailed(
        bim_task_id=bim_task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bim_task_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[BimTaskResponse | ErrorResponseOut]:
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
        Response[BimTaskResponse | ErrorResponseOut]
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
) -> BimTaskResponse | ErrorResponseOut | None:
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
        BimTaskResponse | ErrorResponseOut
    """

    return (
        await asyncio_detailed(
            bim_task_id=bim_task_id,
            client=client,
        )
    ).parsed
