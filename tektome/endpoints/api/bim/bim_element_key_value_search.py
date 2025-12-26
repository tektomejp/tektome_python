from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_element_key_value_search_bim_element_type_v2_path import BimElementKeyValueSearchBimElementTypeV2Path
from ...models.bim_key_value_search_post_in import BimKeyValueSearchPostIn
from ...models.bim_key_value_search_result_post_out import BimKeyValueSearchResultPostOut
from ...types import UNSET, Response


def _get_kwargs(
    bim_element: BimElementKeyValueSearchBimElementTypeV2Path,
    *,
    body: BimKeyValueSearchPostIn,
    bim_project_id: UUID,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_bim_project_id = str(bim_project_id)
    params["bim_project_id"] = json_bim_project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-search/kv-search/{bim_element}/".format(
            bim_element=quote(str(bim_element), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimKeyValueSearchResultPostOut | None:
    if response.status_code == 200:
        response_200 = BimKeyValueSearchResultPostOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimKeyValueSearchResultPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_element: BimElementKeyValueSearchBimElementTypeV2Path,
    *,
    client: AuthenticatedClient,
    body: BimKeyValueSearchPostIn,
    bim_project_id: UUID,
) -> Response[BimKeyValueSearchResultPostOut]:
    r"""Bim Element Key Value Search

     Nh2cP7IZ

    Search BIM elements within a project for entries containing a specific key-value pair.

    This endpoint performs case-sensitive search on BIM element JSON content stored in
    Elasticsearch. It supports both exact matching and wildcard patterns using '*' character.

    Supported BIM element types: bim-object, bim-view, bim-sheet

    Wildcard Pattern Support:
    - Use '*' in key to match any key name (e.g., key=\"*\" matches any key)
    - Use '*' in value to match partial values (e.g., value=\"玄関*\" matches values starting with \"玄関\")
    - Combine wildcards (e.g., key=\"*\", value=\"*扉*\" matches any key with values containing \"扉\")

    Search Process:
    1. Selects the appropriate Elasticsearch document class based on bim_element type
    2. Constructs an Elasticsearch query filtering by project ID
    3. Uses match_phrase queries for exact JSON key-value pattern matching
    4. Executes paginated search against the selected document index
    5. Processes each hit to extract only the requested fields from the JSON content
    6. Returns structured results with field filtering and pagination metadata

    Field Extraction:
    - If 'fields' is provided in payload: extracts only those specified fields
    - If 'fields' is not provided: defaults to extracting only 'id' field
    - Supports nested field paths using dot notation (e.g., \"geometry.location.x\")
    - Always includes the Elasticsearch document ID in the response
    - Handles malformed JSON gracefully by falling back to empty data

    Args:
        request: Django request object (unused)
        payload: Search parameters including key, value, optional fields, and pagination
        bim_project_id: UUID of the BIM project to search within
        bim_element: Type of BIM element to search (bim-object, bim-view, or bim-sheet)

    Returns:
        BimKeyValueSearchResultPostOut: Paginated search results containing:
            - results: List of matching elements with requested fields
            - total: Total number of matching documents
            - page: Current page number
            - page_size: Number of results per page

    Examples:
        1. Search BIM objects for exact match:
        POST /api/bim/{project_id}/kv-search/bim-object/
        {
            \"key\": \"material\",
            \"value\": \"concrete\",
            \"fields\": [\"id\", \"geometry.height\", \"properties.color\"]
        }

        2. Search BIM views for wildcard key:
        POST /api/bim/{project_id}/kv-search/bim-view/
        {
            \"key\": \"*\",
            \"value\": \"玄関扉DW\",
            \"fields\": [\"id\", \"name\"]
        }

        3. Search BIM sheets for partial value match:
        POST /api/bim/{project_id}/kv-search/bim-sheet/
        {
            \"key\": \"name\",
            \"value\": \"玄関*\",
            \"fields\": [\"id\", \"name\"]
        }

    Args:
        bim_element (BimElementKeyValueSearchBimElementTypeV2Path): An enumeration representing
            different BIM (Building Information Modeling) element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element
            type.
        bim_project_id (UUID):
        body (BimKeyValueSearchPostIn): Schema for key-value search in BIM file_content JSON.

            Supports wildcard patterns using '*':
            - key="*" matches any key name
            - value="prefix*" matches values starting with "prefix"
            - value="*suffix" matches values ending with "suffix"
            - value="*middle*" matches values containing "middle"

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimKeyValueSearchResultPostOut]
    """

    kwargs = _get_kwargs(
        bim_element=bim_element,
        body=body,
        bim_project_id=bim_project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_element: BimElementKeyValueSearchBimElementTypeV2Path,
    *,
    client: AuthenticatedClient,
    body: BimKeyValueSearchPostIn,
    bim_project_id: UUID,
) -> BimKeyValueSearchResultPostOut | None:
    r"""Bim Element Key Value Search

     Nh2cP7IZ

    Search BIM elements within a project for entries containing a specific key-value pair.

    This endpoint performs case-sensitive search on BIM element JSON content stored in
    Elasticsearch. It supports both exact matching and wildcard patterns using '*' character.

    Supported BIM element types: bim-object, bim-view, bim-sheet

    Wildcard Pattern Support:
    - Use '*' in key to match any key name (e.g., key=\"*\" matches any key)
    - Use '*' in value to match partial values (e.g., value=\"玄関*\" matches values starting with \"玄関\")
    - Combine wildcards (e.g., key=\"*\", value=\"*扉*\" matches any key with values containing \"扉\")

    Search Process:
    1. Selects the appropriate Elasticsearch document class based on bim_element type
    2. Constructs an Elasticsearch query filtering by project ID
    3. Uses match_phrase queries for exact JSON key-value pattern matching
    4. Executes paginated search against the selected document index
    5. Processes each hit to extract only the requested fields from the JSON content
    6. Returns structured results with field filtering and pagination metadata

    Field Extraction:
    - If 'fields' is provided in payload: extracts only those specified fields
    - If 'fields' is not provided: defaults to extracting only 'id' field
    - Supports nested field paths using dot notation (e.g., \"geometry.location.x\")
    - Always includes the Elasticsearch document ID in the response
    - Handles malformed JSON gracefully by falling back to empty data

    Args:
        request: Django request object (unused)
        payload: Search parameters including key, value, optional fields, and pagination
        bim_project_id: UUID of the BIM project to search within
        bim_element: Type of BIM element to search (bim-object, bim-view, or bim-sheet)

    Returns:
        BimKeyValueSearchResultPostOut: Paginated search results containing:
            - results: List of matching elements with requested fields
            - total: Total number of matching documents
            - page: Current page number
            - page_size: Number of results per page

    Examples:
        1. Search BIM objects for exact match:
        POST /api/bim/{project_id}/kv-search/bim-object/
        {
            \"key\": \"material\",
            \"value\": \"concrete\",
            \"fields\": [\"id\", \"geometry.height\", \"properties.color\"]
        }

        2. Search BIM views for wildcard key:
        POST /api/bim/{project_id}/kv-search/bim-view/
        {
            \"key\": \"*\",
            \"value\": \"玄関扉DW\",
            \"fields\": [\"id\", \"name\"]
        }

        3. Search BIM sheets for partial value match:
        POST /api/bim/{project_id}/kv-search/bim-sheet/
        {
            \"key\": \"name\",
            \"value\": \"玄関*\",
            \"fields\": [\"id\", \"name\"]
        }

    Args:
        bim_element (BimElementKeyValueSearchBimElementTypeV2Path): An enumeration representing
            different BIM (Building Information Modeling) element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element
            type.
        bim_project_id (UUID):
        body (BimKeyValueSearchPostIn): Schema for key-value search in BIM file_content JSON.

            Supports wildcard patterns using '*':
            - key="*" matches any key name
            - value="prefix*" matches values starting with "prefix"
            - value="*suffix" matches values ending with "suffix"
            - value="*middle*" matches values containing "middle"

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimKeyValueSearchResultPostOut
    """

    return sync_detailed(
        bim_element=bim_element,
        client=client,
        body=body,
        bim_project_id=bim_project_id,
    ).parsed


async def asyncio_detailed(
    bim_element: BimElementKeyValueSearchBimElementTypeV2Path,
    *,
    client: AuthenticatedClient,
    body: BimKeyValueSearchPostIn,
    bim_project_id: UUID,
) -> Response[BimKeyValueSearchResultPostOut]:
    r"""Bim Element Key Value Search

     Nh2cP7IZ

    Search BIM elements within a project for entries containing a specific key-value pair.

    This endpoint performs case-sensitive search on BIM element JSON content stored in
    Elasticsearch. It supports both exact matching and wildcard patterns using '*' character.

    Supported BIM element types: bim-object, bim-view, bim-sheet

    Wildcard Pattern Support:
    - Use '*' in key to match any key name (e.g., key=\"*\" matches any key)
    - Use '*' in value to match partial values (e.g., value=\"玄関*\" matches values starting with \"玄関\")
    - Combine wildcards (e.g., key=\"*\", value=\"*扉*\" matches any key with values containing \"扉\")

    Search Process:
    1. Selects the appropriate Elasticsearch document class based on bim_element type
    2. Constructs an Elasticsearch query filtering by project ID
    3. Uses match_phrase queries for exact JSON key-value pattern matching
    4. Executes paginated search against the selected document index
    5. Processes each hit to extract only the requested fields from the JSON content
    6. Returns structured results with field filtering and pagination metadata

    Field Extraction:
    - If 'fields' is provided in payload: extracts only those specified fields
    - If 'fields' is not provided: defaults to extracting only 'id' field
    - Supports nested field paths using dot notation (e.g., \"geometry.location.x\")
    - Always includes the Elasticsearch document ID in the response
    - Handles malformed JSON gracefully by falling back to empty data

    Args:
        request: Django request object (unused)
        payload: Search parameters including key, value, optional fields, and pagination
        bim_project_id: UUID of the BIM project to search within
        bim_element: Type of BIM element to search (bim-object, bim-view, or bim-sheet)

    Returns:
        BimKeyValueSearchResultPostOut: Paginated search results containing:
            - results: List of matching elements with requested fields
            - total: Total number of matching documents
            - page: Current page number
            - page_size: Number of results per page

    Examples:
        1. Search BIM objects for exact match:
        POST /api/bim/{project_id}/kv-search/bim-object/
        {
            \"key\": \"material\",
            \"value\": \"concrete\",
            \"fields\": [\"id\", \"geometry.height\", \"properties.color\"]
        }

        2. Search BIM views for wildcard key:
        POST /api/bim/{project_id}/kv-search/bim-view/
        {
            \"key\": \"*\",
            \"value\": \"玄関扉DW\",
            \"fields\": [\"id\", \"name\"]
        }

        3. Search BIM sheets for partial value match:
        POST /api/bim/{project_id}/kv-search/bim-sheet/
        {
            \"key\": \"name\",
            \"value\": \"玄関*\",
            \"fields\": [\"id\", \"name\"]
        }

    Args:
        bim_element (BimElementKeyValueSearchBimElementTypeV2Path): An enumeration representing
            different BIM (Building Information Modeling) element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element
            type.
        bim_project_id (UUID):
        body (BimKeyValueSearchPostIn): Schema for key-value search in BIM file_content JSON.

            Supports wildcard patterns using '*':
            - key="*" matches any key name
            - value="prefix*" matches values starting with "prefix"
            - value="*suffix" matches values ending with "suffix"
            - value="*middle*" matches values containing "middle"

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimKeyValueSearchResultPostOut]
    """

    kwargs = _get_kwargs(
        bim_element=bim_element,
        body=body,
        bim_project_id=bim_project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_element: BimElementKeyValueSearchBimElementTypeV2Path,
    *,
    client: AuthenticatedClient,
    body: BimKeyValueSearchPostIn,
    bim_project_id: UUID,
) -> BimKeyValueSearchResultPostOut | None:
    r"""Bim Element Key Value Search

     Nh2cP7IZ

    Search BIM elements within a project for entries containing a specific key-value pair.

    This endpoint performs case-sensitive search on BIM element JSON content stored in
    Elasticsearch. It supports both exact matching and wildcard patterns using '*' character.

    Supported BIM element types: bim-object, bim-view, bim-sheet

    Wildcard Pattern Support:
    - Use '*' in key to match any key name (e.g., key=\"*\" matches any key)
    - Use '*' in value to match partial values (e.g., value=\"玄関*\" matches values starting with \"玄関\")
    - Combine wildcards (e.g., key=\"*\", value=\"*扉*\" matches any key with values containing \"扉\")

    Search Process:
    1. Selects the appropriate Elasticsearch document class based on bim_element type
    2. Constructs an Elasticsearch query filtering by project ID
    3. Uses match_phrase queries for exact JSON key-value pattern matching
    4. Executes paginated search against the selected document index
    5. Processes each hit to extract only the requested fields from the JSON content
    6. Returns structured results with field filtering and pagination metadata

    Field Extraction:
    - If 'fields' is provided in payload: extracts only those specified fields
    - If 'fields' is not provided: defaults to extracting only 'id' field
    - Supports nested field paths using dot notation (e.g., \"geometry.location.x\")
    - Always includes the Elasticsearch document ID in the response
    - Handles malformed JSON gracefully by falling back to empty data

    Args:
        request: Django request object (unused)
        payload: Search parameters including key, value, optional fields, and pagination
        bim_project_id: UUID of the BIM project to search within
        bim_element: Type of BIM element to search (bim-object, bim-view, or bim-sheet)

    Returns:
        BimKeyValueSearchResultPostOut: Paginated search results containing:
            - results: List of matching elements with requested fields
            - total: Total number of matching documents
            - page: Current page number
            - page_size: Number of results per page

    Examples:
        1. Search BIM objects for exact match:
        POST /api/bim/{project_id}/kv-search/bim-object/
        {
            \"key\": \"material\",
            \"value\": \"concrete\",
            \"fields\": [\"id\", \"geometry.height\", \"properties.color\"]
        }

        2. Search BIM views for wildcard key:
        POST /api/bim/{project_id}/kv-search/bim-view/
        {
            \"key\": \"*\",
            \"value\": \"玄関扉DW\",
            \"fields\": [\"id\", \"name\"]
        }

        3. Search BIM sheets for partial value match:
        POST /api/bim/{project_id}/kv-search/bim-sheet/
        {
            \"key\": \"name\",
            \"value\": \"玄関*\",
            \"fields\": [\"id\", \"name\"]
        }

    Args:
        bim_element (BimElementKeyValueSearchBimElementTypeV2Path): An enumeration representing
            different BIM (Building Information Modeling) element types for V2 API paths.

            Attributes:
                OBJECT (str): Represents a BIM object element type, mapped to the string "bim-object".
                VIEW (str): Represents a BIM view element type, mapped to the string "bim-view".
                SHEET (str): Represents a BIM sheet element type, mapped to the string "bim-sheet".

            Methods:
                resolve_bim_element_class(bim_element):
                    Resolves and returns the corresponding document class for a given BIM element
            type.
        bim_project_id (UUID):
        body (BimKeyValueSearchPostIn): Schema for key-value search in BIM file_content JSON.

            Supports wildcard patterns using '*':
            - key="*" matches any key name
            - value="prefix*" matches values starting with "prefix"
            - value="*suffix" matches values ending with "suffix"
            - value="*middle*" matches values containing "middle"

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimKeyValueSearchResultPostOut
    """

    return (
        await asyncio_detailed(
            bim_element=bim_element,
            client=client,
            body=body,
            bim_project_id=bim_project_id,
        )
    ).parsed
