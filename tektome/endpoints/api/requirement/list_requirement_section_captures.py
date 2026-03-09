from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resource_capture_section_component_schema import ResourceCaptureSectionComponentSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    requirement_id: UUID,
    *,
    page_number: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_page_number: list[int] | Unset = UNSET
    if not isinstance(page_number, Unset):
        json_page_number = page_number

    params["page_number"] = json_page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/requirements/{requirement_id}/section-captures/".format(
            requirement_id=quote(str(requirement_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ResourceCaptureSectionComponentSchema] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ResourceCaptureSectionComponentSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ResourceCaptureSectionComponentSchema]]:
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
    page_number: list[int] | Unset = UNSET,
) -> Response[list[ResourceCaptureSectionComponentSchema]]:
    """Get Capture Section Components

     Ud57zekz
    Retrieve all CaptureSectionComponent objects for a ResourceSection

    Args:
        filters: filter query params of type GetCaptureSectionComponentQuery
        request: Request object
        path_params: path params of type CreateCaptureSectionComponentPath

    Returns: 200, list[CaptureSectionComponentSchema]

    Args:
        requirement_id (UUID):
        page_number (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ResourceCaptureSectionComponentSchema]]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        page_number=page_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    page_number: list[int] | Unset = UNSET,
) -> list[ResourceCaptureSectionComponentSchema] | None:
    """Get Capture Section Components

     Ud57zekz
    Retrieve all CaptureSectionComponent objects for a ResourceSection

    Args:
        filters: filter query params of type GetCaptureSectionComponentQuery
        request: Request object
        path_params: path params of type CreateCaptureSectionComponentPath

    Returns: 200, list[CaptureSectionComponentSchema]

    Args:
        requirement_id (UUID):
        page_number (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ResourceCaptureSectionComponentSchema]
    """

    return sync_detailed(
        requirement_id=requirement_id,
        client=client,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    page_number: list[int] | Unset = UNSET,
) -> Response[list[ResourceCaptureSectionComponentSchema]]:
    """Get Capture Section Components

     Ud57zekz
    Retrieve all CaptureSectionComponent objects for a ResourceSection

    Args:
        filters: filter query params of type GetCaptureSectionComponentQuery
        request: Request object
        path_params: path params of type CreateCaptureSectionComponentPath

    Returns: 200, list[CaptureSectionComponentSchema]

    Args:
        requirement_id (UUID):
        page_number (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ResourceCaptureSectionComponentSchema]]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    page_number: list[int] | Unset = UNSET,
) -> list[ResourceCaptureSectionComponentSchema] | None:
    """Get Capture Section Components

     Ud57zekz
    Retrieve all CaptureSectionComponent objects for a ResourceSection

    Args:
        filters: filter query params of type GetCaptureSectionComponentQuery
        request: Request object
        path_params: path params of type CreateCaptureSectionComponentPath

    Returns: 200, list[CaptureSectionComponentSchema]

    Args:
        requirement_id (UUID):
        page_number (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ResourceCaptureSectionComponentSchema]
    """

    return (
        await asyncio_detailed(
            requirement_id=requirement_id,
            client=client,
            page_number=page_number,
        )
    ).parsed
