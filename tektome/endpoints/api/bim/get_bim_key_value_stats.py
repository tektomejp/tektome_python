from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_key_value_stats_out import BimKeyValueStatsOut
from ...types import Response


def _get_kwargs(
    bim_project_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/bim/bim-tools/key-value-stats/{bim_project_id}/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimKeyValueStatsOut | str | None:
    if response.status_code == 200:
        response_200 = BimKeyValueStatsOut.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404

    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimKeyValueStatsOut | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[BimKeyValueStatsOut | str]:
    """Bim Key Value Stats

     8MsaUZ2x

    Retrieve key-value statistics for a given BIM project.

    Returns the pre-computed key-value statistics from Elasticsearch for the BIM project.
    If the statistics do not exist, returns a 404 error and clients must trigger generation
    via the POST endpoint.

    Returns:
        200: Key-value statistics as JSON
        404: Statistics not found (trigger generation via POST)
        500: Internal server error

    Args:
        bim_project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimKeyValueStatsOut | str]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
) -> BimKeyValueStatsOut | str | None:
    """Bim Key Value Stats

     8MsaUZ2x

    Retrieve key-value statistics for a given BIM project.

    Returns the pre-computed key-value statistics from Elasticsearch for the BIM project.
    If the statistics do not exist, returns a 404 error and clients must trigger generation
    via the POST endpoint.

    Returns:
        200: Key-value statistics as JSON
        404: Statistics not found (trigger generation via POST)
        500: Internal server error

    Args:
        bim_project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimKeyValueStatsOut | str
    """

    return sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[BimKeyValueStatsOut | str]:
    """Bim Key Value Stats

     8MsaUZ2x

    Retrieve key-value statistics for a given BIM project.

    Returns the pre-computed key-value statistics from Elasticsearch for the BIM project.
    If the statistics do not exist, returns a 404 error and clients must trigger generation
    via the POST endpoint.

    Returns:
        200: Key-value statistics as JSON
        404: Statistics not found (trigger generation via POST)
        500: Internal server error

    Args:
        bim_project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimKeyValueStatsOut | str]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
) -> BimKeyValueStatsOut | str | None:
    """Bim Key Value Stats

     8MsaUZ2x

    Retrieve key-value statistics for a given BIM project.

    Returns the pre-computed key-value statistics from Elasticsearch for the BIM project.
    If the statistics do not exist, returns a 404 error and clients must trigger generation
    via the POST endpoint.

    Returns:
        200: Key-value statistics as JSON
        404: Statistics not found (trigger generation via POST)
        500: Internal server error

    Args:
        bim_project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimKeyValueStatsOut | str
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            client=client,
        )
    ).parsed
