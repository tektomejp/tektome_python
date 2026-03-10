from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataspace_table_attribute_patch_in import DataspaceTableAttributePatchIn
from ...models.upsert_dataspace_table_attributes_dataspace_entity_type import (
    UpsertDataspaceTableAttributesDataspaceEntityType,
)
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    attribute_category: UpsertDataspaceTableAttributesDataspaceEntityType,
    attribute_id: UUID,
    *,
    body: DataspaceTableAttributePatchIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/dataspaces/{dataspace_id}/attributes/{attribute_category}/{attribute_id}/table/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            attribute_category=quote(str(attribute_category), safe=""),
            attribute_id=quote(str(attribute_id), safe=""),
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
    dataspace_id: UUID,
    attribute_category: UpsertDataspaceTableAttributesDataspaceEntityType,
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceTableAttributePatchIn,
) -> Response[Any]:
    """Update table attribute cells

     Set or update individual cells of a table attribute. Includes optimistic concurrency control via
    version to prevent conflicting edits.

    Args:
        dataspace_id (UUID):
        attribute_category (UpsertDataspaceTableAttributesDataspaceEntityType):
        attribute_id (UUID):
        body (DataspaceTableAttributePatchIn): Schema for updating table attribute cells via
            attribute_id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        attribute_category=attribute_category,
        attribute_id=attribute_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    dataspace_id: UUID,
    attribute_category: UpsertDataspaceTableAttributesDataspaceEntityType,
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceTableAttributePatchIn,
) -> Response[Any]:
    """Update table attribute cells

     Set or update individual cells of a table attribute. Includes optimistic concurrency control via
    version to prevent conflicting edits.

    Args:
        dataspace_id (UUID):
        attribute_category (UpsertDataspaceTableAttributesDataspaceEntityType):
        attribute_id (UUID):
        body (DataspaceTableAttributePatchIn): Schema for updating table attribute cells via
            attribute_id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        attribute_category=attribute_category,
        attribute_id=attribute_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
