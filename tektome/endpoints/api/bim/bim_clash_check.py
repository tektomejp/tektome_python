from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_clash_check_post_in import BimClashCheckPostIn
from ...models.bim_clash_check_post_out import BimClashCheckPostOut
from ...models.error_response_post_out import ErrorResponsePostOut
from ...types import Response


def _get_kwargs(
    bim_project_id: UUID,
    *,
    body: BimClashCheckPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-tools/clash-check/{bim_project_id}/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimClashCheckPostOut | ErrorResponsePostOut | None:
    if response.status_code == 200:
        response_200 = BimClashCheckPostOut.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponsePostOut.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponsePostOut.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimClashCheckPostOut | ErrorResponsePostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BimClashCheckPostIn,
) -> Response[BimClashCheckPostOut | ErrorResponsePostOut]:
    """Bim Clash Check

     FL-neCi-

    Perform clash detection on the provided BIM object IDs.

    Args:
        request: The HTTP request object.
        payload: The BIM clash check request payload containing BIM object IDs.

    Returns:
        dict: Response dictionary containing clash detection results.

    Args:
        bim_project_id (UUID):
        body (BimClashCheckPostIn): Schema for BIM clash check request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimClashCheckPostOut | ErrorResponsePostOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BimClashCheckPostIn,
) -> BimClashCheckPostOut | ErrorResponsePostOut | None:
    """Bim Clash Check

     FL-neCi-

    Perform clash detection on the provided BIM object IDs.

    Args:
        request: The HTTP request object.
        payload: The BIM clash check request payload containing BIM object IDs.

    Returns:
        dict: Response dictionary containing clash detection results.

    Args:
        bim_project_id (UUID):
        body (BimClashCheckPostIn): Schema for BIM clash check request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimClashCheckPostOut | ErrorResponsePostOut
    """

    return sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BimClashCheckPostIn,
) -> Response[BimClashCheckPostOut | ErrorResponsePostOut]:
    """Bim Clash Check

     FL-neCi-

    Perform clash detection on the provided BIM object IDs.

    Args:
        request: The HTTP request object.
        payload: The BIM clash check request payload containing BIM object IDs.

    Returns:
        dict: Response dictionary containing clash detection results.

    Args:
        bim_project_id (UUID):
        body (BimClashCheckPostIn): Schema for BIM clash check request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimClashCheckPostOut | ErrorResponsePostOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BimClashCheckPostIn,
) -> BimClashCheckPostOut | ErrorResponsePostOut | None:
    """Bim Clash Check

     FL-neCi-

    Perform clash detection on the provided BIM object IDs.

    Args:
        request: The HTTP request object.
        payload: The BIM clash check request payload containing BIM object IDs.

    Returns:
        dict: Response dictionary containing clash detection results.

    Args:
        bim_project_id (UUID):
        body (BimClashCheckPostIn): Schema for BIM clash check request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimClashCheckPostOut | ErrorResponsePostOut
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            client=client,
            body=body,
        )
    ).parsed
