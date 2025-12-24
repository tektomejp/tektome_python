from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataspace_search_tag_config_in import DataspaceSearchTagConfigIn
from ...models.dataspace_search_tag_config_out import DataspaceSearchTagConfigOut
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    *,
    body: DataspaceSearchTagConfigIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/{dataspace_id}/tag-configs/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DataspaceSearchTagConfigOut | None:
    if response.status_code == 201:
        response_201 = DataspaceSearchTagConfigOut.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchTagConfigIn,
) -> Response[DataspaceSearchTagConfigOut]:
    """Create Dataspace Tag Config

     nmlKz3da

    Create a tag configuration for the current dataspace.

    Args:
        dataspace_id (UUID):
        body (DataspaceSearchTagConfigIn): Schema for creating or updating dataspace tag
            configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceSearchTagConfigOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchTagConfigIn,
) -> DataspaceSearchTagConfigOut | None:
    """Create Dataspace Tag Config

     nmlKz3da

    Create a tag configuration for the current dataspace.

    Args:
        dataspace_id (UUID):
        body (DataspaceSearchTagConfigIn): Schema for creating or updating dataspace tag
            configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceSearchTagConfigOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchTagConfigIn,
) -> Response[DataspaceSearchTagConfigOut]:
    """Create Dataspace Tag Config

     nmlKz3da

    Create a tag configuration for the current dataspace.

    Args:
        dataspace_id (UUID):
        body (DataspaceSearchTagConfigIn): Schema for creating or updating dataspace tag
            configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceSearchTagConfigOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchTagConfigIn,
) -> DataspaceSearchTagConfigOut | None:
    """Create Dataspace Tag Config

     nmlKz3da

    Create a tag configuration for the current dataspace.

    Args:
        dataspace_id (UUID):
        body (DataspaceSearchTagConfigIn): Schema for creating or updating dataspace tag
            configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceSearchTagConfigOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            client=client,
            body=body,
        )
    ).parsed
