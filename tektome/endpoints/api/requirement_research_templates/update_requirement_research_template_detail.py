from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.requirement_research_template_get_out import RequirementResearchTemplateGetOut
from ...models.requirement_research_template_patch_in_patch import RequirementResearchTemplatePatchInPatch
from ...types import Response


def _get_kwargs(
    research_template_id: UUID,
    *,
    body: RequirementResearchTemplatePatchInPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/app/lawtalk/requirement-templates/research-templates/{research_template_id}/".format(
            research_template_id=quote(str(research_template_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RequirementResearchTemplateGetOut | None:
    if response.status_code == 200:
        response_200 = RequirementResearchTemplateGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RequirementResearchTemplateGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    research_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementResearchTemplatePatchInPatch,
) -> Response[RequirementResearchTemplateGetOut]:
    """Patch Research Template

     R1C1E1A2

    Update a research template by its ID.

    Args:
        research_template_id (UUID):
        body (RequirementResearchTemplatePatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementResearchTemplateGetOut]
    """

    kwargs = _get_kwargs(
        research_template_id=research_template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    research_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementResearchTemplatePatchInPatch,
) -> RequirementResearchTemplateGetOut | None:
    """Patch Research Template

     R1C1E1A2

    Update a research template by its ID.

    Args:
        research_template_id (UUID):
        body (RequirementResearchTemplatePatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementResearchTemplateGetOut
    """

    return sync_detailed(
        research_template_id=research_template_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    research_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementResearchTemplatePatchInPatch,
) -> Response[RequirementResearchTemplateGetOut]:
    """Patch Research Template

     R1C1E1A2

    Update a research template by its ID.

    Args:
        research_template_id (UUID):
        body (RequirementResearchTemplatePatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementResearchTemplateGetOut]
    """

    kwargs = _get_kwargs(
        research_template_id=research_template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    research_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementResearchTemplatePatchInPatch,
) -> RequirementResearchTemplateGetOut | None:
    """Patch Research Template

     R1C1E1A2

    Update a research template by its ID.

    Args:
        research_template_id (UUID):
        body (RequirementResearchTemplatePatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementResearchTemplateGetOut
    """

    return (
        await asyncio_detailed(
            research_template_id=research_template_id,
            client=client,
            body=body,
        )
    ).parsed
