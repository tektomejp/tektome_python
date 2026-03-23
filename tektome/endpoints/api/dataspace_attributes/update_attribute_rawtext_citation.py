from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.raw_text_citation_patch_in_patch import RawTextCitationPatchInPatch
from ...models.raw_text_citation_schema_out import RawTextCitationSchemaOut
from ...types import Response


def _get_kwargs(
    dataspace_id: UUID,
    attribute_id: UUID,
    rawtext_citation_id: UUID,
    *,
    body: RawTextCitationPatchInPatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/dataspaces/{dataspace_id}/attributes/{attribute_id}/rawtext-citations/{rawtext_citation_id}/".format(
            dataspace_id=quote(str(dataspace_id), safe=""),
            attribute_id=quote(str(attribute_id), safe=""),
            rawtext_citation_id=quote(str(rawtext_citation_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RawTextCitationSchemaOut | None:
    if response.status_code == 200:
        response_200 = RawTextCitationSchemaOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RawTextCitationSchemaOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataspace_id: UUID,
    attribute_id: UUID,
    rawtext_citation_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RawTextCitationPatchInPatch,
) -> Response[RawTextCitationSchemaOut]:
    """Patch Attribute Rawtext Citation

     uuaZgMa1

    Patch RawText citation given its ID.

    Args:
        dataspace_id (UUID):
        attribute_id (UUID):
        rawtext_citation_id (UUID):
        body (RawTextCitationPatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RawTextCitationSchemaOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        attribute_id=attribute_id,
        rawtext_citation_id=rawtext_citation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataspace_id: UUID,
    attribute_id: UUID,
    rawtext_citation_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RawTextCitationPatchInPatch,
) -> RawTextCitationSchemaOut | None:
    """Patch Attribute Rawtext Citation

     uuaZgMa1

    Patch RawText citation given its ID.

    Args:
        dataspace_id (UUID):
        attribute_id (UUID):
        rawtext_citation_id (UUID):
        body (RawTextCitationPatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RawTextCitationSchemaOut
    """

    return sync_detailed(
        dataspace_id=dataspace_id,
        attribute_id=attribute_id,
        rawtext_citation_id=rawtext_citation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataspace_id: UUID,
    attribute_id: UUID,
    rawtext_citation_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RawTextCitationPatchInPatch,
) -> Response[RawTextCitationSchemaOut]:
    """Patch Attribute Rawtext Citation

     uuaZgMa1

    Patch RawText citation given its ID.

    Args:
        dataspace_id (UUID):
        attribute_id (UUID):
        rawtext_citation_id (UUID):
        body (RawTextCitationPatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RawTextCitationSchemaOut]
    """

    kwargs = _get_kwargs(
        dataspace_id=dataspace_id,
        attribute_id=attribute_id,
        rawtext_citation_id=rawtext_citation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataspace_id: UUID,
    attribute_id: UUID,
    rawtext_citation_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RawTextCitationPatchInPatch,
) -> RawTextCitationSchemaOut | None:
    """Patch Attribute Rawtext Citation

     uuaZgMa1

    Patch RawText citation given its ID.

    Args:
        dataspace_id (UUID):
        attribute_id (UUID):
        rawtext_citation_id (UUID):
        body (RawTextCitationPatchInPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RawTextCitationSchemaOut
    """

    return (
        await asyncio_detailed(
            dataspace_id=dataspace_id,
            attribute_id=attribute_id,
            rawtext_citation_id=rawtext_citation_id,
            client=client,
            body=body,
        )
    ).parsed
