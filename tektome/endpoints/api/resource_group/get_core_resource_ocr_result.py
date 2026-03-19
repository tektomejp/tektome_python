from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.resource_ocr_schema_get_response import ResourceOCRSchemaGetResponse
from ...types import Response


def _get_kwargs(
    resource_group_id: UUID,
    resource_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/{resource_group_id}/resources/{resource_id}/ocr/".format(
            resource_group_id=quote(str(resource_group_id), safe=""),
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ResourceOCRSchemaGetResponse | None:
    if response.status_code == 200:
        response_200 = ResourceOCRSchemaGetResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = ErrorResponse.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = ErrorResponse.from_dict(response.json())

        return response_406

    if response.status_code == 407:
        response_407 = ErrorResponse.from_dict(response.json())

        return response_407

    if response.status_code == 408:
        response_408 = ErrorResponse.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 411:
        response_411 = ErrorResponse.from_dict(response.json())

        return response_411

    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412

    if response.status_code == 416:
        response_416 = ErrorResponse.from_dict(response.json())

        return response_416

    if response.status_code == 418:
        response_418 = ErrorResponse.from_dict(response.json())

        return response_418

    if response.status_code == 425:
        response_425 = ErrorResponse.from_dict(response.json())

        return response_425

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 451:
        response_451 = ErrorResponse.from_dict(response.json())

        return response_451

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ResourceOCRSchemaGetResponse]:
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
) -> Response[ErrorResponse | ResourceOCRSchemaGetResponse]:
    """Get OCR result for a resource

     Retrieve the OCR processing result for the specified resource, including extracted text content.

    Args:
        resource_group_id (UUID):
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ResourceOCRSchemaGetResponse]
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
) -> ErrorResponse | ResourceOCRSchemaGetResponse | None:
    """Get OCR result for a resource

     Retrieve the OCR processing result for the specified resource, including extracted text content.

    Args:
        resource_group_id (UUID):
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ResourceOCRSchemaGetResponse
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
) -> Response[ErrorResponse | ResourceOCRSchemaGetResponse]:
    """Get OCR result for a resource

     Retrieve the OCR processing result for the specified resource, including extracted text content.

    Args:
        resource_group_id (UUID):
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ResourceOCRSchemaGetResponse]
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
) -> ErrorResponse | ResourceOCRSchemaGetResponse | None:
    """Get OCR result for a resource

     Retrieve the OCR processing result for the specified resource, including extracted text content.

    Args:
        resource_group_id (UUID):
        resource_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ResourceOCRSchemaGetResponse
    """

    return (
        await asyncio_detailed(
            resource_group_id=resource_group_id,
            resource_id=resource_id,
            client=client,
        )
    ).parsed
