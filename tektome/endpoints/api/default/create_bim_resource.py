from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_project_post_out import BimProjectPostOut
from ...models.create_bim_resource_file_params import CreateBimResourceFileParams
from ...types import UNSET, Response, Unset


def _get_kwargs(
    resource_group_id: UUID,
    *,
    body: CreateBimResourceFileParams,
    project_name: str | Unset = "Default Project",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["project_name"] = project_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-elements/{resource_group_id}/resources/version-control/".format(
            resource_group_id=quote(str(resource_group_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BimProjectPostOut | None:
    if response.status_code == 200:
        response_200 = BimProjectPostOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BimProjectPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateBimResourceFileParams,
    project_name: str | Unset = "Default Project",
) -> Response[BimProjectPostOut]:
    """Create Bim Resource

     jv0wF1EG

    Create a new BIM resource with the given file.
    Only accepts Revit files (.rvt, .rfa, .rte).

    Args:
        resource_group_id (UUID):
        project_name (str | Unset):  Default: 'Default Project'.
        body (CreateBimResourceFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimProjectPostOut]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
        body=body,
        project_name=project_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateBimResourceFileParams,
    project_name: str | Unset = "Default Project",
) -> BimProjectPostOut | None:
    """Create Bim Resource

     jv0wF1EG

    Create a new BIM resource with the given file.
    Only accepts Revit files (.rvt, .rfa, .rte).

    Args:
        resource_group_id (UUID):
        project_name (str | Unset):  Default: 'Default Project'.
        body (CreateBimResourceFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimProjectPostOut
    """

    return sync_detailed(
        resource_group_id=resource_group_id,
        client=client,
        body=body,
        project_name=project_name,
    ).parsed


async def asyncio_detailed(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateBimResourceFileParams,
    project_name: str | Unset = "Default Project",
) -> Response[BimProjectPostOut]:
    """Create Bim Resource

     jv0wF1EG

    Create a new BIM resource with the given file.
    Only accepts Revit files (.rvt, .rfa, .rte).

    Args:
        resource_group_id (UUID):
        project_name (str | Unset):  Default: 'Default Project'.
        body (CreateBimResourceFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimProjectPostOut]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
        body=body,
        project_name=project_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateBimResourceFileParams,
    project_name: str | Unset = "Default Project",
) -> BimProjectPostOut | None:
    """Create Bim Resource

     jv0wF1EG

    Create a new BIM resource with the given file.
    Only accepts Revit files (.rvt, .rfa, .rte).

    Args:
        resource_group_id (UUID):
        project_name (str | Unset):  Default: 'Default Project'.
        body (CreateBimResourceFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimProjectPostOut
    """

    return (
        await asyncio_detailed(
            resource_group_id=resource_group_id,
            client=client,
            body=body,
            project_name=project_name,
        )
    ).parsed
