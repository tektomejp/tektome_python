from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_value_expression_search_post_in import BimValueExpressionSearchPostIn
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: BimValueExpressionSearchPostIn,
    bim_project_id: UUID,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_bim_project_id = str(bim_project_id)
    params["bim_project_id"] = json_bim_project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-search/kv-search/bim-object/v2/query/stream/",
        "params": params,
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
    *,
    client: AuthenticatedClient,
    body: BimValueExpressionSearchPostIn,
    bim_project_id: UUID,
) -> Response[Any]:
    """Stream BIM value expression search results

     Search BIM elements using a boolean value expression and stream matching element IDs as NDJSON. The
    expression searches across all keys in typed buckets (text, numeric, boolean). Supports AND, OR, NOT
    operators, parenthesised grouping, wildcards (*), and quoted multi-word values. Returns parent
    document IDs only (excludes child chunks). Results are capped at 150,000.

    Args:
        bim_project_id (UUID):
        body (BimValueExpressionSearchPostIn): Input schema for boolean value expression search.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        bim_project_id=bim_project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BimValueExpressionSearchPostIn,
    bim_project_id: UUID,
) -> Response[Any]:
    """Stream BIM value expression search results

     Search BIM elements using a boolean value expression and stream matching element IDs as NDJSON. The
    expression searches across all keys in typed buckets (text, numeric, boolean). Supports AND, OR, NOT
    operators, parenthesised grouping, wildcards (*), and quoted multi-word values. Returns parent
    document IDs only (excludes child chunks). Results are capped at 150,000.

    Args:
        bim_project_id (UUID):
        body (BimValueExpressionSearchPostIn): Input schema for boolean value expression search.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        bim_project_id=bim_project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
