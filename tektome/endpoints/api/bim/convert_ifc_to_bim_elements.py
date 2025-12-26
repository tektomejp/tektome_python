from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_object_post_out import BimObjectPostOut
from ...models.convert_ifc_to_bim_elements_file_params import ConvertIfcToBimElementsFileParams
from ...models.error_response_post_out import ErrorResponsePostOut
from ...types import Response


def _get_kwargs(
    bim_project_id: UUID,
    *,
    body: ConvertIfcToBimElementsFileParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-ifc/convert-ifc/{bim_project_id}/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimObjectPostOut | ErrorResponsePostOut | None:
    if response.status_code == 200:
        response_200 = BimObjectPostOut.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponsePostOut.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimObjectPostOut | ErrorResponsePostOut]:
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
    body: ConvertIfcToBimElementsFileParams,
) -> Response[BimObjectPostOut | ErrorResponsePostOut]:
    r"""Convert Ifc To Bim Elements

     Accepts an IFC file and passes it to a Celery worker for conversion
    into BIM elements.

    Args:
        request: The HTTP request object.
        path_params: Path parameters containing the validated BIM project ID.
        file: The uploaded IFC file to be processed.

    Returns:
        dict: Response dictionary containing:
            - Success: {\"process_id\": str} - Celery task ID for tracking the background process
            - Error: 404 response if BIM project not found (handled by BimProjectPath validator)

    Args:
        bim_project_id (UUID):
        body (ConvertIfcToBimElementsFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimObjectPostOut | ErrorResponsePostOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ConvertIfcToBimElementsFileParams,
) -> BimObjectPostOut | ErrorResponsePostOut | None:
    r"""Convert Ifc To Bim Elements

     Accepts an IFC file and passes it to a Celery worker for conversion
    into BIM elements.

    Args:
        request: The HTTP request object.
        path_params: Path parameters containing the validated BIM project ID.
        file: The uploaded IFC file to be processed.

    Returns:
        dict: Response dictionary containing:
            - Success: {\"process_id\": str} - Celery task ID for tracking the background process
            - Error: 404 response if BIM project not found (handled by BimProjectPath validator)

    Args:
        bim_project_id (UUID):
        body (ConvertIfcToBimElementsFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimObjectPostOut | ErrorResponsePostOut
    """

    return sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ConvertIfcToBimElementsFileParams,
) -> Response[BimObjectPostOut | ErrorResponsePostOut]:
    r"""Convert Ifc To Bim Elements

     Accepts an IFC file and passes it to a Celery worker for conversion
    into BIM elements.

    Args:
        request: The HTTP request object.
        path_params: Path parameters containing the validated BIM project ID.
        file: The uploaded IFC file to be processed.

    Returns:
        dict: Response dictionary containing:
            - Success: {\"process_id\": str} - Celery task ID for tracking the background process
            - Error: 404 response if BIM project not found (handled by BimProjectPath validator)

    Args:
        bim_project_id (UUID):
        body (ConvertIfcToBimElementsFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimObjectPostOut | ErrorResponsePostOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ConvertIfcToBimElementsFileParams,
) -> BimObjectPostOut | ErrorResponsePostOut | None:
    r"""Convert Ifc To Bim Elements

     Accepts an IFC file and passes it to a Celery worker for conversion
    into BIM elements.

    Args:
        request: The HTTP request object.
        path_params: Path parameters containing the validated BIM project ID.
        file: The uploaded IFC file to be processed.

    Returns:
        dict: Response dictionary containing:
            - Success: {\"process_id\": str} - Celery task ID for tracking the background process
            - Error: 404 response if BIM project not found (handled by BimProjectPath validator)

    Args:
        bim_project_id (UUID):
        body (ConvertIfcToBimElementsFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimObjectPostOut | ErrorResponsePostOut
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            client=client,
            body=body,
        )
    ).parsed
