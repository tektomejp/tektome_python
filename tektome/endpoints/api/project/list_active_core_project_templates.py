from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_active_core_project_templates_ui_trigger_kind_choices import (
    ListActiveCoreProjectTemplatesUiTriggerKindChoices,
)
from ...models.paged_template_out import PagedTemplateOut
from ...models.process_type_choices import ProcessTypeChoices
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    *,
    ui_trigger_name: None | str | Unset = UNSET,
    ui_trigger_kinds: list[ListActiveCoreProjectTemplatesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    type_: None | ProcessTypeChoices | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ui_trigger_name: None | str | Unset
    if isinstance(ui_trigger_name, Unset):
        json_ui_trigger_name = UNSET
    else:
        json_ui_trigger_name = ui_trigger_name
    params["ui_trigger_name"] = json_ui_trigger_name

    json_ui_trigger_kinds: list[str] | Unset = UNSET
    if not isinstance(ui_trigger_kinds, Unset):
        json_ui_trigger_kinds = []
        for ui_trigger_kinds_item_data in ui_trigger_kinds:
            ui_trigger_kinds_item = ui_trigger_kinds_item_data.value
            json_ui_trigger_kinds.append(ui_trigger_kinds_item)

    params["ui_trigger_kinds"] = json_ui_trigger_kinds

    json_name: None | str | Unset
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, ProcessTypeChoices):
        json_type_ = type_.value
    else:
        json_type_ = type_
    params["type"] = json_type_

    params["page"] = page

    json_page_size: int | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["page_size"] = json_page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/projects/{project_id}/templates/active/".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedTemplateOut | None:
    if response.status_code == 200:
        response_200 = PagedTemplateOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedTemplateOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    ui_trigger_name: None | str | Unset = UNSET,
    ui_trigger_kinds: list[ListActiveCoreProjectTemplatesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    type_: None | ProcessTypeChoices | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedTemplateOut]:
    """Get Active Project Templates

     j14Y1Xi4

    Retrieve active templates for the current project, which can be used to create processes.
    This endpoint has the same permissions as process creation.

    Args:
        project_id (UUID):
        ui_trigger_name (None | str | Unset): Filter templates by UI trigger name.
        ui_trigger_kinds (list[ListActiveCoreProjectTemplatesUiTriggerKindChoices] | Unset):
            Filter templates by UI trigger kind. Possible values are defined in UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the template to search for.
        type_ (None | ProcessTypeChoices | Unset): Filter templates by type. Possible values are
            defined in ProcessTypeChoices.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedTemplateOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        ui_trigger_name=ui_trigger_name,
        ui_trigger_kinds=ui_trigger_kinds,
        name=name,
        type_=type_,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    ui_trigger_name: None | str | Unset = UNSET,
    ui_trigger_kinds: list[ListActiveCoreProjectTemplatesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    type_: None | ProcessTypeChoices | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedTemplateOut | None:
    """Get Active Project Templates

     j14Y1Xi4

    Retrieve active templates for the current project, which can be used to create processes.
    This endpoint has the same permissions as process creation.

    Args:
        project_id (UUID):
        ui_trigger_name (None | str | Unset): Filter templates by UI trigger name.
        ui_trigger_kinds (list[ListActiveCoreProjectTemplatesUiTriggerKindChoices] | Unset):
            Filter templates by UI trigger kind. Possible values are defined in UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the template to search for.
        type_ (None | ProcessTypeChoices | Unset): Filter templates by type. Possible values are
            defined in ProcessTypeChoices.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedTemplateOut
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        ui_trigger_name=ui_trigger_name,
        ui_trigger_kinds=ui_trigger_kinds,
        name=name,
        type_=type_,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    ui_trigger_name: None | str | Unset = UNSET,
    ui_trigger_kinds: list[ListActiveCoreProjectTemplatesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    type_: None | ProcessTypeChoices | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedTemplateOut]:
    """Get Active Project Templates

     j14Y1Xi4

    Retrieve active templates for the current project, which can be used to create processes.
    This endpoint has the same permissions as process creation.

    Args:
        project_id (UUID):
        ui_trigger_name (None | str | Unset): Filter templates by UI trigger name.
        ui_trigger_kinds (list[ListActiveCoreProjectTemplatesUiTriggerKindChoices] | Unset):
            Filter templates by UI trigger kind. Possible values are defined in UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the template to search for.
        type_ (None | ProcessTypeChoices | Unset): Filter templates by type. Possible values are
            defined in ProcessTypeChoices.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedTemplateOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        ui_trigger_name=ui_trigger_name,
        ui_trigger_kinds=ui_trigger_kinds,
        name=name,
        type_=type_,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    ui_trigger_name: None | str | Unset = UNSET,
    ui_trigger_kinds: list[ListActiveCoreProjectTemplatesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    type_: None | ProcessTypeChoices | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedTemplateOut | None:
    """Get Active Project Templates

     j14Y1Xi4

    Retrieve active templates for the current project, which can be used to create processes.
    This endpoint has the same permissions as process creation.

    Args:
        project_id (UUID):
        ui_trigger_name (None | str | Unset): Filter templates by UI trigger name.
        ui_trigger_kinds (list[ListActiveCoreProjectTemplatesUiTriggerKindChoices] | Unset):
            Filter templates by UI trigger kind. Possible values are defined in UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the template to search for.
        type_ (None | ProcessTypeChoices | Unset): Filter templates by type. Possible values are
            defined in ProcessTypeChoices.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedTemplateOut
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            ui_trigger_name=ui_trigger_name,
            ui_trigger_kinds=ui_trigger_kinds,
            name=name,
            type_=type_,
            page=page,
            page_size=page_size,
        )
    ).parsed
