from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chatroom_id_post_in import ChatroomIdPostIn
from ...models.generic_http_error import GenericHttpError
from ...types import Response


def _get_kwargs(
    chatroom_id: UUID,
    *,
    body: ChatroomIdPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/agents/os/chatrooms/{chatroom_id}/messages/".format(
            chatroom_id=quote(str(chatroom_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | GenericHttpError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = GenericHttpError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GenericHttpError.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GenericHttpError.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GenericHttpError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GenericHttpError.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GenericHttpError.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GenericHttpError.from_dict(response.json())

        return response_406

    if response.status_code == 407:
        response_407 = GenericHttpError.from_dict(response.json())

        return response_407

    if response.status_code == 408:
        response_408 = GenericHttpError.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = GenericHttpError.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = GenericHttpError.from_dict(response.json())

        return response_410

    if response.status_code == 411:
        response_411 = GenericHttpError.from_dict(response.json())

        return response_411

    if response.status_code == 412:
        response_412 = GenericHttpError.from_dict(response.json())

        return response_412

    if response.status_code == 416:
        response_416 = GenericHttpError.from_dict(response.json())

        return response_416

    if response.status_code == 418:
        response_418 = GenericHttpError.from_dict(response.json())

        return response_418

    if response.status_code == 425:
        response_425 = GenericHttpError.from_dict(response.json())

        return response_425

    if response.status_code == 429:
        response_429 = GenericHttpError.from_dict(response.json())

        return response_429

    if response.status_code == 451:
        response_451 = GenericHttpError.from_dict(response.json())

        return response_451

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GenericHttpError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chatroom_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ChatroomIdPostIn,
) -> Response[Any | GenericHttpError]:
    """Send a message to TektomeOS LLM agent in a chatroom

     gBOBN2PR
    Send a message to TektomeOS LLM agent in a chatroom.<br>
    Listen to ElectricSQL appagent_chatroom, appagent_message, appagent_artifact, appagent_toolcall
    tables for updates.<br>
    # Note
    There is about 100ms delay between firing and appagent_chatroom.status updates.<br>
    Optimistically set appagent_chatroom.status to `processing` on client side when sending message.<br>

    Args:
        chatroom_id (UUID):
        body (ChatroomIdPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GenericHttpError]
    """

    kwargs = _get_kwargs(
        chatroom_id=chatroom_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chatroom_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ChatroomIdPostIn,
) -> Any | GenericHttpError | None:
    """Send a message to TektomeOS LLM agent in a chatroom

     gBOBN2PR
    Send a message to TektomeOS LLM agent in a chatroom.<br>
    Listen to ElectricSQL appagent_chatroom, appagent_message, appagent_artifact, appagent_toolcall
    tables for updates.<br>
    # Note
    There is about 100ms delay between firing and appagent_chatroom.status updates.<br>
    Optimistically set appagent_chatroom.status to `processing` on client side when sending message.<br>

    Args:
        chatroom_id (UUID):
        body (ChatroomIdPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GenericHttpError
    """

    return sync_detailed(
        chatroom_id=chatroom_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    chatroom_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ChatroomIdPostIn,
) -> Response[Any | GenericHttpError]:
    """Send a message to TektomeOS LLM agent in a chatroom

     gBOBN2PR
    Send a message to TektomeOS LLM agent in a chatroom.<br>
    Listen to ElectricSQL appagent_chatroom, appagent_message, appagent_artifact, appagent_toolcall
    tables for updates.<br>
    # Note
    There is about 100ms delay between firing and appagent_chatroom.status updates.<br>
    Optimistically set appagent_chatroom.status to `processing` on client side when sending message.<br>

    Args:
        chatroom_id (UUID):
        body (ChatroomIdPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GenericHttpError]
    """

    kwargs = _get_kwargs(
        chatroom_id=chatroom_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chatroom_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ChatroomIdPostIn,
) -> Any | GenericHttpError | None:
    """Send a message to TektomeOS LLM agent in a chatroom

     gBOBN2PR
    Send a message to TektomeOS LLM agent in a chatroom.<br>
    Listen to ElectricSQL appagent_chatroom, appagent_message, appagent_artifact, appagent_toolcall
    tables for updates.<br>
    # Note
    There is about 100ms delay between firing and appagent_chatroom.status updates.<br>
    Optimistically set appagent_chatroom.status to `processing` on client side when sending message.<br>

    Args:
        chatroom_id (UUID):
        body (ChatroomIdPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GenericHttpError
    """

    return (
        await asyncio_detailed(
            chatroom_id=chatroom_id,
            client=client,
            body=body,
        )
    ).parsed
