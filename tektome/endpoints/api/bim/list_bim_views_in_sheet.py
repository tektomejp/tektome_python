from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_bim_views_in_sheet_response import RetrieveBimViewsInSheetResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bim_sheet_id: str,
    *,
    only_ids: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["only_ids"] = only_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/bim/bim-sheet/{bim_sheet_id}/views/".format(
            bim_sheet_id=quote(str(bim_sheet_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrieveBimViewsInSheetResponse | None:
    if response.status_code == 200:
        response_200 = RetrieveBimViewsInSheetResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrieveBimViewsInSheetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_sheet_id: str,
    *,
    client: AuthenticatedClient,
    only_ids: bool | Unset = False,
) -> Response[RetrieveBimViewsInSheetResponse]:
    """List BIM views in a sheet

     Retrieve all BIM views associated with a specific BIM sheet. Optionally return only view IDs.

    Args:
        bim_sheet_id (str):
        only_ids (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBimViewsInSheetResponse]
    """

    kwargs = _get_kwargs(
        bim_sheet_id=bim_sheet_id,
        only_ids=only_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_sheet_id: str,
    *,
    client: AuthenticatedClient,
    only_ids: bool | Unset = False,
) -> RetrieveBimViewsInSheetResponse | None:
    """List BIM views in a sheet

     Retrieve all BIM views associated with a specific BIM sheet. Optionally return only view IDs.

    Args:
        bim_sheet_id (str):
        only_ids (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBimViewsInSheetResponse
    """

    return sync_detailed(
        bim_sheet_id=bim_sheet_id,
        client=client,
        only_ids=only_ids,
    ).parsed


async def asyncio_detailed(
    bim_sheet_id: str,
    *,
    client: AuthenticatedClient,
    only_ids: bool | Unset = False,
) -> Response[RetrieveBimViewsInSheetResponse]:
    """List BIM views in a sheet

     Retrieve all BIM views associated with a specific BIM sheet. Optionally return only view IDs.

    Args:
        bim_sheet_id (str):
        only_ids (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBimViewsInSheetResponse]
    """

    kwargs = _get_kwargs(
        bim_sheet_id=bim_sheet_id,
        only_ids=only_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_sheet_id: str,
    *,
    client: AuthenticatedClient,
    only_ids: bool | Unset = False,
) -> RetrieveBimViewsInSheetResponse | None:
    """List BIM views in a sheet

     Retrieve all BIM views associated with a specific BIM sheet. Optionally return only view IDs.

    Args:
        bim_sheet_id (str):
        only_ids (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBimViewsInSheetResponse
    """

    return (
        await asyncio_detailed(
            bim_sheet_id=bim_sheet_id,
            client=client,
            only_ids=only_ids,
        )
    ).parsed
