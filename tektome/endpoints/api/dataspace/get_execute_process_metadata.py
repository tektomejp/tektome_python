from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execute_process_metadata_get_out import ExecuteProcessMetadataGetOut
from ...models.get_execute_process_metadata_execute_metadata_kind import GetExecuteProcessMetadataExecuteMetadataKind
from ...types import UNSET, Response


def _get_kwargs(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    kind: GetExecuteProcessMetadataExecuteMetadataKind,
    model_entity_ids: list[UUID],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_kind = kind.value
    params["kind"] = json_kind

    json_model_entity_ids = []
    for model_entity_ids_item_data in model_entity_ids:
        model_entity_ids_item = str(model_entity_ids_item_data)
        json_model_entity_ids.append(model_entity_ids_item)

    params["model_entity_ids"] = json_model_entity_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/dataspaces/{dataspace_id}/processes/{process_id}/metadata/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            process_id=quote(str(process_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExecuteProcessMetadataGetOut | None:
    if response.status_code == 200:
        response_200 = ExecuteProcessMetadataGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExecuteProcessMetadataGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    kind: GetExecuteProcessMetadataExecuteMetadataKind,
    model_entity_ids: list[UUID],
) -> Response[ExecuteProcessMetadataGetOut]:
    """Get execution metadata for a configured process

     882BoCbx

    Get execution metadata for a configured process and given model entities.

    Args:
        request: The HTTP request object.
        path_params: ProcessPath
        query_params: ExecuteProcessMetadataQueryIn

    Returns: ExecuteProcessMetadataGetOut

    Args:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.
        kind (GetExecuteProcessMetadataExecuteMetadataKind):
        model_entity_ids (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteProcessMetadataGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        process_id=process_id,
        kind=kind,
        model_entity_ids=model_entity_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    kind: GetExecuteProcessMetadataExecuteMetadataKind,
    model_entity_ids: list[UUID],
) -> ExecuteProcessMetadataGetOut | None:
    """Get execution metadata for a configured process

     882BoCbx

    Get execution metadata for a configured process and given model entities.

    Args:
        request: The HTTP request object.
        path_params: ProcessPath
        query_params: ExecuteProcessMetadataQueryIn

    Returns: ExecuteProcessMetadataGetOut

    Args:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.
        kind (GetExecuteProcessMetadataExecuteMetadataKind):
        model_entity_ids (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteProcessMetadataGetOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        process_id=process_id,
        client=client,
        kind=kind,
        model_entity_ids=model_entity_ids,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    kind: GetExecuteProcessMetadataExecuteMetadataKind,
    model_entity_ids: list[UUID],
) -> Response[ExecuteProcessMetadataGetOut]:
    """Get execution metadata for a configured process

     882BoCbx

    Get execution metadata for a configured process and given model entities.

    Args:
        request: The HTTP request object.
        path_params: ProcessPath
        query_params: ExecuteProcessMetadataQueryIn

    Returns: ExecuteProcessMetadataGetOut

    Args:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.
        kind (GetExecuteProcessMetadataExecuteMetadataKind):
        model_entity_ids (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteProcessMetadataGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        process_id=process_id,
        kind=kind,
        model_entity_ids=model_entity_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    process_id: UUID,
    *,
    client: AuthenticatedClient,
    kind: GetExecuteProcessMetadataExecuteMetadataKind,
    model_entity_ids: list[UUID],
) -> ExecuteProcessMetadataGetOut | None:
    """Get execution metadata for a configured process

     882BoCbx

    Get execution metadata for a configured process and given model entities.

    Args:
        request: The HTTP request object.
        path_params: ProcessPath
        query_params: ExecuteProcessMetadataQueryIn

    Returns: ExecuteProcessMetadataGetOut

    Args:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.
        kind (GetExecuteProcessMetadataExecuteMetadataKind):
        model_entity_ids (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteProcessMetadataGetOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            process_id=process_id,
            client=client,
            kind=kind,
            model_entity_ids=model_entity_ids,
        )
    ).parsed
