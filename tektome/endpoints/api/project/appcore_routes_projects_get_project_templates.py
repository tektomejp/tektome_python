from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appcore_routes_projects_get_project_templates_ui_trigger_kind_choices import (
    AppcoreRoutesProjectsGetProjectTemplatesUiTriggerKindChoices,
)
from ...models.paged_template_out import PagedTemplateOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    *,
    ui_trigger_name: None | str | Unset = UNSET,
    ui_trigger_kinds: list[AppcoreRoutesProjectsGetProjectTemplatesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    for_import: bool | None | Unset = UNSET,
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

    json_for_import: bool | None | Unset
    if isinstance(for_import, Unset):
        json_for_import = UNSET
    else:
        json_for_import = for_import
    params["for_import"] = json_for_import

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
        "url": "/api/core/projects/{project_id}/templates/".format(
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
    ui_trigger_kinds: list[AppcoreRoutesProjectsGetProjectTemplatesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    for_import: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedTemplateOut]:
    """Get Project Templates

     d4RtYh2K

    Get all templates that belong to the given project_id

    Args:
        project_id (UUID):
        ui_trigger_name (None | str | Unset): Filter templates by UI trigger name.
        ui_trigger_kinds (list[AppcoreRoutesProjectsGetProjectTemplatesUiTriggerKindChoices] |
            Unset): Filter templates by UI trigger kind. Possible values are defined in
            UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the template to search for.
        for_import (bool | None | Unset): If true, only return templates that can be imported.
            Otherwise, return all available templates, either default or imported.
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
        for_import=for_import,
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
    ui_trigger_kinds: list[AppcoreRoutesProjectsGetProjectTemplatesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    for_import: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedTemplateOut | None:
    """Get Project Templates

     d4RtYh2K

    Get all templates that belong to the given project_id

    Args:
        project_id (UUID):
        ui_trigger_name (None | str | Unset): Filter templates by UI trigger name.
        ui_trigger_kinds (list[AppcoreRoutesProjectsGetProjectTemplatesUiTriggerKindChoices] |
            Unset): Filter templates by UI trigger kind. Possible values are defined in
            UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the template to search for.
        for_import (bool | None | Unset): If true, only return templates that can be imported.
            Otherwise, return all available templates, either default or imported.
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
        for_import=for_import,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    ui_trigger_name: None | str | Unset = UNSET,
    ui_trigger_kinds: list[AppcoreRoutesProjectsGetProjectTemplatesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    for_import: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> Response[PagedTemplateOut]:
    """Get Project Templates

     d4RtYh2K

    Get all templates that belong to the given project_id

    Args:
        project_id (UUID):
        ui_trigger_name (None | str | Unset): Filter templates by UI trigger name.
        ui_trigger_kinds (list[AppcoreRoutesProjectsGetProjectTemplatesUiTriggerKindChoices] |
            Unset): Filter templates by UI trigger kind. Possible values are defined in
            UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the template to search for.
        for_import (bool | None | Unset): If true, only return templates that can be imported.
            Otherwise, return all available templates, either default or imported.
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
        for_import=for_import,
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
    ui_trigger_kinds: list[AppcoreRoutesProjectsGetProjectTemplatesUiTriggerKindChoices] | Unset = UNSET,
    name: None | str | Unset = UNSET,
    for_import: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | None | Unset = UNSET,
) -> PagedTemplateOut | None:
    """Get Project Templates

     d4RtYh2K

    Get all templates that belong to the given project_id

    Args:
        project_id (UUID):
        ui_trigger_name (None | str | Unset): Filter templates by UI trigger name.
        ui_trigger_kinds (list[AppcoreRoutesProjectsGetProjectTemplatesUiTriggerKindChoices] |
            Unset): Filter templates by UI trigger kind. Possible values are defined in
            UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the template to search for.
        for_import (bool | None | Unset): If true, only return templates that can be imported.
            Otherwise, return all available templates, either default or imported.
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
            for_import=for_import,
            page=page,
            page_size=page_size,
        )
    ).parsed
