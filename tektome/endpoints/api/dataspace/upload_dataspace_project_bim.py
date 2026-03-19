from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.resource_ifc_bim_project_creation_response import ResourceIfcBimProjectCreationResponse
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
) -> ErrorResponse | ResourceIfcBimProjectCreationResponse | None:
    if response.status_code == 201:
        response_201 = ResourceIfcBimProjectCreationResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ResourceIfcBimProjectCreationResponse]:
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
) -> Response[ErrorResponse | ResourceIfcBimProjectCreationResponse]:
    """Upload an IFC file for BIM processing

     Upload an IFC (Building Information Model) file to a project and initiate BIM element extraction and
    classification. Only .ifc files are accepted. This is an asynchronous operation. To retrieve the
    results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the task/process ID
    returned in this response.

    Args:
        project_id (UUID):
        body (UploadDataspaceProjectBimFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ResourceIfcBimProjectCreationResponse]
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
) -> ErrorResponse | ResourceIfcBimProjectCreationResponse | None:
    """Upload an IFC file for BIM processing

     Upload an IFC (Building Information Model) file to a project and initiate BIM element extraction and
    classification. Only .ifc files are accepted. This is an asynchronous operation. To retrieve the
    results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the task/process ID
    returned in this response.

    Args:
        project_id (UUID):
        body (UploadDataspaceProjectBimFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ResourceIfcBimProjectCreationResponse
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
) -> Response[ErrorResponse | ResourceIfcBimProjectCreationResponse]:
    """Upload an IFC file for BIM processing

     Upload an IFC (Building Information Model) file to a project and initiate BIM element extraction and
    classification. Only .ifc files are accepted. This is an asynchronous operation. To retrieve the
    results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the task/process ID
    returned in this response.

    Args:
        project_id (UUID):
        body (UploadDataspaceProjectBimFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ResourceIfcBimProjectCreationResponse]
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
) -> ErrorResponse | ResourceIfcBimProjectCreationResponse | None:
    """Upload an IFC file for BIM processing

     Upload an IFC (Building Information Model) file to a project and initiate BIM element extraction and
    classification. Only .ifc files are accepted. This is an asynchronous operation. To retrieve the
    results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the task/process ID
    returned in this response.

    Args:
        project_id (UUID):
        body (UploadDataspaceProjectBimFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ResourceIfcBimProjectCreationResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
