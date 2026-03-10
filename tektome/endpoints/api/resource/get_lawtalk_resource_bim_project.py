from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_project_stats_get_out import BimProjectStatsGetOut
from ...types import Response


def _get_kwargs(
    resource_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/resources/{resource_id}/bim-project/".format(
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BimProjectStatsGetOut | None:
    if response.status_code == 200:
        response_200 = BimProjectStatsGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimProjectStatsGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[BimProjectStatsGetOut]:
    """Get Resource Bim Project

     HvB42ioW

    Get the latest BIM project data associated with a Lawtalk Resource
    Returns: BIM project ID and BIM statistics (number of BIM objects, views, sheets)

    Args:
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimProjectStatsGetOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> BimProjectStatsGetOut | None:
    """Get Resource Bim Project

     HvB42ioW

    Get the latest BIM project data associated with a Lawtalk Resource
    Returns: BIM project ID and BIM statistics (number of BIM objects, views, sheets)

    Args:
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimProjectStatsGetOut
    """

    return sync_detailed(
        resource_id=resource_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[BimProjectStatsGetOut]:
    """Get Resource Bim Project

     HvB42ioW

    Get the latest BIM project data associated with a Lawtalk Resource
    Returns: BIM project ID and BIM statistics (number of BIM objects, views, sheets)

    Args:
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimProjectStatsGetOut]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> BimProjectStatsGetOut | None:
    """Get Resource Bim Project

     HvB42ioW

    Get the latest BIM project data associated with a Lawtalk Resource
    Returns: BIM project ID and BIM statistics (number of BIM objects, views, sheets)

    Args:
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimProjectStatsGetOut
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            client=client,
        )
    ).parsed
