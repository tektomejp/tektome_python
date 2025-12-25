from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keywords import Keywords
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    text: str,
    include_inflections: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["text"] = text

    params["include_inflections"] = include_inflections

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/utils/keywords/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Keywords | None:
    if response.status_code == 200:
        response_200 = Keywords.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Keywords]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    text: str,
    include_inflections: bool | Unset = False,
) -> Response[Keywords]:
    """Get Keywords

     UOn7hBJp

    Get keywords from text using NLP techniques.

    Args:
        request: Request object
        query_params: request payload of type Text

    Returns:
        A response containing extracted keywords as a list of strings with no inherent order and no
    duplicates.

    Args:
        text (str):
        include_inflections (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Keywords]
    """

    kwargs = _get_kwargs(
        text=text,
        include_inflections=include_inflections,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    text: str,
    include_inflections: bool | Unset = False,
) -> Keywords | None:
    """Get Keywords

     UOn7hBJp

    Get keywords from text using NLP techniques.

    Args:
        request: Request object
        query_params: request payload of type Text

    Returns:
        A response containing extracted keywords as a list of strings with no inherent order and no
    duplicates.

    Args:
        text (str):
        include_inflections (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Keywords
    """

    return sync_detailed(
        client=client,
        text=text,
        include_inflections=include_inflections,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    text: str,
    include_inflections: bool | Unset = False,
) -> Response[Keywords]:
    """Get Keywords

     UOn7hBJp

    Get keywords from text using NLP techniques.

    Args:
        request: Request object
        query_params: request payload of type Text

    Returns:
        A response containing extracted keywords as a list of strings with no inherent order and no
    duplicates.

    Args:
        text (str):
        include_inflections (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Keywords]
    """

    kwargs = _get_kwargs(
        text=text,
        include_inflections=include_inflections,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    text: str,
    include_inflections: bool | Unset = False,
) -> Keywords | None:
    """Get Keywords

     UOn7hBJp

    Get keywords from text using NLP techniques.

    Args:
        request: Request object
        query_params: request payload of type Text

    Returns:
        A response containing extracted keywords as a list of strings with no inherent order and no
    duplicates.

    Args:
        text (str):
        include_inflections (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Keywords
    """

    return (
        await asyncio_detailed(
            client=client,
            text=text,
            include_inflections=include_inflections,
        )
    ).parsed
