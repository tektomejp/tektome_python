from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.process_out import ProcessOut
from ...models.process_post_in_patch import ProcessPostInPatch
from ...types import Response


def _get_kwargs(
    project_id: UUID,
    process_id: UUID,
    *,
    body: ProcessPostInPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/projects/{project_id}/processes/{process_id}/".format(
            project_id=quote(str(project_id), safe=""),
            process_id=quote(str(process_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProcessOut | None:
    if response.status_code == 200:
        response_200 = ProcessOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProcessOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ProcessPostInPatch,
) -> Response[ProcessOut]:
    """Patch Project Process

     yx8aUP5u

    Update a specific process in the current project.

    Args:
        project_id (UUID):
        process_id (UUID): The ID of an existing process.
        body (ProcessPostInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcessOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        process_id=process_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ProcessPostInPatch,
) -> ProcessOut | None:
    """Patch Project Process

     yx8aUP5u

    Update a specific process in the current project.

    Args:
        project_id (UUID):
        process_id (UUID): The ID of an existing process.
        body (ProcessPostInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcessOut
    """

    return sync_detailed(
        project_id=project_id,
        process_id=process_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ProcessPostInPatch,
) -> Response[ProcessOut]:
    """Patch Project Process

     yx8aUP5u

    Update a specific process in the current project.

    Args:
        project_id (UUID):
        process_id (UUID): The ID of an existing process.
        body (ProcessPostInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcessOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        process_id=process_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ProcessPostInPatch,
) -> ProcessOut | None:
    """Patch Project Process

     yx8aUP5u

    Update a specific process in the current project.

    Args:
        project_id (UUID):
        process_id (UUID): The ID of an existing process.
        body (ProcessPostInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcessOut
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            process_id=process_id,
            client=client,
            body=body,
        )
    ).parsed
