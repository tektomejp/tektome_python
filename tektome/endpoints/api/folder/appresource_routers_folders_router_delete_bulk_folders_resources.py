from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_folder_resources_schema import DeleteFolderResourcesSchema
from ...types import Response


def _get_kwargs(
    folder_id: UUID,
    *,
    body: DeleteFolderResourcesSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/core/folders/{folder_id}/subfolders-resources/".format(
            folder_id=quote(str(folder_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: DeleteFolderResourcesSchema,
) -> Response[Any]:
    """Delete Bulk Folders Resources

     Delete parent's subfolders and it's subfolders/resources together with same level resources.

    Args:
        path_params: Path[FolderPathIn] object containing folder_id
        request: Request object
        payload: DeleteFolderResourcesSchema object containing ids of folders to be deleted

    Returns: 204, None

    Args:
        folder_id (UUID):
        body (DeleteFolderResourcesSchema): Schema for deleting resources and folders by their
            IDs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    folder_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DeleteFolderResourcesSchema,
) -> Response[Any]:
    """Delete Bulk Folders Resources

     Delete parent's subfolders and it's subfolders/resources together with same level resources.

    Args:
        path_params: Path[FolderPathIn] object containing folder_id
        request: Request object
        payload: DeleteFolderResourcesSchema object containing ids of folders to be deleted

    Returns: 204, None

    Args:
        folder_id (UUID):
        body (DeleteFolderResourcesSchema): Schema for deleting resources and folders by their
            IDs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
