from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lawtalk_general_attribute_body_put_in import LawtalkGeneralAttributeBodyPutIn
from ...models.update_general_lawtalk_attributes_attribute_object_types import (
    UpdateGeneralLawtalkAttributesAttributeObjectTypes,
)
from ...types import Response


def _get_kwargs(
    object_type: UpdateGeneralLawtalkAttributesAttributeObjectTypes,
    object_id: UUID,
    *,
    body: LawtalkGeneralAttributeBodyPutIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/app/lawtalk/attributes/general/{object_type}/{object_id}/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
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
    object_type: UpdateGeneralLawtalkAttributesAttributeObjectTypes,
    object_id: UUID,
    *,
    client: AuthenticatedClient,
    body: LawtalkGeneralAttributeBodyPutIn,
) -> Response[Any]:
    """Put General Lawtalk Attributes

     gL48dbrw

    Set or update Lawtalk-specific attributes given lawtalk object ID as entrypoint.
    Allows all general and system attributes.

    To set an entity to be public, set the `system:is_public` boolean attribute to `true`.
    All system attributes will be returned without system prefix. e.g `is_public` instead of
    `system:is_public`.

    Args:
        object_type (UpdateGeneralLawtalkAttributesAttributeObjectTypes):
        object_id (UUID):
        body (LawtalkGeneralAttributeBodyPutIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    object_type: UpdateGeneralLawtalkAttributesAttributeObjectTypes,
    object_id: UUID,
    *,
    client: AuthenticatedClient,
    body: LawtalkGeneralAttributeBodyPutIn,
) -> Response[Any]:
    """Put General Lawtalk Attributes

     gL48dbrw

    Set or update Lawtalk-specific attributes given lawtalk object ID as entrypoint.
    Allows all general and system attributes.

    To set an entity to be public, set the `system:is_public` boolean attribute to `true`.
    All system attributes will be returned without system prefix. e.g `is_public` instead of
    `system:is_public`.

    Args:
        object_type (UpdateGeneralLawtalkAttributesAttributeObjectTypes):
        object_id (UUID):
        body (LawtalkGeneralAttributeBodyPutIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
