from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.observability_schema_response import ObservabilitySchemaResponse
from ...models.replace_observability_request import ReplaceObservabilityRequest
from ...types import Response


def _get_kwargs(
    *,
    body: ReplaceObservabilityRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/core/account/generic-observations/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ObservabilitySchemaResponse] | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = ObservabilitySchemaResponse.from_dict(response_201_item_data)

            response_201.append(response_201_item)

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ObservabilitySchemaResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ReplaceObservabilityRequest,
) -> Response[list[ObservabilitySchemaResponse]]:
    """Upsert observation records

     Create or update observation records for entities. Tracks whether entities have been viewed by the
    authenticated user.

    Args:
        body (ReplaceObservabilityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ObservabilitySchemaResponse]]
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
    body: ReplaceObservabilityRequest,
) -> list[ObservabilitySchemaResponse] | None:
    """Upsert observation records

     Create or update observation records for entities. Tracks whether entities have been viewed by the
    authenticated user.

    Args:
        body (ReplaceObservabilityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ObservabilitySchemaResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ReplaceObservabilityRequest,
) -> Response[list[ObservabilitySchemaResponse]]:
    """Upsert observation records

     Create or update observation records for entities. Tracks whether entities have been viewed by the
    authenticated user.

    Args:
        body (ReplaceObservabilityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ObservabilitySchemaResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ReplaceObservabilityRequest,
) -> list[ObservabilitySchemaResponse] | None:
    """Upsert observation records

     Create or update observation records for entities. Tracks whether entities have been viewed by the
    authenticated user.

    Args:
        body (ReplaceObservabilityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ObservabilitySchemaResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
