from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execution_group_get_out_2 import ExecutionGroupGetOut2
from ...types import Response


def _get_kwargs(
    execution_group_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/agents/os/execution-groups/{execution_group_id}/".format(
            execution_group_id=quote(str(execution_group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExecutionGroupGetOut2 | None:
    if response.status_code == 200:
        response_200 = ExecutionGroupGetOut2.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExecutionGroupGetOut2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    execution_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ExecutionGroupGetOut2]:
    """Get Execution Group

     VNpQ2rat

    Retrieve details of a specific execution group by its ID.

    Args:
        request: HttpRequest - The incoming HTTP request.
        path_params: ExecutionGroupPathParams - The path parameters containing the execution group ID.

    Returns: ExecutionGroup - The execution group instance.

    Args:
        execution_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecutionGroupGetOut2]
    """

    kwargs = _get_kwargs(
        execution_group_id=execution_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    execution_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ExecutionGroupGetOut2 | None:
    """Get Execution Group

     VNpQ2rat

    Retrieve details of a specific execution group by its ID.

    Args:
        request: HttpRequest - The incoming HTTP request.
        path_params: ExecutionGroupPathParams - The path parameters containing the execution group ID.

    Returns: ExecutionGroup - The execution group instance.

    Args:
        execution_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecutionGroupGetOut2
    """

    return sync_detailed(
        execution_group_id=execution_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    execution_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ExecutionGroupGetOut2]:
    """Get Execution Group

     VNpQ2rat

    Retrieve details of a specific execution group by its ID.

    Args:
        request: HttpRequest - The incoming HTTP request.
        path_params: ExecutionGroupPathParams - The path parameters containing the execution group ID.

    Returns: ExecutionGroup - The execution group instance.

    Args:
        execution_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecutionGroupGetOut2]
    """

    kwargs = _get_kwargs(
        execution_group_id=execution_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    execution_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ExecutionGroupGetOut2 | None:
    """Get Execution Group

     VNpQ2rat

    Retrieve details of a specific execution group by its ID.

    Args:
        request: HttpRequest - The incoming HTTP request.
        path_params: ExecutionGroupPathParams - The path parameters containing the execution group ID.

    Returns: ExecutionGroup - The execution group instance.

    Args:
        execution_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecutionGroupGetOut2
    """

    return (
        await asyncio_detailed(
            execution_group_id=execution_group_id,
            client=client,
        )
    ).parsed
