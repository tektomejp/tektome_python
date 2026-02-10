from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stream_bim_elements_by_project_bim_element_type_v2_path import (
    StreamBimElementsByProjectBimElementTypeV2Path,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bim_project_id: UUID,
    bim_type: StreamBimElementsByProjectBimElementTypeV2Path,
    *,
    id_only: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id_only"] = id_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/bim/bim-project/{bim_project_id}/{bim_type}/stream/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
            bim_type=quote(str(bim_type), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_project_id: UUID,
    bim_type: StreamBimElementsByProjectBimElementTypeV2Path,
    *,
    client: AuthenticatedClient,
    id_only: bool | Unset = False,
) -> Response[Any]:
    """Stream Bim Elements By Project

     uZvgf1HG

    Stream BIM elements for a specific project and model.

    This function retrieves BIM elements from a project, either as full element data
    or just element IDs, depending on the id_only parameter.

    Args:
        request: The incoming request object (unused in current implementation).
        path (Path[ABimProjectElementTypePath]): Path object containing the BIM project ID
            and BIM model information.
        id_only (bool, optional): If True, returns only element IDs. If False, returns
            full element data. Defaults to False.

    Returns:
        Generator or Iterator: A stream of BIM elements or element IDs depending on
            the id_only parameter. Returns element IDs if id_only is True, otherwise
            returns full element objects.

    Args:
        bim_project_id (UUID):
        bim_type (StreamBimElementsByProjectBimElementTypeV2Path): An enumeration representing
            different BIM (Building Information Modeling) element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element
            type.
        id_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        bim_type=bim_type,
        id_only=id_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    bim_project_id: UUID,
    bim_type: StreamBimElementsByProjectBimElementTypeV2Path,
    *,
    client: AuthenticatedClient,
    id_only: bool | Unset = False,
) -> Response[Any]:
    """Stream Bim Elements By Project

     uZvgf1HG

    Stream BIM elements for a specific project and model.

    This function retrieves BIM elements from a project, either as full element data
    or just element IDs, depending on the id_only parameter.

    Args:
        request: The incoming request object (unused in current implementation).
        path (Path[ABimProjectElementTypePath]): Path object containing the BIM project ID
            and BIM model information.
        id_only (bool, optional): If True, returns only element IDs. If False, returns
            full element data. Defaults to False.

    Returns:
        Generator or Iterator: A stream of BIM elements or element IDs depending on
            the id_only parameter. Returns element IDs if id_only is True, otherwise
            returns full element objects.

    Args:
        bim_project_id (UUID):
        bim_type (StreamBimElementsByProjectBimElementTypeV2Path): An enumeration representing
            different BIM (Building Information Modeling) element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element
            type.
        id_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        bim_type=bim_type,
        id_only=id_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
