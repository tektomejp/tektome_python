from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_bim_sheet_post_in import RetrieveBimSheetPostIn
from ...models.retrieve_bim_sheet_post_out import RetrieveBimSheetPostOut
from ...types import Response


def _get_kwargs(
    *,
    body: RetrieveBimSheetPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-sheet/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrieveBimSheetPostOut | None:
    if response.status_code == 200:
        response_200 = RetrieveBimSheetPostOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrieveBimSheetPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RetrieveBimSheetPostIn,
) -> Response[RetrieveBimSheetPostOut]:
    """Retrieve Bim Sheets In Project

     EmmyoTSu

    Retrieve BIM sheets within a specified project, supporting both full and paginated retrieval.

    Args:
        request: The incoming request object (explicitly ignored in this function).
        payload (RetrieveBimSheetPostIn): Input data containing retrieval options, including project ID,
            pagination parameters, flags for retrieving all sheets or only IDs, and optional field
    selection.

    Returns:
        dict: A dictionary with a single key 'data', containing either:
            - A list of sheet IDs if 'only_ids' is True.
            - A list of detailed sheet payloads if 'only_ids' is False.
            - An empty list if no results are found.

    Notes:
        - Pagination defaults to page 1 and page_size 1 if invalid values are provided.
        - Only instances of BimSheet are included in the detailed payload.
        - The response always conforms to the expected schema: {'data': [...]}

    Args:
        body (RetrieveBimSheetPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBimSheetPostOut]
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
    body: RetrieveBimSheetPostIn,
) -> RetrieveBimSheetPostOut | None:
    """Retrieve Bim Sheets In Project

     EmmyoTSu

    Retrieve BIM sheets within a specified project, supporting both full and paginated retrieval.

    Args:
        request: The incoming request object (explicitly ignored in this function).
        payload (RetrieveBimSheetPostIn): Input data containing retrieval options, including project ID,
            pagination parameters, flags for retrieving all sheets or only IDs, and optional field
    selection.

    Returns:
        dict: A dictionary with a single key 'data', containing either:
            - A list of sheet IDs if 'only_ids' is True.
            - A list of detailed sheet payloads if 'only_ids' is False.
            - An empty list if no results are found.

    Notes:
        - Pagination defaults to page 1 and page_size 1 if invalid values are provided.
        - Only instances of BimSheet are included in the detailed payload.
        - The response always conforms to the expected schema: {'data': [...]}

    Args:
        body (RetrieveBimSheetPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBimSheetPostOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RetrieveBimSheetPostIn,
) -> Response[RetrieveBimSheetPostOut]:
    """Retrieve Bim Sheets In Project

     EmmyoTSu

    Retrieve BIM sheets within a specified project, supporting both full and paginated retrieval.

    Args:
        request: The incoming request object (explicitly ignored in this function).
        payload (RetrieveBimSheetPostIn): Input data containing retrieval options, including project ID,
            pagination parameters, flags for retrieving all sheets or only IDs, and optional field
    selection.

    Returns:
        dict: A dictionary with a single key 'data', containing either:
            - A list of sheet IDs if 'only_ids' is True.
            - A list of detailed sheet payloads if 'only_ids' is False.
            - An empty list if no results are found.

    Notes:
        - Pagination defaults to page 1 and page_size 1 if invalid values are provided.
        - Only instances of BimSheet are included in the detailed payload.
        - The response always conforms to the expected schema: {'data': [...]}

    Args:
        body (RetrieveBimSheetPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBimSheetPostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RetrieveBimSheetPostIn,
) -> RetrieveBimSheetPostOut | None:
    """Retrieve Bim Sheets In Project

     EmmyoTSu

    Retrieve BIM sheets within a specified project, supporting both full and paginated retrieval.

    Args:
        request: The incoming request object (explicitly ignored in this function).
        payload (RetrieveBimSheetPostIn): Input data containing retrieval options, including project ID,
            pagination parameters, flags for retrieving all sheets or only IDs, and optional field
    selection.

    Returns:
        dict: A dictionary with a single key 'data', containing either:
            - A list of sheet IDs if 'only_ids' is True.
            - A list of detailed sheet payloads if 'only_ids' is False.
            - An empty list if no results are found.

    Notes:
        - Pagination defaults to page 1 and page_size 1 if invalid values are provided.
        - Only instances of BimSheet are included in the detailed payload.
        - The response always conforms to the expected schema: {'data': [...]}

    Args:
        body (RetrieveBimSheetPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBimSheetPostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
