from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_bim_element_bim_element_type_path import GetBimElementBimElementTypePath
from ...models.get_bim_element_response import GetBimElementResponse
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


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetBimElementResponse | None:
    if response.status_code == 200:
        response_200 = GetBimElementResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetBimElementResponse]:
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
) -> Response[GetBimElementResponse]:
    """Get a single BIM element

     Retrieve a BIM element (object or view) by its ID and type.

    Args:
        bim_type (GetBimElementBimElementTypePath): Enum for BIM object types.
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBimElementResponse]
    """

    kwargs = _get_kwargs(
        bim_type=bim_type,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_type: GetBimElementBimElementTypePath,
    *,
    client: AuthenticatedClient,
    id: str,
) -> GetBimElementResponse | None:
    """Get a single BIM element

     Retrieve a BIM element (object or view) by its ID and type.

    Args:
        bim_type (GetBimElementBimElementTypePath): Enum for BIM object types.
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBimElementResponse
    """

    return sync_detailed(
        bim_type=bim_type,
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    bim_type: GetBimElementBimElementTypePath,
    *,
    client: AuthenticatedClient,
    id: str,
) -> Response[GetBimElementResponse]:
    """Get a single BIM element

     Retrieve a BIM element (object or view) by its ID and type.

    Args:
        bim_type (GetBimElementBimElementTypePath): Enum for BIM object types.
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBimElementResponse]
    """

    kwargs = _get_kwargs(
        bim_type=bim_type,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_type: GetBimElementBimElementTypePath,
    *,
    client: AuthenticatedClient,
    id: str,
) -> GetBimElementResponse | None:
    """Get a single BIM element

     Retrieve a BIM element (object or view) by its ID and type.

    Args:
        bim_type (GetBimElementBimElementTypePath): Enum for BIM object types.
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBimElementResponse
    """

    return (
        await asyncio_detailed(
            bim_type=bim_type,
            client=client,
            id=id,
        )
    ).parsed
