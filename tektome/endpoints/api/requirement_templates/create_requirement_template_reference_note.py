from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_requirement_template_reference_note_request import CreateRequirementTemplateReferenceNoteRequest
from ...models.requirement_template_reference_note_response import RequirementTemplateReferenceNoteResponse
from ...types import Response


def _get_kwargs(
    requirement_template_id: UUID,
    *,
    body: CreateRequirementTemplateReferenceNoteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/requirement-templates/{requirement_template_id}/reference-note-templates/".format(
            requirement_template_id=quote(str(requirement_template_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RequirementTemplateReferenceNoteResponse | None:
    if response.status_code == 201:
        response_201 = RequirementTemplateReferenceNoteResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RequirementTemplateReferenceNoteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateRequirementTemplateReferenceNoteRequest,
) -> Response[RequirementTemplateReferenceNoteResponse]:
    """Create a reference note template

     Create a new reference note template associated with a requirement template. Reference note
    templates define reusable note structures for requirements.

    Args:
        requirement_template_id (UUID):
        body (CreateRequirementTemplateReferenceNoteRequest): Serializer for Requirement Template
            Reference Note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementTemplateReferenceNoteResponse]
    """

    kwargs = _get_kwargs(
        requirement_template_id=requirement_template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateRequirementTemplateReferenceNoteRequest,
) -> RequirementTemplateReferenceNoteResponse | None:
    """Create a reference note template

     Create a new reference note template associated with a requirement template. Reference note
    templates define reusable note structures for requirements.

    Args:
        requirement_template_id (UUID):
        body (CreateRequirementTemplateReferenceNoteRequest): Serializer for Requirement Template
            Reference Note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementTemplateReferenceNoteResponse
    """

    return sync_detailed(
        requirement_template_id=requirement_template_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateRequirementTemplateReferenceNoteRequest,
) -> Response[RequirementTemplateReferenceNoteResponse]:
    """Create a reference note template

     Create a new reference note template associated with a requirement template. Reference note
    templates define reusable note structures for requirements.

    Args:
        requirement_template_id (UUID):
        body (CreateRequirementTemplateReferenceNoteRequest): Serializer for Requirement Template
            Reference Note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementTemplateReferenceNoteResponse]
    """

    kwargs = _get_kwargs(
        requirement_template_id=requirement_template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateRequirementTemplateReferenceNoteRequest,
) -> RequirementTemplateReferenceNoteResponse | None:
    """Create a reference note template

     Create a new reference note template associated with a requirement template. Reference note
    templates define reusable note structures for requirements.

    Args:
        requirement_template_id (UUID):
        body (CreateRequirementTemplateReferenceNoteRequest): Serializer for Requirement Template
            Reference Note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementTemplateReferenceNoteResponse
    """

    return (
        await asyncio_detailed(
            requirement_template_id=requirement_template_id,
            client=client,
            body=body,
        )
    ).parsed
