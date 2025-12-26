from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sample_simulate_unhandled_exception_response import SampleSimulateUnhandledExceptionResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/sample/simulate-unhandled-exception/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SampleSimulateUnhandledExceptionResponse | None:
    if response.status_code == 200:
        response_200 = SampleSimulateUnhandledExceptionResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SampleSimulateUnhandledExceptionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[SampleSimulateUnhandledExceptionResponse]:
    """Get Simulate Unhandled Exception

     S0PPLHxa
    Simulate unhandled exception

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SampleSimulateUnhandledExceptionResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> SampleSimulateUnhandledExceptionResponse | None:
    """Get Simulate Unhandled Exception

     S0PPLHxa
    Simulate unhandled exception

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SampleSimulateUnhandledExceptionResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[SampleSimulateUnhandledExceptionResponse]:
    """Get Simulate Unhandled Exception

     S0PPLHxa
    Simulate unhandled exception

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SampleSimulateUnhandledExceptionResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> SampleSimulateUnhandledExceptionResponse | None:
    """Get Simulate Unhandled Exception

     S0PPLHxa
    Simulate unhandled exception

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SampleSimulateUnhandledExceptionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
