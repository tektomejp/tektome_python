from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generic_http_error import GenericHttpError
from ...models.notification_get_out import NotificationGetOut
from ...models.notification_testing_post_in import NotificationTestingPostIn
from ...types import Response


def _get_kwargs(
    *,
    body: NotificationTestingPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/notifications/test/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenericHttpError | list[NotificationGetOut] | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = NotificationGetOut.from_dict(response_201_item_data)

            response_201.append(response_201_item)

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
) -> Response[GenericHttpError | list[NotificationGetOut]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NotificationTestingPostIn,
) -> Response[GenericHttpError | list[NotificationGetOut]]:
    """Create test notifications for development purposes. (Disabled in production)

     crspHnfm

    Create test notifications with minimal input for development purposes.

    This endpoint creates one or more notifications for the authenticated user
    and optionally for additional target users within the specified dataspace.
    The launcher (authenticated user) is always included as a recipient.

    Note: This endpoint is marked as obsolete and may be removed in future releases.

    Args:
        body (NotificationTestingPostIn): Input schema for creating test notifications.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericHttpError | list[NotificationGetOut]]
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
    body: NotificationTestingPostIn,
) -> GenericHttpError | list[NotificationGetOut] | None:
    """Create test notifications for development purposes. (Disabled in production)

     crspHnfm

    Create test notifications with minimal input for development purposes.

    This endpoint creates one or more notifications for the authenticated user
    and optionally for additional target users within the specified dataspace.
    The launcher (authenticated user) is always included as a recipient.

    Note: This endpoint is marked as obsolete and may be removed in future releases.

    Args:
        body (NotificationTestingPostIn): Input schema for creating test notifications.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericHttpError | list[NotificationGetOut]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NotificationTestingPostIn,
) -> Response[GenericHttpError | list[NotificationGetOut]]:
    """Create test notifications for development purposes. (Disabled in production)

     crspHnfm

    Create test notifications with minimal input for development purposes.

    This endpoint creates one or more notifications for the authenticated user
    and optionally for additional target users within the specified dataspace.
    The launcher (authenticated user) is always included as a recipient.

    Note: This endpoint is marked as obsolete and may be removed in future releases.

    Args:
        body (NotificationTestingPostIn): Input schema for creating test notifications.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericHttpError | list[NotificationGetOut]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NotificationTestingPostIn,
) -> GenericHttpError | list[NotificationGetOut] | None:
    """Create test notifications for development purposes. (Disabled in production)

     crspHnfm

    Create test notifications with minimal input for development purposes.

    This endpoint creates one or more notifications for the authenticated user
    and optionally for additional target users within the specified dataspace.
    The launcher (authenticated user) is always included as a recipient.

    Note: This endpoint is marked as obsolete and may be removed in future releases.

    Args:
        body (NotificationTestingPostIn): Input schema for creating test notifications.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericHttpError | list[NotificationGetOut]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
