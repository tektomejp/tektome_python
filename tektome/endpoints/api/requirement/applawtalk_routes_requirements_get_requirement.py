from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.requirement_get_out import RequirementGetOut
from ...types import Response


def _get_kwargs(
    requirement_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/requirements/{requirement_id}/".format(
            requirement_id=quote(str(requirement_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RequirementGetOut | None:
    if response.status_code == 200:
        response_200 = RequirementGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RequirementGetOut]:
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
) -> Response[RequirementGetOut]:
    """Get Requirement

     iy_IJGrL

    Get requirement by id
    chatrooms:
        return latest 10 chatrooms for the requirement

    Args:
        requirement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementGetOut]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
) -> RequirementGetOut | None:
    """Get Requirement

     iy_IJGrL

    Get requirement by id
    chatrooms:
        return latest 10 chatrooms for the requirement

    Args:
        requirement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementGetOut
    """

    return sync_detailed(
        requirement_id=requirement_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[RequirementGetOut]:
    """Get Requirement

     iy_IJGrL

    Get requirement by id
    chatrooms:
        return latest 10 chatrooms for the requirement

    Args:
        requirement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementGetOut]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
) -> RequirementGetOut | None:
    """Get Requirement

     iy_IJGrL

    Get requirement by id
    chatrooms:
        return latest 10 chatrooms for the requirement

    Args:
        requirement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementGetOut
    """

    return (
        await asyncio_detailed(
            requirement_id=requirement_id,
            client=client,
        )
    ).parsed
