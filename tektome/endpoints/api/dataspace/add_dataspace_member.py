from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_user_invitation_schema_out import BulkUserInvitationSchemaOut
from ...models.invite_user_by_email_schema_in import InviteUserByEmailSchemaIn
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    *,
    body: list[InviteUserByEmailSchemaIn],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/members/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
        ),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkUserInvitationSchemaOut | None:
    if response.status_code == 200:
        response_200 = BulkUserInvitationSchemaOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BulkUserInvitationSchemaOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: list[InviteUserByEmailSchemaIn],
) -> Response[BulkUserInvitationSchemaOut]:
    """Add Dataspace Member

     MnAo2Kmx

    Add a member to a dataspace

    Args:
        dataspace_id (UUID):
        body (list[InviteUserByEmailSchemaIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkUserInvitationSchemaOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: list[InviteUserByEmailSchemaIn],
) -> BulkUserInvitationSchemaOut | None:
    """Add Dataspace Member

     MnAo2Kmx

    Add a member to a dataspace

    Args:
        dataspace_id (UUID):
        body (list[InviteUserByEmailSchemaIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkUserInvitationSchemaOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: list[InviteUserByEmailSchemaIn],
) -> Response[BulkUserInvitationSchemaOut]:
    """Add Dataspace Member

     MnAo2Kmx

    Add a member to a dataspace

    Args:
        dataspace_id (UUID):
        body (list[InviteUserByEmailSchemaIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkUserInvitationSchemaOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: list[InviteUserByEmailSchemaIn],
) -> BulkUserInvitationSchemaOut | None:
    """Add Dataspace Member

     MnAo2Kmx

    Add a member to a dataspace

    Args:
        dataspace_id (UUID):
        body (list[InviteUserByEmailSchemaIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkUserInvitationSchemaOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            client=client,
            body=body,
        )
    ).parsed
