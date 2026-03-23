from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.section_creation_post_in import SectionCreationPostIn
from ...models.section_get_out import SectionGetOut
from ...types import Response


def _get_kwargs(
    *,
    body: SectionCreationPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/sections/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SectionGetOut | None:
    if response.status_code == 201:
        response_201 = SectionGetOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SectionGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SectionCreationPostIn,
) -> Response[SectionGetOut]:
    """Create Section

     JEi1TvH6

    Create a new section.

    Args:
        request: Request object.

    Returns: newly created section.

    Args:
        body (SectionCreationPostIn): Serializer for creating a new section.
            This serializer includes all necessary fields to create a section.
            It includes fields for resource IDs, page components, paragraphs, tables,
            chunk groups, and attributes.

            Attributes:
                project_id: ID of the project to bind the section.
                resource_ids: List of resource IDs to include in the section.
                page_ids: List of page IDs to include in the section.
                pages_paragraphs_paths: List of SectionParagraphPath to access for paragraphs in
            pages.
                pages_tables_paths: List of SectionTablePath to access for tables in pages.
                chunk_group_ids: List of chunk group IDs to include in the section.
                source_*_attributes: Lists of attributes to include in the section.

            Note:
                1. To retrive attributes' id from section, using GET /api/core/sections/{section_id}/
                    it will return all attributes' ids that are included in the section.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SectionGetOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SectionCreationPostIn,
) -> SectionGetOut | None:
    """Create Section

     JEi1TvH6

    Create a new section.

    Args:
        request: Request object.

    Returns: newly created section.

    Args:
        body (SectionCreationPostIn): Serializer for creating a new section.
            This serializer includes all necessary fields to create a section.
            It includes fields for resource IDs, page components, paragraphs, tables,
            chunk groups, and attributes.

            Attributes:
                project_id: ID of the project to bind the section.
                resource_ids: List of resource IDs to include in the section.
                page_ids: List of page IDs to include in the section.
                pages_paragraphs_paths: List of SectionParagraphPath to access for paragraphs in
            pages.
                pages_tables_paths: List of SectionTablePath to access for tables in pages.
                chunk_group_ids: List of chunk group IDs to include in the section.
                source_*_attributes: Lists of attributes to include in the section.

            Note:
                1. To retrive attributes' id from section, using GET /api/core/sections/{section_id}/
                    it will return all attributes' ids that are included in the section.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SectionGetOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SectionCreationPostIn,
) -> Response[SectionGetOut]:
    """Create Section

     JEi1TvH6

    Create a new section.

    Args:
        request: Request object.

    Returns: newly created section.

    Args:
        body (SectionCreationPostIn): Serializer for creating a new section.
            This serializer includes all necessary fields to create a section.
            It includes fields for resource IDs, page components, paragraphs, tables,
            chunk groups, and attributes.

            Attributes:
                project_id: ID of the project to bind the section.
                resource_ids: List of resource IDs to include in the section.
                page_ids: List of page IDs to include in the section.
                pages_paragraphs_paths: List of SectionParagraphPath to access for paragraphs in
            pages.
                pages_tables_paths: List of SectionTablePath to access for tables in pages.
                chunk_group_ids: List of chunk group IDs to include in the section.
                source_*_attributes: Lists of attributes to include in the section.

            Note:
                1. To retrive attributes' id from section, using GET /api/core/sections/{section_id}/
                    it will return all attributes' ids that are included in the section.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SectionGetOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SectionCreationPostIn,
) -> SectionGetOut | None:
    """Create Section

     JEi1TvH6

    Create a new section.

    Args:
        request: Request object.

    Returns: newly created section.

    Args:
        body (SectionCreationPostIn): Serializer for creating a new section.
            This serializer includes all necessary fields to create a section.
            It includes fields for resource IDs, page components, paragraphs, tables,
            chunk groups, and attributes.

            Attributes:
                project_id: ID of the project to bind the section.
                resource_ids: List of resource IDs to include in the section.
                page_ids: List of page IDs to include in the section.
                pages_paragraphs_paths: List of SectionParagraphPath to access for paragraphs in
            pages.
                pages_tables_paths: List of SectionTablePath to access for tables in pages.
                chunk_group_ids: List of chunk group IDs to include in the section.
                source_*_attributes: Lists of attributes to include in the section.

            Note:
                1. To retrive attributes' id from section, using GET /api/core/sections/{section_id}/
                    it will return all attributes' ids that are included in the section.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SectionGetOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
