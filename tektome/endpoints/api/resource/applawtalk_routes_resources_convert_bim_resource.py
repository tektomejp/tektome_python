from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_out import ErrorOut
from ...models.task_post_out import TaskPostOut
from ...types import Response


def _get_kwargs(
    resource_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/resources/{resource_id}/convert-bim/".format(
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorOut | TaskPostOut | None:
    if response.status_code == 201:
        response_201 = TaskPostOut.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorOut.from_dict(response.json())

        return response_400

    if response.status_code == 429:
        response_429 = ErrorOut.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorOut | TaskPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorOut | TaskPostOut]:
    """Convert Bim Resource

     38rIXHH0

    Convert BIM resource from a file attached to a resource.
    Returns: core resource BimTask id as task id

    Args:
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOut | TaskPostOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorOut | TaskPostOut | None:
    """Convert Bim Resource

     38rIXHH0

    Convert BIM resource from a file attached to a resource.
    Returns: core resource BimTask id as task id

    Args:
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOut | TaskPostOut
    """

    return sync_detailed(
        resource_id=resource_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorOut | TaskPostOut]:
    """Convert Bim Resource

     38rIXHH0

    Convert BIM resource from a file attached to a resource.
    Returns: core resource BimTask id as task id

    Args:
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOut | TaskPostOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorOut | TaskPostOut | None:
    """Convert Bim Resource

     38rIXHH0

    Convert BIM resource from a file attached to a resource.
    Returns: core resource BimTask id as task id

    Args:
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOut | TaskPostOut
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            client=client,
        )
    ).parsed
