from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_review_post_in import BulkReviewPostIn
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    *,
    body: BulkReviewPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/approvals/bulk-review/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
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
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BulkReviewPostIn,
) -> Response[Any]:
    """Post Bulk Review

     lXJK83hc

    Perform bulk review (approve or reject) of approval tickets.
    Approved tickets will trigger further processing.

    Args:
        path_params: DataspaceSchema containing dataspace ID.
        request: The incoming HTTP request.
        payload: BulkReviewPostIn containing approval IDs and action.

    Returns: 204, None

    Args:
        dataspace_id (UUID):
        body (BulkReviewPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BulkReviewPostIn,
) -> Response[Any]:
    """Post Bulk Review

     lXJK83hc

    Perform bulk review (approve or reject) of approval tickets.
    Approved tickets will trigger further processing.

    Args:
        path_params: DataspaceSchema containing dataspace ID.
        request: The incoming HTTP request.
        payload: BulkReviewPostIn containing approval IDs and action.

    Returns: 204, None

    Args:
        dataspace_id (UUID):
        body (BulkReviewPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
