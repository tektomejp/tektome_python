from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.export_usage_reports_period_types import ExportUsageReportsPeriodTypes
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization_id: UUID,
    period_type: ExportUsageReportsPeriodTypes,
    month: int,
    year: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_organization_id = str(organization_id)
    params["organization_id"] = json_organization_id

    json_period_type = period_type.value
    params["period_type"] = json_period_type

    params["month"] = month

    params["year"] = year

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/reports/export-usages/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    period_type: ExportUsageReportsPeriodTypes,
    month: int,
    year: int | Unset = UNSET,
) -> Response[Any]:
    """Get Export Usage Reports

     7wGb8ZfA

    Export usage reports for a specific organization and month/year as a ZIP file containing multiple
    CSV reports.

    Args:
        request: The HTTP request object.
        query_params: Query parameters including organization_id, month, and year.

    Returns: A FileResponse containing the ZIP file with the usage reports.

    Args:
        organization_id (UUID):
        period_type (ExportUsageReportsPeriodTypes):
        month (int): Month as an integer (1-12)
        year (int | Unset): Year as a four-digit integer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        period_type=period_type,
        month=month,
        year=year,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    organization_id: UUID,
    period_type: ExportUsageReportsPeriodTypes,
    month: int,
    year: int | Unset = UNSET,
) -> Response[Any]:
    """Get Export Usage Reports

     7wGb8ZfA

    Export usage reports for a specific organization and month/year as a ZIP file containing multiple
    CSV reports.

    Args:
        request: The HTTP request object.
        query_params: Query parameters including organization_id, month, and year.

    Returns: A FileResponse containing the ZIP file with the usage reports.

    Args:
        organization_id (UUID):
        period_type (ExportUsageReportsPeriodTypes):
        month (int): Month as an integer (1-12)
        year (int | Unset): Year as a four-digit integer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        period_type=period_type,
        month=month,
        year=year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
