from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.folder_post_in import FolderPostIn
from ...models.folder_post_out import FolderPostOut
from ...types import Response


def _get_kwargs(
    folder_id: UUID,
    *,
    body: FolderPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/folders/{folder_id}/subfolder/".format(
            folder_id=quote(str(folder_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FolderPostOut | None:
    if response.status_code == 201:
        response_201 = FolderPostOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FolderPostOut]:
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
    body: FolderPostIn,
) -> Response[FolderPostOut]:
    """Post Create Subfolder

     SPUDyo5b

    Create a new subfolder

    Args:
        request: Request object
        path_params: FolderPathIn object containing folder_id
        payload: FolderPostIn object containing name of the new folder

    Returns: Folder object containing the new folder

    Args:
        folder_id (UUID):
        body (FolderPostIn): Schema for creating a folder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FolderPostOut]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    folder_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FolderPostIn,
) -> FolderPostOut | None:
    """Post Create Subfolder

     SPUDyo5b

    Create a new subfolder

    Args:
        request: Request object
        path_params: FolderPathIn object containing folder_id
        payload: FolderPostIn object containing name of the new folder

    Returns: Folder object containing the new folder

    Args:
        folder_id (UUID):
        body (FolderPostIn): Schema for creating a folder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FolderPostOut
    """

    return sync_detailed(
        folder_id=folder_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    folder_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FolderPostIn,
) -> Response[FolderPostOut]:
    """Post Create Subfolder

     SPUDyo5b

    Create a new subfolder

    Args:
        request: Request object
        path_params: FolderPathIn object containing folder_id
        payload: FolderPostIn object containing name of the new folder

    Returns: Folder object containing the new folder

    Args:
        folder_id (UUID):
        body (FolderPostIn): Schema for creating a folder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FolderPostOut]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    folder_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FolderPostIn,
) -> FolderPostOut | None:
    """Post Create Subfolder

     SPUDyo5b

    Create a new subfolder

    Args:
        request: Request object
        path_params: FolderPathIn object containing folder_id
        payload: FolderPostIn object containing name of the new folder

    Returns: Folder object containing the new folder

    Args:
        folder_id (UUID):
        body (FolderPostIn): Schema for creating a folder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FolderPostOut
    """

    return (
        await asyncio_detailed(
            folder_id=folder_id,
            client=client,
            body=body,
        )
    ).parsed
