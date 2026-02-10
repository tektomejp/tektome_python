from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_object_3d_response_get_out import BimObject3DResponseGetOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bim_project_id: UUID,
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/bim/bim-project/{bim_project_id}/bim-object/3d/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimObject3DResponseGetOut | None:
    if response.status_code == 200:
        response_200 = BimObject3DResponseGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimObject3DResponseGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> Response[BimObject3DResponseGetOut]:
    """Get Bim Project 3D Objects

     96ce9cff

    Get all 3D BIM objects for a project with pagination.
    Returns base64-encoded file content for each object.

    Args:
        path: Path parameters containing the BIM project ID
        page: Page number (starts from 1)
        page_size: Number of objects per page (between 1 and 250)

    Args:
        bim_project_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimObject3DResponseGetOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> BimObject3DResponseGetOut | None:
    """Get Bim Project 3D Objects

     96ce9cff

    Get all 3D BIM objects for a project with pagination.
    Returns base64-encoded file content for each object.

    Args:
        path: Path parameters containing the BIM project ID
        page: Page number (starts from 1)
        page_size: Number of objects per page (between 1 and 250)

    Args:
        bim_project_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimObject3DResponseGetOut
    """

    return sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> Response[BimObject3DResponseGetOut]:
    """Get Bim Project 3D Objects

     96ce9cff

    Get all 3D BIM objects for a project with pagination.
    Returns base64-encoded file content for each object.

    Args:
        path: Path parameters containing the BIM project ID
        page: Page number (starts from 1)
        page_size: Number of objects per page (between 1 and 250)

    Args:
        bim_project_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimObject3DResponseGetOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> BimObject3DResponseGetOut | None:
    """Get Bim Project 3D Objects

     96ce9cff

    Get all 3D BIM objects for a project with pagination.
    Returns base64-encoded file content for each object.

    Args:
        path: Path parameters containing the BIM project ID
        page: Page number (starts from 1)
        page_size: Number of objects per page (between 1 and 250)

    Args:
        bim_project_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimObject3DResponseGetOut
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            client=client,
            page=page,
            page_size=page_size,
        )
    ).parsed
