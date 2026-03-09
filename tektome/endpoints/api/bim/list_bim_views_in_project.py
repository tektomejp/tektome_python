from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_bim_views_in_project_post_in import RetrieveBimViewsInProjectPostIn
from ...models.retrieve_bim_views_in_project_post_out import RetrieveBimViewsInProjectPostOut
from ...types import Response


def _get_kwargs(
    *,
    body: RetrieveBimViewsInProjectPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-view/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrieveBimViewsInProjectPostOut | None:
    if response.status_code == 200:
        response_200 = RetrieveBimViewsInProjectPostOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrieveBimViewsInProjectPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RetrieveBimViewsInProjectPostIn,
) -> Response[RetrieveBimViewsInProjectPostOut]:
    r"""Retrieve Bim Views In Project

     ir8DUfSC

    Retrieves BIM views within a specified project, supporting both bulk and paginated queries.

    If `payload.all_at_once` is True, returns all BIM view elements in the project, optionally only
    their IDs.
    Otherwise, returns a paginated list of BIM views, with optional filtering for only IDs.

    For non-ID-only queries, the function parallelizes the construction of detailed view payloads for
    each BIM view.

    Args:
        request: The HTTP request object (unused in this function).
        payload (RetrieveBimViewsInProjectPostIn): Input data containing project ID, pagination options,
            selection fields, and flags for bulk retrieval and ID-only mode.

    Returns:
        dict: A dictionary with a \"data\" key containing either a list of BIM view IDs or detailed BIM
    view payloads.

    Raises:
        HttpError: If no BIM views are found in the specified project.

    Args:
        body (RetrieveBimViewsInProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBimViewsInProjectPostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RetrieveBimViewsInProjectPostIn,
) -> RetrieveBimViewsInProjectPostOut | None:
    r"""Retrieve Bim Views In Project

     ir8DUfSC

    Retrieves BIM views within a specified project, supporting both bulk and paginated queries.

    If `payload.all_at_once` is True, returns all BIM view elements in the project, optionally only
    their IDs.
    Otherwise, returns a paginated list of BIM views, with optional filtering for only IDs.

    For non-ID-only queries, the function parallelizes the construction of detailed view payloads for
    each BIM view.

    Args:
        request: The HTTP request object (unused in this function).
        payload (RetrieveBimViewsInProjectPostIn): Input data containing project ID, pagination options,
            selection fields, and flags for bulk retrieval and ID-only mode.

    Returns:
        dict: A dictionary with a \"data\" key containing either a list of BIM view IDs or detailed BIM
    view payloads.

    Raises:
        HttpError: If no BIM views are found in the specified project.

    Args:
        body (RetrieveBimViewsInProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBimViewsInProjectPostOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RetrieveBimViewsInProjectPostIn,
) -> Response[RetrieveBimViewsInProjectPostOut]:
    r"""Retrieve Bim Views In Project

     ir8DUfSC

    Retrieves BIM views within a specified project, supporting both bulk and paginated queries.

    If `payload.all_at_once` is True, returns all BIM view elements in the project, optionally only
    their IDs.
    Otherwise, returns a paginated list of BIM views, with optional filtering for only IDs.

    For non-ID-only queries, the function parallelizes the construction of detailed view payloads for
    each BIM view.

    Args:
        request: The HTTP request object (unused in this function).
        payload (RetrieveBimViewsInProjectPostIn): Input data containing project ID, pagination options,
            selection fields, and flags for bulk retrieval and ID-only mode.

    Returns:
        dict: A dictionary with a \"data\" key containing either a list of BIM view IDs or detailed BIM
    view payloads.

    Raises:
        HttpError: If no BIM views are found in the specified project.

    Args:
        body (RetrieveBimViewsInProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBimViewsInProjectPostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RetrieveBimViewsInProjectPostIn,
) -> RetrieveBimViewsInProjectPostOut | None:
    r"""Retrieve Bim Views In Project

     ir8DUfSC

    Retrieves BIM views within a specified project, supporting both bulk and paginated queries.

    If `payload.all_at_once` is True, returns all BIM view elements in the project, optionally only
    their IDs.
    Otherwise, returns a paginated list of BIM views, with optional filtering for only IDs.

    For non-ID-only queries, the function parallelizes the construction of detailed view payloads for
    each BIM view.

    Args:
        request: The HTTP request object (unused in this function).
        payload (RetrieveBimViewsInProjectPostIn): Input data containing project ID, pagination options,
            selection fields, and flags for bulk retrieval and ID-only mode.

    Returns:
        dict: A dictionary with a \"data\" key containing either a list of BIM view IDs or detailed BIM
    view payloads.

    Raises:
        HttpError: If no BIM views are found in the specified project.

    Args:
        body (RetrieveBimViewsInProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBimViewsInProjectPostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
