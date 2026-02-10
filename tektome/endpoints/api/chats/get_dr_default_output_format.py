from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_dr_default_output_format_get_out import GetDRDefaultOutputFormatGetOut
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/agents/chats/get_dr_default_output_format/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetDRDefaultOutputFormatGetOut | None:
    if response.status_code == 200:
        response_200 = GetDRDefaultOutputFormatGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetDRDefaultOutputFormatGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetDRDefaultOutputFormatGetOut]:
    """Get Deep Research Default Output Format

     jxg-Cooc

    Get the default output format for Deep Research.
    If no default exists, returns an empty string.

    Returns:
        str: The default output format for Deep Research, or an empty string if not set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDRDefaultOutputFormatGetOut]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> GetDRDefaultOutputFormatGetOut | None:
    """Get Deep Research Default Output Format

     jxg-Cooc

    Get the default output format for Deep Research.
    If no default exists, returns an empty string.

    Returns:
        str: The default output format for Deep Research, or an empty string if not set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDRDefaultOutputFormatGetOut
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetDRDefaultOutputFormatGetOut]:
    """Get Deep Research Default Output Format

     jxg-Cooc

    Get the default output format for Deep Research.
    If no default exists, returns an empty string.

    Returns:
        str: The default output format for Deep Research, or an empty string if not set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDRDefaultOutputFormatGetOut]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> GetDRDefaultOutputFormatGetOut | None:
    """Get Deep Research Default Output Format

     jxg-Cooc

    Get the default output format for Deep Research.
    If no default exists, returns an empty string.

    Returns:
        str: The default output format for Deep Research, or an empty string if not set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDRDefaultOutputFormatGetOut
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
