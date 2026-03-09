from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.me_patch_in import MePatchIn
from ...models.me_patch_out import MePatchOut
from ...types import Response


def _get_kwargs(
    *,
    body: MePatchIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/account/users/me/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MePatchOut | None:
    if response.status_code == 200:
        response_200 = MePatchOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MePatchOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MePatchIn,
) -> Response[MePatchOut]:
    r"""Patch Me

     Mq2DXyAx
    Patch current user profile
    gender can be one of:
    ```
    \"m\": \"Male\",
    \"f\": \"Female\",
    \"n\": \"Non-binary\",
    \"o\": \"Other\",
    ```

    Args:
        body (MePatchIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MePatchOut]
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
    body: MePatchIn,
) -> MePatchOut | None:
    r"""Patch Me

     Mq2DXyAx
    Patch current user profile
    gender can be one of:
    ```
    \"m\": \"Male\",
    \"f\": \"Female\",
    \"n\": \"Non-binary\",
    \"o\": \"Other\",
    ```

    Args:
        body (MePatchIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MePatchOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MePatchIn,
) -> Response[MePatchOut]:
    r"""Patch Me

     Mq2DXyAx
    Patch current user profile
    gender can be one of:
    ```
    \"m\": \"Male\",
    \"f\": \"Female\",
    \"n\": \"Non-binary\",
    \"o\": \"Other\",
    ```

    Args:
        body (MePatchIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MePatchOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MePatchIn,
) -> MePatchOut | None:
    r"""Patch Me

     Mq2DXyAx
    Patch current user profile
    gender can be one of:
    ```
    \"m\": \"Male\",
    \"f\": \"Female\",
    \"n\": \"Non-binary\",
    \"o\": \"Other\",
    ```

    Args:
        body (MePatchIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MePatchOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
