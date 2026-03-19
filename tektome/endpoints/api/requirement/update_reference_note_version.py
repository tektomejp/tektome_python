from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reference_note_version_response import ReferenceNoteVersionResponse
from ...models.update_reference_note_version_request import UpdateReferenceNoteVersionRequest
from ...types import Response


def _get_kwargs(
    reference_note_id: UUID,
    version_number: int,
    *,
    body: UpdateReferenceNoteVersionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/app/lawtalk/requirements/reference-notes/{reference_note_id}/versions/{version_number}/".format(
            reference_note_id=quote(str(reference_note_id), safe=""),
            version_number=quote(str(version_number), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ReferenceNoteVersionResponse | None:
    if response.status_code == 200:
        response_200 = ReferenceNoteVersionResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ReferenceNoteVersionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reference_note_id: UUID,
    version_number: int,
    *,
    client: AuthenticatedClient,
    body: UpdateReferenceNoteVersionRequest,
) -> Response[ReferenceNoteVersionResponse]:
    """Update a reference note version

     Update the content of a specific version of a reference note.

    Args:
        reference_note_id (UUID):
        version_number (int):
        body (UpdateReferenceNoteVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReferenceNoteVersionResponse]
    """

    kwargs = _get_kwargs(
        reference_note_id=reference_note_id,
        version_number=version_number,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reference_note_id: UUID,
    version_number: int,
    *,
    client: AuthenticatedClient,
    body: UpdateReferenceNoteVersionRequest,
) -> ReferenceNoteVersionResponse | None:
    """Update a reference note version

     Update the content of a specific version of a reference note.

    Args:
        reference_note_id (UUID):
        version_number (int):
        body (UpdateReferenceNoteVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReferenceNoteVersionResponse
    """

    return sync_detailed(
        reference_note_id=reference_note_id,
        version_number=version_number,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    reference_note_id: UUID,
    version_number: int,
    *,
    client: AuthenticatedClient,
    body: UpdateReferenceNoteVersionRequest,
) -> Response[ReferenceNoteVersionResponse]:
    """Update a reference note version

     Update the content of a specific version of a reference note.

    Args:
        reference_note_id (UUID):
        version_number (int):
        body (UpdateReferenceNoteVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReferenceNoteVersionResponse]
    """

    kwargs = _get_kwargs(
        reference_note_id=reference_note_id,
        version_number=version_number,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reference_note_id: UUID,
    version_number: int,
    *,
    client: AuthenticatedClient,
    body: UpdateReferenceNoteVersionRequest,
) -> ReferenceNoteVersionResponse | None:
    """Update a reference note version

     Update the content of a specific version of a reference note.

    Args:
        reference_note_id (UUID):
        version_number (int):
        body (UpdateReferenceNoteVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReferenceNoteVersionResponse
    """

    return (
        await asyncio_detailed(
            reference_note_id=reference_note_id,
            version_number=version_number,
            client=client,
            body=body,
        )
    ).parsed
