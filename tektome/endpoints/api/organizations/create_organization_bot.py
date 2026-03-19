from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_output_schema_out import ErrorOutputSchemaOut
from ...models.organization_bot_user_out import OrganizationBotUserOut
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/account/organizations/{organization_id}/bot/".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorOutputSchemaOut | OrganizationBotUserOut | None:
    if response.status_code == 201:
        response_201 = OrganizationBotUserOut.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorOutputSchemaOut.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorOutputSchemaOut.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorOutputSchemaOut | OrganizationBotUserOut]:
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
) -> Response[ErrorOutputSchemaOut | OrganizationBotUserOut]:
    """Create Organization Bot

     zStwPoBb

    Create a bot user for the organization with Organization Admin role.

    Bot users are system accounts that can perform automated tasks
    within the organization. Only one bot user is allowed per organization.
    The bot user will have Organization Admin privileges.

    Args:
        organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOutputSchemaOut | OrganizationBotUserOut]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ErrorOutputSchemaOut | OrganizationBotUserOut | None:
    """Create Organization Bot

     zStwPoBb

    Create a bot user for the organization with Organization Admin role.

    Bot users are system accounts that can perform automated tasks
    within the organization. Only one bot user is allowed per organization.
    The bot user will have Organization Admin privileges.

    Args:
        organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOutputSchemaOut | OrganizationBotUserOut
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorOutputSchemaOut | OrganizationBotUserOut]:
    """Create Organization Bot

     zStwPoBb

    Create a bot user for the organization with Organization Admin role.

    Bot users are system accounts that can perform automated tasks
    within the organization. Only one bot user is allowed per organization.
    The bot user will have Organization Admin privileges.

    Args:
        organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOutputSchemaOut | OrganizationBotUserOut]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ErrorOutputSchemaOut | OrganizationBotUserOut | None:
    """Create Organization Bot

     zStwPoBb

    Create a bot user for the organization with Organization Admin role.

    Bot users are system accounts that can perform automated tasks
    within the organization. Only one bot user is allowed per organization.
    The bot user will have Organization Admin privileges.

    Args:
        organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOutputSchemaOut | OrganizationBotUserOut
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
        )
    ).parsed
