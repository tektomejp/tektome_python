from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_clash_check_response import BimClashCheckResponse
from ...models.create_bim_clash_check_request import CreateBimClashCheckRequest
from ...models.error_response_post_out import ErrorResponsePostOut
from ...types import Response


def _get_kwargs(
    bim_project_id: UUID,
    *,
    body: CreateBimClashCheckRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-tools/clash-check/{bim_project_id}/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimClashCheckResponse | ErrorResponsePostOut | None:
    if response.status_code == 200:
        response_200 = BimClashCheckResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponsePostOut.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponsePostOut.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimClashCheckResponse | ErrorResponsePostOut]:
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
    body: CreateBimClashCheckRequest,
) -> Response[BimClashCheckResponse | ErrorResponsePostOut]:
    """Run BIM clash detection

     Perform clash detection on the provided BIM object IDs within a BIM project. This is an asynchronous
    operation. To retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint
    with the task/process ID returned in this response.

    Args:
        bim_project_id (UUID):
        body (CreateBimClashCheckRequest): Schema for BIM clash check request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimClashCheckResponse | ErrorResponsePostOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateBimClashCheckRequest,
) -> BimClashCheckResponse | ErrorResponsePostOut | None:
    """Run BIM clash detection

     Perform clash detection on the provided BIM object IDs within a BIM project. This is an asynchronous
    operation. To retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint
    with the task/process ID returned in this response.

    Args:
        bim_project_id (UUID):
        body (CreateBimClashCheckRequest): Schema for BIM clash check request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimClashCheckResponse | ErrorResponsePostOut
    """

    return sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateBimClashCheckRequest,
) -> Response[BimClashCheckResponse | ErrorResponsePostOut]:
    """Run BIM clash detection

     Perform clash detection on the provided BIM object IDs within a BIM project. This is an asynchronous
    operation. To retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint
    with the task/process ID returned in this response.

    Args:
        bim_project_id (UUID):
        body (CreateBimClashCheckRequest): Schema for BIM clash check request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimClashCheckResponse | ErrorResponsePostOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateBimClashCheckRequest,
) -> BimClashCheckResponse | ErrorResponsePostOut | None:
    """Run BIM clash detection

     Perform clash detection on the provided BIM object IDs within a BIM project. This is an asynchronous
    operation. To retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint
    with the task/process ID returned in this response.

    Args:
        bim_project_id (UUID):
        body (CreateBimClashCheckRequest): Schema for BIM clash check request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimClashCheckResponse | ErrorResponsePostOut
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            client=client,
            body=body,
        )
    ).parsed
