from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.template_response import TemplateResponse
from ...models.template_update_request import TemplateUpdateRequest
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    template_id: UUID,
    *,
    body: TemplateUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/agents/os/organizations/{organization_id}/templates/{template_id}/".format(
            organization_id=quote(str(organization_id), safe=""),
            template_id=quote(str(template_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TemplateResponse | None:
    if response.status_code == 200:
        response_200 = TemplateResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TemplateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: TemplateUpdateRequest,
) -> Response[TemplateResponse]:
    """Update a process template

     Update the metadata of an existing organization-level process template. System-level templates
    cannot be modified.

    Args:
        organization_id (UUID):
        template_id (UUID): The ID of an existing template.
        body (TemplateUpdateRequest): Schema for updating an existing template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TemplateResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        template_id=template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: TemplateUpdateRequest,
) -> TemplateResponse | None:
    """Update a process template

     Update the metadata of an existing organization-level process template. System-level templates
    cannot be modified.

    Args:
        organization_id (UUID):
        template_id (UUID): The ID of an existing template.
        body (TemplateUpdateRequest): Schema for updating an existing template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TemplateResponse
    """

    return sync_detailed(
        organization_id=organization_id,
        template_id=template_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: TemplateUpdateRequest,
) -> Response[TemplateResponse]:
    """Update a process template

     Update the metadata of an existing organization-level process template. System-level templates
    cannot be modified.

    Args:
        organization_id (UUID):
        template_id (UUID): The ID of an existing template.
        body (TemplateUpdateRequest): Schema for updating an existing template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TemplateResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        template_id=template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: TemplateUpdateRequest,
) -> TemplateResponse | None:
    """Update a process template

     Update the metadata of an existing organization-level process template. System-level templates
    cannot be modified.

    Args:
        organization_id (UUID):
        template_id (UUID): The ID of an existing template.
        body (TemplateUpdateRequest): Schema for updating an existing template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TemplateResponse
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            template_id=template_id,
            client=client,
            body=body,
        )
    ).parsed
