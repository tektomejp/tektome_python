from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataspace_members_schema_out import DataspaceMembersSchemaOut
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/dataspaces/{dataspace_id}/members/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[DataspaceMembersSchemaOut] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DataspaceMembersSchemaOut.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[DataspaceMembersSchemaOut]]:
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
) -> Response[list[DataspaceMembersSchemaOut]]:
    """Get Dataspace Members

     QoK123Lm

    Retrieve all members of a dataspace

    Args:
        dataspace_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[DataspaceMembersSchemaOut]]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
) -> list[DataspaceMembersSchemaOut] | None:
    """Get Dataspace Members

     QoK123Lm

    Retrieve all members of a dataspace

    Args:
        dataspace_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[DataspaceMembersSchemaOut]
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[list[DataspaceMembersSchemaOut]]:
    """Get Dataspace Members

     QoK123Lm

    Retrieve all members of a dataspace

    Args:
        dataspace_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[DataspaceMembersSchemaOut]]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
) -> list[DataspaceMembersSchemaOut] | None:
    """Get Dataspace Members

     QoK123Lm

    Retrieve all members of a dataspace

    Args:
        dataspace_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[DataspaceMembersSchemaOut]
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            client=client,
        )
    ).parsed
