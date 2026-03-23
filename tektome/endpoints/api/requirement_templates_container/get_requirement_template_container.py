from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.requirement_template_container_get_out import RequirementTemplateContainerGetOut
from ...types import Response


def _get_kwargs(
    requirement_template_container_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/requirement-templates-container/{requirement_template_container_id}/".format(
            requirement_template_container_id=quote(str(requirement_template_container_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RequirementTemplateContainerGetOut | None:
    if response.status_code == 200:
        response_200 = RequirementTemplateContainerGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RequirementTemplateContainerGetOut]:
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
) -> Response[RequirementTemplateContainerGetOut]:
    """Retrieve Requirement Template Container

     B7GNMWv6

    Get all requirement templates containers

    Args:
        requirement_template_container_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementTemplateContainerGetOut]
    """

    kwargs = _get_kwargs(
        requirement_template_container_id=requirement_template_container_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_template_container_id: UUID,
    *,
    client: AuthenticatedClient,
) -> RequirementTemplateContainerGetOut | None:
    """Retrieve Requirement Template Container

     B7GNMWv6

    Get all requirement templates containers

    Args:
        requirement_template_container_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementTemplateContainerGetOut
    """

    return sync_detailed(
        requirement_template_container_id=requirement_template_container_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    requirement_template_container_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[RequirementTemplateContainerGetOut]:
    """Retrieve Requirement Template Container

     B7GNMWv6

    Get all requirement templates containers

    Args:
        requirement_template_container_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementTemplateContainerGetOut]
    """

    kwargs = _get_kwargs(
        requirement_template_container_id=requirement_template_container_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_template_container_id: UUID,
    *,
    client: AuthenticatedClient,
) -> RequirementTemplateContainerGetOut | None:
    """Retrieve Requirement Template Container

     B7GNMWv6

    Get all requirement templates containers

    Args:
        requirement_template_container_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementTemplateContainerGetOut
    """

    return (
        await asyncio_detailed(
            requirement_template_container_id=requirement_template_container_id,
            client=client,
        )
    ).parsed
