from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    requirement_item_column_config_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/app/lawtalk/projects/requirement-item-column-configs/{requirement_item_column_config_id}/".format(
            requirement_item_column_config_id=quote(str(requirement_item_column_config_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    requirement_item_column_config_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete Project Requirement Item Column Config

     3m4n5o6P

    Delete a requirement item column configuration for a project.

    Cascades delete all requirement items associated with this column config.

    Args:
        requirement_item_column_config_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        requirement_item_column_config_id=requirement_item_column_config_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    requirement_item_column_config_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete Project Requirement Item Column Config

     3m4n5o6P

    Delete a requirement item column configuration for a project.

    Cascades delete all requirement items associated with this column config.

    Args:
        requirement_item_column_config_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        requirement_item_column_config_id=requirement_item_column_config_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
