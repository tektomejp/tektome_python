from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.recommend_resource_group_get_out import RecommendResourceGroupGetOut
from ...models.recommend_resource_group_post_in import RecommendResourceGroupPostIn
from ...types import Response


def _get_kwargs(
    *,
    body: RecommendResourceGroupPostIn,
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
) -> RecommendResourceGroupGetOut | None:
    if response.status_code == 200:
        response_200 = RecommendResourceGroupGetOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RecommendResourceGroupGetOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RecommendResourceGroupPostIn,
) -> Response[RecommendResourceGroupGetOut]:
    r"""Post Recommend Resource Group

     9kxmqqUu

    Recommend Lawtalk's Resource Groups based on project attributes.
    Uses LLM to parse natural language locations. The result is cached for 3600 seconds.
    parsed_location is different for each locale:
    gb
    ```
    ...
    parsed_location:
        {
            \"city\": \"chicago\",
            \"state\": \"illinois\",
            \"country\": \"united-states\"
        }
    }
    ```
    jp
    ```
    ...
    parsed_location:
        {
            \"prefecture\": \"tokyo\",
            \"city\": \"shinjuku\",
            \"ward\": \"shinjuku\"
        }
    }
    ```

    Args:
        body (RecommendResourceGroupPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecommendResourceGroupGetOut]
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
    body: RecommendResourceGroupPostIn,
) -> RecommendResourceGroupGetOut | None:
    r"""Post Recommend Resource Group

     9kxmqqUu

    Recommend Lawtalk's Resource Groups based on project attributes.
    Uses LLM to parse natural language locations. The result is cached for 3600 seconds.
    parsed_location is different for each locale:
    gb
    ```
    ...
    parsed_location:
        {
            \"city\": \"chicago\",
            \"state\": \"illinois\",
            \"country\": \"united-states\"
        }
    }
    ```
    jp
    ```
    ...
    parsed_location:
        {
            \"prefecture\": \"tokyo\",
            \"city\": \"shinjuku\",
            \"ward\": \"shinjuku\"
        }
    }
    ```

    Args:
        body (RecommendResourceGroupPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecommendResourceGroupGetOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RecommendResourceGroupPostIn,
) -> Response[RecommendResourceGroupGetOut]:
    r"""Post Recommend Resource Group

     9kxmqqUu

    Recommend Lawtalk's Resource Groups based on project attributes.
    Uses LLM to parse natural language locations. The result is cached for 3600 seconds.
    parsed_location is different for each locale:
    gb
    ```
    ...
    parsed_location:
        {
            \"city\": \"chicago\",
            \"state\": \"illinois\",
            \"country\": \"united-states\"
        }
    }
    ```
    jp
    ```
    ...
    parsed_location:
        {
            \"prefecture\": \"tokyo\",
            \"city\": \"shinjuku\",
            \"ward\": \"shinjuku\"
        }
    }
    ```

    Args:
        body (RecommendResourceGroupPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecommendResourceGroupGetOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RecommendResourceGroupPostIn,
) -> RecommendResourceGroupGetOut | None:
    r"""Post Recommend Resource Group

     9kxmqqUu

    Recommend Lawtalk's Resource Groups based on project attributes.
    Uses LLM to parse natural language locations. The result is cached for 3600 seconds.
    parsed_location is different for each locale:
    gb
    ```
    ...
    parsed_location:
        {
            \"city\": \"chicago\",
            \"state\": \"illinois\",
            \"country\": \"united-states\"
        }
    }
    ```
    jp
    ```
    ...
    parsed_location:
        {
            \"prefecture\": \"tokyo\",
            \"city\": \"shinjuku\",
            \"ward\": \"shinjuku\"
        }
    }
    ```

    Args:
        body (RecommendResourceGroupPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecommendResourceGroupGetOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
