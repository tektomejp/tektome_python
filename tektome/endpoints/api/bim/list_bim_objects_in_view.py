from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_bim_objects_in_view_post_in import RetrieveBimObjectsInViewPostIn
from ...models.retrieve_bim_objects_in_view_post_out import RetrieveBimObjectsInViewPostOut
from ...types import Response


def _get_kwargs(
    bim_view_id: str,
    *,
    body: RetrieveBimObjectsInViewPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-view/{bim_view_id}/objects/".format(
            bim_view_id=quote(str(bim_view_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrieveBimObjectsInViewPostOut | None:
    if response.status_code == 200:
        response_200 = RetrieveBimObjectsInViewPostOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrieveBimObjectsInViewPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_view_id: str,
    *,
    client: AuthenticatedClient,
    body: RetrieveBimObjectsInViewPostIn,
) -> Response[RetrieveBimObjectsInViewPostOut]:
    """Get Bim Objects In View

     G6TIUvXn

    Retrieves BIM objects that intersect with a specified BIM view.

    Args:
        request: The HTTP request object (unused).
        bim_view_id (str): The identifier of the BIM view to query.
        payload (RetrieveBimObjectsInViewPostIn): Parameters for the retrieval, including project ID,
            pagination options, and flags for returning only IDs or all objects at once.

    Returns:
        dict: A dictionary containing the BIM objects data. The format depends on the payload options:
            - If `all_at_once` and `only_ids` are True, returns a list of object IDs.
            - If `all_at_once` is True, returns a list of full object dictionaries.
            - Otherwise, returns paginated results as IDs or full object dictionaries.

    Raises:
        HttpError: If the BIM view is not found, no objects are found, or an internal error occurs.

    Args:
        bim_view_id (str):
        body (RetrieveBimObjectsInViewPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBimObjectsInViewPostOut]
    """

    kwargs = _get_kwargs(
        bim_view_id=bim_view_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_view_id: str,
    *,
    client: AuthenticatedClient,
    body: RetrieveBimObjectsInViewPostIn,
) -> RetrieveBimObjectsInViewPostOut | None:
    """Get Bim Objects In View

     G6TIUvXn

    Retrieves BIM objects that intersect with a specified BIM view.

    Args:
        request: The HTTP request object (unused).
        bim_view_id (str): The identifier of the BIM view to query.
        payload (RetrieveBimObjectsInViewPostIn): Parameters for the retrieval, including project ID,
            pagination options, and flags for returning only IDs or all objects at once.

    Returns:
        dict: A dictionary containing the BIM objects data. The format depends on the payload options:
            - If `all_at_once` and `only_ids` are True, returns a list of object IDs.
            - If `all_at_once` is True, returns a list of full object dictionaries.
            - Otherwise, returns paginated results as IDs or full object dictionaries.

    Raises:
        HttpError: If the BIM view is not found, no objects are found, or an internal error occurs.

    Args:
        bim_view_id (str):
        body (RetrieveBimObjectsInViewPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBimObjectsInViewPostOut
    """

    return sync_detailed(
        bim_view_id=bim_view_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    bim_view_id: str,
    *,
    client: AuthenticatedClient,
    body: RetrieveBimObjectsInViewPostIn,
) -> Response[RetrieveBimObjectsInViewPostOut]:
    """Get Bim Objects In View

     G6TIUvXn

    Retrieves BIM objects that intersect with a specified BIM view.

    Args:
        request: The HTTP request object (unused).
        bim_view_id (str): The identifier of the BIM view to query.
        payload (RetrieveBimObjectsInViewPostIn): Parameters for the retrieval, including project ID,
            pagination options, and flags for returning only IDs or all objects at once.

    Returns:
        dict: A dictionary containing the BIM objects data. The format depends on the payload options:
            - If `all_at_once` and `only_ids` are True, returns a list of object IDs.
            - If `all_at_once` is True, returns a list of full object dictionaries.
            - Otherwise, returns paginated results as IDs or full object dictionaries.

    Raises:
        HttpError: If the BIM view is not found, no objects are found, or an internal error occurs.

    Args:
        bim_view_id (str):
        body (RetrieveBimObjectsInViewPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBimObjectsInViewPostOut]
    """

    kwargs = _get_kwargs(
        bim_view_id=bim_view_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_view_id: str,
    *,
    client: AuthenticatedClient,
    body: RetrieveBimObjectsInViewPostIn,
) -> RetrieveBimObjectsInViewPostOut | None:
    """Get Bim Objects In View

     G6TIUvXn

    Retrieves BIM objects that intersect with a specified BIM view.

    Args:
        request: The HTTP request object (unused).
        bim_view_id (str): The identifier of the BIM view to query.
        payload (RetrieveBimObjectsInViewPostIn): Parameters for the retrieval, including project ID,
            pagination options, and flags for returning only IDs or all objects at once.

    Returns:
        dict: A dictionary containing the BIM objects data. The format depends on the payload options:
            - If `all_at_once` and `only_ids` are True, returns a list of object IDs.
            - If `all_at_once` is True, returns a list of full object dictionaries.
            - Otherwise, returns paginated results as IDs or full object dictionaries.

    Raises:
        HttpError: If the BIM view is not found, no objects are found, or an internal error occurs.

    Args:
        bim_view_id (str):
        body (RetrieveBimObjectsInViewPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBimObjectsInViewPostOut
    """

    return (
        await asyncio_detailed(
            bim_view_id=bim_view_id,
            client=client,
            body=body,
        )
    ).parsed
