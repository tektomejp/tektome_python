from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_key_value_stats_post_response import BimKeyValueStatsPostResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bim_project_id: UUID,
    *,
    refresh: bool | Unset = False,
    limit_keys: int | Unset = 1000,
    limit_values: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["refresh"] = refresh

    params["limit_keys"] = limit_keys

    params["limit_values"] = limit_values

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-tools/key-value-stats/{bim_project_id}/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimKeyValueStatsPostResponse | str | None:
    if response.status_code == 200:
        response_200 = BimKeyValueStatsPostResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400

    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404

    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimKeyValueStatsPostResponse | str]:
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
    refresh: bool | Unset = False,
    limit_keys: int | Unset = 1000,
    limit_values: int | Unset = 50,
) -> Response[BimKeyValueStatsPostResponse | str]:
    """Trigger Bim Kv Stats Generation

     TYYVPyz5

    Trigger generation of BIM key-value statistics for a given BIM project.

    Returns:
        200: Task submission with process_id
        400: Invalid parameters
        404: BIM project not found
        500: Internal server error

    Args:
        bim_project_id (UUID):
        refresh (bool | Unset):  Default: False.
        limit_keys (int | Unset):  Default: 1000.
        limit_values (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimKeyValueStatsPostResponse | str]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        refresh=refresh,
        limit_keys=limit_keys,
        limit_values=limit_values,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    refresh: bool | Unset = False,
    limit_keys: int | Unset = 1000,
    limit_values: int | Unset = 50,
) -> BimKeyValueStatsPostResponse | str | None:
    """Trigger Bim Kv Stats Generation

     TYYVPyz5

    Trigger generation of BIM key-value statistics for a given BIM project.

    Returns:
        200: Task submission with process_id
        400: Invalid parameters
        404: BIM project not found
        500: Internal server error

    Args:
        bim_project_id (UUID):
        refresh (bool | Unset):  Default: False.
        limit_keys (int | Unset):  Default: 1000.
        limit_values (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimKeyValueStatsPostResponse | str
    """

    return sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
        refresh=refresh,
        limit_keys=limit_keys,
        limit_values=limit_values,
    ).parsed


async def asyncio_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    refresh: bool | Unset = False,
    limit_keys: int | Unset = 1000,
    limit_values: int | Unset = 50,
) -> Response[BimKeyValueStatsPostResponse | str]:
    """Trigger Bim Kv Stats Generation

     TYYVPyz5

    Trigger generation of BIM key-value statistics for a given BIM project.

    Returns:
        200: Task submission with process_id
        400: Invalid parameters
        404: BIM project not found
        500: Internal server error

    Args:
        bim_project_id (UUID):
        refresh (bool | Unset):  Default: False.
        limit_keys (int | Unset):  Default: 1000.
        limit_values (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimKeyValueStatsPostResponse | str]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        refresh=refresh,
        limit_keys=limit_keys,
        limit_values=limit_values,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    refresh: bool | Unset = False,
    limit_keys: int | Unset = 1000,
    limit_values: int | Unset = 50,
) -> BimKeyValueStatsPostResponse | str | None:
    """Trigger Bim Kv Stats Generation

     TYYVPyz5

    Trigger generation of BIM key-value statistics for a given BIM project.

    Returns:
        200: Task submission with process_id
        400: Invalid parameters
        404: BIM project not found
        500: Internal server error

    Args:
        bim_project_id (UUID):
        refresh (bool | Unset):  Default: False.
        limit_keys (int | Unset):  Default: 1000.
        limit_values (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimKeyValueStatsPostResponse | str
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            client=client,
            refresh=refresh,
            limit_keys=limit_keys,
            limit_values=limit_values,
        )
    ).parsed
