import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_dataspace_executions_approval_category_types import GetDataspaceExecutionsApprovalCategoryTypes
from ...models.get_dataspace_executions_execution_review_status import GetDataspaceExecutionsExecutionReviewStatus
from ...models.get_dataspace_executions_execution_status import GetDataspaceExecutionsExecutionStatus
from ...models.get_dataspace_executions_process_type_choices import GetDataspaceExecutionsProcessTypeChoices
from ...models.paged_executions_get_out import PagedExecutionsGetOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataspace_id: UUID,
    *,
    process_types: list[GetDataspaceExecutionsProcessTypeChoices] | Unset = UNSET,
    process_ids: list[UUID] | Unset = UNSET,
    status: list[GetDataspaceExecutionsExecutionStatus] | Unset = UNSET,
    review_status: list[GetDataspaceExecutionsExecutionReviewStatus] | Unset = UNSET,
    launched_by_ids: list[UUID] | Unset = UNSET,
    start_datetime: datetime.datetime | None | Unset = UNSET,
    end_datetime: datetime.datetime | None | Unset = UNSET,
    memo: None | str | Unset = UNSET,
    execution_group_ids: list[UUID] | Unset = UNSET,
    target_files_ids: list[UUID] | Unset = UNSET,
    target_entity_ids: list[UUID] | Unset = UNSET,
    category: list[GetDataspaceExecutionsApprovalCategoryTypes] | Unset = UNSET,
    file_attributes_extracted_ids: list[UUID] | Unset = UNSET,
    entity_attributes_extracted_ids: list[UUID] | Unset = UNSET,
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

    json_execution_group_ids: list[str] | Unset = UNSET
    if not isinstance(execution_group_ids, Unset):
        json_execution_group_ids = []
        for execution_group_ids_item_data in execution_group_ids:
            execution_group_ids_item = str(execution_group_ids_item_data)
            json_execution_group_ids.append(execution_group_ids_item)

    params["execution_group_ids"] = json_execution_group_ids

    json_target_files_ids: list[str] | Unset = UNSET
    if not isinstance(target_files_ids, Unset):
        json_target_files_ids = []
        for target_files_ids_item_data in target_files_ids:
            target_files_ids_item = str(target_files_ids_item_data)
            json_target_files_ids.append(target_files_ids_item)

    params["target_files_ids"] = json_target_files_ids

    json_target_entity_ids: list[str] | Unset = UNSET
    if not isinstance(target_entity_ids, Unset):
        json_target_entity_ids = []
        for target_entity_ids_item_data in target_entity_ids:
            target_entity_ids_item = str(target_entity_ids_item_data)
            json_target_entity_ids.append(target_entity_ids_item)

    params["target_entity_ids"] = json_target_entity_ids

    json_category: list[str] | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = []
        for category_item_data in category:
            category_item = category_item_data.value
            json_category.append(category_item)

    params["category"] = json_category

    json_file_attributes_extracted_ids: list[str] | Unset = UNSET
    if not isinstance(file_attributes_extracted_ids, Unset):
        json_file_attributes_extracted_ids = []
        for file_attributes_extracted_ids_item_data in file_attributes_extracted_ids:
            file_attributes_extracted_ids_item = str(file_attributes_extracted_ids_item_data)
            json_file_attributes_extracted_ids.append(file_attributes_extracted_ids_item)

    params["file_attributes_extracted_ids"] = json_file_attributes_extracted_ids

    json_entity_attributes_extracted_ids: list[str] | Unset = UNSET
    if not isinstance(entity_attributes_extracted_ids, Unset):
        json_entity_attributes_extracted_ids = []
        for entity_attributes_extracted_ids_item_data in entity_attributes_extracted_ids:
            entity_attributes_extracted_ids_item = str(entity_attributes_extracted_ids_item_data)
            json_entity_attributes_extracted_ids.append(entity_attributes_extracted_ids_item)

    params["entity_attributes_extracted_ids"] = json_entity_attributes_extracted_ids

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
        "url": "/api/core/dataspaces/{dataspace_id}/executions/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedExecutionsGetOut | None:
    if response.status_code == 200:
        response_200 = PagedExecutionsGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PagedExecutionsGetOut]:
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
    process_types: list[GetDataspaceExecutionsProcessTypeChoices] | Unset = UNSET,
    process_ids: list[UUID] | Unset = UNSET,
    status: list[GetDataspaceExecutionsExecutionStatus] | Unset = UNSET,
    review_status: list[GetDataspaceExecutionsExecutionReviewStatus] | Unset = UNSET,
    launched_by_ids: list[UUID] | Unset = UNSET,
    start_datetime: datetime.datetime | None | Unset = UNSET,
    end_datetime: datetime.datetime | None | Unset = UNSET,
    memo: None | str | Unset = UNSET,
    execution_group_ids: list[UUID] | Unset = UNSET,
    target_files_ids: list[UUID] | Unset = UNSET,
    target_entity_ids: list[UUID] | Unset = UNSET,
    category: list[GetDataspaceExecutionsApprovalCategoryTypes] | Unset = UNSET,
    file_attributes_extracted_ids: list[UUID] | Unset = UNSET,
    entity_attributes_extracted_ids: list[UUID] | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedExecutionsGetOut]:
    """Get Dataspace Executions

     LWV7x0oA

    Retrieve all executions in the current dataspace.

    Filters:
        datetime format - 2025-12-18 00:00:00+00:00

    Args:
        dataspace_id (UUID):
        process_types (list[GetDataspaceExecutionsProcessTypeChoices] | Unset): Process types
        process_ids (list[UUID] | Unset): Process IDs
        status (list[GetDataspaceExecutionsExecutionStatus] | Unset): Execution group statuses
        review_status (list[GetDataspaceExecutionsExecutionReviewStatus] | Unset): Execution's
            review statuses
        launched_by_ids (list[UUID] | Unset): IDs of users who launched the execution groups
        start_datetime (datetime.datetime | None | Unset): Filter execution groups started on or
            after this datetime
        end_datetime (datetime.datetime | None | Unset): Filter execution groups ended on or
            before this datetime
        memo (None | str | Unset): Filter execution groups containing this memo text
        execution_group_ids (list[UUID] | Unset): Execution group IDs
        target_files_ids (list[UUID] | Unset): Target core resource file IDs
        target_entity_ids (list[UUID] | Unset): Target DS entity IDs
        category (list[GetDataspaceExecutionsApprovalCategoryTypes] | Unset): Approval category to
            filter executions
        file_attributes_extracted_ids (list[UUID] | Unset): Filter executions with these UUID file
            attributes extracted
        entity_attributes_extracted_ids (list[UUID] | Unset): Filter executions with these UUID
            entity attributes extracted
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedExecutionsGetOut]
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
        execution_group_ids=execution_group_ids,
        target_files_ids=target_files_ids,
        target_entity_ids=target_entity_ids,
        category=category,
        file_attributes_extracted_ids=file_attributes_extracted_ids,
        entity_attributes_extracted_ids=entity_attributes_extracted_ids,
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
    process_types: list[GetDataspaceExecutionsProcessTypeChoices] | Unset = UNSET,
    process_ids: list[UUID] | Unset = UNSET,
    status: list[GetDataspaceExecutionsExecutionStatus] | Unset = UNSET,
    review_status: list[GetDataspaceExecutionsExecutionReviewStatus] | Unset = UNSET,
    launched_by_ids: list[UUID] | Unset = UNSET,
    start_datetime: datetime.datetime | None | Unset = UNSET,
    end_datetime: datetime.datetime | None | Unset = UNSET,
    memo: None | str | Unset = UNSET,
    execution_group_ids: list[UUID] | Unset = UNSET,
    target_files_ids: list[UUID] | Unset = UNSET,
    target_entity_ids: list[UUID] | Unset = UNSET,
    category: list[GetDataspaceExecutionsApprovalCategoryTypes] | Unset = UNSET,
    file_attributes_extracted_ids: list[UUID] | Unset = UNSET,
    entity_attributes_extracted_ids: list[UUID] | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedExecutionsGetOut | None:
    """Get Dataspace Executions

     LWV7x0oA

    Retrieve all executions in the current dataspace.

    Filters:
        datetime format - 2025-12-18 00:00:00+00:00

    Args:
        dataspace_id (UUID):
        process_types (list[GetDataspaceExecutionsProcessTypeChoices] | Unset): Process types
        process_ids (list[UUID] | Unset): Process IDs
        status (list[GetDataspaceExecutionsExecutionStatus] | Unset): Execution group statuses
        review_status (list[GetDataspaceExecutionsExecutionReviewStatus] | Unset): Execution's
            review statuses
        launched_by_ids (list[UUID] | Unset): IDs of users who launched the execution groups
        start_datetime (datetime.datetime | None | Unset): Filter execution groups started on or
            after this datetime
        end_datetime (datetime.datetime | None | Unset): Filter execution groups ended on or
            before this datetime
        memo (None | str | Unset): Filter execution groups containing this memo text
        execution_group_ids (list[UUID] | Unset): Execution group IDs
        target_files_ids (list[UUID] | Unset): Target core resource file IDs
        target_entity_ids (list[UUID] | Unset): Target DS entity IDs
        category (list[GetDataspaceExecutionsApprovalCategoryTypes] | Unset): Approval category to
            filter executions
        file_attributes_extracted_ids (list[UUID] | Unset): Filter executions with these UUID file
            attributes extracted
        entity_attributes_extracted_ids (list[UUID] | Unset): Filter executions with these UUID
            entity attributes extracted
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedExecutionsGetOut
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
        execution_group_ids=execution_group_ids,
        target_files_ids=target_files_ids,
        target_entity_ids=target_entity_ids,
        category=category,
        file_attributes_extracted_ids=file_attributes_extracted_ids,
        entity_attributes_extracted_ids=entity_attributes_extracted_ids,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    process_types: list[GetDataspaceExecutionsProcessTypeChoices] | Unset = UNSET,
    process_ids: list[UUID] | Unset = UNSET,
    status: list[GetDataspaceExecutionsExecutionStatus] | Unset = UNSET,
    review_status: list[GetDataspaceExecutionsExecutionReviewStatus] | Unset = UNSET,
    launched_by_ids: list[UUID] | Unset = UNSET,
    start_datetime: datetime.datetime | None | Unset = UNSET,
    end_datetime: datetime.datetime | None | Unset = UNSET,
    memo: None | str | Unset = UNSET,
    execution_group_ids: list[UUID] | Unset = UNSET,
    target_files_ids: list[UUID] | Unset = UNSET,
    target_entity_ids: list[UUID] | Unset = UNSET,
    category: list[GetDataspaceExecutionsApprovalCategoryTypes] | Unset = UNSET,
    file_attributes_extracted_ids: list[UUID] | Unset = UNSET,
    entity_attributes_extracted_ids: list[UUID] | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedExecutionsGetOut]:
    """Get Dataspace Executions

     LWV7x0oA

    Retrieve all executions in the current dataspace.

    Filters:
        datetime format - 2025-12-18 00:00:00+00:00

    Args:
        dataspace_id (UUID):
        process_types (list[GetDataspaceExecutionsProcessTypeChoices] | Unset): Process types
        process_ids (list[UUID] | Unset): Process IDs
        status (list[GetDataspaceExecutionsExecutionStatus] | Unset): Execution group statuses
        review_status (list[GetDataspaceExecutionsExecutionReviewStatus] | Unset): Execution's
            review statuses
        launched_by_ids (list[UUID] | Unset): IDs of users who launched the execution groups
        start_datetime (datetime.datetime | None | Unset): Filter execution groups started on or
            after this datetime
        end_datetime (datetime.datetime | None | Unset): Filter execution groups ended on or
            before this datetime
        memo (None | str | Unset): Filter execution groups containing this memo text
        execution_group_ids (list[UUID] | Unset): Execution group IDs
        target_files_ids (list[UUID] | Unset): Target core resource file IDs
        target_entity_ids (list[UUID] | Unset): Target DS entity IDs
        category (list[GetDataspaceExecutionsApprovalCategoryTypes] | Unset): Approval category to
            filter executions
        file_attributes_extracted_ids (list[UUID] | Unset): Filter executions with these UUID file
            attributes extracted
        entity_attributes_extracted_ids (list[UUID] | Unset): Filter executions with these UUID
            entity attributes extracted
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedExecutionsGetOut]
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
        execution_group_ids=execution_group_ids,
        target_files_ids=target_files_ids,
        target_entity_ids=target_entity_ids,
        category=category,
        file_attributes_extracted_ids=file_attributes_extracted_ids,
        entity_attributes_extracted_ids=entity_attributes_extracted_ids,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    *,
    client: AuthenticatedClient,
    process_types: list[GetDataspaceExecutionsProcessTypeChoices] | Unset = UNSET,
    process_ids: list[UUID] | Unset = UNSET,
    status: list[GetDataspaceExecutionsExecutionStatus] | Unset = UNSET,
    review_status: list[GetDataspaceExecutionsExecutionReviewStatus] | Unset = UNSET,
    launched_by_ids: list[UUID] | Unset = UNSET,
    start_datetime: datetime.datetime | None | Unset = UNSET,
    end_datetime: datetime.datetime | None | Unset = UNSET,
    memo: None | str | Unset = UNSET,
    execution_group_ids: list[UUID] | Unset = UNSET,
    target_files_ids: list[UUID] | Unset = UNSET,
    target_entity_ids: list[UUID] | Unset = UNSET,
    category: list[GetDataspaceExecutionsApprovalCategoryTypes] | Unset = UNSET,
    file_attributes_extracted_ids: list[UUID] | Unset = UNSET,
    entity_attributes_extracted_ids: list[UUID] | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedExecutionsGetOut | None:
    """Get Dataspace Executions

     LWV7x0oA

    Retrieve all executions in the current dataspace.

    Filters:
        datetime format - 2025-12-18 00:00:00+00:00

    Args:
        dataspace_id (UUID):
        process_types (list[GetDataspaceExecutionsProcessTypeChoices] | Unset): Process types
        process_ids (list[UUID] | Unset): Process IDs
        status (list[GetDataspaceExecutionsExecutionStatus] | Unset): Execution group statuses
        review_status (list[GetDataspaceExecutionsExecutionReviewStatus] | Unset): Execution's
            review statuses
        launched_by_ids (list[UUID] | Unset): IDs of users who launched the execution groups
        start_datetime (datetime.datetime | None | Unset): Filter execution groups started on or
            after this datetime
        end_datetime (datetime.datetime | None | Unset): Filter execution groups ended on or
            before this datetime
        memo (None | str | Unset): Filter execution groups containing this memo text
        execution_group_ids (list[UUID] | Unset): Execution group IDs
        target_files_ids (list[UUID] | Unset): Target core resource file IDs
        target_entity_ids (list[UUID] | Unset): Target DS entity IDs
        category (list[GetDataspaceExecutionsApprovalCategoryTypes] | Unset): Approval category to
            filter executions
        file_attributes_extracted_ids (list[UUID] | Unset): Filter executions with these UUID file
            attributes extracted
        entity_attributes_extracted_ids (list[UUID] | Unset): Filter executions with these UUID
            entity attributes extracted
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedExecutionsGetOut
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
            execution_group_ids=execution_group_ids,
            target_files_ids=target_files_ids,
            target_entity_ids=target_entity_ids,
            category=category,
            file_attributes_extracted_ids=file_attributes_extracted_ids,
            entity_attributes_extracted_ids=entity_attributes_extracted_ids,
            page=page,
            page_size=page_size,
        )
    ).parsed
