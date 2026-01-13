from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execute_process_post_in import ExecuteProcessPostIn
from ...models.execute_process_post_out import ExecuteProcessPostOut
from ...types import Response


def _get_kwargs(
    process_id: UUID,
    *,
    body: ExecuteProcessPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/agents/os/processes/{process_id}/execute/".format(
            process_id=quote(str(process_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExecuteProcessPostOut | None:
    if response.status_code == 200:
        response_200 = ExecuteProcessPostOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExecuteProcessPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ExecuteProcessPostIn,
) -> Response[ExecuteProcessPostOut]:
    """Execute a process windmill flow

     AqZqtBsA

    2 Entrypoints
    1. [Process Page] Multiple Process in a single execution group run over one resource/project m2m -
    no design and not yet supported
    2. [Resource/Project list] Single Process in a single execution group runs over multiple
    resources/projects

    Default fallback
    3. Run the process without any UI trigger values

    Depending on the kind of process being executed, this endpoint will handle the execution
    accordingly:
    - For 'resource' or 'project' kinds: 1 execution group <-> N executions (fn takes in 1
    resource/project)
        - Iterates over each provided model ID (from `ui_trigger_values.ids` or `ui_trigger_values.id`).
        - For each ID, it creates a unique job ID and prepares a payload for execution.
        - Publishes the execution payload to the message broker for processing.
    - For 'resource[]' or 'project[]' kinds: 1 execution group <-> 1 execution (fn that takes in N
    resources/projects)
        - Creates a single job ID for the entire batch of IDs.
        - Prepares a payload that includes all provided model IDs.
        - Publishes the batch execution payload to the message broker.

    Rate limits the number of concurrent in-progress jobs across the organization

    Args:
        process_id (UUID):
        body (ExecuteProcessPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteProcessPostOut]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ExecuteProcessPostIn,
) -> ExecuteProcessPostOut | None:
    """Execute a process windmill flow

     AqZqtBsA

    2 Entrypoints
    1. [Process Page] Multiple Process in a single execution group run over one resource/project m2m -
    no design and not yet supported
    2. [Resource/Project list] Single Process in a single execution group runs over multiple
    resources/projects

    Default fallback
    3. Run the process without any UI trigger values

    Depending on the kind of process being executed, this endpoint will handle the execution
    accordingly:
    - For 'resource' or 'project' kinds: 1 execution group <-> N executions (fn takes in 1
    resource/project)
        - Iterates over each provided model ID (from `ui_trigger_values.ids` or `ui_trigger_values.id`).
        - For each ID, it creates a unique job ID and prepares a payload for execution.
        - Publishes the execution payload to the message broker for processing.
    - For 'resource[]' or 'project[]' kinds: 1 execution group <-> 1 execution (fn that takes in N
    resources/projects)
        - Creates a single job ID for the entire batch of IDs.
        - Prepares a payload that includes all provided model IDs.
        - Publishes the batch execution payload to the message broker.

    Rate limits the number of concurrent in-progress jobs across the organization

    Args:
        process_id (UUID):
        body (ExecuteProcessPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteProcessPostOut
    """

    return sync_detailed(
        process_id=process_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ExecuteProcessPostIn,
) -> Response[ExecuteProcessPostOut]:
    """Execute a process windmill flow

     AqZqtBsA

    2 Entrypoints
    1. [Process Page] Multiple Process in a single execution group run over one resource/project m2m -
    no design and not yet supported
    2. [Resource/Project list] Single Process in a single execution group runs over multiple
    resources/projects

    Default fallback
    3. Run the process without any UI trigger values

    Depending on the kind of process being executed, this endpoint will handle the execution
    accordingly:
    - For 'resource' or 'project' kinds: 1 execution group <-> N executions (fn takes in 1
    resource/project)
        - Iterates over each provided model ID (from `ui_trigger_values.ids` or `ui_trigger_values.id`).
        - For each ID, it creates a unique job ID and prepares a payload for execution.
        - Publishes the execution payload to the message broker for processing.
    - For 'resource[]' or 'project[]' kinds: 1 execution group <-> 1 execution (fn that takes in N
    resources/projects)
        - Creates a single job ID for the entire batch of IDs.
        - Prepares a payload that includes all provided model IDs.
        - Publishes the batch execution payload to the message broker.

    Rate limits the number of concurrent in-progress jobs across the organization

    Args:
        process_id (UUID):
        body (ExecuteProcessPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteProcessPostOut]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ExecuteProcessPostIn,
) -> ExecuteProcessPostOut | None:
    """Execute a process windmill flow

     AqZqtBsA

    2 Entrypoints
    1. [Process Page] Multiple Process in a single execution group run over one resource/project m2m -
    no design and not yet supported
    2. [Resource/Project list] Single Process in a single execution group runs over multiple
    resources/projects

    Default fallback
    3. Run the process without any UI trigger values

    Depending on the kind of process being executed, this endpoint will handle the execution
    accordingly:
    - For 'resource' or 'project' kinds: 1 execution group <-> N executions (fn takes in 1
    resource/project)
        - Iterates over each provided model ID (from `ui_trigger_values.ids` or `ui_trigger_values.id`).
        - For each ID, it creates a unique job ID and prepares a payload for execution.
        - Publishes the execution payload to the message broker for processing.
    - For 'resource[]' or 'project[]' kinds: 1 execution group <-> 1 execution (fn that takes in N
    resources/projects)
        - Creates a single job ID for the entire batch of IDs.
        - Prepares a payload that includes all provided model IDs.
        - Publishes the batch execution payload to the message broker.

    Rate limits the number of concurrent in-progress jobs across the organization

    Args:
        process_id (UUID):
        body (ExecuteProcessPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteProcessPostOut
    """

    return (
        await asyncio_detailed(
            process_id=process_id,
            client=client,
            body=body,
        )
    ).parsed
