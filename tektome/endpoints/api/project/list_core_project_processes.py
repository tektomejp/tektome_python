from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_core_project_processes_ui_trigger_kind_choices import ListCoreProjectProcessesUiTriggerKindChoices
from ...models.paged_process_out import PagedProcessOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    *,
    ui_trigger_name: None | str | Unset = UNSET,
    ui_trigger_kinds: list[ListCoreProjectProcessesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    template_id: None | Unset | UUID = UNSET,
    show_system_processes: bool | Unset = False,
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

    json_template_id: None | str | Unset
    if isinstance(template_id, Unset):
        json_template_id = UNSET
    elif isinstance(template_id, UUID):
        json_template_id = str(template_id)
    else:
        json_template_id = template_id
    params["template_id"] = json_template_id

    params["show_system_processes"] = show_system_processes

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
        "url": "/api/core/projects/{project_id}/processes/".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedProcessOut | None:
    if response.status_code == 200:
        response_200 = PagedProcessOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedProcessOut]:
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
    ui_trigger_kinds: list[ListCoreProjectProcessesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    template_id: None | Unset | UUID = UNSET,
    show_system_processes: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedProcessOut]:
    """List processes for a project

     Retrieve all processes associated with the specified project. Supports filtering via query
    parameters.

    Args:
        project_id (UUID):
        ui_trigger_name (None | str | Unset): Filter processes by UI trigger name.
        ui_trigger_kinds (list[ListCoreProjectProcessesUiTriggerKindChoices] | Unset): Filter
            processes by UI trigger kind. Possible values are defined in UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the process to search for.
        template_id (None | Unset | UUID): Filter processes by the associated process template ID.
        show_system_processes (bool | Unset): Controls whether to include system-generated
            processes Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedProcessOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        ui_trigger_name=ui_trigger_name,
        ui_trigger_kinds=ui_trigger_kinds,
        name=name,
        template_id=template_id,
        show_system_processes=show_system_processes,
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
    ui_trigger_kinds: list[ListCoreProjectProcessesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    template_id: None | Unset | UUID = UNSET,
    show_system_processes: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedProcessOut | None:
    """List processes for a project

     Retrieve all processes associated with the specified project. Supports filtering via query
    parameters.

    Args:
        project_id (UUID):
        ui_trigger_name (None | str | Unset): Filter processes by UI trigger name.
        ui_trigger_kinds (list[ListCoreProjectProcessesUiTriggerKindChoices] | Unset): Filter
            processes by UI trigger kind. Possible values are defined in UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the process to search for.
        template_id (None | Unset | UUID): Filter processes by the associated process template ID.
        show_system_processes (bool | Unset): Controls whether to include system-generated
            processes Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedProcessOut
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        ui_trigger_name=ui_trigger_name,
        ui_trigger_kinds=ui_trigger_kinds,
        name=name,
        template_id=template_id,
        show_system_processes=show_system_processes,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    ui_trigger_name: None | str | Unset = UNSET,
    ui_trigger_kinds: list[ListCoreProjectProcessesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    template_id: None | Unset | UUID = UNSET,
    show_system_processes: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedProcessOut]:
    """List processes for a project

     Retrieve all processes associated with the specified project. Supports filtering via query
    parameters.

    Args:
        project_id (UUID):
        ui_trigger_name (None | str | Unset): Filter processes by UI trigger name.
        ui_trigger_kinds (list[ListCoreProjectProcessesUiTriggerKindChoices] | Unset): Filter
            processes by UI trigger kind. Possible values are defined in UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the process to search for.
        template_id (None | Unset | UUID): Filter processes by the associated process template ID.
        show_system_processes (bool | Unset): Controls whether to include system-generated
            processes Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedProcessOut]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        ui_trigger_name=ui_trigger_name,
        ui_trigger_kinds=ui_trigger_kinds,
        name=name,
        template_id=template_id,
        show_system_processes=show_system_processes,
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
    ui_trigger_kinds: list[ListCoreProjectProcessesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    template_id: None | Unset | UUID = UNSET,
    show_system_processes: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedProcessOut | None:
    """List processes for a project

     Retrieve all processes associated with the specified project. Supports filtering via query
    parameters.

    Args:
        project_id (UUID):
        ui_trigger_name (None | str | Unset): Filter processes by UI trigger name.
        ui_trigger_kinds (list[ListCoreProjectProcessesUiTriggerKindChoices] | Unset): Filter
            processes by UI trigger kind. Possible values are defined in UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the process to search for.
        template_id (None | Unset | UUID): Filter processes by the associated process template ID.
        show_system_processes (bool | Unset): Controls whether to include system-generated
            processes Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedProcessOut
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            ui_trigger_name=ui_trigger_name,
            ui_trigger_kinds=ui_trigger_kinds,
            name=name,
            template_id=template_id,
            show_system_processes=show_system_processes,
            page=page,
            page_size=page_size,
        )
    ).parsed
