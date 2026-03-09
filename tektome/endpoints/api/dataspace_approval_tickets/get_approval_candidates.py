from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paged_approval_ticket_candidate_out import PagedApprovalTicketCandidateOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataspace_id: UUID,
    approval_id: UUID,
    *,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    json_page_size: int | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["page_size"] = json_page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/dataspaces/{dataspace_id}/approvals/{approval_id}/candidates/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            approval_id=quote(str(approval_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PagedApprovalTicketCandidateOut | None:
    if response.status_code == 200:
        response_200 = PagedApprovalTicketCandidateOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PagedApprovalTicketCandidateOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    approval_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedApprovalTicketCandidateOut]:
    """Get Approval Candidates

     e8eqlFo9

    Retrieve the list of candidates associated with a specific approval ticket.

    Serializes data snapshots for each candidate based on their instructions.
        - If a data snapshot already exists, it uses that.
        - If the ticket is pending and no snapshot exists, it generates one based on instructions.

    Args:
        request: The incoming HTTP request.
        path_params: The path parameters containing the approval ticket ID.

    Returns: A list of ApprovalTicketCandidate instances associated with the approval ticket.

    Args:
        dataspace_id (UUID):
        approval_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedApprovalTicketCandidateOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        approval_id=approval_id,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    approval_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedApprovalTicketCandidateOut | None:
    """Get Approval Candidates

     e8eqlFo9

    Retrieve the list of candidates associated with a specific approval ticket.

    Serializes data snapshots for each candidate based on their instructions.
        - If a data snapshot already exists, it uses that.
        - If the ticket is pending and no snapshot exists, it generates one based on instructions.

    Args:
        request: The incoming HTTP request.
        path_params: The path parameters containing the approval ticket ID.

    Returns: A list of ApprovalTicketCandidate instances associated with the approval ticket.

    Args:
        dataspace_id (UUID):
        approval_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedApprovalTicketCandidateOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        approval_id=approval_id,
        client=client,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    approval_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedApprovalTicketCandidateOut]:
    """Get Approval Candidates

     e8eqlFo9

    Retrieve the list of candidates associated with a specific approval ticket.

    Serializes data snapshots for each candidate based on their instructions.
        - If a data snapshot already exists, it uses that.
        - If the ticket is pending and no snapshot exists, it generates one based on instructions.

    Args:
        request: The incoming HTTP request.
        path_params: The path parameters containing the approval ticket ID.

    Returns: A list of ApprovalTicketCandidate instances associated with the approval ticket.

    Args:
        dataspace_id (UUID):
        approval_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedApprovalTicketCandidateOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        approval_id=approval_id,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    approval_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedApprovalTicketCandidateOut | None:
    """Get Approval Candidates

     e8eqlFo9

    Retrieve the list of candidates associated with a specific approval ticket.

    Serializes data snapshots for each candidate based on their instructions.
        - If a data snapshot already exists, it uses that.
        - If the ticket is pending and no snapshot exists, it generates one based on instructions.

    Args:
        request: The incoming HTTP request.
        path_params: The path parameters containing the approval ticket ID.

    Returns: A list of ApprovalTicketCandidate instances associated with the approval ticket.

    Args:
        dataspace_id (UUID):
        approval_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedApprovalTicketCandidateOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            approval_id=approval_id,
            client=client,
            page=page,
            page_size=page_size,
        )
    ).parsed
