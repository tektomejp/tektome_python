from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.artifact_copy_in import ArtifactCopyIn
from ...models.artifact_copy_out import ArtifactCopyOut
from ...models.generic_http_error import GenericHttpError
from ...models.ttos_folder_copy_out import TtosFolderCopyOut
from ...types import Response


def _get_kwargs(
    artifact_id: UUID,
    *,
    body: ArtifactCopyIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/agents/os/artifacts/{artifact_id}/copy/".format(
            artifact_id=quote(str(artifact_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ArtifactCopyOut | TtosFolderCopyOut | GenericHttpError | None:
    if response.status_code == 201:

        def _parse_response_201(data: object) -> ArtifactCopyOut | TtosFolderCopyOut:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0 = ArtifactCopyOut.from_dict(data)

                return response_201_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_201_type_1 = TtosFolderCopyOut.from_dict(data)

            return response_201_type_1

        response_201 = _parse_response_201(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = GenericHttpError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GenericHttpError.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GenericHttpError.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GenericHttpError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GenericHttpError.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GenericHttpError.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GenericHttpError.from_dict(response.json())

        return response_406

    if response.status_code == 407:
        response_407 = GenericHttpError.from_dict(response.json())

        return response_407

    if response.status_code == 408:
        response_408 = GenericHttpError.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = GenericHttpError.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = GenericHttpError.from_dict(response.json())

        return response_410

    if response.status_code == 411:
        response_411 = GenericHttpError.from_dict(response.json())

        return response_411

    if response.status_code == 412:
        response_412 = GenericHttpError.from_dict(response.json())

        return response_412

    if response.status_code == 416:
        response_416 = GenericHttpError.from_dict(response.json())

        return response_416

    if response.status_code == 418:
        response_418 = GenericHttpError.from_dict(response.json())

        return response_418

    if response.status_code == 425:
        response_425 = GenericHttpError.from_dict(response.json())

        return response_425

    if response.status_code == 429:
        response_429 = GenericHttpError.from_dict(response.json())

        return response_429

    if response.status_code == 451:
        response_451 = GenericHttpError.from_dict(response.json())

        return response_451

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ArtifactCopyOut | TtosFolderCopyOut | GenericHttpError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    artifact_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ArtifactCopyIn,
) -> Response[ArtifactCopyOut | TtosFolderCopyOut | GenericHttpError]:
    """Copy an artifact or folder

     MTeWkhGV
    Copy an artifact to a new path. For .keep artifacts (folders),
    copies all artifacts under the folder prefix.

    Args:
        artifact_id (UUID):
        body (ArtifactCopyIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArtifactCopyOut | TtosFolderCopyOut | GenericHttpError]
    """

    kwargs = _get_kwargs(
        artifact_id=artifact_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    artifact_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ArtifactCopyIn,
) -> ArtifactCopyOut | TtosFolderCopyOut | GenericHttpError | None:
    """Copy an artifact or folder

     MTeWkhGV
    Copy an artifact to a new path. For .keep artifacts (folders),
    copies all artifacts under the folder prefix.

    Args:
        artifact_id (UUID):
        body (ArtifactCopyIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArtifactCopyOut | TtosFolderCopyOut | GenericHttpError
    """

    return sync_detailed(
        artifact_id=artifact_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    artifact_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ArtifactCopyIn,
) -> Response[ArtifactCopyOut | TtosFolderCopyOut | GenericHttpError]:
    """Copy an artifact or folder

     MTeWkhGV
    Copy an artifact to a new path. For .keep artifacts (folders),
    copies all artifacts under the folder prefix.

    Args:
        artifact_id (UUID):
        body (ArtifactCopyIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArtifactCopyOut | TtosFolderCopyOut | GenericHttpError]
    """

    kwargs = _get_kwargs(
        artifact_id=artifact_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    artifact_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ArtifactCopyIn,
) -> ArtifactCopyOut | TtosFolderCopyOut | GenericHttpError | None:
    """Copy an artifact or folder

     MTeWkhGV
    Copy an artifact to a new path. For .keep artifacts (folders),
    copies all artifacts under the folder prefix.

    Args:
        artifact_id (UUID):
        body (ArtifactCopyIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArtifactCopyOut | TtosFolderCopyOut | GenericHttpError
    """

    return (
        await asyncio_detailed(
            artifact_id=artifact_id,
            client=client,
            body=body,
        )
    ).parsed
