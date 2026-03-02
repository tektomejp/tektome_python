from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_citation_polygon_annotation_get_out import ImageCitationPolygonAnnotationGetOut
from ...models.image_citation_polygon_annotation_post_in import ImageCitationPolygonAnnotationPostIn
from ...models.post_image_citation_polygon_annotation_dataspace_entity_type import (
    PostImageCitationPolygonAnnotationDataspaceEntityType,
)
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    attribute_category: PostImageCitationPolygonAnnotationDataspaceEntityType,
    attribute_id: UUID,
    image_citation_id: UUID,
    *,
    body: ImageCitationPolygonAnnotationPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/attributes/{attribute_category}/{attribute_id}/image-citations/{image_citation_id}/polygon-annotations/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            attribute_category=quote(str(attribute_category), safe=""),
            attribute_id=quote(str(attribute_id), safe=""),
            image_citation_id=quote(str(image_citation_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ImageCitationPolygonAnnotationGetOut | None:
    if response.status_code == 201:
        response_201 = ImageCitationPolygonAnnotationGetOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ImageCitationPolygonAnnotationGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    attribute_category: PostImageCitationPolygonAnnotationDataspaceEntityType,
    attribute_id: UUID,
    image_citation_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ImageCitationPolygonAnnotationPostIn,
) -> Response[ImageCitationPolygonAnnotationGetOut]:
    """Add a polygon annotation to the image citation.

     Creates a new image citation polygon

    Args:
        dataspace_id (UUID):
        attribute_category (PostImageCitationPolygonAnnotationDataspaceEntityType):
        attribute_id (UUID):
        image_citation_id (UUID):
        body (ImageCitationPolygonAnnotationPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImageCitationPolygonAnnotationGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        attribute_category=attribute_category,
        attribute_id=attribute_id,
        image_citation_id=image_citation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    attribute_category: PostImageCitationPolygonAnnotationDataspaceEntityType,
    attribute_id: UUID,
    image_citation_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ImageCitationPolygonAnnotationPostIn,
) -> ImageCitationPolygonAnnotationGetOut | None:
    """Add a polygon annotation to the image citation.

     Creates a new image citation polygon

    Args:
        dataspace_id (UUID):
        attribute_category (PostImageCitationPolygonAnnotationDataspaceEntityType):
        attribute_id (UUID):
        image_citation_id (UUID):
        body (ImageCitationPolygonAnnotationPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImageCitationPolygonAnnotationGetOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        attribute_category=attribute_category,
        attribute_id=attribute_id,
        image_citation_id=image_citation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    attribute_category: PostImageCitationPolygonAnnotationDataspaceEntityType,
    attribute_id: UUID,
    image_citation_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ImageCitationPolygonAnnotationPostIn,
) -> Response[ImageCitationPolygonAnnotationGetOut]:
    """Add a polygon annotation to the image citation.

     Creates a new image citation polygon

    Args:
        dataspace_id (UUID):
        attribute_category (PostImageCitationPolygonAnnotationDataspaceEntityType):
        attribute_id (UUID):
        image_citation_id (UUID):
        body (ImageCitationPolygonAnnotationPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImageCitationPolygonAnnotationGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        attribute_category=attribute_category,
        attribute_id=attribute_id,
        image_citation_id=image_citation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    attribute_category: PostImageCitationPolygonAnnotationDataspaceEntityType,
    attribute_id: UUID,
    image_citation_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ImageCitationPolygonAnnotationPostIn,
) -> ImageCitationPolygonAnnotationGetOut | None:
    """Add a polygon annotation to the image citation.

     Creates a new image citation polygon

    Args:
        dataspace_id (UUID):
        attribute_category (PostImageCitationPolygonAnnotationDataspaceEntityType):
        attribute_id (UUID):
        image_citation_id (UUID):
        body (ImageCitationPolygonAnnotationPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImageCitationPolygonAnnotationGetOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            attribute_category=attribute_category,
            attribute_id=attribute_id,
            image_citation_id=image_citation_id,
            client=client,
            body=body,
        )
    ).parsed
