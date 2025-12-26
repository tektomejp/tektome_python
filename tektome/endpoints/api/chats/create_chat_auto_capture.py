from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_chat_auto_capture_response import CreateChatAutoCaptureResponse
from ...models.lawtalk_requirement_chat_post_in import LawtalkRequirementChatPostIn
from ...types import Response


def _get_kwargs(
    *,
    body: LawtalkRequirementChatPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/agents/chats/chat-auto-capture/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateChatAutoCaptureResponse | None:
    if response.status_code == 200:
        response_200 = CreateChatAutoCaptureResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateChatAutoCaptureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LawtalkRequirementChatPostIn,
) -> Response[CreateChatAutoCaptureResponse]:
    """Post Chat Auto Capture

     LYaOS3Op


    Post a chat message to a lawtalk requirement chatroom.

    Args:
        request: The request object containing authentication and user information.
        payload:  The payload containing chatroom ID, prompt, recipe, and requirement details.

    Returns: Chatroom ID of the created or existing chatroom.

    Args:
        body (LawtalkRequirementChatPostIn): Serializer for posting a chat message to a lawtalk
            requirement chatroom.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateChatAutoCaptureResponse]
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
    body: LawtalkRequirementChatPostIn,
) -> CreateChatAutoCaptureResponse | None:
    """Post Chat Auto Capture

     LYaOS3Op


    Post a chat message to a lawtalk requirement chatroom.

    Args:
        request: The request object containing authentication and user information.
        payload:  The payload containing chatroom ID, prompt, recipe, and requirement details.

    Returns: Chatroom ID of the created or existing chatroom.

    Args:
        body (LawtalkRequirementChatPostIn): Serializer for posting a chat message to a lawtalk
            requirement chatroom.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateChatAutoCaptureResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LawtalkRequirementChatPostIn,
) -> Response[CreateChatAutoCaptureResponse]:
    """Post Chat Auto Capture

     LYaOS3Op


    Post a chat message to a lawtalk requirement chatroom.

    Args:
        request: The request object containing authentication and user information.
        payload:  The payload containing chatroom ID, prompt, recipe, and requirement details.

    Returns: Chatroom ID of the created or existing chatroom.

    Args:
        body (LawtalkRequirementChatPostIn): Serializer for posting a chat message to a lawtalk
            requirement chatroom.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateChatAutoCaptureResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LawtalkRequirementChatPostIn,
) -> CreateChatAutoCaptureResponse | None:
    """Post Chat Auto Capture

     LYaOS3Op


    Post a chat message to a lawtalk requirement chatroom.

    Args:
        request: The request object containing authentication and user information.
        payload:  The payload containing chatroom ID, prompt, recipe, and requirement details.

    Returns: Chatroom ID of the created or existing chatroom.

    Args:
        body (LawtalkRequirementChatPostIn): Serializer for posting a chat message to a lawtalk
            requirement chatroom.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateChatAutoCaptureResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
