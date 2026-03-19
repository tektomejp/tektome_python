from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chatroom_post_in import ChatroomPostIn
from ...models.chatroom_post_out import ChatroomPostOut
from ...types import Response


def _get_kwargs(
    *,
    body: ChatroomPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/agents/os/chatrooms/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatroomPostOut | None:
    if response.status_code == 201:
        response_201 = ChatroomPostOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatroomPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ChatroomPostIn,
) -> Response[ChatroomPostOut]:
    """Create a new chatroom for TektomeOS operations and instantiate artifacts

     AqZqtBsY
    Create a new chatroom for TektomeOS operations and instantiate artifacts
    - creates a chatroom
    - creates INSTRUCTIONS.md, this artifact is appended to agent's instruction/system prompt
    - creates main.openflow, this artifact is the main openflow file for the agent

    Args:
        body (ChatroomPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatroomPostOut]
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
    body: ChatroomPostIn,
) -> ChatroomPostOut | None:
    """Create a new chatroom for TektomeOS operations and instantiate artifacts

     AqZqtBsY
    Create a new chatroom for TektomeOS operations and instantiate artifacts
    - creates a chatroom
    - creates INSTRUCTIONS.md, this artifact is appended to agent's instruction/system prompt
    - creates main.openflow, this artifact is the main openflow file for the agent

    Args:
        body (ChatroomPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatroomPostOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ChatroomPostIn,
) -> Response[ChatroomPostOut]:
    """Create a new chatroom for TektomeOS operations and instantiate artifacts

     AqZqtBsY
    Create a new chatroom for TektomeOS operations and instantiate artifacts
    - creates a chatroom
    - creates INSTRUCTIONS.md, this artifact is appended to agent's instruction/system prompt
    - creates main.openflow, this artifact is the main openflow file for the agent

    Args:
        body (ChatroomPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatroomPostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ChatroomPostIn,
) -> ChatroomPostOut | None:
    """Create a new chatroom for TektomeOS operations and instantiate artifacts

     AqZqtBsY
    Create a new chatroom for TektomeOS operations and instantiate artifacts
    - creates a chatroom
    - creates INSTRUCTIONS.md, this artifact is appended to agent's instruction/system prompt
    - creates main.openflow, this artifact is the main openflow file for the agent

    Args:
        body (ChatroomPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatroomPostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
