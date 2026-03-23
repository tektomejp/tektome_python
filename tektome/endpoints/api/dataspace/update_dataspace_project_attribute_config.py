from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataspace_project_attribute_patch_in_patch import DataspaceProjectAttributePatchInPatch
from ...models.dataspace_project_attribute_schema_out import DataspaceProjectAttributeSchemaOut
from ...types import Response


def _get_kwargs(
    attribute_config_id: UUID,
    *,
    body: DataspaceProjectAttributePatchInPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/dataspaces/projects/attribute-configs/{attribute_config_id}/".format(
            attribute_config_id=quote(str(attribute_config_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DataspaceProjectAttributeSchemaOut | None:
    if response.status_code == 200:
        response_200 = DataspaceProjectAttributeSchemaOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DataspaceProjectAttributeSchemaOut]:
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
    body: DataspaceProjectAttributePatchInPatch,
) -> Response[DataspaceProjectAttributeSchemaOut]:
    """Patch Dataspace Project Attribute Config

     x16N0f5B

    Updates the column attributes of a dataspace project.
    attribute name is a computed field based on the attribute label.

    Args:
        attribute_config_id (UUID):
        body (DataspaceProjectAttributePatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceProjectAttributeSchemaOut]
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
    body: DataspaceProjectAttributePatchInPatch,
) -> DataspaceProjectAttributeSchemaOut | None:
    """Patch Dataspace Project Attribute Config

     x16N0f5B

    Updates the column attributes of a dataspace project.
    attribute name is a computed field based on the attribute label.

    Args:
        attribute_config_id (UUID):
        body (DataspaceProjectAttributePatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceProjectAttributeSchemaOut
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
    body: DataspaceProjectAttributePatchInPatch,
) -> Response[DataspaceProjectAttributeSchemaOut]:
    """Patch Dataspace Project Attribute Config

     x16N0f5B

    Updates the column attributes of a dataspace project.
    attribute name is a computed field based on the attribute label.

    Args:
        attribute_config_id (UUID):
        body (DataspaceProjectAttributePatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceProjectAttributeSchemaOut]
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
    body: DataspaceProjectAttributePatchInPatch,
) -> DataspaceProjectAttributeSchemaOut | None:
    """Patch Dataspace Project Attribute Config

     x16N0f5B

    Updates the column attributes of a dataspace project.
    attribute name is a computed field based on the attribute label.

    Args:
        attribute_config_id (UUID):
        body (DataspaceProjectAttributePatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceProjectAttributeSchemaOut
    """

    return (
        await asyncio_detailed(
            attribute_config_id=attribute_config_id,
            client=client,
            body=body,
        )
    ).parsed
