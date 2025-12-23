from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appcore_routes_reports_get_llm_usage_reports_period_types import (
    AppcoreRoutesReportsGetLlmUsageReportsPeriodTypes,
)
from ...models.paged_llm_usage_report_get_out import PagedLLMUsageReportGetOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization_id: UUID,
    period_type: AppcoreRoutesReportsGetLlmUsageReportsPeriodTypes,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id

    json_period_type = period_type.value
    params["period_type"] = json_period_type

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
        "url": "/api/core/reports/llm-usages/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PagedLLMUsageReportGetOut | None:
    if response.status_code == 200:
        response_200 = PagedLLMUsageReportGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PagedLLMUsageReportGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    organization_id: UUID,
    period_type: AppcoreRoutesReportsGetLlmUsageReportsPeriodTypes,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedLLMUsageReportGetOut]:
    """Get Llm Usage Reports

     7wGb8Zfz

    Retrieve LLM usage reports for a specific organization and period type.

    Args:
        request: The HTTP request object.
        query_params: Query parameters including organization_id and period_type.

    Returns: A list of LLMUsageReport objects ordered by period in descending order.

    Args:
        organization_id (UUID):
        period_type (AppcoreRoutesReportsGetLlmUsageReportsPeriodTypes):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedLLMUsageReportGetOut]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        period_type=period_type,
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
    organization_id: UUID,
    period_type: AppcoreRoutesReportsGetLlmUsageReportsPeriodTypes,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedLLMUsageReportGetOut | None:
    """Get Llm Usage Reports

     7wGb8Zfz

    Retrieve LLM usage reports for a specific organization and period type.

    Args:
        request: The HTTP request object.
        query_params: Query parameters including organization_id and period_type.

    Returns: A list of LLMUsageReport objects ordered by period in descending order.

    Args:
        organization_id (UUID):
        period_type (AppcoreRoutesReportsGetLlmUsageReportsPeriodTypes):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedLLMUsageReportGetOut
    """

    return sync_detailed(
        client=client,
        organization_id=organization_id,
        period_type=period_type,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    organization_id: UUID,
    period_type: AppcoreRoutesReportsGetLlmUsageReportsPeriodTypes,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedLLMUsageReportGetOut]:
    """Get Llm Usage Reports

     7wGb8Zfz

    Retrieve LLM usage reports for a specific organization and period type.

    Args:
        request: The HTTP request object.
        query_params: Query parameters including organization_id and period_type.

    Returns: A list of LLMUsageReport objects ordered by period in descending order.

    Args:
        organization_id (UUID):
        period_type (AppcoreRoutesReportsGetLlmUsageReportsPeriodTypes):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedLLMUsageReportGetOut]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        period_type=period_type,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    organization_id: UUID,
    period_type: AppcoreRoutesReportsGetLlmUsageReportsPeriodTypes,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedLLMUsageReportGetOut | None:
    """Get Llm Usage Reports

     7wGb8Zfz

    Retrieve LLM usage reports for a specific organization and period type.

    Args:
        request: The HTTP request object.
        query_params: Query parameters including organization_id and period_type.

    Returns: A list of LLMUsageReport objects ordered by period in descending order.

    Args:
        organization_id (UUID):
        period_type (AppcoreRoutesReportsGetLlmUsageReportsPeriodTypes):
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedLLMUsageReportGetOut
    """

    return (
        await asyncio_detailed(
            client=client,
            organization_id=organization_id,
            period_type=period_type,
            page=page,
            page_size=page_size,
        )
    ).parsed
