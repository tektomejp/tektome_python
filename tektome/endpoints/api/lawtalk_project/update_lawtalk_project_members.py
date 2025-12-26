from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_patch_members_schema_in import ProjectPatchMembersSchemaIn
from ...types import Response


def _get_kwargs(
    project_id: UUID,
    *,
    body: list[ProjectPatchMembersSchemaIn],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/app/lawtalk/projects/{project_id}/members/".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

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
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: list[ProjectPatchMembersSchemaIn],
) -> Response[Any]:
    """Update Project Members

     6mNqfKX0

    Update members of a project with specific roles.

    Args:
        request: Request object.
        path_params: Path params of type ProjectDefaultPath
        user_role_assignments: List of user role assignments.

    Returns: 204, None

    Args:
        project_id (UUID):
        body (list[ProjectPatchMembersSchemaIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: list[ProjectPatchMembersSchemaIn],
) -> Response[Any]:
    """Update Project Members

     6mNqfKX0

    Update members of a project with specific roles.

    Args:
        request: Request object.
        path_params: Path params of type ProjectDefaultPath
        user_role_assignments: List of user role assignments.

    Returns: 204, None

    Args:
        project_id (UUID):
        body (list[ProjectPatchMembersSchemaIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
