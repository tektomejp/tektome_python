from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.aggregate_llm_usage_post_in import AggregateLLMUsagePostIn
from ...models.aggregated_llm_usage_post_out import AggregatedLLMUsagePostOut
from ...types import Response


def _get_kwargs(
    *,
    body: AggregateLLMUsagePostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/usages/aggregate-llm-usage/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AggregatedLLMUsagePostOut | None:
    if response.status_code == 200:
        response_200 = AggregatedLLMUsagePostOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AggregatedLLMUsagePostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AggregateLLMUsagePostIn,
) -> Response[AggregatedLLMUsagePostOut]:
    """Aggregate LLM usage statistics

     Aggregate LLM usage statistics by kind or model within a specified date range. Supports optional
    filtering by organization, dataspace, project, or user.

    Args:
        body (AggregateLLMUsagePostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AggregatedLLMUsagePostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AggregateLLMUsagePostIn,
) -> AggregatedLLMUsagePostOut | None:
    """Aggregate LLM usage statistics

     Aggregate LLM usage statistics by kind or model within a specified date range. Supports optional
    filtering by organization, dataspace, project, or user.

    Args:
        body (AggregateLLMUsagePostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AggregatedLLMUsagePostOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AggregateLLMUsagePostIn,
) -> Response[AggregatedLLMUsagePostOut]:
    """Aggregate LLM usage statistics

     Aggregate LLM usage statistics by kind or model within a specified date range. Supports optional
    filtering by organization, dataspace, project, or user.

    Args:
        body (AggregateLLMUsagePostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AggregatedLLMUsagePostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AggregateLLMUsagePostIn,
) -> AggregatedLLMUsagePostOut | None:
    """Aggregate LLM usage statistics

     Aggregate LLM usage statistics by kind or model within a specified date range. Supports optional
    filtering by organization, dataspace, project, or user.

    Args:
        body (AggregateLLMUsagePostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AggregatedLLMUsagePostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
