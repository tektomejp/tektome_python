from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_topology_search_post_out import BimTopologySearchPostOut
from ...models.bim_topology_search_sphere_post_in import BimTopologySearchSpherePostIn
from ...models.error_response_response import ErrorResponseResponse
from ...types import Response


def _get_kwargs(
    bim_project_id: UUID,
    *,
    body: BimTopologySearchSpherePostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-tools/topology-search/{bim_project_id}/sphere/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimTopologySearchPostOut | ErrorResponseResponse | None:
    if response.status_code == 200:
        response_200 = BimTopologySearchPostOut.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponseResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponseResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimTopologySearchPostOut | ErrorResponseResponse]:
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
    body: BimTopologySearchSpherePostIn,
) -> Response[BimTopologySearchPostOut | ErrorResponseResponse]:
    """Run BIM topology search with a sphere

     Find BIM objects located within a specified region from a set of provided BIM object IDs within a
    BIM project. If BIM object IDs are not provided, the search will be conducted over all BIM objects
    in the BIM project. Search using a spherical range around a point. This is an asynchronous
    operation. To retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint
    with the task/process ID returned in this response.

    Args:
        bim_project_id (UUID):
        body (BimTopologySearchSpherePostIn): Schema for BIM topology search with sphere request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimTopologySearchPostOut | ErrorResponseResponse]
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
    body: BimTopologySearchSpherePostIn,
) -> BimTopologySearchPostOut | ErrorResponseResponse | None:
    """Run BIM topology search with a sphere

     Find BIM objects located within a specified region from a set of provided BIM object IDs within a
    BIM project. If BIM object IDs are not provided, the search will be conducted over all BIM objects
    in the BIM project. Search using a spherical range around a point. This is an asynchronous
    operation. To retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint
    with the task/process ID returned in this response.

    Args:
        bim_project_id (UUID):
        body (BimTopologySearchSpherePostIn): Schema for BIM topology search with sphere request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimTopologySearchPostOut | ErrorResponseResponse
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
    body: BimTopologySearchSpherePostIn,
) -> Response[BimTopologySearchPostOut | ErrorResponseResponse]:
    """Run BIM topology search with a sphere

     Find BIM objects located within a specified region from a set of provided BIM object IDs within a
    BIM project. If BIM object IDs are not provided, the search will be conducted over all BIM objects
    in the BIM project. Search using a spherical range around a point. This is an asynchronous
    operation. To retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint
    with the task/process ID returned in this response.

    Args:
        bim_project_id (UUID):
        body (BimTopologySearchSpherePostIn): Schema for BIM topology search with sphere request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimTopologySearchPostOut | ErrorResponseResponse]
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
    body: BimTopologySearchSpherePostIn,
) -> BimTopologySearchPostOut | ErrorResponseResponse | None:
    """Run BIM topology search with a sphere

     Find BIM objects located within a specified region from a set of provided BIM object IDs within a
    BIM project. If BIM object IDs are not provided, the search will be conducted over all BIM objects
    in the BIM project. Search using a spherical range around a point. This is an asynchronous
    operation. To retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint
    with the task/process ID returned in this response.

    Args:
        bim_project_id (UUID):
        body (BimTopologySearchSpherePostIn): Schema for BIM topology search with sphere request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimTopologySearchPostOut | ErrorResponseResponse
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            client=client,
            body=body,
        )
    ).parsed
