from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appttimport_routes_storage_import_sync_file_multi_part_body_params import (
    AppttimportRoutesStorageImportSyncFileMultiPartBodyParams,
)
from ...models.appttimport_routes_storage_import_sync_file_response import (
    AppttimportRoutesStorageImportSyncFileResponse,
)
from ...models.import_result import ImportResult
from ...types import Response


def _get_kwargs(
    *,
    body: AppttimportRoutesStorageImportSyncFileMultiPartBodyParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/ttimport/sync-file/",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppttimportRoutesStorageImportSyncFileResponse | ImportResult | None:
    if response.status_code == 200:
        response_200 = ImportResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ImportResult.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = AppttimportRoutesStorageImportSyncFileResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppttimportRoutesStorageImportSyncFileResponse | ImportResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AppttimportRoutesStorageImportSyncFileMultiPartBodyParams,
) -> Response[AppttimportRoutesStorageImportSyncFileResponse | ImportResult]:
    """Sync a single file from Rails app

     Sync a single file with metadata and binary content from Rails app.

    Args:
        body (AppttimportRoutesStorageImportSyncFileMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppttimportRoutesStorageImportSyncFileResponse | ImportResult]
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
    body: AppttimportRoutesStorageImportSyncFileMultiPartBodyParams,
) -> AppttimportRoutesStorageImportSyncFileResponse | ImportResult | None:
    """Sync a single file from Rails app

     Sync a single file with metadata and binary content from Rails app.

    Args:
        body (AppttimportRoutesStorageImportSyncFileMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppttimportRoutesStorageImportSyncFileResponse | ImportResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AppttimportRoutesStorageImportSyncFileMultiPartBodyParams,
) -> Response[AppttimportRoutesStorageImportSyncFileResponse | ImportResult]:
    """Sync a single file from Rails app

     Sync a single file with metadata and binary content from Rails app.

    Args:
        body (AppttimportRoutesStorageImportSyncFileMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppttimportRoutesStorageImportSyncFileResponse | ImportResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AppttimportRoutesStorageImportSyncFileMultiPartBodyParams,
) -> AppttimportRoutesStorageImportSyncFileResponse | ImportResult | None:
    """Sync a single file from Rails app

     Sync a single file with metadata and binary content from Rails app.

    Args:
        body (AppttimportRoutesStorageImportSyncFileMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppttimportRoutesStorageImportSyncFileResponse | ImportResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
