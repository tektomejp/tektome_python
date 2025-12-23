from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_requirement_item_column_config_out import ProjectRequirementItemColumnConfigOut
from ...models.project_requirement_item_column_config_post_in import ProjectRequirementItemColumnConfigPostIn
from ...types import Response


def _get_kwargs(
    project_id: UUID,
    *,
    body: ProjectRequirementItemColumnConfigPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/projects/{project_id}/requirement-item-column-configs/".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProjectRequirementItemColumnConfigOut | None:
    if response.status_code == 201:
        response_201 = ProjectRequirementItemColumnConfigOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProjectRequirementItemColumnConfigOut]:
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
    body: ProjectRequirementItemColumnConfigPostIn,
) -> Response[ProjectRequirementItemColumnConfigOut]:
    """Post Project Requirement Item Column Config

     1b2c3d4A

    Create a new requirement item column configuration for a project.

    Args:
        project_id (UUID):
        body (ProjectRequirementItemColumnConfigPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectRequirementItemColumnConfigOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ProjectRequirementItemColumnConfigPostIn,
) -> ProjectRequirementItemColumnConfigOut | None:
    """Post Project Requirement Item Column Config

     1b2c3d4A

    Create a new requirement item column configuration for a project.

    Args:
        project_id (UUID):
        body (ProjectRequirementItemColumnConfigPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectRequirementItemColumnConfigOut
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ProjectRequirementItemColumnConfigPostIn,
) -> Response[ProjectRequirementItemColumnConfigOut]:
    """Post Project Requirement Item Column Config

     1b2c3d4A

    Create a new requirement item column configuration for a project.

    Args:
        project_id (UUID):
        body (ProjectRequirementItemColumnConfigPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectRequirementItemColumnConfigOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ProjectRequirementItemColumnConfigPostIn,
) -> ProjectRequirementItemColumnConfigOut | None:
    """Post Project Requirement Item Column Config

     1b2c3d4A

    Create a new requirement item column configuration for a project.

    Args:
        project_id (UUID):
        body (ProjectRequirementItemColumnConfigPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectRequirementItemColumnConfigOut
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
