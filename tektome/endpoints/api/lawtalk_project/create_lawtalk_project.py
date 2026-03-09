from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_out import ErrorOut
from ...models.lawtalk_project_post_in import LawtalkProjectPostIn
from ...models.lawtalk_project_schema import LawtalkProjectSchema
from ...types import Response


def _get_kwargs(
    *,
    body: LawtalkProjectPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/app/lawtalk/projects/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorOut | LawtalkProjectSchema | None:
    if response.status_code == 201:
        response_201 = LawtalkProjectSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorOut.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorOut.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = ErrorOut.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorOut | LawtalkProjectSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LawtalkProjectPostIn,
) -> Response[ErrorOut | LawtalkProjectSchema]:
    """Post Project

     eWe6HdkR

    Create a new project  in user's current organization.

    Attributes for all countries
    - structures
    - site_area
    - site_area_operator
    - floors_above_ground
    - floors_above_ground_operator
    - floors_below_ground
    - floors_below_ground_operator
    - height
    - height_operator
    - other_details (max 2000 characters)

    Refer to schema for country specific required fields.

    Args:
        body (LawtalkProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOut | LawtalkProjectSchema]
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
    body: LawtalkProjectPostIn,
) -> ErrorOut | LawtalkProjectSchema | None:
    """Post Project

     eWe6HdkR

    Create a new project  in user's current organization.

    Attributes for all countries
    - structures
    - site_area
    - site_area_operator
    - floors_above_ground
    - floors_above_ground_operator
    - floors_below_ground
    - floors_below_ground_operator
    - height
    - height_operator
    - other_details (max 2000 characters)

    Refer to schema for country specific required fields.

    Args:
        body (LawtalkProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOut | LawtalkProjectSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LawtalkProjectPostIn,
) -> Response[ErrorOut | LawtalkProjectSchema]:
    """Post Project

     eWe6HdkR

    Create a new project  in user's current organization.

    Attributes for all countries
    - structures
    - site_area
    - site_area_operator
    - floors_above_ground
    - floors_above_ground_operator
    - floors_below_ground
    - floors_below_ground_operator
    - height
    - height_operator
    - other_details (max 2000 characters)

    Refer to schema for country specific required fields.

    Args:
        body (LawtalkProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorOut | LawtalkProjectSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LawtalkProjectPostIn,
) -> ErrorOut | LawtalkProjectSchema | None:
    """Post Project

     eWe6HdkR

    Create a new project  in user's current organization.

    Attributes for all countries
    - structures
    - site_area
    - site_area_operator
    - floors_above_ground
    - floors_above_ground_operator
    - floors_below_ground
    - floors_below_ground_operator
    - height
    - height_operator
    - other_details (max 2000 characters)

    Refer to schema for country specific required fields.

    Args:
        body (LawtalkProjectPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorOut | LawtalkProjectSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
