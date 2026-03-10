from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blob_upload_complete_in import BlobUploadCompleteIn
from ...models.blob_upload_complete_out import BlobUploadCompleteOut
from ...models.error_out import ErrorOut
from ...types import Response


def _get_kwargs(
    project_id: UUID,
    *,
    body: BlobUploadCompleteIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resources/{project_id}/upload/blob/complete/".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BlobUploadCompleteOut | ErrorOut | None:
    if response.status_code == 201:
        response_201 = BlobUploadCompleteOut.from_dict(response.json())

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
) -> Response[BlobUploadCompleteOut | ErrorOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BlobUploadCompleteIn,
) -> Response[BlobUploadCompleteOut | ErrorOut]:
    """Post Blob Upload Complete

     BYYWWCp2

    Complete a blob upload and create the Resource record.

    After uploading a file directly to Azure Blob Storage using the SAS URL
    from the upload request endpoint, call this endpoint to create the
    Resource and ResourceVersionControl records.

    **Flow:**
    1. Validates the upload_id exists in cache
    2. Verifies the blob exists in Azure Blob Storage
    3. Creates Resource and ResourceVersionControl records
    4. Optionally starts OCR extraction if `initialize` is true

    **Error Codes:**
    - 400: Invalid upload_id or metadata mismatch
    - 404: Blob not found in Azure (upload not completed)

    Args:
        project_id (UUID):
        body (BlobUploadCompleteIn): Request to complete a blob upload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlobUploadCompleteOut | ErrorOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BlobUploadCompleteIn,
) -> BlobUploadCompleteOut | ErrorOut | None:
    """Post Blob Upload Complete

     BYYWWCp2

    Complete a blob upload and create the Resource record.

    After uploading a file directly to Azure Blob Storage using the SAS URL
    from the upload request endpoint, call this endpoint to create the
    Resource and ResourceVersionControl records.

    **Flow:**
    1. Validates the upload_id exists in cache
    2. Verifies the blob exists in Azure Blob Storage
    3. Creates Resource and ResourceVersionControl records
    4. Optionally starts OCR extraction if `initialize` is true

    **Error Codes:**
    - 400: Invalid upload_id or metadata mismatch
    - 404: Blob not found in Azure (upload not completed)

    Args:
        project_id (UUID):
        body (BlobUploadCompleteIn): Request to complete a blob upload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlobUploadCompleteOut | ErrorOut
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BlobUploadCompleteIn,
) -> Response[BlobUploadCompleteOut | ErrorOut]:
    """Post Blob Upload Complete

     BYYWWCp2

    Complete a blob upload and create the Resource record.

    After uploading a file directly to Azure Blob Storage using the SAS URL
    from the upload request endpoint, call this endpoint to create the
    Resource and ResourceVersionControl records.

    **Flow:**
    1. Validates the upload_id exists in cache
    2. Verifies the blob exists in Azure Blob Storage
    3. Creates Resource and ResourceVersionControl records
    4. Optionally starts OCR extraction if `initialize` is true

    **Error Codes:**
    - 400: Invalid upload_id or metadata mismatch
    - 404: Blob not found in Azure (upload not completed)

    Args:
        project_id (UUID):
        body (BlobUploadCompleteIn): Request to complete a blob upload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlobUploadCompleteOut | ErrorOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BlobUploadCompleteIn,
) -> BlobUploadCompleteOut | ErrorOut | None:
    """Post Blob Upload Complete

     BYYWWCp2

    Complete a blob upload and create the Resource record.

    After uploading a file directly to Azure Blob Storage using the SAS URL
    from the upload request endpoint, call this endpoint to create the
    Resource and ResourceVersionControl records.

    **Flow:**
    1. Validates the upload_id exists in cache
    2. Verifies the blob exists in Azure Blob Storage
    3. Creates Resource and ResourceVersionControl records
    4. Optionally starts OCR extraction if `initialize` is true

    **Error Codes:**
    - 400: Invalid upload_id or metadata mismatch
    - 404: Blob not found in Azure (upload not completed)

    Args:
        project_id (UUID):
        body (BlobUploadCompleteIn): Request to complete a blob upload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlobUploadCompleteOut | ErrorOut
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
