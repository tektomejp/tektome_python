from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    attribute_id: UUID,
    pdf_citation_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/core/dataspaces/{dataspace_id}/attributes/{attribute_id}/pdf-citations/{pdf_citation_id}/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            attribute_id=quote(str(attribute_id), safe=""),
            pdf_citation_id=quote(str(pdf_citation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    attribute_id: UUID,
    pdf_citation_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete Attribute Pdf Citation

     acBfega0

    Delete a PDF citation from an attribute.

    Args:
        dataspace_id (UUID):
        attribute_id (UUID):
        pdf_citation_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        attribute_id=attribute_id,
        pdf_citation_id=pdf_citation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    dataspace_id: UUID,
    attribute_id: UUID,
    pdf_citation_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete Attribute Pdf Citation

     acBfega0

    Delete a PDF citation from an attribute.

    Args:
        dataspace_id (UUID):
        attribute_id (UUID):
        pdf_citation_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        attribute_id=attribute_id,
        pdf_citation_id=pdf_citation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
