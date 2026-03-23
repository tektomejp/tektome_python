from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.core_project_post_in import CoreProjectPostIn
from ...models.dataspace_projects_schema_out import DataspaceProjectsSchemaOut
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    *,
    body: CoreProjectPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/projects/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DataspaceProjectsSchemaOut | None:
    if response.status_code == 201:
        response_201 = DataspaceProjectsSchemaOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DataspaceProjectsSchemaOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CoreProjectPostIn,
) -> Response[DataspaceProjectsSchemaOut]:
    """Post Dataspace Project

     ttCTKUG5

    Create a new project in the current dataspace.
    - Creates a project root folder by default.
    - Creates project admin and invited user groups.

    Args:
        dataspace_id (UUID):
        body (CoreProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceProjectsSchemaOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CoreProjectPostIn,
) -> DataspaceProjectsSchemaOut | None:
    """Post Dataspace Project

     ttCTKUG5

    Create a new project in the current dataspace.
    - Creates a project root folder by default.
    - Creates project admin and invited user groups.

    Args:
        dataspace_id (UUID):
        body (CoreProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceProjectsSchemaOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CoreProjectPostIn,
) -> Response[DataspaceProjectsSchemaOut]:
    """Post Dataspace Project

     ttCTKUG5

    Create a new project in the current dataspace.
    - Creates a project root folder by default.
    - Creates project admin and invited user groups.

    Args:
        dataspace_id (UUID):
        body (CoreProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceProjectsSchemaOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CoreProjectPostIn,
) -> DataspaceProjectsSchemaOut | None:
    """Post Dataspace Project

     ttCTKUG5

    Create a new project in the current dataspace.
    - Creates a project root folder by default.
    - Creates project admin and invited user groups.

    Args:
        dataspace_id (UUID):
        body (CoreProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceProjectsSchemaOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            client=client,
            body=body,
        )
    ).parsed
