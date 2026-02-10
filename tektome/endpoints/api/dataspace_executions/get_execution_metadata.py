from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execution_get_out import ExecutionGetOut
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    execution_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/dataspaces/{dataspace_id}/executions/{execution_id}/metadata/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            execution_id=quote(str(execution_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExecutionGetOut | None:
    if response.status_code == 200:
        response_200 = ExecutionGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ExecutionGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ExecutionGetOut]:
    """Get Execution Metadata

     p6cozWCR

    Retrieve details of a specific execution by its ID.

    Args:
        request: HttpRequest - The incoming HTTP request.
        path_params: ExecutionPathParams - The path parameters containing the execution ID.

    Returns: Execution - The execution group instance with serialized detailed metadata.

    Args:
        dataspace_id (UUID):
        execution_id (UUID): The UUID of the execution to cancel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecutionGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        execution_id=execution_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ExecutionGetOut | None:
    """Get Execution Metadata

     p6cozWCR

    Retrieve details of a specific execution by its ID.

    Args:
        request: HttpRequest - The incoming HTTP request.
        path_params: ExecutionPathParams - The path parameters containing the execution ID.

    Returns: Execution - The execution group instance with serialized detailed metadata.

    Args:
        dataspace_id (UUID):
        execution_id (UUID): The UUID of the execution to cancel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecutionGetOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        execution_id=execution_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ExecutionGetOut]:
    """Get Execution Metadata

     p6cozWCR

    Retrieve details of a specific execution by its ID.

    Args:
        request: HttpRequest - The incoming HTTP request.
        path_params: ExecutionPathParams - The path parameters containing the execution ID.

    Returns: Execution - The execution group instance with serialized detailed metadata.

    Args:
        dataspace_id (UUID):
        execution_id (UUID): The UUID of the execution to cancel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecutionGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        execution_id=execution_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    execution_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ExecutionGetOut | None:
    """Get Execution Metadata

     p6cozWCR

    Retrieve details of a specific execution by its ID.

    Args:
        request: HttpRequest - The incoming HTTP request.
        path_params: ExecutionPathParams - The path parameters containing the execution ID.

    Returns: Execution - The execution group instance with serialized detailed metadata.

    Args:
        dataspace_id (UUID):
        execution_id (UUID): The UUID of the execution to cancel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecutionGetOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            execution_id=execution_id,
            client=client,
        )
    ).parsed
