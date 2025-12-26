from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_api_key_post_in import CreateAPIKeyPostIn
from ...models.create_api_key_post_out import CreateAPIKeyPostOut
from ...types import Response


def _get_kwargs(
    *,
    body: CreateAPIKeyPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/account/access/api-keys/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateAPIKeyPostOut | None:
    if response.status_code == 201:
        response_201 = CreateAPIKeyPostOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateAPIKeyPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateAPIKeyPostIn,
) -> Response[CreateAPIKeyPostOut]:
    r"""Create Api Key

     Create a new API key for the current user.
    API Keys can be used to authenticate and authorize API requests according to the specified scopes.
    API Keys can be used in place as the user bearer token ex
    in the Authorization header as
    ```
    Authorization: Bearer <sk-xxxx-xxxx-xxxx-xxxx>
    ```
    Available scopes:
        - \"user:all\": Full access as the user.
    API Keys can be set valid up to one year from the creation date.

    Args:
        body (CreateAPIKeyPostIn): Schema for creating a new API key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAPIKeyPostOut]
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
    body: CreateAPIKeyPostIn,
) -> CreateAPIKeyPostOut | None:
    r"""Create Api Key

     Create a new API key for the current user.
    API Keys can be used to authenticate and authorize API requests according to the specified scopes.
    API Keys can be used in place as the user bearer token ex
    in the Authorization header as
    ```
    Authorization: Bearer <sk-xxxx-xxxx-xxxx-xxxx>
    ```
    Available scopes:
        - \"user:all\": Full access as the user.
    API Keys can be set valid up to one year from the creation date.

    Args:
        body (CreateAPIKeyPostIn): Schema for creating a new API key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAPIKeyPostOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateAPIKeyPostIn,
) -> Response[CreateAPIKeyPostOut]:
    r"""Create Api Key

     Create a new API key for the current user.
    API Keys can be used to authenticate and authorize API requests according to the specified scopes.
    API Keys can be used in place as the user bearer token ex
    in the Authorization header as
    ```
    Authorization: Bearer <sk-xxxx-xxxx-xxxx-xxxx>
    ```
    Available scopes:
        - \"user:all\": Full access as the user.
    API Keys can be set valid up to one year from the creation date.

    Args:
        body (CreateAPIKeyPostIn): Schema for creating a new API key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAPIKeyPostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateAPIKeyPostIn,
) -> CreateAPIKeyPostOut | None:
    r"""Create Api Key

     Create a new API key for the current user.
    API Keys can be used to authenticate and authorize API requests according to the specified scopes.
    API Keys can be used in place as the user bearer token ex
    in the Authorization header as
    ```
    Authorization: Bearer <sk-xxxx-xxxx-xxxx-xxxx>
    ```
    Available scopes:
        - \"user:all\": Full access as the user.
    API Keys can be set valid up to one year from the creation date.

    Args:
        body (CreateAPIKeyPostIn): Schema for creating a new API key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAPIKeyPostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
