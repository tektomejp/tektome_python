from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execution_process_types import ExecutionProcessTypes
from ...models.list_dataspace_process_usages_ui_trigger_kind_choices import (
    ListDataspaceProcessUsagesUiTriggerKindChoices,
)
from ...models.paged_process_out import PagedProcessOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataspace_id: UUID,
    *,
    process_type: ExecutionProcessTypes | None | Unset = UNSET,
    ui_trigger_kinds: list[ListDataspaceProcessUsagesUiTriggerKindChoices] | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_process_type: None | str | Unset
    if isinstance(process_type, Unset):
        json_process_type = UNSET
    elif isinstance(process_type, ExecutionProcessTypes):
        json_process_type = process_type.value
    else:
        json_process_type = process_type
    params["process_type"] = json_process_type

    json_ui_trigger_kinds: list[str] | Unset = UNSET
    if not isinstance(ui_trigger_kinds, Unset):
        json_ui_trigger_kinds = []
        for ui_trigger_kinds_item_data in ui_trigger_kinds:
            ui_trigger_kinds_item = ui_trigger_kinds_item_data.value
            json_ui_trigger_kinds.append(ui_trigger_kinds_item)

    params["ui_trigger_kinds"] = json_ui_trigger_kinds

    params["page"] = page

    json_page_size: int | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["page_size"] = json_page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/dataspaces/{dataspace_id}/processes/top-usages/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedProcessOut | None:
    if response.status_code == 200:
        response_200 = PagedProcessOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedProcessOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    process_type: ExecutionProcessTypes | None | Unset = UNSET,
    ui_trigger_kinds: list[ListDataspaceProcessUsagesUiTriggerKindChoices] | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedProcessOut]:
    """List most used processes

     Retrieve the top N most frequently used processes by the authenticated user within a dataspace.
    Optionally filter by process type.

    Args:
        dataspace_id (UUID):
        process_type (ExecutionProcessTypes | None | Unset): Filter process usage by process type.
            Possible values are defined in ExecutionProcessTypes.
        ui_trigger_kinds (list[ListDataspaceProcessUsagesUiTriggerKindChoices] | Unset): Filter
            process usage by UI trigger kind. Possible values are defined in UiTriggerKindChoices.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedProcessOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        process_type=process_type,
        ui_trigger_kinds=ui_trigger_kinds,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    process_type: ExecutionProcessTypes | None | Unset = UNSET,
    ui_trigger_kinds: list[ListDataspaceProcessUsagesUiTriggerKindChoices] | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedProcessOut | None:
    """List most used processes

     Retrieve the top N most frequently used processes by the authenticated user within a dataspace.
    Optionally filter by process type.

    Args:
        dataspace_id (UUID):
        process_type (ExecutionProcessTypes | None | Unset): Filter process usage by process type.
            Possible values are defined in ExecutionProcessTypes.
        ui_trigger_kinds (list[ListDataspaceProcessUsagesUiTriggerKindChoices] | Unset): Filter
            process usage by UI trigger kind. Possible values are defined in UiTriggerKindChoices.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedProcessOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        client=client,
        process_type=process_type,
        ui_trigger_kinds=ui_trigger_kinds,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    process_type: ExecutionProcessTypes | None | Unset = UNSET,
    ui_trigger_kinds: list[ListDataspaceProcessUsagesUiTriggerKindChoices] | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedProcessOut]:
    """List most used processes

     Retrieve the top N most frequently used processes by the authenticated user within a dataspace.
    Optionally filter by process type.

    Args:
        dataspace_id (UUID):
        process_type (ExecutionProcessTypes | None | Unset): Filter process usage by process type.
            Possible values are defined in ExecutionProcessTypes.
        ui_trigger_kinds (list[ListDataspaceProcessUsagesUiTriggerKindChoices] | Unset): Filter
            process usage by UI trigger kind. Possible values are defined in UiTriggerKindChoices.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedProcessOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        process_type=process_type,
        ui_trigger_kinds=ui_trigger_kinds,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    process_type: ExecutionProcessTypes | None | Unset = UNSET,
    ui_trigger_kinds: list[ListDataspaceProcessUsagesUiTriggerKindChoices] | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedProcessOut | None:
    """List most used processes

     Retrieve the top N most frequently used processes by the authenticated user within a dataspace.
    Optionally filter by process type.

    Args:
        dataspace_id (UUID):
        process_type (ExecutionProcessTypes | None | Unset): Filter process usage by process type.
            Possible values are defined in ExecutionProcessTypes.
        ui_trigger_kinds (list[ListDataspaceProcessUsagesUiTriggerKindChoices] | Unset): Filter
            process usage by UI trigger kind. Possible values are defined in UiTriggerKindChoices.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedProcessOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            client=client,
            process_type=process_type,
            ui_trigger_kinds=ui_trigger_kinds,
            page=page,
            page_size=page_size,
        )
    ).parsed
