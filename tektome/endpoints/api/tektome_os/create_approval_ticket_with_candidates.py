from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.approval_ticket_get_out import ApprovalTicketGetOut
from ...models.create_approval_ticket_with_candidates_multi_part_body_params import (
    CreateApprovalTicketWithCandidatesMultiPartBodyParams,
)
from ...types import Response


def _get_kwargs(
    execution_id: UUID,
    *,
    body: CreateApprovalTicketWithCandidatesMultiPartBodyParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/agents/os/executions/{execution_id}/approvals/".format(
            execution_id=quote(str(execution_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApprovalTicketGetOut | None:
    if response.status_code == 201:
        response_201 = ApprovalTicketGetOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApprovalTicketGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateApprovalTicketWithCandidatesMultiPartBodyParams,
) -> Response[ApprovalTicketGetOut]:
    """Post Approval Ticket

     Dx_aYOR8

    Create an approval ticket for the given execution.

    Args:
        file: Optional file upload, when new resource got generated for approval
        request: Request object
        payload: Approval ticket payload
        path_params: Path parameters containing execution_id

    Returns: 201 Created with the created ApprovalTicket containing updated candidates

    Args:
        execution_id (UUID):
        body (CreateApprovalTicketWithCandidatesMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApprovalTicketGetOut]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateApprovalTicketWithCandidatesMultiPartBodyParams,
) -> ApprovalTicketGetOut | None:
    """Post Approval Ticket

     Dx_aYOR8

    Create an approval ticket for the given execution.

    Args:
        file: Optional file upload, when new resource got generated for approval
        request: Request object
        payload: Approval ticket payload
        path_params: Path parameters containing execution_id

    Returns: 201 Created with the created ApprovalTicket containing updated candidates

    Args:
        execution_id (UUID):
        body (CreateApprovalTicketWithCandidatesMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApprovalTicketGetOut
    """

    return sync_detailed(
        execution_id=execution_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateApprovalTicketWithCandidatesMultiPartBodyParams,
) -> Response[ApprovalTicketGetOut]:
    """Post Approval Ticket

     Dx_aYOR8

    Create an approval ticket for the given execution.

    Args:
        file: Optional file upload, when new resource got generated for approval
        request: Request object
        payload: Approval ticket payload
        path_params: Path parameters containing execution_id

    Returns: 201 Created with the created ApprovalTicket containing updated candidates

    Args:
        execution_id (UUID):
        body (CreateApprovalTicketWithCandidatesMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApprovalTicketGetOut]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateApprovalTicketWithCandidatesMultiPartBodyParams,
) -> ApprovalTicketGetOut | None:
    """Post Approval Ticket

     Dx_aYOR8

    Create an approval ticket for the given execution.

    Args:
        file: Optional file upload, when new resource got generated for approval
        request: Request object
        payload: Approval ticket payload
        path_params: Path parameters containing execution_id

    Returns: 201 Created with the created ApprovalTicket containing updated candidates

    Args:
        execution_id (UUID):
        body (CreateApprovalTicketWithCandidatesMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApprovalTicketGetOut
    """

    return (
        await asyncio_detailed(
            execution_id=execution_id,
            client=client,
            body=body,
        )
    ).parsed
