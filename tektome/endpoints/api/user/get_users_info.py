from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_info_response import GetUsersInfoResponse
from ...models.me_get_out_without_organization import MeGetOutWithoutOrganization
from ...types import UNSET, Response


def _get_kwargs(
    *,
    ids: list[UUID],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids = []
    for ids_item_data in ids:
        ids_item = str(ids_item_data)
        json_ids.append(ids_item)

    params["ids"] = json_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/account/users/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetUsersInfoResponse | list[MeGetOutWithoutOrganization] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MeGetOutWithoutOrganization.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetUsersInfoResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetUsersInfoResponse | list[MeGetOutWithoutOrganization]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[UUID],
) -> Response[GetUsersInfoResponse | list[MeGetOutWithoutOrganization]]:
    """Get Users Info

     1wcEjKTo

    Get info for a list of users by their IDs.

    Args:
        ids (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersInfoResponse | list[MeGetOutWithoutOrganization]]
    """

    kwargs = _get_kwargs(
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[UUID],
) -> GetUsersInfoResponse | list[MeGetOutWithoutOrganization] | None:
    """Get Users Info

     1wcEjKTo

    Get info for a list of users by their IDs.

    Args:
        ids (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersInfoResponse | list[MeGetOutWithoutOrganization]
    """

    return sync_detailed(
        client=client,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[UUID],
) -> Response[GetUsersInfoResponse | list[MeGetOutWithoutOrganization]]:
    """Get Users Info

     1wcEjKTo

    Get info for a list of users by their IDs.

    Args:
        ids (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersInfoResponse | list[MeGetOutWithoutOrganization]]
    """

    kwargs = _get_kwargs(
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[UUID],
) -> GetUsersInfoResponse | list[MeGetOutWithoutOrganization] | None:
    """Get Users Info

     1wcEjKTo

    Get info for a list of users by their IDs.

    Args:
        ids (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersInfoResponse | list[MeGetOutWithoutOrganization]
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
        )
    ).parsed
