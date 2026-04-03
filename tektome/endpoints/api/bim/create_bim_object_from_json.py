from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_object_from_json_response import BimObjectFromJsonResponse
from ...models.create_bim_object_from_json_file_params import CreateBimObjectFromJsonFileParams
from ...models.error_response_post_out import ErrorResponsePostOut
from ...types import Response


def _get_kwargs(
    *,
    body: CreateBimObjectFromJsonFileParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-object/from-json/",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimObjectFromJsonResponse | ErrorResponsePostOut | None:
    if response.status_code == 201:
        response_201 = BimObjectFromJsonResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponsePostOut.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimObjectFromJsonResponse | ErrorResponsePostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateBimObjectFromJsonFileParams,
) -> Response[BimObjectFromJsonResponse | ErrorResponsePostOut]:
    """Create a BIM object from JSON

     Upload a Speckle-compatible JSON file to create a standalone BIM object that is not attached to any
    BIM project. The object ID is recalculated from the JSON content using the Speckle hashing algorithm
    (SHA-256 truncated to 32 hex characters), ensuring the ID is a deterministic content hash.

    The uploaded file must contain a valid JSON object with at least a top-level ``id`` key. All nested
    objects that contain an ``id`` key will also have their IDs recalculated bottom-up.

    Args:
        body (CreateBimObjectFromJsonFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimObjectFromJsonResponse | ErrorResponsePostOut]
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
    body: CreateBimObjectFromJsonFileParams,
) -> BimObjectFromJsonResponse | ErrorResponsePostOut | None:
    """Create a BIM object from JSON

     Upload a Speckle-compatible JSON file to create a standalone BIM object that is not attached to any
    BIM project. The object ID is recalculated from the JSON content using the Speckle hashing algorithm
    (SHA-256 truncated to 32 hex characters), ensuring the ID is a deterministic content hash.

    The uploaded file must contain a valid JSON object with at least a top-level ``id`` key. All nested
    objects that contain an ``id`` key will also have their IDs recalculated bottom-up.

    Args:
        body (CreateBimObjectFromJsonFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimObjectFromJsonResponse | ErrorResponsePostOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateBimObjectFromJsonFileParams,
) -> Response[BimObjectFromJsonResponse | ErrorResponsePostOut]:
    """Create a BIM object from JSON

     Upload a Speckle-compatible JSON file to create a standalone BIM object that is not attached to any
    BIM project. The object ID is recalculated from the JSON content using the Speckle hashing algorithm
    (SHA-256 truncated to 32 hex characters), ensuring the ID is a deterministic content hash.

    The uploaded file must contain a valid JSON object with at least a top-level ``id`` key. All nested
    objects that contain an ``id`` key will also have their IDs recalculated bottom-up.

    Args:
        body (CreateBimObjectFromJsonFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimObjectFromJsonResponse | ErrorResponsePostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateBimObjectFromJsonFileParams,
) -> BimObjectFromJsonResponse | ErrorResponsePostOut | None:
    """Create a BIM object from JSON

     Upload a Speckle-compatible JSON file to create a standalone BIM object that is not attached to any
    BIM project. The object ID is recalculated from the JSON content using the Speckle hashing algorithm
    (SHA-256 truncated to 32 hex characters), ensuring the ID is a deterministic content hash.

    The uploaded file must contain a valid JSON object with at least a top-level ``id`` key. All nested
    objects that contain an ``id`` key will also have their IDs recalculated bottom-up.

    Args:
        body (CreateBimObjectFromJsonFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimObjectFromJsonResponse | ErrorResponsePostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
