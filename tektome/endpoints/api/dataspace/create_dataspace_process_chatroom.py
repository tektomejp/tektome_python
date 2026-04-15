from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generic_http_error import GenericHttpError
from ...models.process_chatroom_response import ProcessChatroomResponse
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    process_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/processes/{process_id}/chatrooms/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            process_id=quote(str(process_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenericHttpError | ProcessChatroomResponse | None:
    if response.status_code == 200:
        response_200 = ProcessChatroomResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = ProcessChatroomResponse.from_dict(response.json())

        return response_201

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
) -> Response[GenericHttpError | ProcessChatroomResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[GenericHttpError | ProcessChatroomResponse]:
    """Create chatroom from process

     Create or retrieve a chatroom linked to an existing OpenFlow process. Returns 201 if a new chatroom
    was created, or 200 if one already exists. The chatroom is initialized with the process's openflow
    JSON as the main artifact, and the process is linked to that artifact.

    Args:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericHttpError | ProcessChatroomResponse]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        process_id=process_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
) -> GenericHttpError | ProcessChatroomResponse | None:
    """Create chatroom from process

     Create or retrieve a chatroom linked to an existing OpenFlow process. Returns 201 if a new chatroom
    was created, or 200 if one already exists. The chatroom is initialized with the process's openflow
    JSON as the main artifact, and the process is linked to that artifact.

    Args:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericHttpError | ProcessChatroomResponse
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        process_id=process_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[GenericHttpError | ProcessChatroomResponse]:
    """Create chatroom from process

     Create or retrieve a chatroom linked to an existing OpenFlow process. Returns 201 if a new chatroom
    was created, or 200 if one already exists. The chatroom is initialized with the process's openflow
    JSON as the main artifact, and the process is linked to that artifact.

    Args:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericHttpError | ProcessChatroomResponse]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        process_id=process_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
) -> GenericHttpError | ProcessChatroomResponse | None:
    """Create chatroom from process

     Create or retrieve a chatroom linked to an existing OpenFlow process. Returns 201 if a new chatroom
    was created, or 200 if one already exists. The chatroom is initialized with the process's openflow
    JSON as the main artifact, and the process is linked to that artifact.

    Args:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericHttpError | ProcessChatroomResponse
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            process_id=process_id,
            client=client,
        )
    ).parsed
