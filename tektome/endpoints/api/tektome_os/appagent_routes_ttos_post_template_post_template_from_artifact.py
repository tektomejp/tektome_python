from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.template_from_artifact_in import TemplateFromArtifactIn
from ...models.template_out import TemplateOut
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    *,
    body: TemplateFromArtifactIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/agents/os/organizations/{organization_id}/templates/from-artifact/".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TemplateOut | None:
    if response.status_code == 201:
        response_201 = TemplateOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TemplateOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    body: TemplateFromArtifactIn,
) -> Response[TemplateOut]:
    """Create a new template from an existing artifact

     VxJkL9mN
    Create a new template from an existing artifact. The artifact must exist and belong to the user.

    Args:
        organization_id (UUID):
        body (TemplateFromArtifactIn): Schema for creating a new template from an artifact.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TemplateOut]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    body: TemplateFromArtifactIn,
) -> TemplateOut | None:
    """Create a new template from an existing artifact

     VxJkL9mN
    Create a new template from an existing artifact. The artifact must exist and belong to the user.

    Args:
        organization_id (UUID):
        body (TemplateFromArtifactIn): Schema for creating a new template from an artifact.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TemplateOut
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    body: TemplateFromArtifactIn,
) -> Response[TemplateOut]:
    """Create a new template from an existing artifact

     VxJkL9mN
    Create a new template from an existing artifact. The artifact must exist and belong to the user.

    Args:
        organization_id (UUID):
        body (TemplateFromArtifactIn): Schema for creating a new template from an artifact.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TemplateOut]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    body: TemplateFromArtifactIn,
) -> TemplateOut | None:
    """Create a new template from an existing artifact

     VxJkL9mN
    Create a new template from an existing artifact. The artifact must exist and belong to the user.

    Args:
        organization_id (UUID):
        body (TemplateFromArtifactIn): Schema for creating a new template from an artifact.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TemplateOut
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            body=body,
        )
    ).parsed
