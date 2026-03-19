from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_search_result_response import BimSearchResultResponse
from ...models.create_bim_search_detail_request import CreateBimSearchDetailRequest
from ...models.search_bim_elements_bim_element_type_path import SearchBimElementsBimElementTypePath
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bim_type: SearchBimElementsBimElementTypePath,
    *,
    body: CreateBimSearchDetailRequest,
    bim_project_id: UUID,
    full: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_bim_project_id = str(bim_project_id)
    params["bim_project_id"] = json_bim_project_id

    params["full"] = full

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-elements/{bim_type}/search/".format(
            bim_type=quote(str(bim_type), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimSearchResultResponse | None:
    if response.status_code == 200:
        response_200 = BimSearchResultResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimSearchResultResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_type: SearchBimElementsBimElementTypePath,
    *,
    client: AuthenticatedClient,
    body: CreateBimSearchDetailRequest,
    bim_project_id: UUID,
    full: bool | Unset = False,
) -> Response[BimSearchResultResponse]:
    """Search BIM elements

     Deprecated. Search for BIM elements by various criteria within a project. Use the V2 streaming
    search endpoint instead.

    Args:
        bim_type (SearchBimElementsBimElementTypePath): Enum for BIM object types.
        bim_project_id (UUID):
        full (bool | Unset):  Default: False.
        body (CreateBimSearchDetailRequest): Schema for BIM search query payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimSearchResultResponse]
    """

    kwargs = _get_kwargs(
        bim_type=bim_type,
        body=body,
        bim_project_id=bim_project_id,
        full=full,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_type: SearchBimElementsBimElementTypePath,
    *,
    client: AuthenticatedClient,
    body: CreateBimSearchDetailRequest,
    bim_project_id: UUID,
    full: bool | Unset = False,
) -> BimSearchResultResponse | None:
    """Search BIM elements

     Deprecated. Search for BIM elements by various criteria within a project. Use the V2 streaming
    search endpoint instead.

    Args:
        bim_type (SearchBimElementsBimElementTypePath): Enum for BIM object types.
        bim_project_id (UUID):
        full (bool | Unset):  Default: False.
        body (CreateBimSearchDetailRequest): Schema for BIM search query payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimSearchResultResponse
    """

    return sync_detailed(
        bim_type=bim_type,
        client=client,
        body=body,
        bim_project_id=bim_project_id,
        full=full,
    ).parsed


async def asyncio_detailed(
    bim_type: SearchBimElementsBimElementTypePath,
    *,
    client: AuthenticatedClient,
    body: CreateBimSearchDetailRequest,
    bim_project_id: UUID,
    full: bool | Unset = False,
) -> Response[BimSearchResultResponse]:
    """Search BIM elements

     Deprecated. Search for BIM elements by various criteria within a project. Use the V2 streaming
    search endpoint instead.

    Args:
        bim_type (SearchBimElementsBimElementTypePath): Enum for BIM object types.
        bim_project_id (UUID):
        full (bool | Unset):  Default: False.
        body (CreateBimSearchDetailRequest): Schema for BIM search query payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimSearchResultResponse]
    """

    kwargs = _get_kwargs(
        bim_type=bim_type,
        body=body,
        bim_project_id=bim_project_id,
        full=full,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_type: SearchBimElementsBimElementTypePath,
    *,
    client: AuthenticatedClient,
    body: CreateBimSearchDetailRequest,
    bim_project_id: UUID,
    full: bool | Unset = False,
) -> BimSearchResultResponse | None:
    """Search BIM elements

     Deprecated. Search for BIM elements by various criteria within a project. Use the V2 streaming
    search endpoint instead.

    Args:
        bim_type (SearchBimElementsBimElementTypePath): Enum for BIM object types.
        bim_project_id (UUID):
        full (bool | Unset):  Default: False.
        body (CreateBimSearchDetailRequest): Schema for BIM search query payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimSearchResultResponse
    """

    return (
        await asyncio_detailed(
            bim_type=bim_type,
            client=client,
            body=body,
            bim_project_id=bim_project_id,
            full=full,
        )
    ).parsed
