from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.azure_presigned_upload_input_schema import AzurePresignedUploadInputSchema
from ...models.azure_presigned_upload_output_schema import AzurePresignedUploadOutputSchema
from ...types import Response


def _get_kwargs(
    *,
    body: AzurePresignedUploadInputSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/core/azure/presigned-file-url/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AzurePresignedUploadOutputSchema | None:
    if response.status_code == 200:
        response_200 = AzurePresignedUploadOutputSchema.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AzurePresignedUploadOutputSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AzurePresignedUploadInputSchema,
) -> Response[AzurePresignedUploadOutputSchema]:
    """Presigned File Url

     cOkNhBwR

    Generate a presigned URL for uploading a file in Azure storage.

    Args:
        request: Request object
        payload: The request payload.

    Returns:
        A presigned URL as a string.

    Args:
        body (AzurePresignedUploadInputSchema): Schema for input when requesting a presigned
            upload URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AzurePresignedUploadOutputSchema]
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
    body: AzurePresignedUploadInputSchema,
) -> AzurePresignedUploadOutputSchema | None:
    """Presigned File Url

     cOkNhBwR

    Generate a presigned URL for uploading a file in Azure storage.

    Args:
        request: Request object
        payload: The request payload.

    Returns:
        A presigned URL as a string.

    Args:
        body (AzurePresignedUploadInputSchema): Schema for input when requesting a presigned
            upload URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AzurePresignedUploadOutputSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AzurePresignedUploadInputSchema,
) -> Response[AzurePresignedUploadOutputSchema]:
    """Presigned File Url

     cOkNhBwR

    Generate a presigned URL for uploading a file in Azure storage.

    Args:
        request: Request object
        payload: The request payload.

    Returns:
        A presigned URL as a string.

    Args:
        body (AzurePresignedUploadInputSchema): Schema for input when requesting a presigned
            upload URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AzurePresignedUploadOutputSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AzurePresignedUploadInputSchema,
) -> AzurePresignedUploadOutputSchema | None:
    """Presigned File Url

     cOkNhBwR

    Generate a presigned URL for uploading a file in Azure storage.

    Args:
        request: Request object
        payload: The request payload.

    Returns:
        A presigned URL as a string.

    Args:
        body (AzurePresignedUploadInputSchema): Schema for input when requesting a presigned
            upload URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AzurePresignedUploadOutputSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
