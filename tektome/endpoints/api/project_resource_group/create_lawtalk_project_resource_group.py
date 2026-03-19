from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resource_group_post_in import ResourceGroupPostIn
from ...models.resource_group_post_out import ResourceGroupPostOut
from ...types import Response


def _get_kwargs(
    project_id: UUID,
    *,
    body: ResourceGroupPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/projects/{project_id}/resource-groups/".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ResourceGroupPostOut | None:
    if response.status_code == 201:
        response_201 = ResourceGroupPostOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResourceGroupPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ResourceGroupPostIn,
) -> Response[ResourceGroupPostOut]:
    """Post Project Resource Group

     aidMfY1a

    Create resource group on project.

    Default lawtalk attributes are set
    - location == everything
    - structure == everything
    - building_type == everything
    - floors_above_ground >= 0
    - floors_below_ground >= 0
    - height >= 0.0
    - land_area >= 0.0
    - building_area >= 0.0

    Args:
        project_id (UUID):
        body (ResourceGroupPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceGroupPostOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ResourceGroupPostIn,
) -> ResourceGroupPostOut | None:
    """Post Project Resource Group

     aidMfY1a

    Create resource group on project.

    Default lawtalk attributes are set
    - location == everything
    - structure == everything
    - building_type == everything
    - floors_above_ground >= 0
    - floors_below_ground >= 0
    - height >= 0.0
    - land_area >= 0.0
    - building_area >= 0.0

    Args:
        project_id (UUID):
        body (ResourceGroupPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceGroupPostOut
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ResourceGroupPostIn,
) -> Response[ResourceGroupPostOut]:
    """Post Project Resource Group

     aidMfY1a

    Create resource group on project.

    Default lawtalk attributes are set
    - location == everything
    - structure == everything
    - building_type == everything
    - floors_above_ground >= 0
    - floors_below_ground >= 0
    - height >= 0.0
    - land_area >= 0.0
    - building_area >= 0.0

    Args:
        project_id (UUID):
        body (ResourceGroupPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceGroupPostOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ResourceGroupPostIn,
) -> ResourceGroupPostOut | None:
    """Post Project Resource Group

     aidMfY1a

    Create resource group on project.

    Default lawtalk attributes are set
    - location == everything
    - structure == everything
    - building_type == everything
    - floors_above_ground >= 0
    - floors_below_ground >= 0
    - height >= 0.0
    - land_area >= 0.0
    - building_area >= 0.0

    Args:
        project_id (UUID):
        body (ResourceGroupPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceGroupPostOut
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
