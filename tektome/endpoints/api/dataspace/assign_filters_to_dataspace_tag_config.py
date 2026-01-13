from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataspace_search_tag_config_out import DataspaceSearchTagConfigOut
from ...models.dataspace_search_tag_config_patch_filter_in import DataspaceSearchTagConfigPatchFilterIn
from ...models.error_out import ErrorOut
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    tag_config_id: UUID,
    *,
    body: DataspaceSearchTagConfigPatchFilterIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/dataspaces/{dataspace_id}/tag-configs/{tag_config_id}/filters/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            tag_config_id=quote(str(tag_config_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DataspaceSearchTagConfigOut | ErrorOut | None:
    if response.status_code == 200:
        response_200 = DataspaceSearchTagConfigOut.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorOut.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorOut.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorOut.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorOut.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorOut.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = ErrorOut.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = ErrorOut.from_dict(response.json())

        return response_406

    if response.status_code == 407:
        response_407 = ErrorOut.from_dict(response.json())

        return response_407

    if response.status_code == 408:
        response_408 = ErrorOut.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = ErrorOut.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorOut.from_dict(response.json())

        return response_410

    if response.status_code == 411:
        response_411 = ErrorOut.from_dict(response.json())

        return response_411

    if response.status_code == 412:
        response_412 = ErrorOut.from_dict(response.json())

        return response_412

    if response.status_code == 416:
        response_416 = ErrorOut.from_dict(response.json())

        return response_416

    if response.status_code == 418:
        response_418 = ErrorOut.from_dict(response.json())

        return response_418

    if response.status_code == 425:
        response_425 = ErrorOut.from_dict(response.json())

        return response_425

    if response.status_code == 429:
        response_429 = ErrorOut.from_dict(response.json())

        return response_429

    if response.status_code == 451:
        response_451 = ErrorOut.from_dict(response.json())

        return response_451

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DataspaceSearchTagConfigOut | ErrorOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    tag_config_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchTagConfigPatchFilterIn,
) -> Response[DataspaceSearchTagConfigOut | ErrorOut]:
    """Patch Filters To Dataspace Tag Config

     W31YpdoE

    Assign filters to a tag configuration for the current dataspace.

    Args:
        dataspace_id (UUID):
        tag_config_id (UUID):
        body (DataspaceSearchTagConfigPatchFilterIn): Schema for patching a dataspace tag
            configuration filters with default search conditions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceSearchTagConfigOut | ErrorOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        tag_config_id=tag_config_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    tag_config_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchTagConfigPatchFilterIn,
) -> DataspaceSearchTagConfigOut | ErrorOut | None:
    """Patch Filters To Dataspace Tag Config

     W31YpdoE

    Assign filters to a tag configuration for the current dataspace.

    Args:
        dataspace_id (UUID):
        tag_config_id (UUID):
        body (DataspaceSearchTagConfigPatchFilterIn): Schema for patching a dataspace tag
            configuration filters with default search conditions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceSearchTagConfigOut | ErrorOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        tag_config_id=tag_config_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    tag_config_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchTagConfigPatchFilterIn,
) -> Response[DataspaceSearchTagConfigOut | ErrorOut]:
    """Patch Filters To Dataspace Tag Config

     W31YpdoE

    Assign filters to a tag configuration for the current dataspace.

    Args:
        dataspace_id (UUID):
        tag_config_id (UUID):
        body (DataspaceSearchTagConfigPatchFilterIn): Schema for patching a dataspace tag
            configuration filters with default search conditions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataspaceSearchTagConfigOut | ErrorOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        tag_config_id=tag_config_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    tag_config_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DataspaceSearchTagConfigPatchFilterIn,
) -> DataspaceSearchTagConfigOut | ErrorOut | None:
    """Patch Filters To Dataspace Tag Config

     W31YpdoE

    Assign filters to a tag configuration for the current dataspace.

    Args:
        dataspace_id (UUID):
        tag_config_id (UUID):
        body (DataspaceSearchTagConfigPatchFilterIn): Schema for patching a dataspace tag
            configuration filters with default search conditions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataspaceSearchTagConfigOut | ErrorOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            tag_config_id=tag_config_id,
            client=client,
            body=body,
        )
    ).parsed
