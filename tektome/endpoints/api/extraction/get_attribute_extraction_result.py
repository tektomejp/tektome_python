from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_extracted_result_response import GetExtractedResultResponse
from ...types import Response


def _get_kwargs(
    attribute_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/extractions/attributes/{attribute_id}/extraction_result/".format(
            attribute_id=quote(str(attribute_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetExtractedResultResponse | None:
    if response.status_code == 200:
        response_200 = GetExtractedResultResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetExtractedResultResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[GetExtractedResultResponse]:
    """Get extraction result for an attribute

     Retrieve the extracted value, status, reasoning, and cited sources for a specific attribute. Returns
    the extraction status, any error messages, and references to source documents.

    Args:
        attribute_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetExtractedResultResponse]
    """

    kwargs = _get_kwargs(
        attribute_id=attribute_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
) -> GetExtractedResultResponse | None:
    """Get extraction result for an attribute

     Retrieve the extracted value, status, reasoning, and cited sources for a specific attribute. Returns
    the extraction status, any error messages, and references to source documents.

    Args:
        attribute_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetExtractedResultResponse
    """

    return sync_detailed(
        attribute_id=attribute_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[GetExtractedResultResponse]:
    """Get extraction result for an attribute

     Retrieve the extracted value, status, reasoning, and cited sources for a specific attribute. Returns
    the extraction status, any error messages, and references to source documents.

    Args:
        attribute_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetExtractedResultResponse]
    """

    kwargs = _get_kwargs(
        attribute_id=attribute_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    attribute_id: UUID,
    *,
    client: AuthenticatedClient,
) -> GetExtractedResultResponse | None:
    """Get extraction result for an attribute

     Retrieve the extracted value, status, reasoning, and cited sources for a specific attribute. Returns
    the extraction status, any error messages, and references to source documents.

    Args:
        attribute_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetExtractedResultResponse
    """

    return (
        await asyncio_detailed(
            attribute_id=attribute_id,
            client=client,
        )
    ).parsed
