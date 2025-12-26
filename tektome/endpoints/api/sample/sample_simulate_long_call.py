from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.simulate_long_call_post_out import SimulateLongCallPostOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    delay: float | Unset = 1.0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["delay"] = delay

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/sample/simulate-long-call/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SimulateLongCallPostOut | None:
    if response.status_code == 200:
        response_200 = SimulateLongCallPostOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SimulateLongCallPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    delay: float | Unset = 1.0,
) -> Response[SimulateLongCallPostOut]:
    """Simulate Long Call

     S0PPLHxz
    Simulate a long call in sync routes

    Args:
        delay (float | Unset):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SimulateLongCallPostOut]
    """

    kwargs = _get_kwargs(
        delay=delay,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    delay: float | Unset = 1.0,
) -> SimulateLongCallPostOut | None:
    """Simulate Long Call

     S0PPLHxz
    Simulate a long call in sync routes

    Args:
        delay (float | Unset):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SimulateLongCallPostOut
    """

    return sync_detailed(
        client=client,
        delay=delay,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    delay: float | Unset = 1.0,
) -> Response[SimulateLongCallPostOut]:
    """Simulate Long Call

     S0PPLHxz
    Simulate a long call in sync routes

    Args:
        delay (float | Unset):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SimulateLongCallPostOut]
    """

    kwargs = _get_kwargs(
        delay=delay,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    delay: float | Unset = 1.0,
) -> SimulateLongCallPostOut | None:
    """Simulate Long Call

     S0PPLHxz
    Simulate a long call in sync routes

    Args:
        delay (float | Unset):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SimulateLongCallPostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            delay=delay,
        )
    ).parsed
