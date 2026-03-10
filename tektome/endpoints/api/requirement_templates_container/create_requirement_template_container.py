from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.requirement_template_container_get_out import RequirementTemplateContainerGetOut
from ...models.requirement_template_container_post_in import RequirementTemplateContainerPostIn
from ...types import Response


def _get_kwargs(
    *,
    body: RequirementTemplateContainerPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/requirement-templates-container/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RequirementTemplateContainerGetOut | None:
    if response.status_code == 201:
        response_201 = RequirementTemplateContainerGetOut.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: RequirementTemplateContainerPostIn,
) -> Response[RequirementTemplateContainerGetOut]:
    """Post Requirement Template Container

     B7GNMW11

    Create a requirement given a project id in the payload.

    Args:
        body (RequirementTemplateContainerPostIn): Serializer for Requirement Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementTemplateContainerGetOut]
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
    body: RequirementTemplateContainerPostIn,
) -> RequirementTemplateContainerGetOut | None:
    """Post Requirement Template Container

     B7GNMW11

    Create a requirement given a project id in the payload.

    Args:
        body (RequirementTemplateContainerPostIn): Serializer for Requirement Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementTemplateContainerGetOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RequirementTemplateContainerPostIn,
) -> Response[RequirementTemplateContainerGetOut]:
    """Post Requirement Template Container

     B7GNMW11

    Create a requirement given a project id in the payload.

    Args:
        body (RequirementTemplateContainerPostIn): Serializer for Requirement Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementTemplateContainerGetOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RequirementTemplateContainerPostIn,
) -> RequirementTemplateContainerGetOut | None:
    """Post Requirement Template Container

     B7GNMW11

    Create a requirement given a project id in the payload.

    Args:
        body (RequirementTemplateContainerPostIn): Serializer for Requirement Template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementTemplateContainerGetOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
