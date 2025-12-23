from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appresource_routers_bims_bims_projects_delete_bim_element_bim_element_type_path import (
    AppresourceRoutersBimsBimsProjectsDeleteBimElementBimElementTypePath,
)
from ...models.error_response_post_out import ErrorResponsePostOut
from ...types import Response


def _get_kwargs(
    bim_project_id: UUID,
    bim_type: AppresourceRoutersBimsBimsProjectsDeleteBimElementBimElementTypePath,
    bim_element_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/core/resource-groups/bim/bim-project/{bim_project_id}/{bim_type}/{bim_element_id}/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
            bim_type=quote(str(bim_type), safe=""),
            bim_element_id=quote(str(bim_element_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponsePostOut | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = ErrorResponsePostOut.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponsePostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_project_id: UUID,
    bim_type: AppresourceRoutersBimsBimsProjectsDeleteBimElementBimElementTypePath,
    bim_element_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ErrorResponsePostOut]:
    """Delete Bim Element

     bb01ed07

    Delete a BIM element. Could be BIM object or view.

    Args:
        bim_project_id (UUID):
        bim_type (AppresourceRoutersBimsBimsProjectsDeleteBimElementBimElementTypePath): Enum for
            BIM object types.
        bim_element_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponsePostOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        bim_type=bim_type,
        bim_element_id=bim_element_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_project_id: UUID,
    bim_type: AppresourceRoutersBimsBimsProjectsDeleteBimElementBimElementTypePath,
    bim_element_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ErrorResponsePostOut | None:
    """Delete Bim Element

     bb01ed07

    Delete a BIM element. Could be BIM object or view.

    Args:
        bim_project_id (UUID):
        bim_type (AppresourceRoutersBimsBimsProjectsDeleteBimElementBimElementTypePath): Enum for
            BIM object types.
        bim_element_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponsePostOut
    """

    return sync_detailed(
        bim_project_id=bim_project_id,
        bim_type=bim_type,
        bim_element_id=bim_element_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bim_project_id: UUID,
    bim_type: AppresourceRoutersBimsBimsProjectsDeleteBimElementBimElementTypePath,
    bim_element_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ErrorResponsePostOut]:
    """Delete Bim Element

     bb01ed07

    Delete a BIM element. Could be BIM object or view.

    Args:
        bim_project_id (UUID):
        bim_type (AppresourceRoutersBimsBimsProjectsDeleteBimElementBimElementTypePath): Enum for
            BIM object types.
        bim_element_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponsePostOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        bim_type=bim_type,
        bim_element_id=bim_element_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_project_id: UUID,
    bim_type: AppresourceRoutersBimsBimsProjectsDeleteBimElementBimElementTypePath,
    bim_element_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ErrorResponsePostOut | None:
    """Delete Bim Element

     bb01ed07

    Delete a BIM element. Could be BIM object or view.

    Args:
        bim_project_id (UUID):
        bim_type (AppresourceRoutersBimsBimsProjectsDeleteBimElementBimElementTypePath): Enum for
            BIM object types.
        bim_element_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponsePostOut
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            bim_type=bim_type,
            bim_element_id=bim_element_id,
            client=client,
        )
    ).parsed
