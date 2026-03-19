from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.approval_ticket_response import ApprovalTicketResponse
from ...models.create_execution_approval_ticket_with_candidates_multi_part_body_params import (
    CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams,
)
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    execution_id: UUID,
    *,
    body: CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/executions/{execution_id}/approvals/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            execution_id=quote(str(execution_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApprovalTicketResponse | None:
    if response.status_code == 201:
        response_201 = ApprovalTicketResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApprovalTicketResponse]:
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
    body: CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams,
) -> Response[ApprovalTicketResponse]:
    """Create an approval ticket for an execution

     Create an approval ticket with candidates for the specified execution. If a file is provided, it is
    uploaded for history tracking. Auto-approve settings are applied when configured.

    Args:
        dataspace_id (UUID):
        execution_id (UUID):
        body (CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApprovalTicketResponse]
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


def sync(
    dataspace_id: UUID,
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams,
) -> ApprovalTicketResponse | None:
    """Create an approval ticket for an execution

     Create an approval ticket with candidates for the specified execution. If a file is provided, it is
    uploaded for history tracking. Auto-approve settings are applied when configured.

    Args:
        dataspace_id (UUID):
        execution_id (UUID):
        body (CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApprovalTicketResponse
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        execution_id=execution_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams,
) -> Response[ApprovalTicketResponse]:
    """Create an approval ticket for an execution

     Create an approval ticket with candidates for the specified execution. If a file is provided, it is
    uploaded for history tracking. Auto-approve settings are applied when configured.

    Args:
        dataspace_id (UUID):
        execution_id (UUID):
        body (CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApprovalTicketResponse]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        execution_id=execution_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams,
) -> ApprovalTicketResponse | None:
    """Create an approval ticket for an execution

     Create an approval ticket with candidates for the specified execution. If a file is provided, it is
    uploaded for history tracking. Auto-approve settings are applied when configured.

    Args:
        dataspace_id (UUID):
        execution_id (UUID):
        body (CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApprovalTicketResponse
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            execution_id=execution_id,
            client=client,
            body=body,
        )
    ).parsed
