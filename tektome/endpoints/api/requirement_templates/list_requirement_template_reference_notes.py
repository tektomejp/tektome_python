from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paged_requirement_template_reference_note_get_out import PagedRequirementTemplateReferenceNoteGetOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    requirement_template_id: UUID,
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
        "url": "/api/app/lawtalk/requirement-templates/{requirement_template_id}/reference-note-templates/".format(
            requirement_template_id=quote(str(requirement_template_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PagedRequirementTemplateReferenceNoteGetOut | None:
    if response.status_code == 200:
        response_200 = PagedRequirementTemplateReferenceNoteGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PagedRequirementTemplateReferenceNoteGetOut]:
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
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedRequirementTemplateReferenceNoteGetOut]:
    """Get Requirement Template Reference Notes

     OWvaVaLA

    Get all requirement templates reference notes

    Args:
        requirement_template_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedRequirementTemplateReferenceNoteGetOut]
    """

    kwargs = _get_kwargs(
        requirement_template_id=requirement_template_id,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedRequirementTemplateReferenceNoteGetOut | None:
    """Get Requirement Template Reference Notes

     OWvaVaLA

    Get all requirement templates reference notes

    Args:
        requirement_template_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedRequirementTemplateReferenceNoteGetOut
    """

    return sync_detailed(
        requirement_template_id=requirement_template_id,
        client=client,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedRequirementTemplateReferenceNoteGetOut]:
    """Get Requirement Template Reference Notes

     OWvaVaLA

    Get all requirement templates reference notes

    Args:
        requirement_template_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedRequirementTemplateReferenceNoteGetOut]
    """

    kwargs = _get_kwargs(
        requirement_template_id=requirement_template_id,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedRequirementTemplateReferenceNoteGetOut | None:
    """Get Requirement Template Reference Notes

     OWvaVaLA

    Get all requirement templates reference notes

    Args:
        requirement_template_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedRequirementTemplateReferenceNoteGetOut
    """

    return (
        await asyncio_detailed(
            requirement_template_id=requirement_template_id,
            client=client,
            page=page,
            page_size=page_size,
        )
    ).parsed
