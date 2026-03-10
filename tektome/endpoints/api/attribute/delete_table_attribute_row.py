from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_table_attribute_row_attribute_object_types import DeleteTableAttributeRowAttributeObjectTypes
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_type: DeleteTableAttributeRowAttributeObjectTypes,
    object_id: UUID,
    *,
    name: str,
    row_index: int,
    version: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params["row_index"] = row_index

    json_version: int | None | Unset
    if isinstance(version, Unset):
        json_version = UNSET
    else:
        json_version = version
    params["version"] = json_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/core/attributes/general/{object_type}/{object_id}/table/row/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
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
    object_type: DeleteTableAttributeRowAttributeObjectTypes,
    object_id: UUID,
    *,
    client: AuthenticatedClient,
    name: str,
    row_index: int,
    version: int | None | Unset = UNSET,
) -> Response[Any]:
    """Delete Table Row

     TuDNpTaM

    Delete a row from a table attribute.

    Args:
        object_type (DeleteTableAttributeRowAttributeObjectTypes):
        object_id (UUID):
        name (str):
        row_index (int):
        version (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        name=name,
        row_index=row_index,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    object_type: DeleteTableAttributeRowAttributeObjectTypes,
    object_id: UUID,
    *,
    client: AuthenticatedClient,
    name: str,
    row_index: int,
    version: int | None | Unset = UNSET,
) -> Response[Any]:
    """Delete Table Row

     TuDNpTaM

    Delete a row from a table attribute.

    Args:
        object_type (DeleteTableAttributeRowAttributeObjectTypes):
        object_id (UUID):
        name (str):
        row_index (int):
        version (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        name=name,
        row_index=row_index,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
