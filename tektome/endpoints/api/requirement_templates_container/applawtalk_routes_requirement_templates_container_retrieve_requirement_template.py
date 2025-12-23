from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.requirement_template_get_out import RequirementTemplateGetOut
from ...types import Response


def _get_kwargs(
    requirement_template_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/requirement-templates-container/requirement-templates/{requirement_template_id}/".format(
            requirement_template_id=quote(str(requirement_template_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RequirementTemplateGetOut | None:
    if response.status_code == 200:
        response_200 = RequirementTemplateGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RequirementTemplateGetOut]:
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
) -> Response[RequirementTemplateGetOut]:
    """Retrieve Requirement Template

     B7GNMWvD

    Get single requirement templates inside a requirement template container.

    Args:
        requirement_template_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementTemplateGetOut]
    """

    kwargs = _get_kwargs(
        requirement_template_id=requirement_template_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
) -> RequirementTemplateGetOut | None:
    """Retrieve Requirement Template

     B7GNMWvD

    Get single requirement templates inside a requirement template container.

    Args:
        requirement_template_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementTemplateGetOut
    """

    return sync_detailed(
        requirement_template_id=requirement_template_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[RequirementTemplateGetOut]:
    """Retrieve Requirement Template

     B7GNMWvD

    Get single requirement templates inside a requirement template container.

    Args:
        requirement_template_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementTemplateGetOut]
    """

    kwargs = _get_kwargs(
        requirement_template_id=requirement_template_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_template_id: UUID,
    *,
    client: AuthenticatedClient,
) -> RequirementTemplateGetOut | None:
    """Retrieve Requirement Template

     B7GNMWvD

    Get single requirement templates inside a requirement template container.

    Args:
        requirement_template_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementTemplateGetOut
    """

    return (
        await asyncio_detailed(
            requirement_template_id=requirement_template_id,
            client=client,
        )
    ).parsed
