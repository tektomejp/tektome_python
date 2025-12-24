from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.run_artifact_post_in import RunArtifactPostIn
from ...models.run_artifact_post_out import RunArtifactPostOut
from ...types import Response


def _get_kwargs(
    artifact_id: UUID,
    *,
    body: RunArtifactPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/agents/os/artifacts/{artifact_id}/run/".format(
            artifact_id=quote(str(artifact_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RunArtifactPostOut | None:
    if response.status_code == 201:
        response_201 = RunArtifactPostOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RunArtifactPostOut]:
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
    body: RunArtifactPostIn,
) -> Response[RunArtifactPostOut]:
    """Post Run Artifact

     h0Yl75SU
    Run an artifact by its ID.
    Only .openflow artifacts are supported. .py artifacts are not supported yet.
    The result is saved as another artifact. If `result_artifact_id` is provided, the result will be
    saved to that artifact. Otherwise, a new artifact will be created.
    - If `result_artifact_id` is provided, it must belong to the same chatroom as the artifact being
    run.
    - If `result_artifact_id` is provided, result_artifact_name and result_artifact_extension must not
    be provided.
    - If `result_artifact_id` is not provided, a new artifact will be created with the provided
    `result_artifact_name` and `result_artifact_extension`.
    - If `result_artifact_id` is provided, its status must be one of `completed` or `failed`.

    Args:
        artifact_id (UUID):
        body (RunArtifactPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RunArtifactPostOut]
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
    body: RunArtifactPostIn,
) -> RunArtifactPostOut | None:
    """Post Run Artifact

     h0Yl75SU
    Run an artifact by its ID.
    Only .openflow artifacts are supported. .py artifacts are not supported yet.
    The result is saved as another artifact. If `result_artifact_id` is provided, the result will be
    saved to that artifact. Otherwise, a new artifact will be created.
    - If `result_artifact_id` is provided, it must belong to the same chatroom as the artifact being
    run.
    - If `result_artifact_id` is provided, result_artifact_name and result_artifact_extension must not
    be provided.
    - If `result_artifact_id` is not provided, a new artifact will be created with the provided
    `result_artifact_name` and `result_artifact_extension`.
    - If `result_artifact_id` is provided, its status must be one of `completed` or `failed`.

    Args:
        artifact_id (UUID):
        body (RunArtifactPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RunArtifactPostOut
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
    body: RunArtifactPostIn,
) -> Response[RunArtifactPostOut]:
    """Post Run Artifact

     h0Yl75SU
    Run an artifact by its ID.
    Only .openflow artifacts are supported. .py artifacts are not supported yet.
    The result is saved as another artifact. If `result_artifact_id` is provided, the result will be
    saved to that artifact. Otherwise, a new artifact will be created.
    - If `result_artifact_id` is provided, it must belong to the same chatroom as the artifact being
    run.
    - If `result_artifact_id` is provided, result_artifact_name and result_artifact_extension must not
    be provided.
    - If `result_artifact_id` is not provided, a new artifact will be created with the provided
    `result_artifact_name` and `result_artifact_extension`.
    - If `result_artifact_id` is provided, its status must be one of `completed` or `failed`.

    Args:
        artifact_id (UUID):
        body (RunArtifactPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RunArtifactPostOut]
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
    body: RunArtifactPostIn,
) -> RunArtifactPostOut | None:
    """Post Run Artifact

     h0Yl75SU
    Run an artifact by its ID.
    Only .openflow artifacts are supported. .py artifacts are not supported yet.
    The result is saved as another artifact. If `result_artifact_id` is provided, the result will be
    saved to that artifact. Otherwise, a new artifact will be created.
    - If `result_artifact_id` is provided, it must belong to the same chatroom as the artifact being
    run.
    - If `result_artifact_id` is provided, result_artifact_name and result_artifact_extension must not
    be provided.
    - If `result_artifact_id` is not provided, a new artifact will be created with the provided
    `result_artifact_name` and `result_artifact_extension`.
    - If `result_artifact_id` is provided, its status must be one of `completed` or `failed`.

    Args:
        artifact_id (UUID):
        body (RunArtifactPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RunArtifactPostOut
    """

    return (
        await asyncio_detailed(
            artifact_id=artifact_id,
            client=client,
            body=body,
        )
    ).parsed
