from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_simulate_task_request import CreateSimulateTaskRequest
from ...models.simulate_task_response import SimulateTaskResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CreateSimulateTaskRequest,
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


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SimulateTaskResponse | None:
    if response.status_code == 200:
        response_200 = SimulateTaskResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SimulateTaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSimulateTaskRequest,
    delay: int,
) -> Response[SimulateTaskResponse]:
    """Simulate an asynchronous task

     Submit a sample asynchronous task for testing purposes. This is an asynchronous operation. To
    retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the
    task/process ID returned in this response.

    Args:
        delay (int):
        body (CreateSimulateTaskRequest): For demonstration purpose, this should be in
            /serializers/<same_name_as_this_file>.py

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SimulateTaskResponse]
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
    body: CreateSimulateTaskRequest,
    delay: int,
) -> SimulateTaskResponse | None:
    """Simulate an asynchronous task

     Submit a sample asynchronous task for testing purposes. This is an asynchronous operation. To
    retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the
    task/process ID returned in this response.

    Args:
        delay (int):
        body (CreateSimulateTaskRequest): For demonstration purpose, this should be in
            /serializers/<same_name_as_this_file>.py

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SimulateTaskResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        delay=delay,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSimulateTaskRequest,
    delay: int,
) -> Response[SimulateTaskResponse]:
    """Simulate an asynchronous task

     Submit a sample asynchronous task for testing purposes. This is an asynchronous operation. To
    retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the
    task/process ID returned in this response.

    Args:
        delay (int):
        body (CreateSimulateTaskRequest): For demonstration purpose, this should be in
            /serializers/<same_name_as_this_file>.py

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SimulateTaskResponse]
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
    body: CreateSimulateTaskRequest,
    delay: int,
) -> SimulateTaskResponse | None:
    """Simulate an asynchronous task

     Submit a sample asynchronous task for testing purposes. This is an asynchronous operation. To
    retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the
    task/process ID returned in this response.

    Args:
        delay (int):
        body (CreateSimulateTaskRequest): For demonstration purpose, this should be in
            /serializers/<same_name_as_this_file>.py

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SimulateTaskResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            delay=delay,
        )
    ).parsed
