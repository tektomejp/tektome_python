from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bim_project_id: UUID,
    *,
    id_only: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id_only"] = id_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/bim/bim-object/project/{bim_project_id}/stream/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    id_only: bool | Unset = False,
) -> Response[Any]:
    """Get Bim Objects By Project

     JQCKkusu

    Get all BIM objects linked to a specific project.
    Args:
        bim_project_id: The ID of the BIM project to retrieve objects for.
    Returns:
        A list of BIM objects linked to the specified project.

    Args:
        bim_project_id (UUID):
        id_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        id_only=id_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    id_only: bool | Unset = False,
) -> Response[Any]:
    """Get Bim Objects By Project

     JQCKkusu

    Get all BIM objects linked to a specific project.
    Args:
        bim_project_id: The ID of the BIM project to retrieve objects for.
    Returns:
        A list of BIM objects linked to the specified project.

    Args:
        bim_project_id (UUID):
        id_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        id_only=id_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
