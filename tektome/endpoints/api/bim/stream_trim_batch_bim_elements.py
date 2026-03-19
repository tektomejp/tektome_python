from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_bim_batch_trim_element_request_request import CreateBimBatchTrimElementRequestRequest
from ...models.stream_trim_batch_bim_elements_bim_element_type_path import StreamTrimBatchBimElementsBimElementTypePath
from ...types import Response


def _get_kwargs(
    bim_type: StreamTrimBatchBimElementsBimElementTypePath,
    *,
    body: CreateBimBatchTrimElementRequestRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-elements/{bim_type}/stream/trim/".format(
            bim_type=quote(str(bim_type), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
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
    bim_type: StreamTrimBatchBimElementsBimElementTypePath,
    *,
    client: AuthenticatedClient,
    body: CreateBimBatchTrimElementRequestRequest,
) -> Response[Any]:
    """Stream trimmed BIM elements as NDJSON

     Stream multiple BIM elements with only specified fields included, using NDJSON format. Useful for
    retrieving a subset of element data efficiently.

    Args:
        bim_type (StreamTrimBatchBimElementsBimElementTypePath): Enum for BIM object types.
        body (CreateBimBatchTrimElementRequestRequest): Schema for batch BIM element retrieval
            with trimming request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bim_type=bim_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    bim_type: StreamTrimBatchBimElementsBimElementTypePath,
    *,
    client: AuthenticatedClient,
    body: CreateBimBatchTrimElementRequestRequest,
) -> Response[Any]:
    """Stream trimmed BIM elements as NDJSON

     Stream multiple BIM elements with only specified fields included, using NDJSON format. Useful for
    retrieving a subset of element data efficiently.

    Args:
        bim_type (StreamTrimBatchBimElementsBimElementTypePath): Enum for BIM object types.
        body (CreateBimBatchTrimElementRequestRequest): Schema for batch BIM element retrieval
            with trimming request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bim_type=bim_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
