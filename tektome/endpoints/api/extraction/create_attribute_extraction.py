from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attribute_extraction_post_out import AttributeExtractionPostOut
from ...models.extraction_post_in import ExtractionPostIn
from ...types import Response


def _get_kwargs(
    *,
    body: ExtractionPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/extractions/attributes/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AttributeExtractionPostOut | None:
    if response.status_code == 201:
        response_201 = AttributeExtractionPostOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AttributeExtractionPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ExtractionPostIn,
) -> Response[AttributeExtractionPostOut]:
    """Extract attributes from a section

     Submit an attribute extraction job for a section. The section should be specifically created for
    attribute extraction, and contain all relevant data. section_id is not the same as the section_is
    listed on OCR chunks. Multiple attributes can be extracted in a single request. This is an
    asynchronous operation. Check the attributes' statuses to see when the extraction is done.

    Args:
        body (ExtractionPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributeExtractionPostOut]
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
    body: ExtractionPostIn,
) -> AttributeExtractionPostOut | None:
    """Extract attributes from a section

     Submit an attribute extraction job for a section. The section should be specifically created for
    attribute extraction, and contain all relevant data. section_id is not the same as the section_is
    listed on OCR chunks. Multiple attributes can be extracted in a single request. This is an
    asynchronous operation. Check the attributes' statuses to see when the extraction is done.

    Args:
        body (ExtractionPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributeExtractionPostOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ExtractionPostIn,
) -> Response[AttributeExtractionPostOut]:
    """Extract attributes from a section

     Submit an attribute extraction job for a section. The section should be specifically created for
    attribute extraction, and contain all relevant data. section_id is not the same as the section_is
    listed on OCR chunks. Multiple attributes can be extracted in a single request. This is an
    asynchronous operation. Check the attributes' statuses to see when the extraction is done.

    Args:
        body (ExtractionPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributeExtractionPostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ExtractionPostIn,
) -> AttributeExtractionPostOut | None:
    """Extract attributes from a section

     Submit an attribute extraction job for a section. The section should be specifically created for
    attribute extraction, and contain all relevant data. section_id is not the same as the section_is
    listed on OCR chunks. Multiple attributes can be extracted in a single request. This is an
    asynchronous operation. Check the attributes' statuses to see when the extraction is done.

    Args:
        body (ExtractionPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributeExtractionPostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
