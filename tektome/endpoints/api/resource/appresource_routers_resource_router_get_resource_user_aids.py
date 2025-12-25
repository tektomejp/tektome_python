from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_resource_user_aids_get_out import GetResourceUserAidsGetOut
from ...types import UNSET, Response


def _get_kwargs(
    resource_id: UUID,
    *,
    attribute_id: UUID,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_attribute_id = str(attribute_id)
    params["attribute_id"] = json_attribute_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resources/{resource_id}/get_resource_user_aids/".format(
            resource_id=quote(str(resource_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetResourceUserAidsGetOut | None:
    if response.status_code == 200:
        response_200 = GetResourceUserAidsGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetResourceUserAidsGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
    attribute_id: UUID,
) -> Response[GetResourceUserAidsGetOut]:
    """Get all user aids for the given Resource-Attribute pair

     xGjEXPha

    Get all user aids for the given Resource-Attribute pair.

    Args:
        request: Request object
        path_params: Path parameters containing resource_id
        query_payload: Payload containing attribute_id

    Args:
        resource_id (UUID):
        attribute_id (UUID): UUID of the attribute

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetResourceUserAidsGetOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        attribute_id=attribute_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
    attribute_id: UUID,
) -> GetResourceUserAidsGetOut | None:
    """Get all user aids for the given Resource-Attribute pair

     xGjEXPha

    Get all user aids for the given Resource-Attribute pair.

    Args:
        request: Request object
        path_params: Path parameters containing resource_id
        query_payload: Payload containing attribute_id

    Args:
        resource_id (UUID):
        attribute_id (UUID): UUID of the attribute

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetResourceUserAidsGetOut
    """

    return sync_detailed(
        resource_id=resource_id,
        client=client,
        attribute_id=attribute_id,
    ).parsed


async def asyncio_detailed(
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
    attribute_id: UUID,
) -> Response[GetResourceUserAidsGetOut]:
    """Get all user aids for the given Resource-Attribute pair

     xGjEXPha

    Get all user aids for the given Resource-Attribute pair.

    Args:
        request: Request object
        path_params: Path parameters containing resource_id
        query_payload: Payload containing attribute_id

    Args:
        resource_id (UUID):
        attribute_id (UUID): UUID of the attribute

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetResourceUserAidsGetOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        attribute_id=attribute_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
    attribute_id: UUID,
) -> GetResourceUserAidsGetOut | None:
    """Get all user aids for the given Resource-Attribute pair

     xGjEXPha

    Get all user aids for the given Resource-Attribute pair.

    Args:
        request: Request object
        path_params: Path parameters containing resource_id
        query_payload: Payload containing attribute_id

    Args:
        resource_id (UUID):
        attribute_id (UUID): UUID of the attribute

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetResourceUserAidsGetOut
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            client=client,
            attribute_id=attribute_id,
        )
    ).parsed
