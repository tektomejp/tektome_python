from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_requirement_research_template_request import CreateRequirementResearchTemplateRequest
from ...models.requirement_research_template_response import RequirementResearchTemplateResponse
from ...types import Response


def _get_kwargs(
    requirement_template_id: UUID,
    *,
    body: CreateRequirementResearchTemplateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/requirement-templates/{requirement_template_id}/research-templates/".format(
            requirement_template_id=quote(str(requirement_template_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RequirementResearchTemplateResponse | None:
    if response.status_code == 201:
        response_201 = RequirementResearchTemplateResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RequirementResearchTemplateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateRequirementResearchTemplateRequest,
) -> Response[RequirementResearchTemplateResponse]:
    """Create an AI research template

     Create a new AI research template for a requirement template. The specified public resource groups
    must already exist in the parent requirement template container.

    Args:
        requirement_template_id (UUID):
        body (CreateRequirementResearchTemplateRequest): Serializer for Requirement Template
            Research Template Post Input.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementResearchTemplateResponse]
    """

    kwargs = _get_kwargs(
        requirement_template_id=requirement_template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateRequirementResearchTemplateRequest,
) -> RequirementResearchTemplateResponse | None:
    """Create an AI research template

     Create a new AI research template for a requirement template. The specified public resource groups
    must already exist in the parent requirement template container.

    Args:
        requirement_template_id (UUID):
        body (CreateRequirementResearchTemplateRequest): Serializer for Requirement Template
            Research Template Post Input.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementResearchTemplateResponse
    """

    return sync_detailed(
        requirement_template_id=requirement_template_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateRequirementResearchTemplateRequest,
) -> Response[RequirementResearchTemplateResponse]:
    """Create an AI research template

     Create a new AI research template for a requirement template. The specified public resource groups
    must already exist in the parent requirement template container.

    Args:
        requirement_template_id (UUID):
        body (CreateRequirementResearchTemplateRequest): Serializer for Requirement Template
            Research Template Post Input.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementResearchTemplateResponse]
    """

    kwargs = _get_kwargs(
        requirement_template_id=requirement_template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateRequirementResearchTemplateRequest,
) -> RequirementResearchTemplateResponse | None:
    """Create an AI research template

     Create a new AI research template for a requirement template. The specified public resource groups
    must already exist in the parent requirement template container.

    Args:
        requirement_template_id (UUID):
        body (CreateRequirementResearchTemplateRequest): Serializer for Requirement Template
            Research Template Post Input.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementResearchTemplateResponse
    """

    return (
        await asyncio_detailed(
            requirement_template_id=requirement_template_id,
            client=client,
            body=body,
        )
    ).parsed
