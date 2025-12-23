from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blob_upload_request_post_in import BlobUploadRequestPostIn
from ...models.blob_upload_request_post_out import BlobUploadRequestPostOut
from ...types import Response


def _get_kwargs(
    resource_group_id: UUID,
    *,
    body: BlobUploadRequestPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/resources/groups/{resource_group_id}/upload/blob/request/".format(
            resource_group_id=quote(str(resource_group_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BlobUploadRequestPostOut | None:
    if response.status_code == 200:
        response_200 = BlobUploadRequestPostOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BlobUploadRequestPostOut]:
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
    body: BlobUploadRequestPostIn,
) -> Response[BlobUploadRequestPostOut]:
    """Post Blob Upload Request

     U71dMUjv

    Request a blob upload URL for large files.

    This endpoint is designed for uploading large files (500MB-1GB+) that would
    otherwise timeout or consume excessive server memory. Instead of uploading
    through the server, the client receives a write-only SAS URL to upload
    directly to Azure Blob Storage.

    **Flow:**
    1. Call this endpoint with the file name to get an upload URL
    2. Upload the file directly to Azure Blob Storage using the returned `upload_url`
    3. Call POST /groups/{resource_group_id}/upload/complete/ with the `upload_id`

    **Security:**
    - The SAS URL is write-only (cannot read other blobs)
    - The SAS URL is path-specific (can only write to the designated blob)
    - The SAS URL expires after a short time (default 15 minutes)

    **Notes:**
    - The `upload_id` must be used within the expiration time
    - The blob path is auto-generated with a UUID to prevent conflicts

    Args:
        resource_group_id (UUID): Resource group ID
        body (BlobUploadRequestPostIn): Input schema for requesting a streaming upload SAS URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlobUploadRequestPostOut]
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
    body: BlobUploadRequestPostIn,
) -> BlobUploadRequestPostOut | None:
    """Post Blob Upload Request

     U71dMUjv

    Request a blob upload URL for large files.

    This endpoint is designed for uploading large files (500MB-1GB+) that would
    otherwise timeout or consume excessive server memory. Instead of uploading
    through the server, the client receives a write-only SAS URL to upload
    directly to Azure Blob Storage.

    **Flow:**
    1. Call this endpoint with the file name to get an upload URL
    2. Upload the file directly to Azure Blob Storage using the returned `upload_url`
    3. Call POST /groups/{resource_group_id}/upload/complete/ with the `upload_id`

    **Security:**
    - The SAS URL is write-only (cannot read other blobs)
    - The SAS URL is path-specific (can only write to the designated blob)
    - The SAS URL expires after a short time (default 15 minutes)

    **Notes:**
    - The `upload_id` must be used within the expiration time
    - The blob path is auto-generated with a UUID to prevent conflicts

    Args:
        resource_group_id (UUID): Resource group ID
        body (BlobUploadRequestPostIn): Input schema for requesting a streaming upload SAS URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlobUploadRequestPostOut
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
    body: BlobUploadRequestPostIn,
) -> Response[BlobUploadRequestPostOut]:
    """Post Blob Upload Request

     U71dMUjv

    Request a blob upload URL for large files.

    This endpoint is designed for uploading large files (500MB-1GB+) that would
    otherwise timeout or consume excessive server memory. Instead of uploading
    through the server, the client receives a write-only SAS URL to upload
    directly to Azure Blob Storage.

    **Flow:**
    1. Call this endpoint with the file name to get an upload URL
    2. Upload the file directly to Azure Blob Storage using the returned `upload_url`
    3. Call POST /groups/{resource_group_id}/upload/complete/ with the `upload_id`

    **Security:**
    - The SAS URL is write-only (cannot read other blobs)
    - The SAS URL is path-specific (can only write to the designated blob)
    - The SAS URL expires after a short time (default 15 minutes)

    **Notes:**
    - The `upload_id` must be used within the expiration time
    - The blob path is auto-generated with a UUID to prevent conflicts

    Args:
        resource_group_id (UUID): Resource group ID
        body (BlobUploadRequestPostIn): Input schema for requesting a streaming upload SAS URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlobUploadRequestPostOut]
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
    body: BlobUploadRequestPostIn,
) -> BlobUploadRequestPostOut | None:
    """Post Blob Upload Request

     U71dMUjv

    Request a blob upload URL for large files.

    This endpoint is designed for uploading large files (500MB-1GB+) that would
    otherwise timeout or consume excessive server memory. Instead of uploading
    through the server, the client receives a write-only SAS URL to upload
    directly to Azure Blob Storage.

    **Flow:**
    1. Call this endpoint with the file name to get an upload URL
    2. Upload the file directly to Azure Blob Storage using the returned `upload_url`
    3. Call POST /groups/{resource_group_id}/upload/complete/ with the `upload_id`

    **Security:**
    - The SAS URL is write-only (cannot read other blobs)
    - The SAS URL is path-specific (can only write to the designated blob)
    - The SAS URL expires after a short time (default 15 minutes)

    **Notes:**
    - The `upload_id` must be used within the expiration time
    - The blob path is auto-generated with a UUID to prevent conflicts

    Args:
        resource_group_id (UUID): Resource group ID
        body (BlobUploadRequestPostIn): Input schema for requesting a streaming upload SAS URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlobUploadRequestPostOut
    """

    return (
        await asyncio_detailed(
            resource_group_id=resource_group_id,
            client=client,
            body=body,
        )
    ).parsed
