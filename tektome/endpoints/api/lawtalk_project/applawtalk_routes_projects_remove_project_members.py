from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.users_schema_in import UsersSchemaIn
from ...types import Response


def _get_kwargs(
    project_id: UUID,
    *,
    body: UsersSchemaIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/app/lawtalk/projects/{project_id}/members/".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

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
    body: UsersSchemaIn,
) -> Response[Any]:
    """Remove Project Members

     Xh2JkL9m

    Remove multiple members from a project. If member has no account login yet and member has no other
    invitations, then delete the user member.

    Args:
        request: Request object.
        path_params: Path params of type ProjectDefaultPath
        payload: payload of type ProjectBulkRemoveMembersIn

    Returns: 204, None

    Args:
        project_id (UUID):
        body (UsersSchemaIn): Schema for getting user IDs

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
    body: UsersSchemaIn,
) -> Response[Any]:
    """Remove Project Members

     Xh2JkL9m

    Remove multiple members from a project. If member has no account login yet and member has no other
    invitations, then delete the user member.

    Args:
        request: Request object.
        path_params: Path params of type ProjectDefaultPath
        payload: payload of type ProjectBulkRemoveMembersIn

    Returns: 204, None

    Args:
        project_id (UUID):
        body (UsersSchemaIn): Schema for getting user IDs

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
