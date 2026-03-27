from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_project_v2_index_status_response import BimProjectV2IndexStatusResponse
from ...models.error_response_out import ErrorResponseOut
from ...types import Response


def _get_kwargs(
    bim_project_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/bim/bim-project/{bim_project_id}/index-v2/status/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimProjectV2IndexStatusResponse | ErrorResponseOut | None:
    if response.status_code == 200:
        response_200 = BimProjectV2IndexStatusResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponseOut.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponseOut.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimProjectV2IndexStatusResponse | ErrorResponseOut]:
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
) -> Response[BimProjectV2IndexStatusResponse | ErrorResponseOut]:
    """Get BIM project V2 index status

     Query Elasticsearch V2 indices to retrieve the count of indexed BIM objects, views, and sheets for
    the specified BIM project. Only parent documents are counted (text-chunk child documents are
    excluded). Use this endpoint to verify whether a BIM project has been fully indexed after triggering
    a V2 reindex task.

    Args:
        bim_project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimProjectV2IndexStatusResponse | ErrorResponseOut]
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
) -> BimProjectV2IndexStatusResponse | ErrorResponseOut | None:
    """Get BIM project V2 index status

     Query Elasticsearch V2 indices to retrieve the count of indexed BIM objects, views, and sheets for
    the specified BIM project. Only parent documents are counted (text-chunk child documents are
    excluded). Use this endpoint to verify whether a BIM project has been fully indexed after triggering
    a V2 reindex task.

    Args:
        bim_project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimProjectV2IndexStatusResponse | ErrorResponseOut
    """

    return sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[BimProjectV2IndexStatusResponse | ErrorResponseOut]:
    """Get BIM project V2 index status

     Query Elasticsearch V2 indices to retrieve the count of indexed BIM objects, views, and sheets for
    the specified BIM project. Only parent documents are counted (text-chunk child documents are
    excluded). Use this endpoint to verify whether a BIM project has been fully indexed after triggering
    a V2 reindex task.

    Args:
        bim_project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimProjectV2IndexStatusResponse | ErrorResponseOut]
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
) -> BimProjectV2IndexStatusResponse | ErrorResponseOut | None:
    """Get BIM project V2 index status

     Query Elasticsearch V2 indices to retrieve the count of indexed BIM objects, views, and sheets for
    the specified BIM project. Only parent documents are counted (text-chunk child documents are
    excluded). Use this endpoint to verify whether a BIM project has been fully indexed after triggering
    a V2 reindex task.

    Args:
        bim_project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimProjectV2IndexStatusResponse | ErrorResponseOut
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            client=client,
        )
    ).parsed
