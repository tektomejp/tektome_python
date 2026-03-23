from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_project_post_in import BimProjectPostIn
from ...models.bim_project_post_out import BimProjectPostOut
from ...models.error_response_post_out import ErrorResponsePostOut
from ...types import Response


def _get_kwargs(
    *,
    body: BimProjectPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-project/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimProjectPostOut | ErrorResponsePostOut | None:
    if response.status_code == 200:
        response_200 = BimProjectPostOut.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponsePostOut.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimProjectPostOut | ErrorResponsePostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BimProjectPostIn,
) -> Response[BimProjectPostOut | ErrorResponsePostOut]:
    """Post Bim Project

     a50433ae

    Post a BIM project.

    Args:
        body (BimProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimProjectPostOut | ErrorResponsePostOut]
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
    body: BimProjectPostIn,
) -> BimProjectPostOut | ErrorResponsePostOut | None:
    """Post Bim Project

     a50433ae

    Post a BIM project.

    Args:
        body (BimProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimProjectPostOut | ErrorResponsePostOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BimProjectPostIn,
) -> Response[BimProjectPostOut | ErrorResponsePostOut]:
    """Post Bim Project

     a50433ae

    Post a BIM project.

    Args:
        body (BimProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimProjectPostOut | ErrorResponsePostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BimProjectPostIn,
) -> BimProjectPostOut | ErrorResponsePostOut | None:
    """Post Bim Project

     a50433ae

    Post a BIM project.

    Args:
        body (BimProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimProjectPostOut | ErrorResponsePostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
