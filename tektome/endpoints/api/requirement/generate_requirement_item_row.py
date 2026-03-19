from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generate_requirement_item_row_post_in import GenerateRequirementItemRowPostIn
from ...models.project_requirement_item_get_out import ProjectRequirementItemGetOut
from ...types import Response


def _get_kwargs(
    requirement_id: UUID,
    *,
    body: GenerateRequirementItemRowPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/requirements/{requirement_id}/generate-row-requirement-items/".format(
            requirement_id=quote(str(requirement_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProjectRequirementItemGetOut | None:
    if response.status_code == 200:
        response_200 = ProjectRequirementItemGetOut.from_dict(response.json())

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProjectRequirementItemGetOut]:
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
    body: GenerateRequirementItemRowPostIn,
) -> Response[Any | ProjectRequirementItemGetOut]:
    """Post Generate Row Requirement Item

     JnQkM31D

    Generate a row for requirement items based on the project data and requirement's sections and
    captures.

    Args:
        requirement_id (UUID):
        body (GenerateRequirementItemRowPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectRequirementItemGetOut]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    body: GenerateRequirementItemRowPostIn,
) -> Any | ProjectRequirementItemGetOut | None:
    """Post Generate Row Requirement Item

     JnQkM31D

    Generate a row for requirement items based on the project data and requirement's sections and
    captures.

    Args:
        requirement_id (UUID):
        body (GenerateRequirementItemRowPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectRequirementItemGetOut
    """

    return sync_detailed(
        requirement_id=requirement_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    body: GenerateRequirementItemRowPostIn,
) -> Response[Any | ProjectRequirementItemGetOut]:
    """Post Generate Row Requirement Item

     JnQkM31D

    Generate a row for requirement items based on the project data and requirement's sections and
    captures.

    Args:
        requirement_id (UUID):
        body (GenerateRequirementItemRowPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectRequirementItemGetOut]
    """

    kwargs = _get_kwargs(
        requirement_id=requirement_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    requirement_id: UUID,
    *,
    client: AuthenticatedClient,
    body: GenerateRequirementItemRowPostIn,
) -> Any | ProjectRequirementItemGetOut | None:
    """Post Generate Row Requirement Item

     JnQkM31D

    Generate a row for requirement items based on the project data and requirement's sections and
    captures.

    Args:
        requirement_id (UUID):
        body (GenerateRequirementItemRowPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectRequirementItemGetOut
    """

    return (
        await asyncio_detailed(
            requirement_id=requirement_id,
            client=client,
            body=body,
        )
    ).parsed
