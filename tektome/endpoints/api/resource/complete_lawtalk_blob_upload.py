from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blob_upload_complete_post_in import BlobUploadCompletePostIn
from ...models.resource_schema_2 import ResourceSchema2
from ...types import Response


def _get_kwargs(
    resource_group_id: UUID,
    *,
    body: BlobUploadCompletePostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/resources/groups/{resource_group_id}/upload/blob/complete/".format(
            resource_group_id=quote(str(resource_group_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ResourceSchema2 | None:
    if response.status_code == 201:
        response_201 = ResourceSchema2.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ResourceSchema2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BlobUploadCompletePostIn,
) -> Response[ResourceSchema2]:
    """Post Blob Upload Complete

     8swvdVq1

    Complete a blob upload and create the Resource record.

    After uploading a file directly to Azure Blob Storage using the SAS URL
    from the upload request endpoint, call this endpoint to create the
    Resource and LawtalkResource records.

    **Flow:**
    1. Validates the upload_id exists in Redis
    2. Verifies the resource_group_id matches the original request
    3. Confirms the blob exists in Azure Blob Storage
    4. Creates Resource and LawtalkResource records
    5. Optionally starts OCR extraction if `initialize` is true

    **Error Codes:**
    - 400: Invalid upload_id or resource_group_id mismatch
    - 404: Blob not found in Azure (upload not completed)

    Args:
        resource_group_id (UUID): Resource group ID
        body (BlobUploadCompletePostIn): Input schema for completing a blob upload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceSchema2]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BlobUploadCompletePostIn,
) -> ResourceSchema2 | None:
    """Post Blob Upload Complete

     8swvdVq1

    Complete a blob upload and create the Resource record.

    After uploading a file directly to Azure Blob Storage using the SAS URL
    from the upload request endpoint, call this endpoint to create the
    Resource and LawtalkResource records.

    **Flow:**
    1. Validates the upload_id exists in Redis
    2. Verifies the resource_group_id matches the original request
    3. Confirms the blob exists in Azure Blob Storage
    4. Creates Resource and LawtalkResource records
    5. Optionally starts OCR extraction if `initialize` is true

    **Error Codes:**
    - 400: Invalid upload_id or resource_group_id mismatch
    - 404: Blob not found in Azure (upload not completed)

    Args:
        resource_group_id (UUID): Resource group ID
        body (BlobUploadCompletePostIn): Input schema for completing a blob upload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceSchema2
    """

    return sync_detailed(
        resource_group_id=resource_group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BlobUploadCompletePostIn,
) -> Response[ResourceSchema2]:
    """Post Blob Upload Complete

     8swvdVq1

    Complete a blob upload and create the Resource record.

    After uploading a file directly to Azure Blob Storage using the SAS URL
    from the upload request endpoint, call this endpoint to create the
    Resource and LawtalkResource records.

    **Flow:**
    1. Validates the upload_id exists in Redis
    2. Verifies the resource_group_id matches the original request
    3. Confirms the blob exists in Azure Blob Storage
    4. Creates Resource and LawtalkResource records
    5. Optionally starts OCR extraction if `initialize` is true

    **Error Codes:**
    - 400: Invalid upload_id or resource_group_id mismatch
    - 404: Blob not found in Azure (upload not completed)

    Args:
        resource_group_id (UUID): Resource group ID
        body (BlobUploadCompletePostIn): Input schema for completing a blob upload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceSchema2]
    """

    kwargs = _get_kwargs(
        resource_group_id=resource_group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BlobUploadCompletePostIn,
) -> ResourceSchema2 | None:
    """Post Blob Upload Complete

     8swvdVq1

    Complete a blob upload and create the Resource record.

    After uploading a file directly to Azure Blob Storage using the SAS URL
    from the upload request endpoint, call this endpoint to create the
    Resource and LawtalkResource records.

    **Flow:**
    1. Validates the upload_id exists in Redis
    2. Verifies the resource_group_id matches the original request
    3. Confirms the blob exists in Azure Blob Storage
    4. Creates Resource and LawtalkResource records
    5. Optionally starts OCR extraction if `initialize` is true

    **Error Codes:**
    - 400: Invalid upload_id or resource_group_id mismatch
    - 404: Blob not found in Azure (upload not completed)

    Args:
        resource_group_id (UUID): Resource group ID
        body (BlobUploadCompletePostIn): Input schema for completing a blob upload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceSchema2
    """

    return (
        await asyncio_detailed(
            resource_group_id=resource_group_id,
            client=client,
            body=body,
        )
    ).parsed
