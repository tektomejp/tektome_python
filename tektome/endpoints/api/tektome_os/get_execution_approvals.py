from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.approval_category_types import ApprovalCategoryTypes
from ...models.approval_status import ApprovalStatus
from ...models.paged_execution_approvals_get_out import PagedExecutionApprovalsGetOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    execution_id: None | Unset | UUID = UNSET,
    execution_group_id: None | Unset | UUID = UNSET,
    status: ApprovalStatus | None | Unset = UNSET,
    category: ApprovalCategoryTypes | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_execution_id: None | str | Unset
    if isinstance(execution_id, Unset):
        json_execution_id = UNSET
    elif isinstance(execution_id, UUID):
        json_execution_id = str(execution_id)
    else:
        json_execution_id = execution_id
    params["execution_id"] = json_execution_id

    json_execution_group_id: None | str | Unset
    if isinstance(execution_group_id, Unset):
        json_execution_group_id = UNSET
    elif isinstance(execution_group_id, UUID):
        json_execution_group_id = str(execution_group_id)
    else:
        json_execution_group_id = execution_group_id
    params["execution_group_id"] = json_execution_group_id

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, ApprovalStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_category: None | str | Unset
    if isinstance(category, Unset):
        json_category = UNSET
    elif isinstance(category, ApprovalCategoryTypes):
        json_category = category.value
    else:
        json_category = category
    params["category"] = json_category

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
        "url": "/api/core/agents/os/executions/approvals/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PagedExecutionApprovalsGetOut | None:
    if response.status_code == 200:
        response_200 = PagedExecutionApprovalsGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PagedExecutionApprovalsGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    execution_id: None | Unset | UUID = UNSET,
    execution_group_id: None | Unset | UUID = UNSET,
    status: ApprovalStatus | None | Unset = UNSET,
    category: ApprovalCategoryTypes | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedExecutionApprovalsGetOut]:
    """Get Execution Approvals

     EfJhkBlZ

    Retrieve a list of approval tickets based on query parameters.

    Args:
        request: The incoming HTTP request.
        query_params: The query parameters for filtering approval tickets.

    Returns: A list of ApprovalTicket instances matching the query parameters.

    Args:
        execution_id (None | Unset | UUID):
        execution_group_id (None | Unset | UUID):
        status (ApprovalStatus | None | Unset):
        category (ApprovalCategoryTypes | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedExecutionApprovalsGetOut]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
        execution_group_id=execution_group_id,
        status=status,
        category=category,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    execution_id: None | Unset | UUID = UNSET,
    execution_group_id: None | Unset | UUID = UNSET,
    status: ApprovalStatus | None | Unset = UNSET,
    category: ApprovalCategoryTypes | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedExecutionApprovalsGetOut | None:
    """Get Execution Approvals

     EfJhkBlZ

    Retrieve a list of approval tickets based on query parameters.

    Args:
        request: The incoming HTTP request.
        query_params: The query parameters for filtering approval tickets.

    Returns: A list of ApprovalTicket instances matching the query parameters.

    Args:
        execution_id (None | Unset | UUID):
        execution_group_id (None | Unset | UUID):
        status (ApprovalStatus | None | Unset):
        category (ApprovalCategoryTypes | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedExecutionApprovalsGetOut
    """

    return sync_detailed(
        client=client,
        execution_id=execution_id,
        execution_group_id=execution_group_id,
        status=status,
        category=category,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    execution_id: None | Unset | UUID = UNSET,
    execution_group_id: None | Unset | UUID = UNSET,
    status: ApprovalStatus | None | Unset = UNSET,
    category: ApprovalCategoryTypes | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedExecutionApprovalsGetOut]:
    """Get Execution Approvals

     EfJhkBlZ

    Retrieve a list of approval tickets based on query parameters.

    Args:
        request: The incoming HTTP request.
        query_params: The query parameters for filtering approval tickets.

    Returns: A list of ApprovalTicket instances matching the query parameters.

    Args:
        execution_id (None | Unset | UUID):
        execution_group_id (None | Unset | UUID):
        status (ApprovalStatus | None | Unset):
        category (ApprovalCategoryTypes | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedExecutionApprovalsGetOut]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
        execution_group_id=execution_group_id,
        status=status,
        category=category,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    execution_id: None | Unset | UUID = UNSET,
    execution_group_id: None | Unset | UUID = UNSET,
    status: ApprovalStatus | None | Unset = UNSET,
    category: ApprovalCategoryTypes | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedExecutionApprovalsGetOut | None:
    """Get Execution Approvals

     EfJhkBlZ

    Retrieve a list of approval tickets based on query parameters.

    Args:
        request: The incoming HTTP request.
        query_params: The query parameters for filtering approval tickets.

    Returns: A list of ApprovalTicket instances matching the query parameters.

    Args:
        execution_id (None | Unset | UUID):
        execution_group_id (None | Unset | UUID):
        status (ApprovalStatus | None | Unset):
        category (ApprovalCategoryTypes | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedExecutionApprovalsGetOut
    """

    return (
        await asyncio_detailed(
            client=client,
            execution_id=execution_id,
            execution_group_id=execution_group_id,
            status=status,
            category=category,
            page=page,
            page_size=page_size,
        )
    ).parsed
