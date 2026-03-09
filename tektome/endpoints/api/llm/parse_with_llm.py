from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.llm_parser_post_in import LlmParserPostIn
from ...models.llm_parser_post_out import LlmParserPostOut
from ...types import Response


def _get_kwargs(
    *,
    body: LlmParserPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/llms/llm-parser/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> LlmParserPostOut | None:
    if response.status_code == 200:
        response_200 = LlmParserPostOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[LlmParserPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LlmParserPostIn,
) -> Response[LlmParserPostOut]:
    """Parse text using an LLM

     Send a query to a configured LLM model for parsing and return the result. The LLM configuration is
    loaded from the database or falls back to defaults.

    Args:
        body (LlmParserPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LlmParserPostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: LlmParserPostIn,
) -> LlmParserPostOut | None:
    """Parse text using an LLM

     Send a query to a configured LLM model for parsing and return the result. The LLM configuration is
    loaded from the database or falls back to defaults.

    Args:
        body (LlmParserPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LlmParserPostOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LlmParserPostIn,
) -> Response[LlmParserPostOut]:
    """Parse text using an LLM

     Send a query to a configured LLM model for parsing and return the result. The LLM configuration is
    loaded from the database or falls back to defaults.

    Args:
        body (LlmParserPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LlmParserPostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LlmParserPostIn,
) -> LlmParserPostOut | None:
    """Parse text using an LLM

     Send a query to a configured LLM model for parsing and return the result. The LLM configuration is
    loaded from the database or falls back to defaults.

    Args:
        body (LlmParserPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LlmParserPostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
