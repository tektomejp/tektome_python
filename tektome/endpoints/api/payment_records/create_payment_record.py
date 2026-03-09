from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_payment_record_multi_part_body_params import CreatePaymentRecordMultiPartBodyParams
from ...models.payment_record_out_base import PaymentRecordOutBase
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    *,
    body: CreatePaymentRecordMultiPartBodyParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/account/organizations/{organization_id}/payment-records/".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaymentRecordOutBase | None:
    if response.status_code == 201:
        response_201 = PaymentRecordOutBase.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaymentRecordOutBase]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreatePaymentRecordMultiPartBodyParams,
) -> Response[PaymentRecordOutBase]:
    """Post Payment Records

     YSCUc2FA

    Create a new payment record for an organization.

    Args:
        organization_id (UUID):
        body (CreatePaymentRecordMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentRecordOutBase]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreatePaymentRecordMultiPartBodyParams,
) -> PaymentRecordOutBase | None:
    """Post Payment Records

     YSCUc2FA

    Create a new payment record for an organization.

    Args:
        organization_id (UUID):
        body (CreatePaymentRecordMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentRecordOutBase
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreatePaymentRecordMultiPartBodyParams,
) -> Response[PaymentRecordOutBase]:
    """Post Payment Records

     YSCUc2FA

    Create a new payment record for an organization.

    Args:
        organization_id (UUID):
        body (CreatePaymentRecordMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentRecordOutBase]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreatePaymentRecordMultiPartBodyParams,
) -> PaymentRecordOutBase | None:
    """Post Payment Records

     YSCUc2FA

    Create a new payment record for an organization.

    Args:
        organization_id (UUID):
        body (CreatePaymentRecordMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentRecordOutBase
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            body=body,
        )
    ).parsed
