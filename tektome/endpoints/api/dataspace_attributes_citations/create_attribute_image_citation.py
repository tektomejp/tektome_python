from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_attribute_image_citation_dataspace_entity_type import (
    CreateAttributeImageCitationDataspaceEntityType,
)
from ...models.create_image_citation_request import CreateImageCitationRequest
from ...models.error_response import ErrorResponse
from ...models.image_citation_schema_response import ImageCitationSchemaResponse
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    attribute_category: CreateAttributeImageCitationDataspaceEntityType,
    attribute_id: UUID,
    *,
    body: CreateImageCitationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/attributes/{attribute_category}/{attribute_id}/image-citations/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            attribute_category=quote(str(attribute_category), safe=""),
            attribute_id=quote(str(attribute_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ImageCitationSchemaResponse | None:
    if response.status_code == 201:
        response_201 = ImageCitationSchemaResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = ErrorResponse.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = ErrorResponse.from_dict(response.json())

        return response_406

    if response.status_code == 407:
        response_407 = ErrorResponse.from_dict(response.json())

        return response_407

    if response.status_code == 408:
        response_408 = ErrorResponse.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 411:
        response_411 = ErrorResponse.from_dict(response.json())

        return response_411

    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412

    if response.status_code == 416:
        response_416 = ErrorResponse.from_dict(response.json())

        return response_416

    if response.status_code == 418:
        response_418 = ErrorResponse.from_dict(response.json())

        return response_418

    if response.status_code == 425:
        response_425 = ErrorResponse.from_dict(response.json())

        return response_425

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 451:
        response_451 = ErrorResponse.from_dict(response.json())

        return response_451

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ImageCitationSchemaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    attribute_category: CreateAttributeImageCitationDataspaceEntityType,
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateImageCitationRequest,
) -> Response[ErrorResponse | ImageCitationSchemaResponse]:
    """Create an image citation for an attribute

     Create a new image citation linking an image source to the specified attribute.

    Args:
        dataspace_id (UUID):
        attribute_category (CreateAttributeImageCitationDataspaceEntityType):
        attribute_id (UUID):
        body (CreateImageCitationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ImageCitationSchemaResponse]
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


def sync(
    dataspace_id: UUID,
    attribute_category: CreateAttributeImageCitationDataspaceEntityType,
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateImageCitationRequest,
) -> ErrorResponse | ImageCitationSchemaResponse | None:
    """Create an image citation for an attribute

     Create a new image citation linking an image source to the specified attribute.

    Args:
        dataspace_id (UUID):
        attribute_category (CreateAttributeImageCitationDataspaceEntityType):
        attribute_id (UUID):
        body (CreateImageCitationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ImageCitationSchemaResponse
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        attribute_category=attribute_category,
        attribute_id=attribute_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    attribute_category: CreateAttributeImageCitationDataspaceEntityType,
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateImageCitationRequest,
) -> Response[ErrorResponse | ImageCitationSchemaResponse]:
    """Create an image citation for an attribute

     Create a new image citation linking an image source to the specified attribute.

    Args:
        dataspace_id (UUID):
        attribute_category (CreateAttributeImageCitationDataspaceEntityType):
        attribute_id (UUID):
        body (CreateImageCitationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ImageCitationSchemaResponse]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        attribute_category=attribute_category,
        attribute_id=attribute_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    attribute_category: CreateAttributeImageCitationDataspaceEntityType,
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateImageCitationRequest,
) -> ErrorResponse | ImageCitationSchemaResponse | None:
    """Create an image citation for an attribute

     Create a new image citation linking an image source to the specified attribute.

    Args:
        dataspace_id (UUID):
        attribute_category (CreateAttributeImageCitationDataspaceEntityType):
        attribute_id (UUID):
        body (CreateImageCitationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ImageCitationSchemaResponse
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            attribute_category=attribute_category,
            attribute_id=attribute_id,
            client=client,
            body=body,
        )
    ).parsed
