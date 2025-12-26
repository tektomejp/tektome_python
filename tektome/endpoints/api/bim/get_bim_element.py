from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_bim_element_bim_element_type_path import GetBimElementBimElementTypePath
from ...types import UNSET, Response


def _get_kwargs(
    bim_type: GetBimElementBimElementTypePath,
    *,
    id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/bim/bim-elements/{bim_type}/".format(
            bim_type=quote(str(bim_type), safe=""),
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
    bim_type: GetBimElementBimElementTypePath,
    *,
    client: AuthenticatedClient,
    id: str,
) -> Response[Any]:
    """Get Bim Element

     d4769d26

    Get a BIM element. Could be BIM object or view.

    Arguments:
        - bim_type: Type of BIM element (object or view)
        - id: The ID of the BIM element to retrieve

    Args:
        bim_type (GetBimElementBimElementTypePath): Enum for BIM object types.
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bim_type=bim_type,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    bim_type: GetBimElementBimElementTypePath,
    *,
    client: AuthenticatedClient,
    id: str,
) -> Response[Any]:
    """Get Bim Element

     d4769d26

    Get a BIM element. Could be BIM object or view.

    Arguments:
        - bim_type: Type of BIM element (object or view)
        - id: The ID of the BIM element to retrieve

    Args:
        bim_type (GetBimElementBimElementTypePath): Enum for BIM object types.
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bim_type=bim_type,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
