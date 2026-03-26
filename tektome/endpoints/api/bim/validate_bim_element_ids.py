from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_validate_ids_request import BimValidateIdsRequest
from ...models.bim_validate_ids_response import BimValidateIdsResponse
from ...models.validate_bim_element_ids_bim_element_type_v2_path import ValidateBimElementIdsBimElementTypeV2Path
from ...types import UNSET, Response


def _get_kwargs(
    bim_element: ValidateBimElementIdsBimElementTypeV2Path,
    *,
    body: BimValidateIdsRequest,
    bim_project_id: UUID,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_bim_project_id = str(bim_project_id)
    params["bim_project_id"] = json_bim_project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-search/kv-search/{bim_element}/v2/validate-ids/".format(
            bim_element=quote(str(bim_element), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BimValidateIdsResponse | None:
    if response.status_code == 200:
        response_200 = BimValidateIdsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimValidateIdsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_element: ValidateBimElementIdsBimElementTypeV2Path,
    *,
    client: AuthenticatedClient,
    body: BimValidateIdsRequest,
    bim_project_id: UUID,
) -> Response[BimValidateIdsResponse]:
    """Batch validate BIM element IDs

     Check which element IDs exist in the BIM index for a given project. Returns the subset of provided
    IDs that exist. The maximum number of IDs per request is configured server-side (default 500).

    Args:
        bim_element (ValidateBimElementIdsBimElementTypeV2Path): An enumeration representing
            different BIM (Building Information Modeling) element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element
            type.
        bim_project_id (UUID):
        body (BimValidateIdsRequest): Schema for batch element ID validation.
            Accepts a list of element IDs to check for existence in the BIM index.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimValidateIdsResponse]
    """

    kwargs = _get_kwargs(
        bim_element=bim_element,
        body=body,
        bim_project_id=bim_project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_element: ValidateBimElementIdsBimElementTypeV2Path,
    *,
    client: AuthenticatedClient,
    body: BimValidateIdsRequest,
    bim_project_id: UUID,
) -> BimValidateIdsResponse | None:
    """Batch validate BIM element IDs

     Check which element IDs exist in the BIM index for a given project. Returns the subset of provided
    IDs that exist. The maximum number of IDs per request is configured server-side (default 500).

    Args:
        bim_element (ValidateBimElementIdsBimElementTypeV2Path): An enumeration representing
            different BIM (Building Information Modeling) element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element
            type.
        bim_project_id (UUID):
        body (BimValidateIdsRequest): Schema for batch element ID validation.
            Accepts a list of element IDs to check for existence in the BIM index.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimValidateIdsResponse
    """

    return sync_detailed(
        bim_element=bim_element,
        client=client,
        body=body,
        bim_project_id=bim_project_id,
    ).parsed


async def asyncio_detailed(
    bim_element: ValidateBimElementIdsBimElementTypeV2Path,
    *,
    client: AuthenticatedClient,
    body: BimValidateIdsRequest,
    bim_project_id: UUID,
) -> Response[BimValidateIdsResponse]:
    """Batch validate BIM element IDs

     Check which element IDs exist in the BIM index for a given project. Returns the subset of provided
    IDs that exist. The maximum number of IDs per request is configured server-side (default 500).

    Args:
        bim_element (ValidateBimElementIdsBimElementTypeV2Path): An enumeration representing
            different BIM (Building Information Modeling) element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element
            type.
        bim_project_id (UUID):
        body (BimValidateIdsRequest): Schema for batch element ID validation.
            Accepts a list of element IDs to check for existence in the BIM index.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimValidateIdsResponse]
    """

    kwargs = _get_kwargs(
        bim_element=bim_element,
        body=body,
        bim_project_id=bim_project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_element: ValidateBimElementIdsBimElementTypeV2Path,
    *,
    client: AuthenticatedClient,
    body: BimValidateIdsRequest,
    bim_project_id: UUID,
) -> BimValidateIdsResponse | None:
    """Batch validate BIM element IDs

     Check which element IDs exist in the BIM index for a given project. Returns the subset of provided
    IDs that exist. The maximum number of IDs per request is configured server-side (default 500).

    Args:
        bim_element (ValidateBimElementIdsBimElementTypeV2Path): An enumeration representing
            different BIM (Building Information Modeling) element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element
            type.
        bim_project_id (UUID):
        body (BimValidateIdsRequest): Schema for batch element ID validation.
            Accepts a list of element IDs to check for existence in the BIM index.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimValidateIdsResponse
    """

    return (
        await asyncio_detailed(
            bim_element=bim_element,
            client=client,
            body=body,
            bim_project_id=bim_project_id,
        )
    ).parsed
