from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.requirement_research_template_response import RequirementResearchTemplateResponse
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
) -> RequirementResearchTemplateResponse | None:
    if response.status_code == 200:
        response_200 = RequirementResearchTemplateResponse.from_dict(response.json())

        return response_200

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
    research_template_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[RequirementResearchTemplateResponse]:
    """Get an AI research template by ID

     Retrieve a specific AI research template by its ID.

    Args:
        research_template_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementResearchTemplateResponse]
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
) -> RequirementResearchTemplateResponse | None:
    """Get an AI research template by ID

     Retrieve a specific AI research template by its ID.

    Args:
        research_template_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementResearchTemplateResponse
    """

    return sync_detailed(
        research_template_id=research_template_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    research_template_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[RequirementResearchTemplateResponse]:
    """Get an AI research template by ID

     Retrieve a specific AI research template by its ID.

    Args:
        research_template_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementResearchTemplateResponse]
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
) -> RequirementResearchTemplateResponse | None:
    """Get an AI research template by ID

     Retrieve a specific AI research template by its ID.

    Args:
        research_template_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementResearchTemplateResponse
    """

    return (
        await asyncio_detailed(
            research_template_id=research_template_id,
            client=client,
        )
    ).parsed
