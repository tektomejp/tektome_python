from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.applawtalk_routes_requirements_post_capture_section_component_multi_part_body_params import (
    ApplawtalkRoutesRequirementsPostCaptureSectionComponentMultiPartBodyParams,
)
from ...models.resource_capture_section_component_schema import ResourceCaptureSectionComponentSchema
from ...types import Response


def _get_kwargs(
    section_id: UUID,
    *,
    body: ApplawtalkRoutesRequirementsPostCaptureSectionComponentMultiPartBodyParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/requirements/sections/{section_id}/section-component/capture/".format(
            section_id=quote(str(section_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ResourceCaptureSectionComponentSchema | None:
    if response.status_code == 201:
        response_201 = ResourceCaptureSectionComponentSchema.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResourceCaptureSectionComponentSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    section_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ApplawtalkRoutesRequirementsPostCaptureSectionComponentMultiPartBodyParams,
) -> Response[ResourceCaptureSectionComponentSchema]:
    """Post Capture Section Component

     y0Pe8-Po


    Create a CaptureSectionComponent object

    Args:
        request: Request object
        path_params: path params of type CreateCaptureSectionComponentPath
        payload: request payload of type CreateCaptureSectionComponentPostIn
        screenshot_file: image file object

    Returns: 201, CaptureSectionComponentSchema

    Args:
        section_id (UUID):
        body (ApplawtalkRoutesRequirementsPostCaptureSectionComponentMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceCaptureSectionComponentSchema]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    section_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ApplawtalkRoutesRequirementsPostCaptureSectionComponentMultiPartBodyParams,
) -> ResourceCaptureSectionComponentSchema | None:
    """Post Capture Section Component

     y0Pe8-Po


    Create a CaptureSectionComponent object

    Args:
        request: Request object
        path_params: path params of type CreateCaptureSectionComponentPath
        payload: request payload of type CreateCaptureSectionComponentPostIn
        screenshot_file: image file object

    Returns: 201, CaptureSectionComponentSchema

    Args:
        section_id (UUID):
        body (ApplawtalkRoutesRequirementsPostCaptureSectionComponentMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceCaptureSectionComponentSchema
    """

    return sync_detailed(
        section_id=section_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    section_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ApplawtalkRoutesRequirementsPostCaptureSectionComponentMultiPartBodyParams,
) -> Response[ResourceCaptureSectionComponentSchema]:
    """Post Capture Section Component

     y0Pe8-Po


    Create a CaptureSectionComponent object

    Args:
        request: Request object
        path_params: path params of type CreateCaptureSectionComponentPath
        payload: request payload of type CreateCaptureSectionComponentPostIn
        screenshot_file: image file object

    Returns: 201, CaptureSectionComponentSchema

    Args:
        section_id (UUID):
        body (ApplawtalkRoutesRequirementsPostCaptureSectionComponentMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceCaptureSectionComponentSchema]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    section_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ApplawtalkRoutesRequirementsPostCaptureSectionComponentMultiPartBodyParams,
) -> ResourceCaptureSectionComponentSchema | None:
    """Post Capture Section Component

     y0Pe8-Po


    Create a CaptureSectionComponent object

    Args:
        request: Request object
        path_params: path params of type CreateCaptureSectionComponentPath
        payload: request payload of type CreateCaptureSectionComponentPostIn
        screenshot_file: image file object

    Returns: 201, CaptureSectionComponentSchema

    Args:
        section_id (UUID):
        body (ApplawtalkRoutesRequirementsPostCaptureSectionComponentMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceCaptureSectionComponentSchema
    """

    return (
        await asyncio_detailed(
            section_id=section_id,
            client=client,
            body=body,
        )
    ).parsed
