from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_payment_record_file_file_params import UploadPaymentRecordFileFileParams
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    payment_record_id: UUID,
    *,
    body: UploadPaymentRecordFileFileParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/account/organizations/{organization_id}/payment-records/{payment_record_id}/upload/".format(
            organization_id=quote(str(organization_id), safe=""),
            payment_record_id=quote(str(payment_record_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
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
    organization_id: UUID,
    payment_record_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UploadPaymentRecordFileFileParams,
) -> Response[Any]:
    """Post Payment Record File

     YSCUc2FL

    POST replace/upload a supporting file for a payment record.

    This is done as a POST endpoint to handle file uploads as Django PATCH/PUT behavior does not work
    well on unit tests
    https://django-ninja.dev/guides/input/file-params/#handling-requestfiles-in-putpatch-requests

    Args:
        request: HttpRequest
        path_params: Path parameters containing organization_id and payment_record_id
        file: UploadedFile - The file to be uploaded as proof for the payment record

    Returns: 204 No Content on success

    Args:
        organization_id (UUID):
        payment_record_id (UUID):
        body (UploadPaymentRecordFileFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        payment_record_id=payment_record_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    organization_id: UUID,
    payment_record_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UploadPaymentRecordFileFileParams,
) -> Response[Any]:
    """Post Payment Record File

     YSCUc2FL

    POST replace/upload a supporting file for a payment record.

    This is done as a POST endpoint to handle file uploads as Django PATCH/PUT behavior does not work
    well on unit tests
    https://django-ninja.dev/guides/input/file-params/#handling-requestfiles-in-putpatch-requests

    Args:
        request: HttpRequest
        path_params: Path parameters containing organization_id and payment_record_id
        file: UploadedFile - The file to be uploaded as proof for the payment record

    Returns: 204 No Content on success

    Args:
        organization_id (UUID):
        payment_record_id (UUID):
        body (UploadPaymentRecordFileFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        payment_record_id=payment_record_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
