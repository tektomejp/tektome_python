import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_dataspace_execution_groups_execution_group_status import (
    GetDataspaceExecutionGroupsExecutionGroupStatus,
)
from ...models.get_dataspace_execution_groups_execution_review_status import (
    GetDataspaceExecutionGroupsExecutionReviewStatus,
)
from ...models.get_dataspace_execution_groups_process_type_choices import GetDataspaceExecutionGroupsProcessTypeChoices
from ...models.paged_execution_group_get_out import PagedExecutionGroupGetOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataspace_id: str,
    *,
    process_types: list[GetDataspaceExecutionGroupsProcessTypeChoices] | Unset = UNSET,
    process_ids: list[UUID] | Unset = UNSET,
    status: list[GetDataspaceExecutionGroupsExecutionGroupStatus] | Unset = UNSET,
    review_status: list[GetDataspaceExecutionGroupsExecutionReviewStatus] | Unset = UNSET,
    launched_by_ids: list[UUID] | Unset = UNSET,
    start_datetime: datetime.datetime | None | Unset = UNSET,
    end_datetime: datetime.datetime | None | Unset = UNSET,
    memo: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_process_types: list[str] | Unset = UNSET
    if not isinstance(process_types, Unset):
        json_process_types = []
        for process_types_item_data in process_types:
            process_types_item = process_types_item_data.value
            json_process_types.append(process_types_item)

    params["process_types"] = json_process_types

    json_process_ids: list[str] | Unset = UNSET
    if not isinstance(process_ids, Unset):
        json_process_ids = []
        for process_ids_item_data in process_ids:
            process_ids_item = str(process_ids_item_data)
            json_process_ids.append(process_ids_item)

    params["process_ids"] = json_process_ids

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    json_review_status: list[str] | Unset = UNSET
    if not isinstance(review_status, Unset):
        json_review_status = []
        for review_status_item_data in review_status:
            review_status_item = review_status_item_data.value
            json_review_status.append(review_status_item)

    params["review_status"] = json_review_status

    json_launched_by_ids: list[str] | Unset = UNSET
    if not isinstance(launched_by_ids, Unset):
        json_launched_by_ids = []
        for launched_by_ids_item_data in launched_by_ids:
            launched_by_ids_item = str(launched_by_ids_item_data)
            json_launched_by_ids.append(launched_by_ids_item)

    params["launched_by_ids"] = json_launched_by_ids

    json_start_datetime: None | str | Unset
    if isinstance(start_datetime, Unset):
        json_start_datetime = UNSET
    elif isinstance(start_datetime, datetime.datetime):
        json_start_datetime = start_datetime.isoformat()
    else:
        json_start_datetime = start_datetime
    params["start_datetime"] = json_start_datetime

    json_end_datetime: None | str | Unset
    if isinstance(end_datetime, Unset):
        json_end_datetime = UNSET
    elif isinstance(end_datetime, datetime.datetime):
        json_end_datetime = end_datetime.isoformat()
    else:
        json_end_datetime = end_datetime
    params["end_datetime"] = json_end_datetime

    json_memo: None | str | Unset
    if isinstance(memo, Unset):
        json_memo = UNSET
    else:
        json_memo = memo
    params["memo"] = json_memo

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
        "url": "/api/core/dataspaces/{dataspace_id}/execution-groups/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PagedExecutionGroupGetOut | None:
    if response.status_code == 200:
        response_200 = PagedExecutionGroupGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PagedExecutionGroupGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: str,
    *,
    client: AuthenticatedClient,
    process_types: list[GetDataspaceExecutionGroupsProcessTypeChoices] | Unset = UNSET,
    process_ids: list[UUID] | Unset = UNSET,
    status: list[GetDataspaceExecutionGroupsExecutionGroupStatus] | Unset = UNSET,
    review_status: list[GetDataspaceExecutionGroupsExecutionReviewStatus] | Unset = UNSET,
    launched_by_ids: list[UUID] | Unset = UNSET,
    start_datetime: datetime.datetime | None | Unset = UNSET,
    end_datetime: datetime.datetime | None | Unset = UNSET,
    memo: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedExecutionGroupGetOut]:
    """Get Dataspace Execution Groups

     LWV7x0oY

    Retrieve all execution groups in the current dataspace.

    Filters:
        datetime format - 2025-12-18 00:00:00+00:00

    Args:
        dataspace_id (str):
        process_types (list[GetDataspaceExecutionGroupsProcessTypeChoices] | Unset): Process types
        process_ids (list[UUID] | Unset): Process IDs
        status (list[GetDataspaceExecutionGroupsExecutionGroupStatus] | Unset): Execution group
            statuses
        review_status (list[GetDataspaceExecutionGroupsExecutionReviewStatus] | Unset):
            Execution's review statuses
        launched_by_ids (list[UUID] | Unset): IDs of users who launched the execution groups
        start_datetime (datetime.datetime | None | Unset): Filter execution groups started on or
            after this datetime
        end_datetime (datetime.datetime | None | Unset): Filter execution groups ended on or
            before this datetime
        memo (None | str | Unset): Filter execution groups containing this memo text
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedExecutionGroupGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        process_types=process_types,
        process_ids=process_ids,
        status=status,
        review_status=review_status,
        launched_by_ids=launched_by_ids,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        memo=memo,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: str,
    *,
    client: AuthenticatedClient,
    process_types: list[GetDataspaceExecutionGroupsProcessTypeChoices] | Unset = UNSET,
    process_ids: list[UUID] | Unset = UNSET,
    status: list[GetDataspaceExecutionGroupsExecutionGroupStatus] | Unset = UNSET,
    review_status: list[GetDataspaceExecutionGroupsExecutionReviewStatus] | Unset = UNSET,
    launched_by_ids: list[UUID] | Unset = UNSET,
    start_datetime: datetime.datetime | None | Unset = UNSET,
    end_datetime: datetime.datetime | None | Unset = UNSET,
    memo: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedExecutionGroupGetOut | None:
    """Get Dataspace Execution Groups

     LWV7x0oY

    Retrieve all execution groups in the current dataspace.

    Filters:
        datetime format - 2025-12-18 00:00:00+00:00

    Args:
        dataspace_id (str):
        process_types (list[GetDataspaceExecutionGroupsProcessTypeChoices] | Unset): Process types
        process_ids (list[UUID] | Unset): Process IDs
        status (list[GetDataspaceExecutionGroupsExecutionGroupStatus] | Unset): Execution group
            statuses
        review_status (list[GetDataspaceExecutionGroupsExecutionReviewStatus] | Unset):
            Execution's review statuses
        launched_by_ids (list[UUID] | Unset): IDs of users who launched the execution groups
        start_datetime (datetime.datetime | None | Unset): Filter execution groups started on or
            after this datetime
        end_datetime (datetime.datetime | None | Unset): Filter execution groups ended on or
            before this datetime
        memo (None | str | Unset): Filter execution groups containing this memo text
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedExecutionGroupGetOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        client=client,
        process_types=process_types,
        process_ids=process_ids,
        status=status,
        review_status=review_status,
        launched_by_ids=launched_by_ids,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        memo=memo,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    dataspace_id: str,
    *,
    client: AuthenticatedClient,
    process_types: list[GetDataspaceExecutionGroupsProcessTypeChoices] | Unset = UNSET,
    process_ids: list[UUID] | Unset = UNSET,
    status: list[GetDataspaceExecutionGroupsExecutionGroupStatus] | Unset = UNSET,
    review_status: list[GetDataspaceExecutionGroupsExecutionReviewStatus] | Unset = UNSET,
    launched_by_ids: list[UUID] | Unset = UNSET,
    start_datetime: datetime.datetime | None | Unset = UNSET,
    end_datetime: datetime.datetime | None | Unset = UNSET,
    memo: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedExecutionGroupGetOut]:
    """Get Dataspace Execution Groups

     LWV7x0oY

    Retrieve all execution groups in the current dataspace.

    Filters:
        datetime format - 2025-12-18 00:00:00+00:00

    Args:
        dataspace_id (str):
        process_types (list[GetDataspaceExecutionGroupsProcessTypeChoices] | Unset): Process types
        process_ids (list[UUID] | Unset): Process IDs
        status (list[GetDataspaceExecutionGroupsExecutionGroupStatus] | Unset): Execution group
            statuses
        review_status (list[GetDataspaceExecutionGroupsExecutionReviewStatus] | Unset):
            Execution's review statuses
        launched_by_ids (list[UUID] | Unset): IDs of users who launched the execution groups
        start_datetime (datetime.datetime | None | Unset): Filter execution groups started on or
            after this datetime
        end_datetime (datetime.datetime | None | Unset): Filter execution groups ended on or
            before this datetime
        memo (None | str | Unset): Filter execution groups containing this memo text
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedExecutionGroupGetOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        process_types=process_types,
        process_ids=process_ids,
        status=status,
        review_status=review_status,
        launched_by_ids=launched_by_ids,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        memo=memo,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: str,
    *,
    client: AuthenticatedClient,
    process_types: list[GetDataspaceExecutionGroupsProcessTypeChoices] | Unset = UNSET,
    process_ids: list[UUID] | Unset = UNSET,
    status: list[GetDataspaceExecutionGroupsExecutionGroupStatus] | Unset = UNSET,
    review_status: list[GetDataspaceExecutionGroupsExecutionReviewStatus] | Unset = UNSET,
    launched_by_ids: list[UUID] | Unset = UNSET,
    start_datetime: datetime.datetime | None | Unset = UNSET,
    end_datetime: datetime.datetime | None | Unset = UNSET,
    memo: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedExecutionGroupGetOut | None:
    """Get Dataspace Execution Groups

     LWV7x0oY

    Retrieve all execution groups in the current dataspace.

    Filters:
        datetime format - 2025-12-18 00:00:00+00:00

    Args:
        dataspace_id (str):
        process_types (list[GetDataspaceExecutionGroupsProcessTypeChoices] | Unset): Process types
        process_ids (list[UUID] | Unset): Process IDs
        status (list[GetDataspaceExecutionGroupsExecutionGroupStatus] | Unset): Execution group
            statuses
        review_status (list[GetDataspaceExecutionGroupsExecutionReviewStatus] | Unset):
            Execution's review statuses
        launched_by_ids (list[UUID] | Unset): IDs of users who launched the execution groups
        start_datetime (datetime.datetime | None | Unset): Filter execution groups started on or
            after this datetime
        end_datetime (datetime.datetime | None | Unset): Filter execution groups ended on or
            before this datetime
        memo (None | str | Unset): Filter execution groups containing this memo text
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedExecutionGroupGetOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            client=client,
            process_types=process_types,
            process_ids=process_ids,
            status=status,
            review_status=review_status,
            launched_by_ids=launched_by_ids,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            memo=memo,
            page=page,
            page_size=page_size,
        )
    ).parsed
