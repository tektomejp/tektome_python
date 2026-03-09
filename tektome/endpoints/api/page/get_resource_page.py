from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_component_schema_get_out import PageComponentSchemaGetOut
from ...types import Response


def _get_kwargs(
    resource_id: UUID,
    page_num: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/resources/{resource_id}/pages/{page_num}/".format(
            resource_id=quote(str(resource_id), safe=""),
            page_num=quote(str(page_num), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageComponentSchemaGetOut | None:
    if response.status_code == 200:
        response_200 = PageComponentSchemaGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageComponentSchemaGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_id: UUID,
    page_num: int,
    *,
    client: AuthenticatedClient,
) -> Response[PageComponentSchemaGetOut]:
    """Get Resource Page

     ICLG7SjX

    Retrieve a specific page of a resource.

    Args:
        resource_id (UUID):
        page_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageComponentSchemaGetOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        page_num=page_num,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_id: UUID,
    page_num: int,
    *,
    client: AuthenticatedClient,
) -> PageComponentSchemaGetOut | None:
    """Get Resource Page

     ICLG7SjX

    Retrieve a specific page of a resource.

    Args:
        resource_id (UUID):
        page_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageComponentSchemaGetOut
    """

    return sync_detailed(
        resource_id=resource_id,
        page_num=page_num,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_id: UUID,
    page_num: int,
    *,
    client: AuthenticatedClient,
) -> Response[PageComponentSchemaGetOut]:
    """Get Resource Page

     ICLG7SjX

    Retrieve a specific page of a resource.

    Args:
        resource_id (UUID):
        page_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageComponentSchemaGetOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        page_num=page_num,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_id: UUID,
    page_num: int,
    *,
    client: AuthenticatedClient,
) -> PageComponentSchemaGetOut | None:
    """Get Resource Page

     ICLG7SjX

    Retrieve a specific page of a resource.

    Args:
        resource_id (UUID):
        page_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageComponentSchemaGetOut
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            page_num=page_num,
            client=client,
        )
    ).parsed
