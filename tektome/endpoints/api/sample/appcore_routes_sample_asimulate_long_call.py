from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.a_simulate_long_call_post_out import ASimulateLongCallPostOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sync_delay: float | Unset = 0.5,
    async_delay: float | Unset = 0.5,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sync_delay"] = sync_delay

    params["async_delay"] = async_delay

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/sample/asimulate-long-call/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ASimulateLongCallPostOut | None:
    if response.status_code == 200:
        response_200 = ASimulateLongCallPostOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ASimulateLongCallPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    sync_delay: float | Unset = 0.5,
    async_delay: float | Unset = 0.5,
) -> Response[ASimulateLongCallPostOut]:
    """Asimulate Long Call

     L2y-7-xi
    Simulate a long call in async routes
    sync_delay: `sleep(sync_delay)`
    async_delay: `await asyncio.sleep(async_delay)`

    Args:
        sync_delay (float | Unset):  Default: 0.5.
        async_delay (float | Unset):  Default: 0.5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ASimulateLongCallPostOut]
    """

    kwargs = _get_kwargs(
        sync_delay=sync_delay,
        async_delay=async_delay,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sync_delay: float | Unset = 0.5,
    async_delay: float | Unset = 0.5,
) -> ASimulateLongCallPostOut | None:
    """Asimulate Long Call

     L2y-7-xi
    Simulate a long call in async routes
    sync_delay: `sleep(sync_delay)`
    async_delay: `await asyncio.sleep(async_delay)`

    Args:
        sync_delay (float | Unset):  Default: 0.5.
        async_delay (float | Unset):  Default: 0.5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ASimulateLongCallPostOut
    """

    return sync_detailed(
        client=client,
        sync_delay=sync_delay,
        async_delay=async_delay,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sync_delay: float | Unset = 0.5,
    async_delay: float | Unset = 0.5,
) -> Response[ASimulateLongCallPostOut]:
    """Asimulate Long Call

     L2y-7-xi
    Simulate a long call in async routes
    sync_delay: `sleep(sync_delay)`
    async_delay: `await asyncio.sleep(async_delay)`

    Args:
        sync_delay (float | Unset):  Default: 0.5.
        async_delay (float | Unset):  Default: 0.5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ASimulateLongCallPostOut]
    """

    kwargs = _get_kwargs(
        sync_delay=sync_delay,
        async_delay=async_delay,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sync_delay: float | Unset = 0.5,
    async_delay: float | Unset = 0.5,
) -> ASimulateLongCallPostOut | None:
    """Asimulate Long Call

     L2y-7-xi
    Simulate a long call in async routes
    sync_delay: `sleep(sync_delay)`
    async_delay: `await asyncio.sleep(async_delay)`

    Args:
        sync_delay (float | Unset):  Default: 0.5.
        async_delay (float | Unset):  Default: 0.5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ASimulateLongCallPostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            sync_delay=sync_delay,
            async_delay=async_delay,
        )
    ).parsed
