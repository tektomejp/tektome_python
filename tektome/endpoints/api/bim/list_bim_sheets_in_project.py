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
    """List BIM sheets in a project

     Retrieve BIM sheets within a project, supporting both full retrieval and paginated queries.
    Optionally return only sheet IDs.

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
    """List BIM sheets in a project

     Retrieve BIM sheets within a project, supporting both full retrieval and paginated queries.
    Optionally return only sheet IDs.

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
    """List BIM sheets in a project

     Retrieve BIM sheets within a project, supporting both full retrieval and paginated queries.
    Optionally return only sheet IDs.

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
    """List BIM sheets in a project

     Retrieve BIM sheets within a project, supporting both full retrieval and paginated queries.
    Optionally return only sheet IDs.

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
