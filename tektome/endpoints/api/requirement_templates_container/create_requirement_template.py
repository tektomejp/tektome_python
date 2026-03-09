from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.requirement_template_get_out import RequirementTemplateGetOut
from ...models.requirement_template_post_in import RequirementTemplatePostIn
from ...types import Response


def _get_kwargs(
    requirement_template_container_id: UUID,
    *,
    body: RequirementTemplatePostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/requirement-templates-container/{requirement_template_container_id}/requirement-templates/".format(
            requirement_template_container_id=quote(str(requirement_template_container_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RequirementTemplateGetOut | None:
    if response.status_code == 201:
        response_201 = RequirementTemplateGetOut.from_dict(response.json())

        return response_201

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
    requirement_template_container_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementTemplatePostIn,
) -> Response[RequirementTemplateGetOut]:
    """Post Requirement Template

     B7GNMWv9

    Create a requirement template inside a requirement template container.

    Args:
        requirement_template_container_id (UUID):
        body (RequirementTemplatePostIn): Serializer for creating a Requirement Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementTemplateGetOut]
    """

    kwargs = _get_kwargs(
        requirement_template_container_id=requirement_template_container_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_template_container_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementTemplatePostIn,
) -> RequirementTemplateGetOut | None:
    """Post Requirement Template

     B7GNMWv9

    Create a requirement template inside a requirement template container.

    Args:
        requirement_template_container_id (UUID):
        body (RequirementTemplatePostIn): Serializer for creating a Requirement Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementTemplateGetOut
    """

    return sync_detailed(
        requirement_template_container_id=requirement_template_container_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    requirement_template_container_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementTemplatePostIn,
) -> Response[RequirementTemplateGetOut]:
    """Post Requirement Template

     B7GNMWv9

    Create a requirement template inside a requirement template container.

    Args:
        requirement_template_container_id (UUID):
        body (RequirementTemplatePostIn): Serializer for creating a Requirement Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementTemplateGetOut]
    """

    kwargs = _get_kwargs(
        requirement_template_container_id=requirement_template_container_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_template_container_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementTemplatePostIn,
) -> RequirementTemplateGetOut | None:
    """Post Requirement Template

     B7GNMWv9

    Create a requirement template inside a requirement template container.

    Args:
        requirement_template_container_id (UUID):
        body (RequirementTemplatePostIn): Serializer for creating a Requirement Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementTemplateGetOut
    """

    return (
        await asyncio_detailed(
            requirement_template_container_id=requirement_template_container_id,
            client=client,
            body=body,
        )
    ).parsed
