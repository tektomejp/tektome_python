from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.folder_get_out import FolderGetOut
from ...types import Response


def _get_kwargs(
    folder_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/folders/{folder_id}/".format(
            folder_id=quote(str(folder_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FolderGetOut | None:
    if response.status_code == 200:
        response_200 = FolderGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FolderGetOut]:
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
) -> Response[FolderGetOut]:
    """Get Folder

     isvFT8ZQ

    Get a folder and list all
    - resources
    - children of the folder

    Args:
        request: Request object
        path_params: Path parameters containing folder_id

    Returns: Folder containing resources and children

    Args:
        folder_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FolderGetOut]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    folder_id: UUID,
    *,
    client: AuthenticatedClient,
) -> FolderGetOut | None:
    """Get Folder

     isvFT8ZQ

    Get a folder and list all
    - resources
    - children of the folder

    Args:
        request: Request object
        path_params: Path parameters containing folder_id

    Returns: Folder containing resources and children

    Args:
        folder_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FolderGetOut
    """

    return sync_detailed(
        folder_id=folder_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    folder_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[FolderGetOut]:
    """Get Folder

     isvFT8ZQ

    Get a folder and list all
    - resources
    - children of the folder

    Args:
        request: Request object
        path_params: Path parameters containing folder_id

    Returns: Folder containing resources and children

    Args:
        folder_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FolderGetOut]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    folder_id: UUID,
    *,
    client: AuthenticatedClient,
) -> FolderGetOut | None:
    """Get Folder

     isvFT8ZQ

    Get a folder and list all
    - resources
    - children of the folder

    Args:
        request: Request object
        path_params: Path parameters containing folder_id

    Returns: Folder containing resources and children

    Args:
        folder_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FolderGetOut
    """

    return (
        await asyncio_detailed(
            folder_id=folder_id,
            client=client,
        )
    ).parsed
