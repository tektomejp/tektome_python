from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_key_value_search_post_v2_in import BimKeyValueSearchPostV2In
from ...models.stream_bim_element_key_value_search_bim_element_type_v2_path import (
    StreamBimElementKeyValueSearchBimElementTypeV2Path,
)
from ...types import UNSET, Response


def _get_kwargs(
    bim_element: StreamBimElementKeyValueSearchBimElementTypeV2Path,
    *,
    body: BimKeyValueSearchPostV2In,
    bim_project_id: UUID,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_bim_project_id = str(bim_project_id)
    params["bim_project_id"] = json_bim_project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-search/kv-search/{bim_element}/v2/stream/".format(
            bim_element=quote(str(bim_element), safe=""),
        ),
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
    bim_element: StreamBimElementKeyValueSearchBimElementTypeV2Path,
    *,
    client: AuthenticatedClient,
    body: BimKeyValueSearchPostV2In,
    bim_project_id: UUID,
) -> Response[Any]:
    r"""Bim Element Key Value Search V2

     zYFYOkp6

    Scroll-based search endpoint that streams IDs only as NDJSON.

    - Uses Elasticsearch scroll API via .scan() method for automatic handling.
    - Returns only document IDs (lightweight) streamed as newline-delimited JSON.
    - Caps results at 150_000 to avoid runaway exports.
    - Streams results as they are retrieved, no waiting for full result set.
    - Supports BIM element types: bim-object, bim-view, bim-sheet

    Response format: NDJSON (one JSON object per line)
    Each line: {\"id\": \"document_id\"}

    Args:
        bim_element (StreamBimElementKeyValueSearchBimElementTypeV2Path): An enumeration
            representing different BIM (Building Information Modeling) element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element
            type.
        bim_project_id (UUID):
        body (BimKeyValueSearchPostV2In): Schema for key-value search in BIM file_content JSON.

            Supports wildcard patterns using '*':
            - key="*" matches any key name
            - value="prefix*" matches values starting with "prefix"
            - value="*suffix" matches values ending with "suffix"
            - value="*middle*" matches values containing "middle"

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bim_element=bim_element,
        body=body,
        bim_project_id=bim_project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    bim_element: StreamBimElementKeyValueSearchBimElementTypeV2Path,
    *,
    client: AuthenticatedClient,
    body: BimKeyValueSearchPostV2In,
    bim_project_id: UUID,
) -> Response[Any]:
    r"""Bim Element Key Value Search V2

     zYFYOkp6

    Scroll-based search endpoint that streams IDs only as NDJSON.

    - Uses Elasticsearch scroll API via .scan() method for automatic handling.
    - Returns only document IDs (lightweight) streamed as newline-delimited JSON.
    - Caps results at 150_000 to avoid runaway exports.
    - Streams results as they are retrieved, no waiting for full result set.
    - Supports BIM element types: bim-object, bim-view, bim-sheet

    Response format: NDJSON (one JSON object per line)
    Each line: {\"id\": \"document_id\"}

    Args:
        bim_element (StreamBimElementKeyValueSearchBimElementTypeV2Path): An enumeration
            representing different BIM (Building Information Modeling) element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element
            type.
        bim_project_id (UUID):
        body (BimKeyValueSearchPostV2In): Schema for key-value search in BIM file_content JSON.

            Supports wildcard patterns using '*':
            - key="*" matches any key name
            - value="prefix*" matches values starting with "prefix"
            - value="*suffix" matches values ending with "suffix"
            - value="*middle*" matches values containing "middle"

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bim_element=bim_element,
        body=body,
        bim_project_id=bim_project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
