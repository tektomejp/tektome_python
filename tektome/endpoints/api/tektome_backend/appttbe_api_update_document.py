from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_project_update import DocumentProjectUpdate
from ...types import Response


def _get_kwargs(
    *,
    body: DocumentProjectUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/app/tektomebe/v1/document/update/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DocumentProjectUpdate,
) -> Response[Any]:
    r"""Update Document

         Update the project_id of a document in the vector database and Azure Search.
        TODO:
        - possible bug
        - call https://tektome.postman.co/workspace/tektome~f85cbc2b-55e1-48fe-8824-
    4e6ca228b024/request/37568547-fd6911d6-3d36-46ac-9398-4618c11a4b94?action=share&source=copy-
    link&creator=37568547&ctx=documentation
        - then call https://tektome.postman.co/workspace/tektome~f85cbc2b-55e1-48fe-8824-
    4e6ca228b024/request/37568547-7ac588a1-91ee-478e-af41-0d0711d5fd21?action=share&source=copy-
    link&creator=37568547&ctx=documentation
        {
            \"message\": [
                \"Document updated in page search index\",
                \"Document updated in chunk group search index\",
                \"Document moved in storage\"
            ],
            \"error\": [
                \"Failed to update document in attribute search index: (MissingRequiredParameter) The
    request is invalid. Details: actions : No indexing actions found in the request. Please include
    between 1 and 32000 indexing actions in your request.
    Code: MissingRequiredParameter
    Message: The request is invalid. Details: actions : No indexing actions found in the request. Please
    include between 1 and 32000 indexing actions in your request.
    Exception Details:      (MissingIndexDocumentsActions) No indexing actions found in the request.
    Please include between 1 and 32000 indexing actions in your request. Parameters: actions
            Code: MissingIndexDocumentsActions
            Message: No indexing actions found in the request. Please include between 1 and 32000
    indexing actions in your request. Parameters: actions\"
            ]
        }


    Args:
        body (DocumentProjectUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DocumentProjectUpdate,
) -> Response[Any]:
    r"""Update Document

         Update the project_id of a document in the vector database and Azure Search.
        TODO:
        - possible bug
        - call https://tektome.postman.co/workspace/tektome~f85cbc2b-55e1-48fe-8824-
    4e6ca228b024/request/37568547-fd6911d6-3d36-46ac-9398-4618c11a4b94?action=share&source=copy-
    link&creator=37568547&ctx=documentation
        - then call https://tektome.postman.co/workspace/tektome~f85cbc2b-55e1-48fe-8824-
    4e6ca228b024/request/37568547-7ac588a1-91ee-478e-af41-0d0711d5fd21?action=share&source=copy-
    link&creator=37568547&ctx=documentation
        {
            \"message\": [
                \"Document updated in page search index\",
                \"Document updated in chunk group search index\",
                \"Document moved in storage\"
            ],
            \"error\": [
                \"Failed to update document in attribute search index: (MissingRequiredParameter) The
    request is invalid. Details: actions : No indexing actions found in the request. Please include
    between 1 and 32000 indexing actions in your request.
    Code: MissingRequiredParameter
    Message: The request is invalid. Details: actions : No indexing actions found in the request. Please
    include between 1 and 32000 indexing actions in your request.
    Exception Details:      (MissingIndexDocumentsActions) No indexing actions found in the request.
    Please include between 1 and 32000 indexing actions in your request. Parameters: actions
            Code: MissingIndexDocumentsActions
            Message: No indexing actions found in the request. Please include between 1 and 32000
    indexing actions in your request. Parameters: actions\"
            ]
        }


    Args:
        body (DocumentProjectUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
