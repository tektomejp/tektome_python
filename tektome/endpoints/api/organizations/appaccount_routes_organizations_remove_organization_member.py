from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_output_schema_out import ErrorOutputSchemaOut
from ...models.users_schema_in import UsersSchemaIn
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    *,
    body: UsersSchemaIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/core/account/organizations/{organization_id}/members/".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorOutputSchemaOut | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ErrorOutputSchemaOut.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorOutputSchemaOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UsersSchemaIn,
) -> Response[Any | ErrorOutputSchemaOut]:
    """Remove Organization Member

     k3MWcA12

    Remove a member from an organization.

    Prevents removal of users who own dataspaces or projects in the organization.

    Args:
        organization_id (UUID):
        body (UsersSchemaIn): Schema for getting user IDs

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorOutputSchemaOut]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UsersSchemaIn,
) -> Any | ErrorOutputSchemaOut | None:
    """Remove Organization Member

     k3MWcA12

    Remove a member from an organization.

    Prevents removal of users who own dataspaces or projects in the organization.

    Args:
        organization_id (UUID):
        body (UsersSchemaIn): Schema for getting user IDs

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorOutputSchemaOut
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UsersSchemaIn,
) -> Response[Any | ErrorOutputSchemaOut]:
    """Remove Organization Member

     k3MWcA12

    Remove a member from an organization.

    Prevents removal of users who own dataspaces or projects in the organization.

    Args:
        organization_id (UUID):
        body (UsersSchemaIn): Schema for getting user IDs

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorOutputSchemaOut]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UsersSchemaIn,
) -> Any | ErrorOutputSchemaOut | None:
    """Remove Organization Member

     k3MWcA12

    Remove a member from an organization.

    Prevents removal of users who own dataspaces or projects in the organization.

    Args:
        organization_id (UUID):
        body (UsersSchemaIn): Schema for getting user IDs

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorOutputSchemaOut
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            body=body,
        )
    ).parsed
