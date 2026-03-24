from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_recommend_resource_group_request import CreateRecommendResourceGroupRequest
from ...models.recommend_resource_group_response import RecommendResourceGroupResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateRecommendResourceGroupRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/resources/groups/recommend-resource-group/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RecommendResourceGroupResponse | None:
    if response.status_code == 200:
        response_200 = RecommendResourceGroupResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RecommendResourceGroupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateRecommendResourceGroupRequest,
) -> Response[RecommendResourceGroupResponse]:
    """Recommend resource groups

     Get AI-powered resource group recommendations based on project attributes such as location,
    structure, building type, and dimensions. Results are ranked by relevance score.

    Args:
        body (CreateRecommendResourceGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecommendResourceGroupResponse]
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
    body: CreateRecommendResourceGroupRequest,
) -> RecommendResourceGroupResponse | None:
    """Recommend resource groups

     Get AI-powered resource group recommendations based on project attributes such as location,
    structure, building type, and dimensions. Results are ranked by relevance score.

    Args:
        body (CreateRecommendResourceGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecommendResourceGroupResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateRecommendResourceGroupRequest,
) -> Response[RecommendResourceGroupResponse]:
    """Recommend resource groups

     Get AI-powered resource group recommendations based on project attributes such as location,
    structure, building type, and dimensions. Results are ranked by relevance score.

    Args:
        body (CreateRecommendResourceGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecommendResourceGroupResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateRecommendResourceGroupRequest,
) -> RecommendResourceGroupResponse | None:
    """Recommend resource groups

     Get AI-powered resource group recommendations based on project attributes such as location,
    structure, building type, and dimensions. Results are ranked by relevance score.

    Args:
        body (CreateRecommendResourceGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecommendResourceGroupResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
