from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_organization_multi_part_body_params import CreateOrganizationMultiPartBodyParams
from ...models.create_organization_response import CreateOrganizationResponse
from ...models.organizations_get_out import OrganizationsGetOut
from ...types import Response


def _get_kwargs(
    *,
    body: CreateOrganizationMultiPartBodyParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/account/organizations/",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateOrganizationResponse | OrganizationsGetOut | None:
    if response.status_code == 201:
        response_201 = OrganizationsGetOut.from_dict(response.json())

        return response_201

    if response.status_code == 416:
        response_416 = CreateOrganizationResponse.from_dict(response.json())

        return response_416

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateOrganizationResponse | OrganizationsGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateOrganizationMultiPartBodyParams,
) -> Response[CreateOrganizationResponse | OrganizationsGetOut]:
    """Post Organization

     YSCUc2Fk

    Create a new organization.

    Allows optional custom UUID for tektome users.

    Args:
        body (CreateOrganizationMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrganizationResponse | OrganizationsGetOut]
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
    body: CreateOrganizationMultiPartBodyParams,
) -> CreateOrganizationResponse | OrganizationsGetOut | None:
    """Post Organization

     YSCUc2Fk

    Create a new organization.

    Allows optional custom UUID for tektome users.

    Args:
        body (CreateOrganizationMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrganizationResponse | OrganizationsGetOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateOrganizationMultiPartBodyParams,
) -> Response[CreateOrganizationResponse | OrganizationsGetOut]:
    """Post Organization

     YSCUc2Fk

    Create a new organization.

    Allows optional custom UUID for tektome users.

    Args:
        body (CreateOrganizationMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrganizationResponse | OrganizationsGetOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateOrganizationMultiPartBodyParams,
) -> CreateOrganizationResponse | OrganizationsGetOut | None:
    """Post Organization

     YSCUc2Fk

    Create a new organization.

    Allows optional custom UUID for tektome users.

    Args:
        body (CreateOrganizationMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrganizationResponse | OrganizationsGetOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
