from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.artifact_template_group_kind import ArtifactTemplateGroupKind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    kind: ArtifactTemplateGroupKind | None | Unset = UNSET,
    is_default: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_kind: None | str | Unset
    if isinstance(kind, Unset):
        json_kind = UNSET
    elif isinstance(kind, ArtifactTemplateGroupKind):
        json_kind = kind.value
    else:
        json_kind = kind
    params["kind"] = json_kind

    json_is_default: bool | None | Unset
    if isinstance(is_default, Unset):
        json_is_default = UNSET
    else:
        json_is_default = is_default
    params["is_default"] = json_is_default

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

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
        "url": "/api/core/agents/os/artifact-templates/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    kind: ArtifactTemplateGroupKind | None | Unset = UNSET,
    is_default: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[Any]:
    """List active artifact template groups

     Returns paginated artifact template groups available for installation. Template groups are pre-
    defined bundles of files (skills, SDK references, starter kits) that can be installed into a
    chatroom. Filter by kind (skill/artifact), default status, or search by name.

    Args:
        kind (ArtifactTemplateGroupKind | None | Unset):
        is_default (bool | None | Unset):
        search (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        kind=kind,
        is_default=is_default,
        search=search,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    kind: ArtifactTemplateGroupKind | None | Unset = UNSET,
    is_default: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[Any]:
    """List active artifact template groups

     Returns paginated artifact template groups available for installation. Template groups are pre-
    defined bundles of files (skills, SDK references, starter kits) that can be installed into a
    chatroom. Filter by kind (skill/artifact), default status, or search by name.

    Args:
        kind (ArtifactTemplateGroupKind | None | Unset):
        is_default (bool | None | Unset):
        search (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        kind=kind,
        is_default=is_default,
        search=search,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
