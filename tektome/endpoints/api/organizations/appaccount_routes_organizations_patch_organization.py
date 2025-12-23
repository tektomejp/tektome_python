from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appaccount_routes_organizations_patch_organization_multi_part_body_params import (
    AppaccountRoutesOrganizationsPatchOrganizationMultiPartBodyParams,
)
from ...models.error_output_schema_out import ErrorOutputSchemaOut
from ...models.organizations_get_out import OrganizationsGetOut
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    *,
    body: AppaccountRoutesOrganizationsPatchOrganizationMultiPartBodyParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/account/organizations/{organization_id}/".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorOutputSchemaOut | OrganizationsGetOut | None:
    if response.status_code == 200:
        response_200 = OrganizationsGetOut.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorOutputSchemaOut.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorOutputSchemaOut | OrganizationsGetOut]:
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
    body: AppaccountRoutesOrganizationsPatchOrganizationMultiPartBodyParams,
) -> Response[ErrorOutputSchemaOut | OrganizationsGetOut]:
    """Patch Organization

     k3_uR6LY

    Update an organization.

    Args:
        organization_id (UUID):
        body (AppaccountRoutesOrganizationsPatchOrganizationMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOutputSchemaOut | OrganizationsGetOut]
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
    body: AppaccountRoutesOrganizationsPatchOrganizationMultiPartBodyParams,
) -> ErrorOutputSchemaOut | OrganizationsGetOut | None:
    """Patch Organization

     k3_uR6LY

    Update an organization.

    Args:
        organization_id (UUID):
        body (AppaccountRoutesOrganizationsPatchOrganizationMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOutputSchemaOut | OrganizationsGetOut
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
    body: AppaccountRoutesOrganizationsPatchOrganizationMultiPartBodyParams,
) -> Response[ErrorOutputSchemaOut | OrganizationsGetOut]:
    """Patch Organization

     k3_uR6LY

    Update an organization.

    Args:
        organization_id (UUID):
        body (AppaccountRoutesOrganizationsPatchOrganizationMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOutputSchemaOut | OrganizationsGetOut]
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
    body: AppaccountRoutesOrganizationsPatchOrganizationMultiPartBodyParams,
) -> ErrorOutputSchemaOut | OrganizationsGetOut | None:
    """Patch Organization

     k3_uR6LY

    Update an organization.

    Args:
        organization_id (UUID):
        body (AppaccountRoutesOrganizationsPatchOrganizationMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOutputSchemaOut | OrganizationsGetOut
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            body=body,
        )
    ).parsed
