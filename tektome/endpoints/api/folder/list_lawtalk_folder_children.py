from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lawtalk_folder_children_get_out import LawtalkFolderChildrenGetOut
from ...models.order_by import OrderBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    folder_id: UUID,
    *,
    sort_by: str | Unset = "name",
    order_by: None | OrderBy | Unset = OrderBy.ASCENDING,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    dataspace_id: None | Unset | UUID = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sort_by"] = sort_by

    json_order_by: None | str | Unset
    if isinstance(order_by, Unset):
        json_order_by = UNSET
    elif isinstance(order_by, OrderBy):
        json_order_by = order_by.value
    else:
        json_order_by = order_by
    params["order_by"] = json_order_by

    params["page"] = page

    params["page_size"] = page_size

    json_dataspace_id: None | str | Unset
    if isinstance(dataspace_id, Unset):
        json_dataspace_id = UNSET
    elif isinstance(dataspace_id, UUID):
        json_dataspace_id = str(dataspace_id)
    else:
        json_dataspace_id = dataspace_id
    params["dataspace_id"] = json_dataspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/folders/{folder_id}/children/".format(
            folder_id=quote(str(folder_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LawtalkFolderChildrenGetOut | None:
    if response.status_code == 200:
        response_200 = LawtalkFolderChildrenGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LawtalkFolderChildrenGetOut]:
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
    sort_by: str | Unset = "name",
    order_by: None | OrderBy | Unset = OrderBy.ASCENDING,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    dataspace_id: None | Unset | UUID = UNSET,
) -> Response[LawtalkFolderChildrenGetOut]:
    """Get Folder Children

     g7i4ub58

    Retrieve both folders and resources in current level. Folder will appear first in alphabetical
    order.

    Use cases:
        This is used in both main application page and admin page to show folders and resources.
        The uploaded resources in admin page are manually linked to resource group root folder.
        This is to cater pagination for both folders and resources in *admin page* only.

    Args:
        request: The HTTP request object.
        path_params: Path[FolderPathIn] object containing folder_id
        query_params: Query[FolderQuery] object containing pagination parameters

    Returns:

    Args:
        folder_id (UUID):
        sort_by (str | Unset):  Default: 'name'.
        order_by (None | OrderBy | Unset):  Default: OrderBy.ASCENDING.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        dataspace_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LawtalkFolderChildrenGetOut]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        sort_by=sort_by,
        order_by=order_by,
        page=page,
        page_size=page_size,
        dataspace_id=dataspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    folder_id: UUID,
    *,
    client: AuthenticatedClient,
    sort_by: str | Unset = "name",
    order_by: None | OrderBy | Unset = OrderBy.ASCENDING,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    dataspace_id: None | Unset | UUID = UNSET,
) -> LawtalkFolderChildrenGetOut | None:
    """Get Folder Children

     g7i4ub58

    Retrieve both folders and resources in current level. Folder will appear first in alphabetical
    order.

    Use cases:
        This is used in both main application page and admin page to show folders and resources.
        The uploaded resources in admin page are manually linked to resource group root folder.
        This is to cater pagination for both folders and resources in *admin page* only.

    Args:
        request: The HTTP request object.
        path_params: Path[FolderPathIn] object containing folder_id
        query_params: Query[FolderQuery] object containing pagination parameters

    Returns:

    Args:
        folder_id (UUID):
        sort_by (str | Unset):  Default: 'name'.
        order_by (None | OrderBy | Unset):  Default: OrderBy.ASCENDING.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        dataspace_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LawtalkFolderChildrenGetOut
    """

    return sync_detailed(
        folder_id=folder_id,
        client=client,
        sort_by=sort_by,
        order_by=order_by,
        page=page,
        page_size=page_size,
        dataspace_id=dataspace_id,
    ).parsed


async def asyncio_detailed(
    folder_id: UUID,
    *,
    client: AuthenticatedClient,
    sort_by: str | Unset = "name",
    order_by: None | OrderBy | Unset = OrderBy.ASCENDING,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    dataspace_id: None | Unset | UUID = UNSET,
) -> Response[LawtalkFolderChildrenGetOut]:
    """Get Folder Children

     g7i4ub58

    Retrieve both folders and resources in current level. Folder will appear first in alphabetical
    order.

    Use cases:
        This is used in both main application page and admin page to show folders and resources.
        The uploaded resources in admin page are manually linked to resource group root folder.
        This is to cater pagination for both folders and resources in *admin page* only.

    Args:
        request: The HTTP request object.
        path_params: Path[FolderPathIn] object containing folder_id
        query_params: Query[FolderQuery] object containing pagination parameters

    Returns:

    Args:
        folder_id (UUID):
        sort_by (str | Unset):  Default: 'name'.
        order_by (None | OrderBy | Unset):  Default: OrderBy.ASCENDING.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        dataspace_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LawtalkFolderChildrenGetOut]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        sort_by=sort_by,
        order_by=order_by,
        page=page,
        page_size=page_size,
        dataspace_id=dataspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    folder_id: UUID,
    *,
    client: AuthenticatedClient,
    sort_by: str | Unset = "name",
    order_by: None | OrderBy | Unset = OrderBy.ASCENDING,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    dataspace_id: None | Unset | UUID = UNSET,
) -> LawtalkFolderChildrenGetOut | None:
    """Get Folder Children

     g7i4ub58

    Retrieve both folders and resources in current level. Folder will appear first in alphabetical
    order.

    Use cases:
        This is used in both main application page and admin page to show folders and resources.
        The uploaded resources in admin page are manually linked to resource group root folder.
        This is to cater pagination for both folders and resources in *admin page* only.

    Args:
        request: The HTTP request object.
        path_params: Path[FolderPathIn] object containing folder_id
        query_params: Query[FolderQuery] object containing pagination parameters

    Returns:

    Args:
        folder_id (UUID):
        sort_by (str | Unset):  Default: 'name'.
        order_by (None | OrderBy | Unset):  Default: OrderBy.ASCENDING.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        dataspace_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LawtalkFolderChildrenGetOut
    """

    return (
        await asyncio_detailed(
            folder_id=folder_id,
            client=client,
            sort_by=sort_by,
            order_by=order_by,
            page=page,
            page_size=page_size,
            dataspace_id=dataspace_id,
        )
    ).parsed
