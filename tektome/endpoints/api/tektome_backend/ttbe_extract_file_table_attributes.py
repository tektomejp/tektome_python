from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_table_attribute_extraction import FileTableAttributeExtraction
from ...models.ttbe_extract_file_table_attributes_response import TtbeExtractFileTableAttributesResponse
from ...types import Response


def _get_kwargs(
    *,
    body: FileTableAttributeExtraction,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/tektomebe/v1/file_attributes/table/extraction/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TtbeExtractFileTableAttributesResponse | None:
    if response.status_code == 200:
        response_200 = TtbeExtractFileTableAttributesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TtbeExtractFileTableAttributesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: FileTableAttributeExtraction,
) -> Response[TtbeExtractFileTableAttributesResponse]:
    """File Attributes Table Extraction

    Args:
        body (FileTableAttributeExtraction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TtbeExtractFileTableAttributesResponse]
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
    body: FileTableAttributeExtraction,
) -> TtbeExtractFileTableAttributesResponse | None:
    """File Attributes Table Extraction

    Args:
        body (FileTableAttributeExtraction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TtbeExtractFileTableAttributesResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: FileTableAttributeExtraction,
) -> Response[TtbeExtractFileTableAttributesResponse]:
    """File Attributes Table Extraction

    Args:
        body (FileTableAttributeExtraction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TtbeExtractFileTableAttributesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: FileTableAttributeExtraction,
) -> TtbeExtractFileTableAttributesResponse | None:
    """File Attributes Table Extraction

    Args:
        body (FileTableAttributeExtraction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TtbeExtractFileTableAttributesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
