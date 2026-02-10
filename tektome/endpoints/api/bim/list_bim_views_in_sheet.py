from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_bim_views_in_sheet_get_out import RetrieveBimViewsInSheetGetOut
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
) -> RetrieveBimViewsInSheetGetOut | None:
    if response.status_code == 200:
        response_200 = RetrieveBimViewsInSheetGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrieveBimViewsInSheetGetOut]:
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
) -> Response[RetrieveBimViewsInSheetGetOut]:
    r"""Retrieve Bim Views In Sheets

     8V6ckG7x

    Retrieve BIM views associated with a specific BIM sheet.

    Args:
        request: The request object (unused in this function).
        bim_sheet_id (str): The unique identifier of the BIM sheet.
        only_ids (bool, optional): If True, return only the IDs of the views. Defaults to False.

    Returns:
        dict: A dictionary containing either the list of views (under \"data\") and None for \"error\",
              or an error message (under \"error\") and an empty list for \"data\" if the sheet or views
    are not found.

    Args:
        bim_sheet_id (str):
        only_ids (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBimViewsInSheetGetOut]
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
) -> RetrieveBimViewsInSheetGetOut | None:
    r"""Retrieve Bim Views In Sheets

     8V6ckG7x

    Retrieve BIM views associated with a specific BIM sheet.

    Args:
        request: The request object (unused in this function).
        bim_sheet_id (str): The unique identifier of the BIM sheet.
        only_ids (bool, optional): If True, return only the IDs of the views. Defaults to False.

    Returns:
        dict: A dictionary containing either the list of views (under \"data\") and None for \"error\",
              or an error message (under \"error\") and an empty list for \"data\" if the sheet or views
    are not found.

    Args:
        bim_sheet_id (str):
        only_ids (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBimViewsInSheetGetOut
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
) -> Response[RetrieveBimViewsInSheetGetOut]:
    r"""Retrieve Bim Views In Sheets

     8V6ckG7x

    Retrieve BIM views associated with a specific BIM sheet.

    Args:
        request: The request object (unused in this function).
        bim_sheet_id (str): The unique identifier of the BIM sheet.
        only_ids (bool, optional): If True, return only the IDs of the views. Defaults to False.

    Returns:
        dict: A dictionary containing either the list of views (under \"data\") and None for \"error\",
              or an error message (under \"error\") and an empty list for \"data\" if the sheet or views
    are not found.

    Args:
        bim_sheet_id (str):
        only_ids (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBimViewsInSheetGetOut]
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
) -> RetrieveBimViewsInSheetGetOut | None:
    r"""Retrieve Bim Views In Sheets

     8V6ckG7x

    Retrieve BIM views associated with a specific BIM sheet.

    Args:
        request: The request object (unused in this function).
        bim_sheet_id (str): The unique identifier of the BIM sheet.
        only_ids (bool, optional): If True, return only the IDs of the views. Defaults to False.

    Returns:
        dict: A dictionary containing either the list of views (under \"data\") and None for \"error\",
              or an error message (under \"error\") and an empty list for \"data\" if the sheet or views
    are not found.

    Args:
        bim_sheet_id (str):
        only_ids (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBimViewsInSheetGetOut
    """

    return (
        await asyncio_detailed(
            bim_sheet_id=bim_sheet_id,
            client=client,
            only_ids=only_ids,
        )
    ).parsed
