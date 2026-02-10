from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_extracted_page_get_out import GetExtractedPageGetOut
from ...types import Response


def _get_kwargs(
    resource_id: str,
    page_num: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/resources/{resource_id}/initialized/page/{page_num}/".format(
            resource_id=quote(str(resource_id), safe=""),
            page_num=quote(str(page_num), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetExtractedPageGetOut | None:
    if response.status_code == 200:
        response_200 = GetExtractedPageGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetExtractedPageGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_id: str,
    page_num: int,
    *,
    client: AuthenticatedClient,
) -> Response[GetExtractedPageGetOut]:
    """Get Initialized Page

     gcN-KWes

    Get the initialized data from a page

    Args:
        resource_id (str):
        page_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetExtractedPageGetOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        page_num=page_num,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_id: str,
    page_num: int,
    *,
    client: AuthenticatedClient,
) -> GetExtractedPageGetOut | None:
    """Get Initialized Page

     gcN-KWes

    Get the initialized data from a page

    Args:
        resource_id (str):
        page_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetExtractedPageGetOut
    """

    return sync_detailed(
        resource_id=resource_id,
        page_num=page_num,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_id: str,
    page_num: int,
    *,
    client: AuthenticatedClient,
) -> Response[GetExtractedPageGetOut]:
    """Get Initialized Page

     gcN-KWes

    Get the initialized data from a page

    Args:
        resource_id (str):
        page_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetExtractedPageGetOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        page_num=page_num,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_id: str,
    page_num: int,
    *,
    client: AuthenticatedClient,
) -> GetExtractedPageGetOut | None:
    """Get Initialized Page

     gcN-KWes

    Get the initialized data from a page

    Args:
        resource_id (str):
        page_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetExtractedPageGetOut
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            page_num=page_num,
            client=client,
        )
    ).parsed
