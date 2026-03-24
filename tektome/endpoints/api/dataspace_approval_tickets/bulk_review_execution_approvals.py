from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.scoped_bulk_review_post_in import ScopedBulkReviewPostIn
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    execution_id: UUID,
    *,
    body: ScopedBulkReviewPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/executions/{execution_id}/approvals/bulk-review/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            execution_id=quote(str(execution_id), safe=""),
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
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ScopedBulkReviewPostIn,
) -> Response[Any]:
    """Bulk review approvals in execution

     Approve or reject all pending approval tickets within a specific execution.

    Args:
        dataspace_id (UUID):
        execution_id (UUID): The UUID of the execution to cancel
        body (ScopedBulkReviewPostIn): Scoped bulk review input for reviewing all pending tickets
            in a scope

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        execution_id=execution_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    dataspace_id: UUID,
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ScopedBulkReviewPostIn,
) -> Response[Any]:
    """Bulk review approvals in execution

     Approve or reject all pending approval tickets within a specific execution.

    Args:
        dataspace_id (UUID):
        execution_id (UUID): The UUID of the execution to cancel
        body (ScopedBulkReviewPostIn): Scoped bulk review input for reviewing all pending tickets
            in a scope

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        execution_id=execution_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
