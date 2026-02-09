from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    requirement_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/requirements/{requirement_id}/summarize/".format(
            requirement_id=quote(str(requirement_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
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
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get Requirement Summary

     gvl_NLA2

    Streams a summary of requirement's sections using Server-Sent Events (SSE).
    The summary is saved to the requirement after streaming is complete.

    Sample usage:
    ```
    curl -N -X 'GET'
    'http://localhost:8000/api/app/lawtalk/requirements/89138b7a-3753-467d-a3b1-49c2d26d9cf1/summarize/'
    -H 'accept: text/event-stream'       -H 'Authorization: Bearer <bearer_token>'
    ```

    Args:
        requirement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get Requirement Summary

     gvl_NLA2

    Streams a summary of requirement's sections using Server-Sent Events (SSE).
    The summary is saved to the requirement after streaming is complete.

    Sample usage:
    ```
    curl -N -X 'GET'
    'http://localhost:8000/api/app/lawtalk/requirements/89138b7a-3753-467d-a3b1-49c2d26d9cf1/summarize/'
    -H 'accept: text/event-stream'       -H 'Authorization: Bearer <bearer_token>'
    ```

    Args:
        requirement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
