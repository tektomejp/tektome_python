from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.core_project_schema import CoreProjectSchema
from ...models.create_core_project_request import CreateCoreProjectRequest
from ...models.error_output_schema_response import ErrorOutputSchemaResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateCoreProjectRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/projects/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CoreProjectSchema | ErrorOutputSchemaResponse | None:
    if response.status_code == 201:
        response_201 = CoreProjectSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_406

    if response.status_code == 407:
        response_407 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_407

    if response.status_code == 408:
        response_408 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_410

    if response.status_code == 411:
        response_411 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_411

    if response.status_code == 412:
        response_412 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_412

    if response.status_code == 416:
        response_416 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_416

    if response.status_code == 418:
        response_418 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_418

    if response.status_code == 425:
        response_425 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_425

    if response.status_code == 429:
        response_429 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_429

    if response.status_code == 451:
        response_451 = ErrorOutputSchemaResponse.from_dict(response.json())

        return response_451

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CoreProjectSchema | ErrorOutputSchemaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCoreProjectRequest,
) -> Response[CoreProjectSchema | ErrorOutputSchemaResponse]:
    """Create a new project

     Create a new project in the authenticated user's current organization.

    Args:
        body (CreateCoreProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CoreProjectSchema | ErrorOutputSchemaResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateCoreProjectRequest,
) -> CoreProjectSchema | ErrorOutputSchemaResponse | None:
    """Create a new project

     Create a new project in the authenticated user's current organization.

    Args:
        body (CreateCoreProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CoreProjectSchema | ErrorOutputSchemaResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCoreProjectRequest,
) -> Response[CoreProjectSchema | ErrorOutputSchemaResponse]:
    """Create a new project

     Create a new project in the authenticated user's current organization.

    Args:
        body (CreateCoreProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CoreProjectSchema | ErrorOutputSchemaResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateCoreProjectRequest,
) -> CoreProjectSchema | ErrorOutputSchemaResponse | None:
    """Create a new project

     Create a new project in the authenticated user's current organization.

    Args:
        body (CreateCoreProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CoreProjectSchema | ErrorOutputSchemaResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
