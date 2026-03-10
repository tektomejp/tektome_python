from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_out import ErrorOut
from ...models.resource_ifc_bim_project_creation_post_out import ResourceIfcBimProjectCreationPostOut
from ...models.upload_dataspace_project_bim_file_params import UploadDataspaceProjectBimFileParams
from ...types import Response


def _get_kwargs(
    project_id: UUID,
    *,
    body: UploadDataspaceProjectBimFileParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/dataspaces/projects/{project_id}/upload/bim/".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorOut | ResourceIfcBimProjectCreationPostOut | None:
    if response.status_code == 201:
        response_201 = ResourceIfcBimProjectCreationPostOut.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorOut.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorOut | ResourceIfcBimProjectCreationPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UploadDataspaceProjectBimFileParams,
) -> Response[ErrorOut | ResourceIfcBimProjectCreationPostOut]:
    """Post Upload Dataspace Project Resource Bim

     AuBjLcqo

    Upload and process an IFC (Building Information Model) file for BIM analysis.

    This endpoint handles the upload of IFC files and initiates an asynchronous processing
    pipeline to extract and classify BIM elements. The workflow creates a Resource entity
    for the uploaded file and a BimProject entity to manage the BIM processing state.

    Args:
        request: The HTTP request object containing authentication information.
        path_params: Path parameters containing the project_id.
        file: The uploaded IFC file (UploadedFile).

    Returns:
        Tuple[int, dict]: HTTP 201 with response containing:
            - task_id (UUID): Celery task ID for async BIM processing
            - resource_id (UUID): ID of created Resource entity
            - bim_project_id (UUID): ID of created BimProject entity
            - file_name (str): Original filename (cleaned of path separators)
            - created (datetime): Resource creation timestamp
            - updated (datetime): Resource update timestamp

    Raises:
        HttpError(400): If file is not .ifc format or BIM project creation fails.

    Processing Flow:
        1. Validates file extension (case-insensitive .ifc check)
        2. Creates Resource entity with version control
        3. Creates BimProject associated with Resource
        4. Triggers async Celery task: process_resource_ifc_to_bim_elements
        5. Returns task ID for client to poll progress
        6. On error: Cleans up Resource and returns error response

    Args:
        project_id (UUID):
        body (UploadDataspaceProjectBimFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOut | ResourceIfcBimProjectCreationPostOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UploadDataspaceProjectBimFileParams,
) -> ErrorOut | ResourceIfcBimProjectCreationPostOut | None:
    """Post Upload Dataspace Project Resource Bim

     AuBjLcqo

    Upload and process an IFC (Building Information Model) file for BIM analysis.

    This endpoint handles the upload of IFC files and initiates an asynchronous processing
    pipeline to extract and classify BIM elements. The workflow creates a Resource entity
    for the uploaded file and a BimProject entity to manage the BIM processing state.

    Args:
        request: The HTTP request object containing authentication information.
        path_params: Path parameters containing the project_id.
        file: The uploaded IFC file (UploadedFile).

    Returns:
        Tuple[int, dict]: HTTP 201 with response containing:
            - task_id (UUID): Celery task ID for async BIM processing
            - resource_id (UUID): ID of created Resource entity
            - bim_project_id (UUID): ID of created BimProject entity
            - file_name (str): Original filename (cleaned of path separators)
            - created (datetime): Resource creation timestamp
            - updated (datetime): Resource update timestamp

    Raises:
        HttpError(400): If file is not .ifc format or BIM project creation fails.

    Processing Flow:
        1. Validates file extension (case-insensitive .ifc check)
        2. Creates Resource entity with version control
        3. Creates BimProject associated with Resource
        4. Triggers async Celery task: process_resource_ifc_to_bim_elements
        5. Returns task ID for client to poll progress
        6. On error: Cleans up Resource and returns error response

    Args:
        project_id (UUID):
        body (UploadDataspaceProjectBimFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOut | ResourceIfcBimProjectCreationPostOut
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UploadDataspaceProjectBimFileParams,
) -> Response[ErrorOut | ResourceIfcBimProjectCreationPostOut]:
    """Post Upload Dataspace Project Resource Bim

     AuBjLcqo

    Upload and process an IFC (Building Information Model) file for BIM analysis.

    This endpoint handles the upload of IFC files and initiates an asynchronous processing
    pipeline to extract and classify BIM elements. The workflow creates a Resource entity
    for the uploaded file and a BimProject entity to manage the BIM processing state.

    Args:
        request: The HTTP request object containing authentication information.
        path_params: Path parameters containing the project_id.
        file: The uploaded IFC file (UploadedFile).

    Returns:
        Tuple[int, dict]: HTTP 201 with response containing:
            - task_id (UUID): Celery task ID for async BIM processing
            - resource_id (UUID): ID of created Resource entity
            - bim_project_id (UUID): ID of created BimProject entity
            - file_name (str): Original filename (cleaned of path separators)
            - created (datetime): Resource creation timestamp
            - updated (datetime): Resource update timestamp

    Raises:
        HttpError(400): If file is not .ifc format or BIM project creation fails.

    Processing Flow:
        1. Validates file extension (case-insensitive .ifc check)
        2. Creates Resource entity with version control
        3. Creates BimProject associated with Resource
        4. Triggers async Celery task: process_resource_ifc_to_bim_elements
        5. Returns task ID for client to poll progress
        6. On error: Cleans up Resource and returns error response

    Args:
        project_id (UUID):
        body (UploadDataspaceProjectBimFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOut | ResourceIfcBimProjectCreationPostOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UploadDataspaceProjectBimFileParams,
) -> ErrorOut | ResourceIfcBimProjectCreationPostOut | None:
    """Post Upload Dataspace Project Resource Bim

     AuBjLcqo

    Upload and process an IFC (Building Information Model) file for BIM analysis.

    This endpoint handles the upload of IFC files and initiates an asynchronous processing
    pipeline to extract and classify BIM elements. The workflow creates a Resource entity
    for the uploaded file and a BimProject entity to manage the BIM processing state.

    Args:
        request: The HTTP request object containing authentication information.
        path_params: Path parameters containing the project_id.
        file: The uploaded IFC file (UploadedFile).

    Returns:
        Tuple[int, dict]: HTTP 201 with response containing:
            - task_id (UUID): Celery task ID for async BIM processing
            - resource_id (UUID): ID of created Resource entity
            - bim_project_id (UUID): ID of created BimProject entity
            - file_name (str): Original filename (cleaned of path separators)
            - created (datetime): Resource creation timestamp
            - updated (datetime): Resource update timestamp

    Raises:
        HttpError(400): If file is not .ifc format or BIM project creation fails.

    Processing Flow:
        1. Validates file extension (case-insensitive .ifc check)
        2. Creates Resource entity with version control
        3. Creates BimProject associated with Resource
        4. Triggers async Celery task: process_resource_ifc_to_bim_elements
        5. Returns task ID for client to poll progress
        6. On error: Cleans up Resource and returns error response

    Args:
        project_id (UUID):
        body (UploadDataspaceProjectBimFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOut | ResourceIfcBimProjectCreationPostOut
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
