from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generic_http_error import GenericHttpError
from ...models.paged_resource_glob_out import PagedResourceGlobOut
from ...models.resource_glob_in import ResourceGlobIn
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    *,
    body: ResourceGlobIn,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

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
        "method": "post",
        "url": "/api/core/resource-paths/projects/{project_id}/glob/".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenericHttpError | PagedResourceGlobOut | None:
    if response.status_code == 200:
        response_200 = PagedResourceGlobOut.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GenericHttpError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GenericHttpError.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GenericHttpError.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GenericHttpError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GenericHttpError.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GenericHttpError.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GenericHttpError.from_dict(response.json())

        return response_406

    if response.status_code == 407:
        response_407 = GenericHttpError.from_dict(response.json())

        return response_407

    if response.status_code == 408:
        response_408 = GenericHttpError.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = GenericHttpError.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = GenericHttpError.from_dict(response.json())

        return response_410

    if response.status_code == 411:
        response_411 = GenericHttpError.from_dict(response.json())

        return response_411

    if response.status_code == 412:
        response_412 = GenericHttpError.from_dict(response.json())

        return response_412

    if response.status_code == 416:
        response_416 = GenericHttpError.from_dict(response.json())

        return response_416

    if response.status_code == 418:
        response_418 = GenericHttpError.from_dict(response.json())

        return response_418

    if response.status_code == 425:
        response_425 = GenericHttpError.from_dict(response.json())

        return response_425

    if response.status_code == 429:
        response_429 = GenericHttpError.from_dict(response.json())

        return response_429

    if response.status_code == 451:
        response_451 = GenericHttpError.from_dict(response.json())

        return response_451

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GenericHttpError | PagedResourceGlobOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ResourceGlobIn,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[GenericHttpError | PagedResourceGlobOut]:
    """Glob match resource paths

     Search for resources matching a glob pattern within a project. Supports standard glob syntax
    including * (single segment), ** (any depth), ? (single character), and character classes. Results
    are paginated.

    Args:
        project_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):
        body (ResourceGlobIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericHttpError | PagedResourceGlobOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ResourceGlobIn,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> GenericHttpError | PagedResourceGlobOut | None:
    """Glob match resource paths

     Search for resources matching a glob pattern within a project. Supports standard glob syntax
    including * (single segment), ** (any depth), ? (single character), and character classes. Results
    are paginated.

    Args:
        project_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):
        body (ResourceGlobIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericHttpError | PagedResourceGlobOut
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ResourceGlobIn,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[GenericHttpError | PagedResourceGlobOut]:
    """Glob match resource paths

     Search for resources matching a glob pattern within a project. Supports standard glob syntax
    including * (single segment), ** (any depth), ? (single character), and character classes. Results
    are paginated.

    Args:
        project_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):
        body (ResourceGlobIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericHttpError | PagedResourceGlobOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ResourceGlobIn,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> GenericHttpError | PagedResourceGlobOut | None:
    """Glob match resource paths

     Search for resources matching a glob pattern within a project. Supports standard glob syntax
    including * (single segment), ** (any depth), ? (single character), and character classes. Results
    are paginated.

    Args:
        project_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):
        body (ResourceGlobIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericHttpError | PagedResourceGlobOut
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
            page=page,
            page_size=page_size,
        )
    ).parsed
