from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    folder_id: UUID,
    *,
    include_resources: bool | Unset = False,
    force: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_resources"] = include_resources

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/core/folders/{folder_id}/".format(
            folder_id=quote(str(folder_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
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
    folder_id: UUID,
    *,
    client: AuthenticatedClient,
    include_resources: bool | Unset = False,
    force: bool | Unset = False,
) -> Response[Any]:
    """Delete Folder

     k4-aSnXD

    Delete a folder. User may choose to also delete all resources in the folder.

    Args:
        request: Request object
        path_params: FolderPathIn object containing folder_id
        query_params: FolderDeleteQuery object containing delete options

    Returns: None

    Args:
        folder_id (UUID):
        include_resources (bool | Unset):  Default: False.
        force (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        include_resources=include_resources,
        force=force,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    folder_id: UUID,
    *,
    client: AuthenticatedClient,
    include_resources: bool | Unset = False,
    force: bool | Unset = False,
) -> Response[Any]:
    """Delete Folder

     k4-aSnXD

    Delete a folder. User may choose to also delete all resources in the folder.

    Args:
        request: Request object
        path_params: FolderPathIn object containing folder_id
        query_params: FolderDeleteQuery object containing delete options

    Returns: None

    Args:
        folder_id (UUID):
        include_resources (bool | Unset):  Default: False.
        force (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        include_resources=include_resources,
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
