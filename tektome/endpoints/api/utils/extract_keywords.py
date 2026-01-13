from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyword_extraction import KeywordExtraction
from ...models.keywords import Keywords
from ...types import Response


def _get_kwargs(
    *,
    body: KeywordExtraction,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/utils/keywords/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Keywords | None:
    if response.status_code == 200:
        response_200 = Keywords.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Keywords]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: KeywordExtraction,
) -> Response[Keywords]:
    """Extract Keywords

     UOn7hBJp

    Extract keywords from text using NLP techniques.
    Currently only English and Japanese are supported.
    The value of the return mode only affects English text.
    Defaults to returning surface forms of keywords (i.e. as they appear in the text).
    Japanese keywords are returned in surface form.
    The Language Detector service is used to determine the language of the input text.

    Args:
        request: Request object
        payload: request payload containing the text to extract from, and return mode for the keywords

    Returns:
        A response containing extracted keywords as a list of strings with no inherent order and no
    duplicates.

    Args:
        body (KeywordExtraction): Schema for keyword extraction requests.

            This schema defines the structure for keyword extraction operations,
            allowing users to specify the text to analyze and whether to include
            word inflections in the extraction process.

            Attributes:
                text (str): The input text from which keywords will be extracted.
                return_mode (str): The mode to determine the form of keywords to return.
                    - SURFACE: Return surface forms of keywords.
                    - ROOT: Return root/lemma forms of keywords (or surface in case of measurements).
                    - INFLECTIONS: Return all inflected forms of keywords (just surface in case of
            measurements).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Keywords]
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
    body: KeywordExtraction,
) -> Keywords | None:
    """Extract Keywords

     UOn7hBJp

    Extract keywords from text using NLP techniques.
    Currently only English and Japanese are supported.
    The value of the return mode only affects English text.
    Defaults to returning surface forms of keywords (i.e. as they appear in the text).
    Japanese keywords are returned in surface form.
    The Language Detector service is used to determine the language of the input text.

    Args:
        request: Request object
        payload: request payload containing the text to extract from, and return mode for the keywords

    Returns:
        A response containing extracted keywords as a list of strings with no inherent order and no
    duplicates.

    Args:
        body (KeywordExtraction): Schema for keyword extraction requests.

            This schema defines the structure for keyword extraction operations,
            allowing users to specify the text to analyze and whether to include
            word inflections in the extraction process.

            Attributes:
                text (str): The input text from which keywords will be extracted.
                return_mode (str): The mode to determine the form of keywords to return.
                    - SURFACE: Return surface forms of keywords.
                    - ROOT: Return root/lemma forms of keywords (or surface in case of measurements).
                    - INFLECTIONS: Return all inflected forms of keywords (just surface in case of
            measurements).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Keywords
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: KeywordExtraction,
) -> Response[Keywords]:
    """Extract Keywords

     UOn7hBJp

    Extract keywords from text using NLP techniques.
    Currently only English and Japanese are supported.
    The value of the return mode only affects English text.
    Defaults to returning surface forms of keywords (i.e. as they appear in the text).
    Japanese keywords are returned in surface form.
    The Language Detector service is used to determine the language of the input text.

    Args:
        request: Request object
        payload: request payload containing the text to extract from, and return mode for the keywords

    Returns:
        A response containing extracted keywords as a list of strings with no inherent order and no
    duplicates.

    Args:
        body (KeywordExtraction): Schema for keyword extraction requests.

            This schema defines the structure for keyword extraction operations,
            allowing users to specify the text to analyze and whether to include
            word inflections in the extraction process.

            Attributes:
                text (str): The input text from which keywords will be extracted.
                return_mode (str): The mode to determine the form of keywords to return.
                    - SURFACE: Return surface forms of keywords.
                    - ROOT: Return root/lemma forms of keywords (or surface in case of measurements).
                    - INFLECTIONS: Return all inflected forms of keywords (just surface in case of
            measurements).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Keywords]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: KeywordExtraction,
) -> Keywords | None:
    """Extract Keywords

     UOn7hBJp

    Extract keywords from text using NLP techniques.
    Currently only English and Japanese are supported.
    The value of the return mode only affects English text.
    Defaults to returning surface forms of keywords (i.e. as they appear in the text).
    Japanese keywords are returned in surface form.
    The Language Detector service is used to determine the language of the input text.

    Args:
        request: Request object
        payload: request payload containing the text to extract from, and return mode for the keywords

    Returns:
        A response containing extracted keywords as a list of strings with no inherent order and no
    duplicates.

    Args:
        body (KeywordExtraction): Schema for keyword extraction requests.

            This schema defines the structure for keyword extraction operations,
            allowing users to specify the text to analyze and whether to include
            word inflections in the extraction process.

            Attributes:
                text (str): The input text from which keywords will be extracted.
                return_mode (str): The mode to determine the form of keywords to return.
                    - SURFACE: Return surface forms of keywords.
                    - ROOT: Return root/lemma forms of keywords (or surface in case of measurements).
                    - INFLECTIONS: Return all inflected forms of keywords (just surface in case of
            measurements).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Keywords
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
