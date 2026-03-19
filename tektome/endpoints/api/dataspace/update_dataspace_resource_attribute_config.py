from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataspace_resource_file_attribute_schema_response import DataspaceResourceFileAttributeSchemaResponse
from ...models.update_dataspace_resource_attribute_request import UpdateDataspaceResourceAttributeRequest
from ...types import Response


def _get_kwargs(
    attribute_config_id: UUID,
    *,
    body: UpdateDataspaceResourceAttributeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/dataspaces/resources/attribute-configs/{attribute_config_id}/".format(
            attribute_config_id=quote(str(attribute_config_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DataspaceResourceFileAttributeSchemaResponse | None:
    if response.status_code == 200:
        response_200 = DataspaceResourceFileAttributeSchemaResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DataspaceResourceFileAttributeSchemaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attribute_config_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateDataspaceResourceAttributeRequest,
) -> Response[DataspaceResourceFileAttributeSchemaResponse]:
    """Update a resource attribute column configuration

     Update an existing resource attribute column configuration, including its label, metadata, and table
    or select options. Renaming propagates to all resources across projects in the dataspace.

    Args:
        attribute_config_id (UUID):
        body (UpdateDataspaceResourceAttributeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceResourceFileAttributeSchemaResponse]
    """

    kwargs = _get_kwargs(
        attribute_config_id=attribute_config_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    attribute_config_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateDataspaceResourceAttributeRequest,
) -> DataspaceResourceFileAttributeSchemaResponse | None:
    """Update a resource attribute column configuration

     Update an existing resource attribute column configuration, including its label, metadata, and table
    or select options. Renaming propagates to all resources across projects in the dataspace.

    Args:
        attribute_config_id (UUID):
        body (UpdateDataspaceResourceAttributeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceResourceFileAttributeSchemaResponse
    """

    return sync_detailed(
        attribute_config_id=attribute_config_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    attribute_config_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateDataspaceResourceAttributeRequest,
) -> Response[DataspaceResourceFileAttributeSchemaResponse]:
    """Update a resource attribute column configuration

     Update an existing resource attribute column configuration, including its label, metadata, and table
    or select options. Renaming propagates to all resources across projects in the dataspace.

    Args:
        attribute_config_id (UUID):
        body (UpdateDataspaceResourceAttributeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceResourceFileAttributeSchemaResponse]
    """

    kwargs = _get_kwargs(
        attribute_config_id=attribute_config_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    attribute_config_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateDataspaceResourceAttributeRequest,
) -> DataspaceResourceFileAttributeSchemaResponse | None:
    """Update a resource attribute column configuration

     Update an existing resource attribute column configuration, including its label, metadata, and table
    or select options. Renaming propagates to all resources across projects in the dataspace.

    Args:
        attribute_config_id (UUID):
        body (UpdateDataspaceResourceAttributeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceResourceFileAttributeSchemaResponse
    """

    return (
        await asyncio_detailed(
            attribute_config_id=attribute_config_id,
            client=client,
            body=body,
        )
    ).parsed
