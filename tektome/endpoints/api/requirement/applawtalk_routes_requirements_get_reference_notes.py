from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.applawtalk_routes_requirements_get_reference_notes_sort import (
    ApplawtalkRoutesRequirementsGetReferenceNotesSort,
)
from ...models.paged_reference_note_schema import PagedReferenceNoteSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    requirement_id: UUID,
    *,
    sort: ApplawtalkRoutesRequirementsGetReferenceNotesSort
    | Unset = ApplawtalkRoutesRequirementsGetReferenceNotesSort.ASC,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

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
        "url": "/api/app/lawtalk/requirements/{requirement_id}/reference-notes/".format(
            requirement_id=quote(str(requirement_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PagedReferenceNoteSchema | None:
    if response.status_code == 200:
        response_200 = PagedReferenceNoteSchema.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PagedReferenceNoteSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    sort: ApplawtalkRoutesRequirementsGetReferenceNotesSort
    | Unset = ApplawtalkRoutesRequirementsGetReferenceNotesSort.ASC,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedReferenceNoteSchema]:
    """Get Reference Notes

     JnQkM31B

    Get reference notes associated to a requirement

    Args:
        request: Request object
        path_params: path params of type RequirementPath

    Args:
        requirement_id (UUID):
        sort (ApplawtalkRoutesRequirementsGetReferenceNotesSort | Unset):  Default:
            ApplawtalkRoutesRequirementsGetReferenceNotesSort.ASC.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedReferenceNoteSchema]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        sort=sort,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    sort: ApplawtalkRoutesRequirementsGetReferenceNotesSort
    | Unset = ApplawtalkRoutesRequirementsGetReferenceNotesSort.ASC,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedReferenceNoteSchema | None:
    """Get Reference Notes

     JnQkM31B

    Get reference notes associated to a requirement

    Args:
        request: Request object
        path_params: path params of type RequirementPath

    Args:
        requirement_id (UUID):
        sort (ApplawtalkRoutesRequirementsGetReferenceNotesSort | Unset):  Default:
            ApplawtalkRoutesRequirementsGetReferenceNotesSort.ASC.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedReferenceNoteSchema
    """

    return sync_detailed(
        requirement_id=requirement_id,
        client=client,
        sort=sort,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    sort: ApplawtalkRoutesRequirementsGetReferenceNotesSort
    | Unset = ApplawtalkRoutesRequirementsGetReferenceNotesSort.ASC,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedReferenceNoteSchema]:
    """Get Reference Notes

     JnQkM31B

    Get reference notes associated to a requirement

    Args:
        request: Request object
        path_params: path params of type RequirementPath

    Args:
        requirement_id (UUID):
        sort (ApplawtalkRoutesRequirementsGetReferenceNotesSort | Unset):  Default:
            ApplawtalkRoutesRequirementsGetReferenceNotesSort.ASC.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedReferenceNoteSchema]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        sort=sort,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    sort: ApplawtalkRoutesRequirementsGetReferenceNotesSort
    | Unset = ApplawtalkRoutesRequirementsGetReferenceNotesSort.ASC,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedReferenceNoteSchema | None:
    """Get Reference Notes

     JnQkM31B

    Get reference notes associated to a requirement

    Args:
        request: Request object
        path_params: path params of type RequirementPath

    Args:
        requirement_id (UUID):
        sort (ApplawtalkRoutesRequirementsGetReferenceNotesSort | Unset):  Default:
            ApplawtalkRoutesRequirementsGetReferenceNotesSort.ASC.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedReferenceNoteSchema
    """

    return (
        await asyncio_detailed(
            requirement_id=requirement_id,
            client=client,
            sort=sort,
            page=page,
            page_size=page_size,
        )
    ).parsed
