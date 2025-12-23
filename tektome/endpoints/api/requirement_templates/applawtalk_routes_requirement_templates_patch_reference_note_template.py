from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.requirement_template_reference_note_get_out import RequirementTemplateReferenceNoteGetOut
from ...models.requirement_template_reference_note_post_in_patch import RequirementTemplateReferenceNotePostInPatch
from ...types import Response


def _get_kwargs(
    reference_note_template_id: UUID,
    *,
    body: RequirementTemplateReferenceNotePostInPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/app/lawtalk/requirement-templates/reference-note-templates/{reference_note_template_id}/".format(
            reference_note_template_id=quote(str(reference_note_template_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RequirementTemplateReferenceNoteGetOut | None:
    if response.status_code == 200:
        response_200 = RequirementTemplateReferenceNoteGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RequirementTemplateReferenceNoteGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reference_note_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementTemplateReferenceNotePostInPatch,
) -> Response[RequirementTemplateReferenceNoteGetOut]:
    """Patch Reference Note Template

     OWvaVaLB

    Update a requirement template container by its ID.

    Args:
        reference_note_template_id (UUID):
        body (RequirementTemplateReferenceNotePostInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementTemplateReferenceNoteGetOut]
    """

    kwargs = _get_kwargs(
        reference_note_template_id=reference_note_template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reference_note_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementTemplateReferenceNotePostInPatch,
) -> RequirementTemplateReferenceNoteGetOut | None:
    """Patch Reference Note Template

     OWvaVaLB

    Update a requirement template container by its ID.

    Args:
        reference_note_template_id (UUID):
        body (RequirementTemplateReferenceNotePostInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementTemplateReferenceNoteGetOut
    """

    return sync_detailed(
        reference_note_template_id=reference_note_template_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    reference_note_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementTemplateReferenceNotePostInPatch,
) -> Response[RequirementTemplateReferenceNoteGetOut]:
    """Patch Reference Note Template

     OWvaVaLB

    Update a requirement template container by its ID.

    Args:
        reference_note_template_id (UUID):
        body (RequirementTemplateReferenceNotePostInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementTemplateReferenceNoteGetOut]
    """

    kwargs = _get_kwargs(
        reference_note_template_id=reference_note_template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reference_note_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementTemplateReferenceNotePostInPatch,
) -> RequirementTemplateReferenceNoteGetOut | None:
    """Patch Reference Note Template

     OWvaVaLB

    Update a requirement template container by its ID.

    Args:
        reference_note_template_id (UUID):
        body (RequirementTemplateReferenceNotePostInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementTemplateReferenceNoteGetOut
    """

    return (
        await asyncio_detailed(
            reference_note_template_id=reference_note_template_id,
            client=client,
            body=body,
        )
    ).parsed
