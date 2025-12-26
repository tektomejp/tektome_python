from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paged_lawtalk_project_schema_get_out import PagedLawtalkProjectSchemaGetOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    recent: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["recent"] = recent

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
        "url": "/api/app/lawtalk/projects/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PagedLawtalkProjectSchemaGetOut | None:
    if response.status_code == 200:
        response_200 = PagedLawtalkProjectSchemaGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PagedLawtalkProjectSchemaGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    recent: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedLawtalkProjectSchemaGetOut]:
    """Get Projects

     iRKICjKO

    Fetches a list of projects for the authenticated user based on query parameters.

    This endpoint retrieves projects associated with the authenticated user. The list
    of projects can be filtered using the provided query parameters, specifically
    for recent projects based on the user's last used projects.

    Args:
        request: The HTTP request object containing user authentication and metadata.
        query_params: Query parameters that define filtering options for retrieving
            projects, including a flag for recent projects.

    Returns:
        list[LawtalkProjectSchemaGetOut]: A list of serialized project data conforming
        to the schema provided in `LawtalkProjectSchemaGetOut`.

    Args:
        recent (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedLawtalkProjectSchemaGetOut]
    """

    kwargs = _get_kwargs(
        recent=recent,
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
    recent: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedLawtalkProjectSchemaGetOut | None:
    """Get Projects

     iRKICjKO

    Fetches a list of projects for the authenticated user based on query parameters.

    This endpoint retrieves projects associated with the authenticated user. The list
    of projects can be filtered using the provided query parameters, specifically
    for recent projects based on the user's last used projects.

    Args:
        request: The HTTP request object containing user authentication and metadata.
        query_params: Query parameters that define filtering options for retrieving
            projects, including a flag for recent projects.

    Returns:
        list[LawtalkProjectSchemaGetOut]: A list of serialized project data conforming
        to the schema provided in `LawtalkProjectSchemaGetOut`.

    Args:
        recent (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedLawtalkProjectSchemaGetOut
    """

    return sync_detailed(
        client=client,
        recent=recent,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    recent: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedLawtalkProjectSchemaGetOut]:
    """Get Projects

     iRKICjKO

    Fetches a list of projects for the authenticated user based on query parameters.

    This endpoint retrieves projects associated with the authenticated user. The list
    of projects can be filtered using the provided query parameters, specifically
    for recent projects based on the user's last used projects.

    Args:
        request: The HTTP request object containing user authentication and metadata.
        query_params: Query parameters that define filtering options for retrieving
            projects, including a flag for recent projects.

    Returns:
        list[LawtalkProjectSchemaGetOut]: A list of serialized project data conforming
        to the schema provided in `LawtalkProjectSchemaGetOut`.

    Args:
        recent (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedLawtalkProjectSchemaGetOut]
    """

    kwargs = _get_kwargs(
        recent=recent,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    recent: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedLawtalkProjectSchemaGetOut | None:
    """Get Projects

     iRKICjKO

    Fetches a list of projects for the authenticated user based on query parameters.

    This endpoint retrieves projects associated with the authenticated user. The list
    of projects can be filtered using the provided query parameters, specifically
    for recent projects based on the user's last used projects.

    Args:
        request: The HTTP request object containing user authentication and metadata.
        query_params: Query parameters that define filtering options for retrieving
            projects, including a flag for recent projects.

    Returns:
        list[LawtalkProjectSchemaGetOut]: A list of serialized project data conforming
        to the schema provided in `LawtalkProjectSchemaGetOut`.

    Args:
        recent (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedLawtalkProjectSchemaGetOut
    """

    return (
        await asyncio_detailed(
            client=client,
            recent=recent,
            page=page,
            page_size=page_size,
        )
    ).parsed
