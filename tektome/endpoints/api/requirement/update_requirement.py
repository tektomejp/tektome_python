from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.requirement_patch_in_patch import RequirementPatchInPatch
from ...models.requirement_schema import RequirementSchema
from ...types import Response


def _get_kwargs(
    requirement_id: UUID,
    *,
    body: RequirementPatchInPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/app/lawtalk/requirements/{requirement_id}/".format(
            requirement_id=quote(str(requirement_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RequirementSchema | None:
    if response.status_code == 200:
        response_200 = RequirementSchema.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RequirementSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementPatchInPatch,
) -> Response[RequirementSchema]:
    """Patch Requirement

     L6y3h9iF

    Update a requirement given a project id and requirement id

    Args:
        requirement_id (UUID):
        body (RequirementPatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementSchema]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementPatchInPatch,
) -> RequirementSchema | None:
    """Patch Requirement

     L6y3h9iF

    Update a requirement given a project id and requirement id

    Args:
        requirement_id (UUID):
        body (RequirementPatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementSchema
    """

    return sync_detailed(
        requirement_id=requirement_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementPatchInPatch,
) -> Response[RequirementSchema]:
    """Patch Requirement

     L6y3h9iF

    Update a requirement given a project id and requirement id

    Args:
        requirement_id (UUID):
        body (RequirementPatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementSchema]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RequirementPatchInPatch,
) -> RequirementSchema | None:
    """Patch Requirement

     L6y3h9iF

    Update a requirement given a project id and requirement id

    Args:
        requirement_id (UUID):
        body (RequirementPatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementSchema
    """

    return (
        await asyncio_detailed(
            requirement_id=requirement_id,
            client=client,
            body=body,
        )
    ).parsed
