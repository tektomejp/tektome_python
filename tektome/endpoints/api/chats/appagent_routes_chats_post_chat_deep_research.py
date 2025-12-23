from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appagent_routes_chats_post_chat_deep_research_response import (
    AppagentRoutesChatsPostChatDeepResearchResponse,
)
from ...models.deep_research_chat_post_in import DeepResearchChatPostIn
from ...types import Response


def _get_kwargs(
    *,
    body: DeepResearchChatPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/agents/chats/suite/chat-deep-research/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppagentRoutesChatsPostChatDeepResearchResponse | None:
    if response.status_code == 200:
        response_200 = AppagentRoutesChatsPostChatDeepResearchResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppagentRoutesChatsPostChatDeepResearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DeepResearchChatPostIn,
) -> Response[AppagentRoutesChatsPostChatDeepResearchResponse]:
    """Post Chat Deep Research

     iwVaQyqG

    Post a chat message to a lawtalk requirement chatroom for deep research.

    Args:
        request: The request object containing authentication and user information.
        payload: The payload containing chatroom ID, prompt, recipe, requirement, and output format
    details.

    Returns: Chatroom ID of the created or existing chatroom.

    Args:
        body (DeepResearchChatPostIn): Serializer for posting a deep research chat message.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppagentRoutesChatsPostChatDeepResearchResponse]
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
    body: DeepResearchChatPostIn,
) -> AppagentRoutesChatsPostChatDeepResearchResponse | None:
    """Post Chat Deep Research

     iwVaQyqG

    Post a chat message to a lawtalk requirement chatroom for deep research.

    Args:
        request: The request object containing authentication and user information.
        payload: The payload containing chatroom ID, prompt, recipe, requirement, and output format
    details.

    Returns: Chatroom ID of the created or existing chatroom.

    Args:
        body (DeepResearchChatPostIn): Serializer for posting a deep research chat message.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppagentRoutesChatsPostChatDeepResearchResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DeepResearchChatPostIn,
) -> Response[AppagentRoutesChatsPostChatDeepResearchResponse]:
    """Post Chat Deep Research

     iwVaQyqG

    Post a chat message to a lawtalk requirement chatroom for deep research.

    Args:
        request: The request object containing authentication and user information.
        payload: The payload containing chatroom ID, prompt, recipe, requirement, and output format
    details.

    Returns: Chatroom ID of the created or existing chatroom.

    Args:
        body (DeepResearchChatPostIn): Serializer for posting a deep research chat message.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppagentRoutesChatsPostChatDeepResearchResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DeepResearchChatPostIn,
) -> AppagentRoutesChatsPostChatDeepResearchResponse | None:
    """Post Chat Deep Research

     iwVaQyqG

    Post a chat message to a lawtalk requirement chatroom for deep research.

    Args:
        request: The request object containing authentication and user information.
        payload: The payload containing chatroom ID, prompt, recipe, requirement, and output format
    details.

    Returns: Chatroom ID of the created or existing chatroom.

    Args:
        body (DeepResearchChatPostIn): Serializer for posting a deep research chat message.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppagentRoutesChatsPostChatDeepResearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
