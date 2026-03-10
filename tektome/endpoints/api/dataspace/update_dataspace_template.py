from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.template_out import TemplateOut
from ...models.template_override_in import TemplateOverrideIn
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    template_id: UUID,
    *,
    body: TemplateOverrideIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/dataspaces/{dataspace_id}/templates/{template_id}/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            template_id=quote(str(template_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TemplateOut | None:
    if response.status_code == 200:
        response_200 = TemplateOut.from_dict(response.json())

        return response_200

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
    dataspace_id: UUID,
    template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: TemplateOverrideIn,
) -> Response[TemplateOut]:
    """Patch Dataspace Template

     gQK6dWXU

    Update a template in the current dataspace.

    Args:
        dataspace_id (UUID):
        template_id (UUID): The ID of an existing template.
        body (TemplateOverrideIn): Schema for modifying the arguments of dataspace/project-level
            templates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TemplateOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        template_id=template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: TemplateOverrideIn,
) -> TemplateOut | None:
    """Patch Dataspace Template

     gQK6dWXU

    Update a template in the current dataspace.

    Args:
        dataspace_id (UUID):
        template_id (UUID): The ID of an existing template.
        body (TemplateOverrideIn): Schema for modifying the arguments of dataspace/project-level
            templates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TemplateOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        template_id=template_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: TemplateOverrideIn,
) -> Response[TemplateOut]:
    """Patch Dataspace Template

     gQK6dWXU

    Update a template in the current dataspace.

    Args:
        dataspace_id (UUID):
        template_id (UUID): The ID of an existing template.
        body (TemplateOverrideIn): Schema for modifying the arguments of dataspace/project-level
            templates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TemplateOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        template_id=template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: TemplateOverrideIn,
) -> TemplateOut | None:
    """Patch Dataspace Template

     gQK6dWXU

    Update a template in the current dataspace.

    Args:
        dataspace_id (UUID):
        template_id (UUID): The ID of an existing template.
        body (TemplateOverrideIn): Schema for modifying the arguments of dataspace/project-level
            templates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TemplateOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            template_id=template_id,
            client=client,
            body=body,
        )
    ).parsed
