from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.folder_bulk_move_post_in import FolderBulkMovePostIn
from ...models.generic_http_error import GenericHttpError
from ...types import Response


def _get_kwargs(
    *,
    body: FolderBulkMovePostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/folders/bulk-move/",
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
    *,
    client: AuthenticatedClient,
    body: FolderBulkMovePostIn,
) -> Response[Any | GenericHttpError]:
    """Post Bulk Move

     wK8mN3pL

    This API purpose is to move multiple folders and/or resources to a target folder in bulk.

    This endpoint allows moving multiple folders and resources to a specified
    target folder. It validates that no name collisions occur (unless disabled)
    and prevents circular references when moving folders.

    Args:
    payload: Input schema containing:
        - folder_id: Destination folder UUID (target)
        - folder_ids: List of folder UUIDs to move (optional)
        - resource_ids: List of resource UUIDs to move (optional)
        - check_collisions: Whether to check for name collisions (default: True)

    Returns:
        204: No Content if successful.
        400: Bad Request if name collisions detected or validation fails.
        404: Not Found if target folder or any items don't exist.

    Args:
        body (FolderBulkMovePostIn): Schema for bulk moving folders and resources to a target
            folder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GenericHttpError]
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
    body: FolderBulkMovePostIn,
) -> Any | GenericHttpError | None:
    """Post Bulk Move

     wK8mN3pL

    This API purpose is to move multiple folders and/or resources to a target folder in bulk.

    This endpoint allows moving multiple folders and resources to a specified
    target folder. It validates that no name collisions occur (unless disabled)
    and prevents circular references when moving folders.

    Args:
    payload: Input schema containing:
        - folder_id: Destination folder UUID (target)
        - folder_ids: List of folder UUIDs to move (optional)
        - resource_ids: List of resource UUIDs to move (optional)
        - check_collisions: Whether to check for name collisions (default: True)

    Returns:
        204: No Content if successful.
        400: Bad Request if name collisions detected or validation fails.
        404: Not Found if target folder or any items don't exist.

    Args:
        body (FolderBulkMovePostIn): Schema for bulk moving folders and resources to a target
            folder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GenericHttpError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: FolderBulkMovePostIn,
) -> Response[Any | GenericHttpError]:
    """Post Bulk Move

     wK8mN3pL

    This API purpose is to move multiple folders and/or resources to a target folder in bulk.

    This endpoint allows moving multiple folders and resources to a specified
    target folder. It validates that no name collisions occur (unless disabled)
    and prevents circular references when moving folders.

    Args:
    payload: Input schema containing:
        - folder_id: Destination folder UUID (target)
        - folder_ids: List of folder UUIDs to move (optional)
        - resource_ids: List of resource UUIDs to move (optional)
        - check_collisions: Whether to check for name collisions (default: True)

    Returns:
        204: No Content if successful.
        400: Bad Request if name collisions detected or validation fails.
        404: Not Found if target folder or any items don't exist.

    Args:
        body (FolderBulkMovePostIn): Schema for bulk moving folders and resources to a target
            folder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GenericHttpError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: FolderBulkMovePostIn,
) -> Any | GenericHttpError | None:
    """Post Bulk Move

     wK8mN3pL

    This API purpose is to move multiple folders and/or resources to a target folder in bulk.

    This endpoint allows moving multiple folders and resources to a specified
    target folder. It validates that no name collisions occur (unless disabled)
    and prevents circular references when moving folders.

    Args:
    payload: Input schema containing:
        - folder_id: Destination folder UUID (target)
        - folder_ids: List of folder UUIDs to move (optional)
        - resource_ids: List of resource UUIDs to move (optional)
        - check_collisions: Whether to check for name collisions (default: True)

    Returns:
        204: No Content if successful.
        400: Bad Request if name collisions detected or validation fails.
        404: Not Found if target folder or any items don't exist.

    Args:
        body (FolderBulkMovePostIn): Schema for bulk moving folders and resources to a target
            folder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GenericHttpError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
