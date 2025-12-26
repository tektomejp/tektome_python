from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.requirement_research_template_get_out import RequirementResearchTemplateGetOut
from ...types import Response


def _get_kwargs(
    research_template_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/requirement-templates/research-templates/{research_template_id}/".format(
            research_template_id=quote(str(research_template_id), safe=""),
        ),
    }

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
) -> Response[RequirementResearchTemplateGetOut]:
    """Retrieve Research Template

     R1C1E1A4

    Retrieve a research template by its ID.

    Args:
        path_params: Path parameters containing the research_template_id.

    Returns: The retrieved ResearchTemplate instance.

    Args:
        research_template_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementResearchTemplateGetOut]
    """

    kwargs = _get_kwargs(
        research_template_id=research_template_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    research_template_id: UUID,
    *,
    client: AuthenticatedClient,
) -> RequirementResearchTemplateGetOut | None:
    """Retrieve Research Template

     R1C1E1A4

    Retrieve a research template by its ID.

    Args:
        path_params: Path parameters containing the research_template_id.

    Returns: The retrieved ResearchTemplate instance.

    Args:
        research_template_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementResearchTemplateGetOut
    """

    return sync_detailed(
        research_template_id=research_template_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    research_template_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[RequirementResearchTemplateGetOut]:
    """Retrieve Research Template

     R1C1E1A4

    Retrieve a research template by its ID.

    Args:
        path_params: Path parameters containing the research_template_id.

    Returns: The retrieved ResearchTemplate instance.

    Args:
        research_template_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementResearchTemplateGetOut]
    """

    kwargs = _get_kwargs(
        research_template_id=research_template_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    research_template_id: UUID,
    *,
    client: AuthenticatedClient,
) -> RequirementResearchTemplateGetOut | None:
    """Retrieve Research Template

     R1C1E1A4

    Retrieve a research template by its ID.

    Args:
        path_params: Path parameters containing the research_template_id.

    Returns: The retrieved ResearchTemplate instance.

    Args:
        research_template_id (UUID):

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
        )
    ).parsed
