from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_response_requirement_template_get_out import PaginatedResponseRequirementTemplateGetOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    requirement_template_container_id: UUID,
    *,
    view_mode: None | str | Unset = UNSET,
    page: int | None | Unset = 1,
    page_size: int | None | Unset = 30,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_view_mode: None | str | Unset
    if isinstance(view_mode, Unset):
        json_view_mode = UNSET
    else:
        json_view_mode = view_mode
    params["view_mode"] = json_view_mode

    json_page: int | None | Unset
    if isinstance(page, Unset):
        json_page = UNSET
    else:
        json_page = page
    params["page"] = json_page

    json_page_size: int | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["page_size"] = json_page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/requirement-templates-container/{requirement_template_container_id}/requirement-templates/".format(
            requirement_template_container_id=quote(str(requirement_template_container_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponseRequirementTemplateGetOut | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseRequirementTemplateGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedResponseRequirementTemplateGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    requirement_template_container_id: UUID,
    *,
    client: AuthenticatedClient,
    view_mode: None | str | Unset = UNSET,
    page: int | None | Unset = 1,
    page_size: int | None | Unset = 30,
) -> Response[PaginatedResponseRequirementTemplateGetOut]:
    """Get Requirement Templates

     B7GNMWva

    Get all requirement templates inside a requirement template container.

    Manually paginated to allow for updating EntityTracker records after viewed.

    Annotated
        is_updated_since_last_seen: bool - Whether the template has been updated since the user last saw
    it.

    Args:
        requirement_template_container_id (UUID):
        view_mode (None | str | Unset):
        page (int | None | Unset):  Default: 1.
        page_size (int | None | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseRequirementTemplateGetOut]
    """

    kwargs = _get_kwargs(
        requirement_template_container_id=requirement_template_container_id,
        view_mode=view_mode,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_template_container_id: UUID,
    *,
    client: AuthenticatedClient,
    view_mode: None | str | Unset = UNSET,
    page: int | None | Unset = 1,
    page_size: int | None | Unset = 30,
) -> PaginatedResponseRequirementTemplateGetOut | None:
    """Get Requirement Templates

     B7GNMWva

    Get all requirement templates inside a requirement template container.

    Manually paginated to allow for updating EntityTracker records after viewed.

    Annotated
        is_updated_since_last_seen: bool - Whether the template has been updated since the user last saw
    it.

    Args:
        requirement_template_container_id (UUID):
        view_mode (None | str | Unset):
        page (int | None | Unset):  Default: 1.
        page_size (int | None | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseRequirementTemplateGetOut
    """

    return sync_detailed(
        requirement_template_container_id=requirement_template_container_id,
        client=client,
        view_mode=view_mode,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    requirement_template_container_id: UUID,
    *,
    client: AuthenticatedClient,
    view_mode: None | str | Unset = UNSET,
    page: int | None | Unset = 1,
    page_size: int | None | Unset = 30,
) -> Response[PaginatedResponseRequirementTemplateGetOut]:
    """Get Requirement Templates

     B7GNMWva

    Get all requirement templates inside a requirement template container.

    Manually paginated to allow for updating EntityTracker records after viewed.

    Annotated
        is_updated_since_last_seen: bool - Whether the template has been updated since the user last saw
    it.

    Args:
        requirement_template_container_id (UUID):
        view_mode (None | str | Unset):
        page (int | None | Unset):  Default: 1.
        page_size (int | None | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseRequirementTemplateGetOut]
    """

    kwargs = _get_kwargs(
        requirement_template_container_id=requirement_template_container_id,
        view_mode=view_mode,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_template_container_id: UUID,
    *,
    client: AuthenticatedClient,
    view_mode: None | str | Unset = UNSET,
    page: int | None | Unset = 1,
    page_size: int | None | Unset = 30,
) -> PaginatedResponseRequirementTemplateGetOut | None:
    """Get Requirement Templates

     B7GNMWva

    Get all requirement templates inside a requirement template container.

    Manually paginated to allow for updating EntityTracker records after viewed.

    Annotated
        is_updated_since_last_seen: bool - Whether the template has been updated since the user last saw
    it.

    Args:
        requirement_template_container_id (UUID):
        view_mode (None | str | Unset):
        page (int | None | Unset):  Default: 1.
        page_size (int | None | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseRequirementTemplateGetOut
    """

    return (
        await asyncio_detailed(
            requirement_template_container_id=requirement_template_container_id,
            client=client,
            view_mode=view_mode,
            page=page,
            page_size=page_size,
        )
    ).parsed
