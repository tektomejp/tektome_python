from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataspace_search_tag_config_out import DataspaceSearchTagConfigOut
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    tag_config_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/dataspaces/{dataspace_id}/tag-configs/{tag_config_id}/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            tag_config_id=quote(str(tag_config_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DataspaceSearchTagConfigOut | None:
    if response.status_code == 200:
        response_200 = DataspaceSearchTagConfigOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DataspaceSearchTagConfigOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    tag_config_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[DataspaceSearchTagConfigOut]:
    """Get Dataspace Tag Config

     rSl3dZxK

    Retrieve a tag configuration for the current dataspace.

    Args:
        dataspace_id (UUID):
        tag_config_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceSearchTagConfigOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        tag_config_id=tag_config_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    tag_config_id: UUID,
    *,
    client: AuthenticatedClient,
) -> DataspaceSearchTagConfigOut | None:
    """Get Dataspace Tag Config

     rSl3dZxK

    Retrieve a tag configuration for the current dataspace.

    Args:
        dataspace_id (UUID):
        tag_config_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceSearchTagConfigOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        tag_config_id=tag_config_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    tag_config_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[DataspaceSearchTagConfigOut]:
    """Get Dataspace Tag Config

     rSl3dZxK

    Retrieve a tag configuration for the current dataspace.

    Args:
        dataspace_id (UUID):
        tag_config_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceSearchTagConfigOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        tag_config_id=tag_config_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    tag_config_id: UUID,
    *,
    client: AuthenticatedClient,
) -> DataspaceSearchTagConfigOut | None:
    """Get Dataspace Tag Config

     rSl3dZxK

    Retrieve a tag configuration for the current dataspace.

    Args:
        dataspace_id (UUID):
        tag_config_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceSearchTagConfigOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            tag_config_id=tag_config_id,
            client=client,
        )
    ).parsed
