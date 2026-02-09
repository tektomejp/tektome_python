from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_out import ErrorOut
from ...models.resource_ocr_schema_post_out import ResourceOCRSchemaPostOut
from ...types import Response


def _get_kwargs(
    resource_group_id: UUID,
    resource_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/{resource_group_id}/resources/{resource_id}/ocr/".format(
            resource_group_id=quote(str(resource_group_id), safe=""),
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorOut | ResourceOCRSchemaPostOut | None:
    if response.status_code == 201:
        response_201 = ResourceOCRSchemaPostOut.from_dict(response.json())

        return response_201

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
) -> Response[ErrorOut | ResourceOCRSchemaPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_group_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorOut | ResourceOCRSchemaPostOut]:
    """Submit Ocr Task

     5TLaNZZs

    Submit OCR task for the given resource_id

    Raise 404 if resource_id not found

    Args:
        resource_group_id (UUID):
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOut | ResourceOCRSchemaPostOut]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_group_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ErrorOut | ResourceOCRSchemaPostOut | None:
    """Submit Ocr Task

     5TLaNZZs

    Submit OCR task for the given resource_id

    Raise 404 if resource_id not found

    Args:
        resource_group_id (UUID):
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOut | ResourceOCRSchemaPostOut
    """

    return sync_detailed(
        resource_group_id=resource_group_id,
        resource_id=resource_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_group_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorOut | ResourceOCRSchemaPostOut]:
    """Submit Ocr Task

     5TLaNZZs

    Submit OCR task for the given resource_id

    Raise 404 if resource_id not found

    Args:
        resource_group_id (UUID):
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOut | ResourceOCRSchemaPostOut]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_group_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ErrorOut | ResourceOCRSchemaPostOut | None:
    """Submit Ocr Task

     5TLaNZZs

    Submit OCR task for the given resource_id

    Raise 404 if resource_id not found

    Args:
        resource_group_id (UUID):
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOut | ResourceOCRSchemaPostOut
    """

    return (
        await asyncio_detailed(
            resource_group_id=resource_group_id,
            resource_id=resource_id,
            client=client,
        )
    ).parsed
