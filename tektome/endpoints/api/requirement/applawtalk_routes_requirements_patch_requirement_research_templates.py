from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.requirement_view_research_template_patch_in import RequirementViewResearchTemplatePatchIn
from ...types import Response


def _get_kwargs(
    requirement_id: UUID,
    research_template_id: UUID,
    *,
    body: RequirementViewResearchTemplatePatchIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/app/lawtalk/requirements/{requirement_id}/research-templates/{research_template_id}/".format(
            requirement_id=quote(str(requirement_id), safe=""),
            research_template_id=quote(str(research_template_id), safe=""),
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
    requirement_id: UUID,
    research_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementViewResearchTemplatePatchIn,
) -> Response[Any]:
    """Patch Requirement Research Templates

     JnQkM31N

    Update the view status of a research template associated to a requirement's requirement template

    Args:
        request: Request object
        path_params: path params of type RequirementResearchTemplatePath
        payload: request payload of type RequirementViewResearchTemplatePatchIn

    Args:
        requirement_id (UUID):
        research_template_id (UUID):
        body (RequirementViewResearchTemplatePatchIn): Schema for updating a Requirement Research
            Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        research_template_id=research_template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    requirement_id: UUID,
    research_template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementViewResearchTemplatePatchIn,
) -> Response[Any]:
    """Patch Requirement Research Templates

     JnQkM31N

    Update the view status of a research template associated to a requirement's requirement template

    Args:
        request: Request object
        path_params: path params of type RequirementResearchTemplatePath
        payload: request payload of type RequirementViewResearchTemplatePatchIn

    Args:
        requirement_id (UUID):
        research_template_id (UUID):
        body (RequirementViewResearchTemplatePatchIn): Schema for updating a Requirement Research
            Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        research_template_id=research_template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
