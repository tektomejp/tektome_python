from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_requirement_items_response_200_type_1 import GetRequirementItemsResponse200Type1
from ...models.project_requirement_item_table_response import ProjectRequirementItemTableResponse
from ...types import Response


def _get_kwargs(
    requirement_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/app/lawtalk/requirements/{requirement_id}/requirement-items/".format(
            requirement_id=quote(str(requirement_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRequirementItemsResponse200Type1 | ProjectRequirementItemTableResponse | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> GetRequirementItemsResponse200Type1 | ProjectRequirementItemTableResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ProjectRequirementItemTableResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = GetRequirementItemsResponse200Type1.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetRequirementItemsResponse200Type1 | ProjectRequirementItemTableResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[GetRequirementItemsResponse200Type1 | ProjectRequirementItemTableResponse]:
    """Get requirement items

     Retrieve the requirement items table associated with a requirement.

    Args:
        requirement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRequirementItemsResponse200Type1 | ProjectRequirementItemTableResponse]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
) -> GetRequirementItemsResponse200Type1 | ProjectRequirementItemTableResponse | None:
    """Get requirement items

     Retrieve the requirement items table associated with a requirement.

    Args:
        requirement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRequirementItemsResponse200Type1 | ProjectRequirementItemTableResponse
    """

    return sync_detailed(
        requirement_id=requirement_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[GetRequirementItemsResponse200Type1 | ProjectRequirementItemTableResponse]:
    """Get requirement items

     Retrieve the requirement items table associated with a requirement.

    Args:
        requirement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRequirementItemsResponse200Type1 | ProjectRequirementItemTableResponse]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
) -> GetRequirementItemsResponse200Type1 | ProjectRequirementItemTableResponse | None:
    """Get requirement items

     Retrieve the requirement items table associated with a requirement.

    Args:
        requirement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRequirementItemsResponse200Type1 | ProjectRequirementItemTableResponse
    """

    return (
        await asyncio_detailed(
            requirement_id=requirement_id,
            client=client,
        )
    ).parsed
