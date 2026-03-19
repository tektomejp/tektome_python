from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.section_creation_put_in import SectionCreationPutIn
from ...models.section_get_out import SectionGetOut
from ...types import Response


def _get_kwargs(
    section_id: UUID,
    *,
    body: SectionCreationPutIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/core/sections/{section_id}/".format(
            section_id=quote(str(section_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SectionGetOut | None:
    if response.status_code == 200:
        response_200 = SectionGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SectionGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    section_id: UUID,
    *,
    client: AuthenticatedClient,
    body: SectionCreationPutIn,
) -> Response[SectionGetOut]:
    """Update Section

     wpRZ_ydW

    Update a section by its ID.
    It will replace the existing section data's fields with the new data provided in the payload.

    Args:
        request: Request object.
        path_params: path parameters containing section ID.
        payload: SectionCreationPostIn with updated data.

    Returns: updated section details.

    Args:
        section_id (UUID):
        body (SectionCreationPutIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SectionGetOut]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    section_id: UUID,
    *,
    client: AuthenticatedClient,
    body: SectionCreationPutIn,
) -> SectionGetOut | None:
    """Update Section

     wpRZ_ydW

    Update a section by its ID.
    It will replace the existing section data's fields with the new data provided in the payload.

    Args:
        request: Request object.
        path_params: path parameters containing section ID.
        payload: SectionCreationPostIn with updated data.

    Returns: updated section details.

    Args:
        section_id (UUID):
        body (SectionCreationPutIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SectionGetOut
    """

    return sync_detailed(
        section_id=section_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    section_id: UUID,
    *,
    client: AuthenticatedClient,
    body: SectionCreationPutIn,
) -> Response[SectionGetOut]:
    """Update Section

     wpRZ_ydW

    Update a section by its ID.
    It will replace the existing section data's fields with the new data provided in the payload.

    Args:
        request: Request object.
        path_params: path parameters containing section ID.
        payload: SectionCreationPostIn with updated data.

    Returns: updated section details.

    Args:
        section_id (UUID):
        body (SectionCreationPutIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SectionGetOut]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    section_id: UUID,
    *,
    client: AuthenticatedClient,
    body: SectionCreationPutIn,
) -> SectionGetOut | None:
    """Update Section

     wpRZ_ydW

    Update a section by its ID.
    It will replace the existing section data's fields with the new data provided in the payload.

    Args:
        request: Request object.
        path_params: path parameters containing section ID.
        payload: SectionCreationPostIn with updated data.

    Returns: updated section details.

    Args:
        section_id (UUID):
        body (SectionCreationPutIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SectionGetOut
    """

    return (
        await asyncio_detailed(
            section_id=section_id,
            client=client,
            body=body,
        )
    ).parsed
