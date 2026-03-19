from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_query_to_keys_values_request import BimQueryToKeysValuesRequest
from ...models.bim_query_to_keys_values_response import BimQueryToKeysValuesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bim_project_id: UUID,
    *,
    body: BimQueryToKeysValuesRequest,
    limit: int | Unset = 100,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-tools/key-value-embeddings/{bim_project_id}/query-to-keys-values/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimQueryToKeysValuesResponse | None:
    if response.status_code == 200:
        response_200 = BimQueryToKeysValuesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BimQueryToKeysValuesResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = BimQueryToKeysValuesResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = BimQueryToKeysValuesResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimQueryToKeysValuesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BimQueryToKeysValuesRequest,
    limit: int | Unset = 100,
) -> Response[BimQueryToKeysValuesResponse]:
    r"""Query To Keys Values

     4K3g3D3e

    Query BIM key-value embeddings by search terms.

    This function searches for relevant keys and values in a BIM project's embeddings
    based on a user-provided query string. It returns matching keys and values up to
    a limit of 100 results each.

    Args:
        request: The HTTP request object (unused).
        payload (BimQueryToKeysValuesIn): The query payload containing the search string.
        path (Path[BimProjectPath]): The BIM project path information.
        limit (int): Maximum number of results to return (default 100, max 1000).

    Returns:
        tuple: A tuple containing:
            - int: HTTP status code (200 on success, 404 if no embeddings found, 500 on error)
            - dict: Response dictionary with keys:
                - \"keys\" (list): List of matching key names from embeddings
                - \"values\" (list): List of matching values from embeddings
                - \"error\" (str | None): Error message if applicable, None on success

    Raises:
        BimKeyValueError: Handled internally when embeddings don't exist for the project.
        HttpError: Handled internally for HTTP-related errors during embedding search.
        Exception: Handles any unexpected errors during query processing.

    Note:
        - Returns HTTP 404 if the BIM project has no key-value embeddings
        - Returns HTTP 500 if any error occurs during processing
        - All exceptions are caught and logged via logfire
        - Search is limited to 100 results by default per query type

    Args:
        bim_project_id (UUID):
        limit (int | Unset):  Default: 100.
        body (BimQueryToKeysValuesRequest): Schema for validating BIM query input to retrieve key-
            value embeddings.

            This schema ensures that a query string is provided and non-empty before
            processing BIM key-value embedding requests.

            Attributes:
                query (str): The query string used to search or filter BIM key-value data.

            Raises:
                BimKeyValueError: If the query field is empty or not provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimQueryToKeysValuesResponse]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        body=body,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BimQueryToKeysValuesRequest,
    limit: int | Unset = 100,
) -> BimQueryToKeysValuesResponse | None:
    r"""Query To Keys Values

     4K3g3D3e

    Query BIM key-value embeddings by search terms.

    This function searches for relevant keys and values in a BIM project's embeddings
    based on a user-provided query string. It returns matching keys and values up to
    a limit of 100 results each.

    Args:
        request: The HTTP request object (unused).
        payload (BimQueryToKeysValuesIn): The query payload containing the search string.
        path (Path[BimProjectPath]): The BIM project path information.
        limit (int): Maximum number of results to return (default 100, max 1000).

    Returns:
        tuple: A tuple containing:
            - int: HTTP status code (200 on success, 404 if no embeddings found, 500 on error)
            - dict: Response dictionary with keys:
                - \"keys\" (list): List of matching key names from embeddings
                - \"values\" (list): List of matching values from embeddings
                - \"error\" (str | None): Error message if applicable, None on success

    Raises:
        BimKeyValueError: Handled internally when embeddings don't exist for the project.
        HttpError: Handled internally for HTTP-related errors during embedding search.
        Exception: Handles any unexpected errors during query processing.

    Note:
        - Returns HTTP 404 if the BIM project has no key-value embeddings
        - Returns HTTP 500 if any error occurs during processing
        - All exceptions are caught and logged via logfire
        - Search is limited to 100 results by default per query type

    Args:
        bim_project_id (UUID):
        limit (int | Unset):  Default: 100.
        body (BimQueryToKeysValuesRequest): Schema for validating BIM query input to retrieve key-
            value embeddings.

            This schema ensures that a query string is provided and non-empty before
            processing BIM key-value embedding requests.

            Attributes:
                query (str): The query string used to search or filter BIM key-value data.

            Raises:
                BimKeyValueError: If the query field is empty or not provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimQueryToKeysValuesResponse
    """

    return sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
        body=body,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BimQueryToKeysValuesRequest,
    limit: int | Unset = 100,
) -> Response[BimQueryToKeysValuesResponse]:
    r"""Query To Keys Values

     4K3g3D3e

    Query BIM key-value embeddings by search terms.

    This function searches for relevant keys and values in a BIM project's embeddings
    based on a user-provided query string. It returns matching keys and values up to
    a limit of 100 results each.

    Args:
        request: The HTTP request object (unused).
        payload (BimQueryToKeysValuesIn): The query payload containing the search string.
        path (Path[BimProjectPath]): The BIM project path information.
        limit (int): Maximum number of results to return (default 100, max 1000).

    Returns:
        tuple: A tuple containing:
            - int: HTTP status code (200 on success, 404 if no embeddings found, 500 on error)
            - dict: Response dictionary with keys:
                - \"keys\" (list): List of matching key names from embeddings
                - \"values\" (list): List of matching values from embeddings
                - \"error\" (str | None): Error message if applicable, None on success

    Raises:
        BimKeyValueError: Handled internally when embeddings don't exist for the project.
        HttpError: Handled internally for HTTP-related errors during embedding search.
        Exception: Handles any unexpected errors during query processing.

    Note:
        - Returns HTTP 404 if the BIM project has no key-value embeddings
        - Returns HTTP 500 if any error occurs during processing
        - All exceptions are caught and logged via logfire
        - Search is limited to 100 results by default per query type

    Args:
        bim_project_id (UUID):
        limit (int | Unset):  Default: 100.
        body (BimQueryToKeysValuesRequest): Schema for validating BIM query input to retrieve key-
            value embeddings.

            This schema ensures that a query string is provided and non-empty before
            processing BIM key-value embedding requests.

            Attributes:
                query (str): The query string used to search or filter BIM key-value data.

            Raises:
                BimKeyValueError: If the query field is empty or not provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimQueryToKeysValuesResponse]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        body=body,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BimQueryToKeysValuesRequest,
    limit: int | Unset = 100,
) -> BimQueryToKeysValuesResponse | None:
    r"""Query To Keys Values

     4K3g3D3e

    Query BIM key-value embeddings by search terms.

    This function searches for relevant keys and values in a BIM project's embeddings
    based on a user-provided query string. It returns matching keys and values up to
    a limit of 100 results each.

    Args:
        request: The HTTP request object (unused).
        payload (BimQueryToKeysValuesIn): The query payload containing the search string.
        path (Path[BimProjectPath]): The BIM project path information.
        limit (int): Maximum number of results to return (default 100, max 1000).

    Returns:
        tuple: A tuple containing:
            - int: HTTP status code (200 on success, 404 if no embeddings found, 500 on error)
            - dict: Response dictionary with keys:
                - \"keys\" (list): List of matching key names from embeddings
                - \"values\" (list): List of matching values from embeddings
                - \"error\" (str | None): Error message if applicable, None on success

    Raises:
        BimKeyValueError: Handled internally when embeddings don't exist for the project.
        HttpError: Handled internally for HTTP-related errors during embedding search.
        Exception: Handles any unexpected errors during query processing.

    Note:
        - Returns HTTP 404 if the BIM project has no key-value embeddings
        - Returns HTTP 500 if any error occurs during processing
        - All exceptions are caught and logged via logfire
        - Search is limited to 100 results by default per query type

    Args:
        bim_project_id (UUID):
        limit (int | Unset):  Default: 100.
        body (BimQueryToKeysValuesRequest): Schema for validating BIM query input to retrieve key-
            value embeddings.

            This schema ensures that a query string is provided and non-empty before
            processing BIM key-value embedding requests.

            Attributes:
                query (str): The query string used to search or filter BIM key-value data.

            Raises:
                BimKeyValueError: If the query field is empty or not provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimQueryToKeysValuesResponse
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            client=client,
            body=body,
            limit=limit,
        )
    ).parsed
