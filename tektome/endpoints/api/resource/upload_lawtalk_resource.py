from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resource_schema_2 import ResourceSchema2
from ...models.upload_lawtalk_resource_multi_part_body_params import UploadLawtalkResourceMultiPartBodyParams
from ...types import Response


def _get_kwargs(
    resource_group_id: UUID,
    *,
    body: UploadLawtalkResourceMultiPartBodyParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/resources/groups/{resource_group_id}/upload/".format(
            resource_group_id=quote(str(resource_group_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

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
    body: UploadLawtalkResourceMultiPartBodyParams,
) -> Response[ResourceSchema2]:
    """Post Resource

     KYnire59


    Upload a file to a resource group and create a Lawtalk resource.

    This endpoint allows uploading a file (e.g., PDF, DOCX, IFC) to a specified resource group.
    It creates a new LawtalkResource and a corresponding core resource with version control.
    The uploaded file's metadata (name, kind) is stored as string attributes.
    Optionally, OCR extraction or BIM conversion can be initialized on upload.

    **Notes:**
    - If `initialize` is true, OCR extraction or BIM conversion is started for the uploaded file.

    Args:
        resource_group_id (UUID): Resource group ID
        body (UploadLawtalkResourceMultiPartBodyParams):

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
    body: UploadLawtalkResourceMultiPartBodyParams,
) -> ResourceSchema2 | None:
    """Post Resource

     KYnire59


    Upload a file to a resource group and create a Lawtalk resource.

    This endpoint allows uploading a file (e.g., PDF, DOCX, IFC) to a specified resource group.
    It creates a new LawtalkResource and a corresponding core resource with version control.
    The uploaded file's metadata (name, kind) is stored as string attributes.
    Optionally, OCR extraction or BIM conversion can be initialized on upload.

    **Notes:**
    - If `initialize` is true, OCR extraction or BIM conversion is started for the uploaded file.

    Args:
        resource_group_id (UUID): Resource group ID
        body (UploadLawtalkResourceMultiPartBodyParams):

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
    body: UploadLawtalkResourceMultiPartBodyParams,
) -> Response[ResourceSchema2]:
    """Post Resource

     KYnire59


    Upload a file to a resource group and create a Lawtalk resource.

    This endpoint allows uploading a file (e.g., PDF, DOCX, IFC) to a specified resource group.
    It creates a new LawtalkResource and a corresponding core resource with version control.
    The uploaded file's metadata (name, kind) is stored as string attributes.
    Optionally, OCR extraction or BIM conversion can be initialized on upload.

    **Notes:**
    - If `initialize` is true, OCR extraction or BIM conversion is started for the uploaded file.

    Args:
        resource_group_id (UUID): Resource group ID
        body (UploadLawtalkResourceMultiPartBodyParams):

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
    body: UploadLawtalkResourceMultiPartBodyParams,
) -> ResourceSchema2 | None:
    """Post Resource

     KYnire59


    Upload a file to a resource group and create a Lawtalk resource.

    This endpoint allows uploading a file (e.g., PDF, DOCX, IFC) to a specified resource group.
    It creates a new LawtalkResource and a corresponding core resource with version control.
    The uploaded file's metadata (name, kind) is stored as string attributes.
    Optionally, OCR extraction or BIM conversion can be initialized on upload.

    **Notes:**
    - If `initialize` is true, OCR extraction or BIM conversion is started for the uploaded file.

    Args:
        resource_group_id (UUID): Resource group ID
        body (UploadLawtalkResourceMultiPartBodyParams):

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
