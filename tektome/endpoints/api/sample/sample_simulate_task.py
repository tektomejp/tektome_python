from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.simulate_task_post_in import SimulateTaskPostIn
from ...models.simulate_task_post_out import SimulateTaskPostOut
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: SimulateTaskPostIn,
    delay: int,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["delay"] = delay

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/sample/simulate-task/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SimulateTaskPostOut | None:
    if response.status_code == 200:
        response_200 = SimulateTaskPostOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SimulateTaskPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SimulateTaskPostIn,
    delay: int,
) -> Response[SimulateTaskPostOut]:
    """Post Simulate Task

     3F0LPj5x
    Simulate an async task to test the celery worker.

    Args:
        delay (int):
        body (SimulateTaskPostIn): For demonstration purpose, this should be in
            /serializers/<same_name_as_this_file>.py

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SimulateTaskPostOut]
    """

    kwargs = _get_kwargs(
        body=body,
        delay=delay,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SimulateTaskPostIn,
    delay: int,
) -> SimulateTaskPostOut | None:
    """Post Simulate Task

     3F0LPj5x
    Simulate an async task to test the celery worker.

    Args:
        delay (int):
        body (SimulateTaskPostIn): For demonstration purpose, this should be in
            /serializers/<same_name_as_this_file>.py

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SimulateTaskPostOut
    """

    return sync_detailed(
        client=client,
        body=body,
        delay=delay,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SimulateTaskPostIn,
    delay: int,
) -> Response[SimulateTaskPostOut]:
    """Post Simulate Task

     3F0LPj5x
    Simulate an async task to test the celery worker.

    Args:
        delay (int):
        body (SimulateTaskPostIn): For demonstration purpose, this should be in
            /serializers/<same_name_as_this_file>.py

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SimulateTaskPostOut]
    """

    kwargs = _get_kwargs(
        body=body,
        delay=delay,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SimulateTaskPostIn,
    delay: int,
) -> SimulateTaskPostOut | None:
    """Post Simulate Task

     3F0LPj5x
    Simulate an async task to test the celery worker.

    Args:
        delay (int):
        body (SimulateTaskPostIn): For demonstration purpose, this should be in
            /serializers/<same_name_as_this_file>.py

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SimulateTaskPostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            delay=delay,
        )
    ).parsed
