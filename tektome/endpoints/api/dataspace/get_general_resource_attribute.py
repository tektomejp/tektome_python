from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attribute_get_out import AttributeGetOut
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    attribute_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/dataspaces/{dataspace_id}/attributes/{attribute_id}/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            attribute_id=quote(str(attribute_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AttributeGetOut | None:
    if response.status_code == 200:
        response_200 = AttributeGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AttributeGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[AttributeGetOut]:
    """Get General Resource Attribute

     CpgPOHHA

    Retrieve a general dataspace attribute by ID.
    Can either be a resource attribute or project attribute.

    Args:
        path_params: The path parameters containing the dataspace ID and attribute ID.
        request: The incoming request object.
        payload: The payload containing attribute details.

    Returns: 200, attribute

    Args:
        dataspace_id (UUID):
        attribute_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributeGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        attribute_id=attribute_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
) -> AttributeGetOut | None:
    """Get General Resource Attribute

     CpgPOHHA

    Retrieve a general dataspace attribute by ID.
    Can either be a resource attribute or project attribute.

    Args:
        path_params: The path parameters containing the dataspace ID and attribute ID.
        request: The incoming request object.
        payload: The payload containing attribute details.

    Returns: 200, attribute

    Args:
        dataspace_id (UUID):
        attribute_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributeGetOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        attribute_id=attribute_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[AttributeGetOut]:
    """Get General Resource Attribute

     CpgPOHHA

    Retrieve a general dataspace attribute by ID.
    Can either be a resource attribute or project attribute.

    Args:
        path_params: The path parameters containing the dataspace ID and attribute ID.
        request: The incoming request object.
        payload: The payload containing attribute details.

    Returns: 200, attribute

    Args:
        dataspace_id (UUID):
        attribute_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributeGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        attribute_id=attribute_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
) -> AttributeGetOut | None:
    """Get General Resource Attribute

     CpgPOHHA

    Retrieve a general dataspace attribute by ID.
    Can either be a resource attribute or project attribute.

    Args:
        path_params: The path parameters containing the dataspace ID and attribute ID.
        request: The incoming request object.
        payload: The payload containing attribute details.

    Returns: 200, attribute

    Args:
        dataspace_id (UUID):
        attribute_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributeGetOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            attribute_id=attribute_id,
            client=client,
        )
    ).parsed
