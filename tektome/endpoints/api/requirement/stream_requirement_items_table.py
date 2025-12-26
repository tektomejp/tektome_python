from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_requirement_item_get_out import ProjectRequirementItemGetOut
from ...types import UNSET, Response


def _get_kwargs(
    requirement_id: UUID,
    *,
    nonce: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["nonce"] = nonce

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/requirements/{requirement_id}/stream-table-requirement-items/".format(
            requirement_id=quote(str(requirement_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProjectRequirementItemGetOut | None:
    if response.status_code == 200:
        response_200 = ProjectRequirementItemGetOut.from_dict(response.json())

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProjectRequirementItemGetOut]:
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
    nonce: int,
) -> Response[Any | ProjectRequirementItemGetOut]:
    """Get Stream Table Requirement Items

     JnQkM31Z

    Streams a new requirement items table using Server-Sent Events (SSE).
    The new requirement items table is saved to the requirement after streaming is complete.

    If there is no change, the following event is sent:

    ```
    event: end
    data: NO_CHANGE
    ```

    If there is an error, the following event is sent:

    ```
    event: error
    data: error message
    ```

    Otherwise, the generated rows are sent as they are produced:

    ```
    data: [{row1}]

    data: [{row1},{row2}]

    ...

    event: end
    data: DONE
    ```

    Args:
        requirement_id (UUID):
        nonce (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectRequirementItemGetOut]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        nonce=nonce,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    nonce: int,
) -> Any | ProjectRequirementItemGetOut | None:
    """Get Stream Table Requirement Items

     JnQkM31Z

    Streams a new requirement items table using Server-Sent Events (SSE).
    The new requirement items table is saved to the requirement after streaming is complete.

    If there is no change, the following event is sent:

    ```
    event: end
    data: NO_CHANGE
    ```

    If there is an error, the following event is sent:

    ```
    event: error
    data: error message
    ```

    Otherwise, the generated rows are sent as they are produced:

    ```
    data: [{row1}]

    data: [{row1},{row2}]

    ...

    event: end
    data: DONE
    ```

    Args:
        requirement_id (UUID):
        nonce (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectRequirementItemGetOut
    """

    return sync_detailed(
        requirement_id=requirement_id,
        client=client,
        nonce=nonce,
    ).parsed


async def asyncio_detailed(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    nonce: int,
) -> Response[Any | ProjectRequirementItemGetOut]:
    """Get Stream Table Requirement Items

     JnQkM31Z

    Streams a new requirement items table using Server-Sent Events (SSE).
    The new requirement items table is saved to the requirement after streaming is complete.

    If there is no change, the following event is sent:

    ```
    event: end
    data: NO_CHANGE
    ```

    If there is an error, the following event is sent:

    ```
    event: error
    data: error message
    ```

    Otherwise, the generated rows are sent as they are produced:

    ```
    data: [{row1}]

    data: [{row1},{row2}]

    ...

    event: end
    data: DONE
    ```

    Args:
        requirement_id (UUID):
        nonce (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectRequirementItemGetOut]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        nonce=nonce,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    nonce: int,
) -> Any | ProjectRequirementItemGetOut | None:
    """Get Stream Table Requirement Items

     JnQkM31Z

    Streams a new requirement items table using Server-Sent Events (SSE).
    The new requirement items table is saved to the requirement after streaming is complete.

    If there is no change, the following event is sent:

    ```
    event: end
    data: NO_CHANGE
    ```

    If there is an error, the following event is sent:

    ```
    event: error
    data: error message
    ```

    Otherwise, the generated rows are sent as they are produced:

    ```
    data: [{row1}]

    data: [{row1},{row2}]

    ...

    event: end
    data: DONE
    ```

    Args:
        requirement_id (UUID):
        nonce (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectRequirementItemGetOut
    """

    return (
        await asyncio_detailed(
            requirement_id=requirement_id,
            client=client,
            nonce=nonce,
        )
    ).parsed
