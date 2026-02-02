from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execution_group_processes_metadata_get_out import ExecutionGroupProcessesMetadataGetOut
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    execution_group_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/dataspaces/{dataspace_id}/execution-groups/{execution_group_id}/metadata/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            execution_group_id=quote(str(execution_group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExecutionGroupProcessesMetadataGetOut | None:
    if response.status_code == 200:
        response_200 = ExecutionGroupProcessesMetadataGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExecutionGroupProcessesMetadataGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    execution_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ExecutionGroupProcessesMetadataGetOut]:
    """Get Execution Group Metadata

     bbRd7fnc

    Retrieve details of a specific execution group by its ID.

    Args:
        request: HttpRequest - The incoming HTTP request.
        path_params: ExecutionGroupPathParams - The path parameters containing the execution group ID.

    Returns: ExecutionGroup - The execution group instance.

    Args:
        dataspace_id (UUID):
        execution_group_id (UUID): The UUID of the execution group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecutionGroupProcessesMetadataGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        execution_group_id=execution_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    execution_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ExecutionGroupProcessesMetadataGetOut | None:
    """Get Execution Group Metadata

     bbRd7fnc

    Retrieve details of a specific execution group by its ID.

    Args:
        request: HttpRequest - The incoming HTTP request.
        path_params: ExecutionGroupPathParams - The path parameters containing the execution group ID.

    Returns: ExecutionGroup - The execution group instance.

    Args:
        dataspace_id (UUID):
        execution_group_id (UUID): The UUID of the execution group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecutionGroupProcessesMetadataGetOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        execution_group_id=execution_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    execution_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ExecutionGroupProcessesMetadataGetOut]:
    """Get Execution Group Metadata

     bbRd7fnc

    Retrieve details of a specific execution group by its ID.

    Args:
        request: HttpRequest - The incoming HTTP request.
        path_params: ExecutionGroupPathParams - The path parameters containing the execution group ID.

    Returns: ExecutionGroup - The execution group instance.

    Args:
        dataspace_id (UUID):
        execution_group_id (UUID): The UUID of the execution group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecutionGroupProcessesMetadataGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        execution_group_id=execution_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    execution_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ExecutionGroupProcessesMetadataGetOut | None:
    """Get Execution Group Metadata

     bbRd7fnc

    Retrieve details of a specific execution group by its ID.

    Args:
        request: HttpRequest - The incoming HTTP request.
        path_params: ExecutionGroupPathParams - The path parameters containing the execution group ID.

    Returns: ExecutionGroup - The execution group instance.

    Args:
        dataspace_id (UUID):
        execution_group_id (UUID): The UUID of the execution group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecutionGroupProcessesMetadataGetOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            execution_group_id=execution_group_id,
            client=client,
        )
    ).parsed
