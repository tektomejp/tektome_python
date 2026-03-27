from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_element_link_parent_children import BimElementLinkParentChildren
from ...types import Response


def _get_kwargs(
    bim_element_type: str,
    *,
    body: list[BimElementLinkParentChildren],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-elements/{bim_element_type}/link-parent-children/".format(
            bim_element_type=quote(str(bim_element_type), safe=""),
        ),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_element_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: list[BimElementLinkParentChildren],
) -> Response[str]:
    """Link BIM element parent-child relationships

     Establish parent-child relationships between BIM elements. This is an asynchronous operation. To
    retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the
    task/process ID returned in this response.

    Args:
        bim_element_type (str):
        body (list[BimElementLinkParentChildren]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        bim_element_type=bim_element_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_element_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: list[BimElementLinkParentChildren],
) -> str | None:
    """Link BIM element parent-child relationships

     Establish parent-child relationships between BIM elements. This is an asynchronous operation. To
    retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the
    task/process ID returned in this response.

    Args:
        bim_element_type (str):
        body (list[BimElementLinkParentChildren]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        bim_element_type=bim_element_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    bim_element_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: list[BimElementLinkParentChildren],
) -> Response[str]:
    """Link BIM element parent-child relationships

     Establish parent-child relationships between BIM elements. This is an asynchronous operation. To
    retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the
    task/process ID returned in this response.

    Args:
        bim_element_type (str):
        body (list[BimElementLinkParentChildren]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        bim_element_type=bim_element_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_element_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: list[BimElementLinkParentChildren],
) -> str | None:
    """Link BIM element parent-child relationships

     Establish parent-child relationships between BIM elements. This is an asynchronous operation. To
    retrieve the results, use the get_celery_task (/api/core/tasks/{task_id}/) endpoint with the
    task/process ID returned in this response.

    Args:
        bim_element_type (str):
        body (list[BimElementLinkParentChildren]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            bim_element_type=bim_element_type,
            client=client,
            body=body,
        )
    ).parsed
