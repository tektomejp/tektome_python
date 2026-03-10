from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.improve_user_prompt_query_in import ImproveUserPromptQueryIn
from ...types import Response


def _get_kwargs(
    *,
    body: ImproveUserPromptQueryIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/agents/chats/suite/followup-user-query/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ImproveUserPromptQueryIn,
) -> Response[str]:
    """Post Followup User Query

     iwVaQyqA

    Post a chat message to a lawtalk requirement chatroom for improving user query.
    Args:
        request: The request object containing authentication and user information.
        payload: The payload containing user prompt to improve.

    Returns: Stream 3 followup string questions based on the user query in this format:
    ```
    1. <followup question 1>
    2. <followup question 2>
    3. <followup question 3>
    ```
    The client should listen to the stream and display the followup questions as they arrive.

    Args:
        body (ImproveUserPromptQueryIn): Serializer for improving user prompt query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
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
    body: ImproveUserPromptQueryIn,
) -> str | None:
    """Post Followup User Query

     iwVaQyqA

    Post a chat message to a lawtalk requirement chatroom for improving user query.
    Args:
        request: The request object containing authentication and user information.
        payload: The payload containing user prompt to improve.

    Returns: Stream 3 followup string questions based on the user query in this format:
    ```
    1. <followup question 1>
    2. <followup question 2>
    3. <followup question 3>
    ```
    The client should listen to the stream and display the followup questions as they arrive.

    Args:
        body (ImproveUserPromptQueryIn): Serializer for improving user prompt query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ImproveUserPromptQueryIn,
) -> Response[str]:
    """Post Followup User Query

     iwVaQyqA

    Post a chat message to a lawtalk requirement chatroom for improving user query.
    Args:
        request: The request object containing authentication and user information.
        payload: The payload containing user prompt to improve.

    Returns: Stream 3 followup string questions based on the user query in this format:
    ```
    1. <followup question 1>
    2. <followup question 2>
    3. <followup question 3>
    ```
    The client should listen to the stream and display the followup questions as they arrive.

    Args:
        body (ImproveUserPromptQueryIn): Serializer for improving user prompt query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ImproveUserPromptQueryIn,
) -> str | None:
    """Post Followup User Query

     iwVaQyqA

    Post a chat message to a lawtalk requirement chatroom for improving user query.
    Args:
        request: The request object containing authentication and user information.
        payload: The payload containing user prompt to improve.

    Returns: Stream 3 followup string questions based on the user query in this format:
    ```
    1. <followup question 1>
    2. <followup question 2>
    3. <followup question 3>
    ```
    The client should listen to the stream and display the followup questions as they arrive.

    Args:
        body (ImproveUserPromptQueryIn): Serializer for improving user prompt query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
