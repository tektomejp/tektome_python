from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attribute_extraction_post_out import AttributeExtractionPostOut
from ...models.extraction_post_in import ExtractionPostIn
from ...types import Response


def _get_kwargs(
    *,
    body: ExtractionPostIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/extractions/attributes/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AttributeExtractionPostOut | None:
    if response.status_code == 201:
        response_201 = AttributeExtractionPostOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AttributeExtractionPostOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ExtractionPostIn,
) -> Response[AttributeExtractionPostOut]:
    r"""Post Attribute Extraction

     # ATTN:<br>
    attributes[0].id is not required, if provided it needs to be uuid4, and unique, otherwise the whole
    process is forced to fail, and db tx reverted.<br>
    unless there is a specific reason to use the id, it is better to let the system generate it.<br>
    if Section.*Attribute already exists, it will not be created again, but the id will be replaced, and
    returned in the created list.<br>

    This endpoint extracts *Attributes from a Section. Multiple *Attributes can be extracted at once.
    When multiple attributes are provided, <br>
    they are extracted in one shot.<br>
    To extract in multiple shots, call this endpoint multiple times with different attributes.<br>
    # Usage:
    section_id: is the ID of the Section from which to extract attributes.<br> It is converted to an LLM
    friendly format.
    recipe: is the versioned extraction recipe to use for the extraction.<br>
    attributes: is a list of attributes to extract. Each attribute has a name, prompt, and kind.<br>
        id(optional): is the UUID of the attribute. If provided, it must be unique.
        name: is the name of the attribute. It must be lowercased, and cannot contain spaces or start
    with \"system:\", it must not end with _error_message, nor _sources.
        kind: is the kind of the attribute, it must be one of the AttributeType enum values.
    enduser_prompt: is the prompt provided by the end user, it is appended LAST to the user prompt.
    include_pdf_pages_as_images: if true, includes the PDF pages as images in the extraction context.

    Args:
        body (ExtractionPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributeExtractionPostOut]
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
    body: ExtractionPostIn,
) -> AttributeExtractionPostOut | None:
    r"""Post Attribute Extraction

     # ATTN:<br>
    attributes[0].id is not required, if provided it needs to be uuid4, and unique, otherwise the whole
    process is forced to fail, and db tx reverted.<br>
    unless there is a specific reason to use the id, it is better to let the system generate it.<br>
    if Section.*Attribute already exists, it will not be created again, but the id will be replaced, and
    returned in the created list.<br>

    This endpoint extracts *Attributes from a Section. Multiple *Attributes can be extracted at once.
    When multiple attributes are provided, <br>
    they are extracted in one shot.<br>
    To extract in multiple shots, call this endpoint multiple times with different attributes.<br>
    # Usage:
    section_id: is the ID of the Section from which to extract attributes.<br> It is converted to an LLM
    friendly format.
    recipe: is the versioned extraction recipe to use for the extraction.<br>
    attributes: is a list of attributes to extract. Each attribute has a name, prompt, and kind.<br>
        id(optional): is the UUID of the attribute. If provided, it must be unique.
        name: is the name of the attribute. It must be lowercased, and cannot contain spaces or start
    with \"system:\", it must not end with _error_message, nor _sources.
        kind: is the kind of the attribute, it must be one of the AttributeType enum values.
    enduser_prompt: is the prompt provided by the end user, it is appended LAST to the user prompt.
    include_pdf_pages_as_images: if true, includes the PDF pages as images in the extraction context.

    Args:
        body (ExtractionPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributeExtractionPostOut
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ExtractionPostIn,
) -> Response[AttributeExtractionPostOut]:
    r"""Post Attribute Extraction

     # ATTN:<br>
    attributes[0].id is not required, if provided it needs to be uuid4, and unique, otherwise the whole
    process is forced to fail, and db tx reverted.<br>
    unless there is a specific reason to use the id, it is better to let the system generate it.<br>
    if Section.*Attribute already exists, it will not be created again, but the id will be replaced, and
    returned in the created list.<br>

    This endpoint extracts *Attributes from a Section. Multiple *Attributes can be extracted at once.
    When multiple attributes are provided, <br>
    they are extracted in one shot.<br>
    To extract in multiple shots, call this endpoint multiple times with different attributes.<br>
    # Usage:
    section_id: is the ID of the Section from which to extract attributes.<br> It is converted to an LLM
    friendly format.
    recipe: is the versioned extraction recipe to use for the extraction.<br>
    attributes: is a list of attributes to extract. Each attribute has a name, prompt, and kind.<br>
        id(optional): is the UUID of the attribute. If provided, it must be unique.
        name: is the name of the attribute. It must be lowercased, and cannot contain spaces or start
    with \"system:\", it must not end with _error_message, nor _sources.
        kind: is the kind of the attribute, it must be one of the AttributeType enum values.
    enduser_prompt: is the prompt provided by the end user, it is appended LAST to the user prompt.
    include_pdf_pages_as_images: if true, includes the PDF pages as images in the extraction context.

    Args:
        body (ExtractionPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributeExtractionPostOut]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ExtractionPostIn,
) -> AttributeExtractionPostOut | None:
    r"""Post Attribute Extraction

     # ATTN:<br>
    attributes[0].id is not required, if provided it needs to be uuid4, and unique, otherwise the whole
    process is forced to fail, and db tx reverted.<br>
    unless there is a specific reason to use the id, it is better to let the system generate it.<br>
    if Section.*Attribute already exists, it will not be created again, but the id will be replaced, and
    returned in the created list.<br>

    This endpoint extracts *Attributes from a Section. Multiple *Attributes can be extracted at once.
    When multiple attributes are provided, <br>
    they are extracted in one shot.<br>
    To extract in multiple shots, call this endpoint multiple times with different attributes.<br>
    # Usage:
    section_id: is the ID of the Section from which to extract attributes.<br> It is converted to an LLM
    friendly format.
    recipe: is the versioned extraction recipe to use for the extraction.<br>
    attributes: is a list of attributes to extract. Each attribute has a name, prompt, and kind.<br>
        id(optional): is the UUID of the attribute. If provided, it must be unique.
        name: is the name of the attribute. It must be lowercased, and cannot contain spaces or start
    with \"system:\", it must not end with _error_message, nor _sources.
        kind: is the kind of the attribute, it must be one of the AttributeType enum values.
    enduser_prompt: is the prompt provided by the end user, it is appended LAST to the user prompt.
    include_pdf_pages_as_images: if true, includes the PDF pages as images in the extraction context.

    Args:
        body (ExtractionPostIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributeExtractionPostOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
