from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.approval_ticket_candidate_patch_out import ApprovalTicketCandidatePatchOut
from ...models.candidate_select_post_in import CandidateSelectPostIn
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    approval_id: UUID,
    candidate_id: UUID,
    *,
    body: CandidateSelectPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/approvals/{approval_id}/candidates/{candidate_id}/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            approval_id=quote(str(approval_id), safe=""),
            candidate_id=quote(str(candidate_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApprovalTicketCandidatePatchOut | None:
    if response.status_code == 200:
        response_200 = ApprovalTicketCandidatePatchOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApprovalTicketCandidatePatchOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    approval_id: UUID,
    candidate_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CandidateSelectPostIn,
) -> Response[ApprovalTicketCandidatePatchOut]:
    """Select or unselect a candidate

     Select or unselect a candidate variation on an approval ticket. Selecting a candidate auto-unselects
    all other candidates on the same ticket.

    Args:
        dataspace_id (UUID):
        approval_id (UUID):
        candidate_id (UUID):
        body (CandidateSelectPostIn): Serializer for selecting/unselecting a candidate variation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApprovalTicketCandidatePatchOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        approval_id=approval_id,
        candidate_id=candidate_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    approval_id: UUID,
    candidate_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CandidateSelectPostIn,
) -> ApprovalTicketCandidatePatchOut | None:
    """Select or unselect a candidate

     Select or unselect a candidate variation on an approval ticket. Selecting a candidate auto-unselects
    all other candidates on the same ticket.

    Args:
        dataspace_id (UUID):
        approval_id (UUID):
        candidate_id (UUID):
        body (CandidateSelectPostIn): Serializer for selecting/unselecting a candidate variation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApprovalTicketCandidatePatchOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        approval_id=approval_id,
        candidate_id=candidate_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    approval_id: UUID,
    candidate_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CandidateSelectPostIn,
) -> Response[ApprovalTicketCandidatePatchOut]:
    """Select or unselect a candidate

     Select or unselect a candidate variation on an approval ticket. Selecting a candidate auto-unselects
    all other candidates on the same ticket.

    Args:
        dataspace_id (UUID):
        approval_id (UUID):
        candidate_id (UUID):
        body (CandidateSelectPostIn): Serializer for selecting/unselecting a candidate variation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApprovalTicketCandidatePatchOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        approval_id=approval_id,
        candidate_id=candidate_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    approval_id: UUID,
    candidate_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CandidateSelectPostIn,
) -> ApprovalTicketCandidatePatchOut | None:
    """Select or unselect a candidate

     Select or unselect a candidate variation on an approval ticket. Selecting a candidate auto-unselects
    all other candidates on the same ticket.

    Args:
        dataspace_id (UUID):
        approval_id (UUID):
        candidate_id (UUID):
        body (CandidateSelectPostIn): Serializer for selecting/unselecting a candidate variation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApprovalTicketCandidatePatchOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            approval_id=approval_id,
            candidate_id=candidate_id,
            client=client,
            body=body,
        )
    ).parsed
