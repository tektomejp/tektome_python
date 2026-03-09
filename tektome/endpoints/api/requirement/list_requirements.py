from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paged_requirements_list_get_out import PagedRequirementsListGetOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: UUID,
    recent: bool | Unset = False,
    filter_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_project_id = str(project_id)
    params["project_id"] = json_project_id

    params["recent"] = recent

    json_filter_name: None | str | Unset
    if isinstance(filter_name, Unset):
        json_filter_name = UNSET
    else:
        json_filter_name = filter_name
    params["filter_name"] = json_filter_name

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
        "url": "/api/app/lawtalk/requirements/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PagedRequirementsListGetOut | None:
    if response.status_code == 200:
        response_200 = PagedRequirementsListGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PagedRequirementsListGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_id: UUID,
    recent: bool | Unset = False,
    filter_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedRequirementsListGetOut]:
    """Get Requirements

     9yNtf4iG

    Get all requirements given a project id in query parameters

    Args:
        project_id (UUID):
        recent (bool | Unset):  Default: False.
        filter_name (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedRequirementsListGetOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        recent=recent,
        filter_name=filter_name,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    project_id: UUID,
    recent: bool | Unset = False,
    filter_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedRequirementsListGetOut | None:
    """Get Requirements

     9yNtf4iG

    Get all requirements given a project id in query parameters

    Args:
        project_id (UUID):
        recent (bool | Unset):  Default: False.
        filter_name (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedRequirementsListGetOut
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        recent=recent,
        filter_name=filter_name,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_id: UUID,
    recent: bool | Unset = False,
    filter_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedRequirementsListGetOut]:
    """Get Requirements

     9yNtf4iG

    Get all requirements given a project id in query parameters

    Args:
        project_id (UUID):
        recent (bool | Unset):  Default: False.
        filter_name (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedRequirementsListGetOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        recent=recent,
        filter_name=filter_name,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    project_id: UUID,
    recent: bool | Unset = False,
    filter_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedRequirementsListGetOut | None:
    """Get Requirements

     9yNtf4iG

    Get all requirements given a project id in query parameters

    Args:
        project_id (UUID):
        recent (bool | Unset):  Default: False.
        filter_name (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedRequirementsListGetOut
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            recent=recent,
            filter_name=filter_name,
            page=page,
            page_size=page_size,
        )
    ).parsed
