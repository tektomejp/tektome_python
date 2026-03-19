from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bim_object_post_out import BimObjectPostOut
from ...models.bim_view_object_link_post_out import BimViewObjectLinkPostOut
from ...models.bim_view_post_out import BimViewPostOut
from ...models.create_bim_element_bim_element_type_path import CreateBimElementBimElementTypePath
from ...models.create_bim_element_file_params import CreateBimElementFileParams
from ...models.error_response_post_out import ErrorResponsePostOut
from ...types import Response


def _get_kwargs(
    bim_project_id: UUID,
    bim_type: CreateBimElementBimElementTypePath,
    *,
    body: CreateBimElementFileParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/resource-groups/bim/bim-project/{bim_project_id}/{bim_type}/".format(
            bim_project_id=quote(str(bim_project_id), safe=""),
            bim_type=quote(str(bim_type), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BimObjectPostOut | BimViewObjectLinkPostOut | BimViewPostOut | ErrorResponsePostOut | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> BimObjectPostOut | BimViewObjectLinkPostOut | BimViewPostOut:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = BimObjectPostOut.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = BimViewPostOut.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = BimViewObjectLinkPostOut.from_dict(data)

            return response_200_type_2

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponsePostOut.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponsePostOut.from_dict(response.json())

        return response_404

    if response.status_code == 501:
        response_501 = ErrorResponsePostOut.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BimObjectPostOut | BimViewObjectLinkPostOut | BimViewPostOut | ErrorResponsePostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bim_project_id: UUID,
    bim_type: CreateBimElementBimElementTypePath,
    *,
    client: AuthenticatedClient,
    body: CreateBimElementFileParams,
) -> Response[BimObjectPostOut | BimViewObjectLinkPostOut | BimViewPostOut | ErrorResponsePostOut]:
    """Post Bim Element Handler

     1lv861wz

    Post a BIM element. Could be BIM object, BIM view, or agnostically wherein the handler will try to
    determine the type of the element submitted.

    Args:
        bim_project_id (UUID):
        bim_type (CreateBimElementBimElementTypePath): Enum for BIM object types.
        body (CreateBimElementFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimObjectPostOut | BimViewObjectLinkPostOut | BimViewPostOut | ErrorResponsePostOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        bim_type=bim_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bim_project_id: UUID,
    bim_type: CreateBimElementBimElementTypePath,
    *,
    client: AuthenticatedClient,
    body: CreateBimElementFileParams,
) -> BimObjectPostOut | BimViewObjectLinkPostOut | BimViewPostOut | ErrorResponsePostOut | None:
    """Post Bim Element Handler

     1lv861wz

    Post a BIM element. Could be BIM object, BIM view, or agnostically wherein the handler will try to
    determine the type of the element submitted.

    Args:
        bim_project_id (UUID):
        bim_type (CreateBimElementBimElementTypePath): Enum for BIM object types.
        body (CreateBimElementFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimObjectPostOut | BimViewObjectLinkPostOut | BimViewPostOut | ErrorResponsePostOut
    """

    return sync_detailed(
        bim_project_id=bim_project_id,
        bim_type=bim_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    bim_project_id: UUID,
    bim_type: CreateBimElementBimElementTypePath,
    *,
    client: AuthenticatedClient,
    body: CreateBimElementFileParams,
) -> Response[BimObjectPostOut | BimViewObjectLinkPostOut | BimViewPostOut | ErrorResponsePostOut]:
    """Post Bim Element Handler

     1lv861wz

    Post a BIM element. Could be BIM object, BIM view, or agnostically wherein the handler will try to
    determine the type of the element submitted.

    Args:
        bim_project_id (UUID):
        bim_type (CreateBimElementBimElementTypePath): Enum for BIM object types.
        body (CreateBimElementFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BimObjectPostOut | BimViewObjectLinkPostOut | BimViewPostOut | ErrorResponsePostOut]
    """

    kwargs = _get_kwargs(
        bim_project_id=bim_project_id,
        bim_type=bim_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bim_project_id: UUID,
    bim_type: CreateBimElementBimElementTypePath,
    *,
    client: AuthenticatedClient,
    body: CreateBimElementFileParams,
) -> BimObjectPostOut | BimViewObjectLinkPostOut | BimViewPostOut | ErrorResponsePostOut | None:
    """Post Bim Element Handler

     1lv861wz

    Post a BIM element. Could be BIM object, BIM view, or agnostically wherein the handler will try to
    determine the type of the element submitted.

    Args:
        bim_project_id (UUID):
        bim_type (CreateBimElementBimElementTypePath): Enum for BIM object types.
        body (CreateBimElementFileParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BimObjectPostOut | BimViewObjectLinkPostOut | BimViewPostOut | ErrorResponsePostOut
    """

    return (
        await asyncio_detailed(
            bim_project_id=bim_project_id,
            bim_type=bim_type,
            client=client,
            body=body,
        )
    ).parsed
