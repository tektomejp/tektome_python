from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.payment_record_patch_in_patch import PaymentRecordPatchInPatch
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    payment_record_id: UUID,
    *,
    body: PaymentRecordPatchInPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/account/organizations/{organization_id}/payment-records/{payment_record_id}/".format(
            organization_id=quote(str(organization_id), safe=""),
            payment_record_id=quote(str(payment_record_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

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
    body: PaymentRecordPatchInPatch,
) -> Response[Any]:
    """Patch Payment Record

     YSCUc2FC

    Patch a payment record.

    for debit transactions, updating credits_amount must not result in negative organization balance.

    1. we negate the current credits amount of the payment record to get the balance before applying the
    new amount
    2. we add the new credits amount to the organization balance
    3. if the adjusted balance is negative, we raise an error

    Args:
        organization_id (UUID):
        payment_record_id (UUID):
        body (PaymentRecordPatchInPatch):

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
    body: PaymentRecordPatchInPatch,
) -> Response[Any]:
    """Patch Payment Record

     YSCUc2FC

    Patch a payment record.

    for debit transactions, updating credits_amount must not result in negative organization balance.

    1. we negate the current credits amount of the payment record to get the balance before applying the
    new amount
    2. we add the new credits amount to the organization balance
    3. if the adjusted balance is negative, we raise an error

    Args:
        organization_id (UUID):
        payment_record_id (UUID):
        body (PaymentRecordPatchInPatch):

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
