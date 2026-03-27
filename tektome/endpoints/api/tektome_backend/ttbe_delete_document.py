from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_delete import DocumentDelete
from ...models.ttbe_delete_document_response import TtbeDeleteDocumentResponse
from ...types import Response


def _get_kwargs(
    *,
    body: DocumentDelete,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/tektomebe/v1/document/delete/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TtbeDeleteDocumentResponse | None:
    if response.status_code == 200:
        response_200 = TtbeDeleteDocumentResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TtbeDeleteDocumentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DocumentDelete,
) -> Response[TtbeDeleteDocumentResponse]:
    """Delete Document

     Delete a document from the vector database.

    Deletes from chunk group, page and attribute search indexes.

    TODO:
    - It is possible to parallelize the deletion of the indexes by moving it to Celery. Priority medium.

    Args:
        body (DocumentDelete):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TtbeDeleteDocumentResponse]
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
    body: DocumentDelete,
) -> TtbeDeleteDocumentResponse | None:
    """Delete Document

     Delete a document from the vector database.

    Deletes from chunk group, page and attribute search indexes.

    TODO:
    - It is possible to parallelize the deletion of the indexes by moving it to Celery. Priority medium.

    Args:
        body (DocumentDelete):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TtbeDeleteDocumentResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DocumentDelete,
) -> Response[TtbeDeleteDocumentResponse]:
    """Delete Document

     Delete a document from the vector database.

    Deletes from chunk group, page and attribute search indexes.

    TODO:
    - It is possible to parallelize the deletion of the indexes by moving it to Celery. Priority medium.

    Args:
        body (DocumentDelete):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TtbeDeleteDocumentResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DocumentDelete,
) -> TtbeDeleteDocumentResponse | None:
    """Delete Document

     Delete a document from the vector database.

    Deletes from chunk group, page and attribute search indexes.

    TODO:
    - It is possible to parallelize the deletion of the indexes by moving it to Celery. Priority medium.

    Args:
        body (DocumentDelete):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TtbeDeleteDocumentResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
