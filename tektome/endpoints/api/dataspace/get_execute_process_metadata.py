from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execute_process_metadata_post_request import ExecuteProcessMetadataPostRequest
from ...models.execute_process_metadata_response import ExecuteProcessMetadataResponse
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    body: ExecuteProcessMetadataPostRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/processes/{process_id}/metadata/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            process_id=quote(str(process_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExecuteProcessMetadataResponse | None:
    if response.status_code == 200:
        response_200 = ExecuteProcessMetadataResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExecuteProcessMetadataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ExecuteProcessMetadataPostRequest,
) -> Response[ExecuteProcessMetadataResponse]:
    """Get execution metadata for a configured process

     Retrieve execution metadata for a process, including attribute information for the specified model
    entities (projects or resources).

    Args:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.
        body (ExecuteProcessMetadataPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteProcessMetadataResponse]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        process_id=process_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ExecuteProcessMetadataPostRequest,
) -> ExecuteProcessMetadataResponse | None:
    """Get execution metadata for a configured process

     Retrieve execution metadata for a process, including attribute information for the specified model
    entities (projects or resources).

    Args:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.
        body (ExecuteProcessMetadataPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteProcessMetadataResponse
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        process_id=process_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ExecuteProcessMetadataPostRequest,
) -> Response[ExecuteProcessMetadataResponse]:
    """Get execution metadata for a configured process

     Retrieve execution metadata for a process, including attribute information for the specified model
    entities (projects or resources).

    Args:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.
        body (ExecuteProcessMetadataPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteProcessMetadataResponse]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        process_id=process_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ExecuteProcessMetadataPostRequest,
) -> ExecuteProcessMetadataResponse | None:
    """Get execution metadata for a configured process

     Retrieve execution metadata for a process, including attribute information for the specified model
    entities (projects or resources).

    Args:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.
        body (ExecuteProcessMetadataPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteProcessMetadataResponse
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            process_id=process_id,
            client=client,
            body=body,
        )
    ).parsed
