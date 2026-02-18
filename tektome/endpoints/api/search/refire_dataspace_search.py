from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataspace_search_request_schema import DataspaceSearchRequestSchema
from ...models.dataspace_search_result_out import DataspaceSearchResultOut
from ...models.error_out import ErrorOut
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    search_request_id: UUID,
    *,
    body: DataspaceSearchRequestSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/search/requests/{search_request_id}/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            search_request_id=quote(str(search_request_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DataspaceSearchResultOut | ErrorOut | None:
    if response.status_code == 200:
        response_200 = DataspaceSearchResultOut.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorOut.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorOut.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorOut.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorOut.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorOut.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = ErrorOut.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = ErrorOut.from_dict(response.json())

        return response_406

    if response.status_code == 407:
        response_407 = ErrorOut.from_dict(response.json())

        return response_407

    if response.status_code == 408:
        response_408 = ErrorOut.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = ErrorOut.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorOut.from_dict(response.json())

        return response_410

    if response.status_code == 411:
        response_411 = ErrorOut.from_dict(response.json())

        return response_411

    if response.status_code == 412:
        response_412 = ErrorOut.from_dict(response.json())

        return response_412

    if response.status_code == 416:
        response_416 = ErrorOut.from_dict(response.json())

        return response_416

    if response.status_code == 418:
        response_418 = ErrorOut.from_dict(response.json())

        return response_418

    if response.status_code == 425:
        response_425 = ErrorOut.from_dict(response.json())

        return response_425

    if response.status_code == 429:
        response_429 = ErrorOut.from_dict(response.json())

        return response_429

    if response.status_code == 451:
        response_451 = ErrorOut.from_dict(response.json())

        return response_451

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DataspaceSearchResultOut | ErrorOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    search_request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchRequestSchema,
) -> Response[DataspaceSearchResultOut | ErrorOut]:
    """Post Refire Search

     tP9Xn3Mq

    Refire an existing search request with optional updates.

    Updates the search request with new parameters if provided,
    then executes the search and returns paginated results.

    Args:
        dataspace_id (UUID):
        search_request_id (UUID):
        body (DataspaceSearchRequestSchema): Base schema for search request fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceSearchResultOut | ErrorOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        search_request_id=search_request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    search_request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchRequestSchema,
) -> DataspaceSearchResultOut | ErrorOut | None:
    """Post Refire Search

     tP9Xn3Mq

    Refire an existing search request with optional updates.

    Updates the search request with new parameters if provided,
    then executes the search and returns paginated results.

    Args:
        dataspace_id (UUID):
        search_request_id (UUID):
        body (DataspaceSearchRequestSchema): Base schema for search request fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceSearchResultOut | ErrorOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        search_request_id=search_request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    search_request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchRequestSchema,
) -> Response[DataspaceSearchResultOut | ErrorOut]:
    """Post Refire Search

     tP9Xn3Mq

    Refire an existing search request with optional updates.

    Updates the search request with new parameters if provided,
    then executes the search and returns paginated results.

    Args:
        dataspace_id (UUID):
        search_request_id (UUID):
        body (DataspaceSearchRequestSchema): Base schema for search request fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceSearchResultOut | ErrorOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        search_request_id=search_request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    search_request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchRequestSchema,
) -> DataspaceSearchResultOut | ErrorOut | None:
    """Post Refire Search

     tP9Xn3Mq

    Refire an existing search request with optional updates.

    Updates the search request with new parameters if provided,
    then executes the search and returns paginated results.

    Args:
        dataspace_id (UUID):
        search_request_id (UUID):
        body (DataspaceSearchRequestSchema): Base schema for search request fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceSearchResultOut | ErrorOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            search_request_id=search_request_id,
            client=client,
            body=body,
        )
    ).parsed
