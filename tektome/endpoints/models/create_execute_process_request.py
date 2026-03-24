from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ui_trigger_kind_choices import UiTriggerKindChoices
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_execute_process_request_execution_run_args import CreateExecuteProcessRequestExecutionRunArgs


T = TypeVar("T", bound="CreateExecuteProcessRequest")


@_attrs_define
class CreateExecuteProcessRequest:
    """
    Attributes:
        execution_run_args (CreateExecuteProcessRequestExecutionRunArgs):
        process_id (UUID):
        project_ids (list[UUID] | None | Unset): List of project IDs to execute on processes
        folder_ids (list[UUID] | None | Unset): List of folder IDs to execute on processes
        kind (None | UiTriggerKindChoices | Unset):
        ui_trigger_ids (list[UUID] | None | Unset):
    """

    execution_run_args: CreateExecuteProcessRequestExecutionRunArgs
    process_id: UUID
    project_ids: list[UUID] | None | Unset = UNSET
    folder_ids: list[UUID] | None | Unset = UNSET
    kind: None | UiTriggerKindChoices | Unset = UNSET
    ui_trigger_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_run_args = self.execution_run_args.to_dict()

        process_id = str(self.process_id)

        project_ids: list[str] | None | Unset
        if isinstance(self.project_ids, Unset):
            project_ids = UNSET
        elif isinstance(self.project_ids, list):
            project_ids = []
            for project_ids_type_0_item_data in self.project_ids:
                project_ids_type_0_item = str(project_ids_type_0_item_data)
                project_ids.append(project_ids_type_0_item)

        else:
            project_ids = self.project_ids

        folder_ids: list[str] | None | Unset
        if isinstance(self.folder_ids, Unset):
            folder_ids = UNSET
        elif isinstance(self.folder_ids, list):
            folder_ids = []
            for folder_ids_type_0_item_data in self.folder_ids:
                folder_ids_type_0_item = str(folder_ids_type_0_item_data)
                folder_ids.append(folder_ids_type_0_item)

        else:
            folder_ids = self.folder_ids

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        elif isinstance(self.kind, UiTriggerKindChoices):
            kind = self.kind.value
        else:
            kind = self.kind

        ui_trigger_ids: list[str] | None | Unset
        if isinstance(self.ui_trigger_ids, Unset):
            ui_trigger_ids = UNSET
        elif isinstance(self.ui_trigger_ids, list):
            ui_trigger_ids = []
            for ui_trigger_ids_type_0_item_data in self.ui_trigger_ids:
                ui_trigger_ids_type_0_item = str(ui_trigger_ids_type_0_item_data)
                ui_trigger_ids.append(ui_trigger_ids_type_0_item)

        else:
            ui_trigger_ids = self.ui_trigger_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "execution_run_args": execution_run_args,
                "process_id": process_id,
            }
        )
        if project_ids is not UNSET:
            field_dict["project_ids"] = project_ids
        if folder_ids is not UNSET:
            field_dict["folder_ids"] = folder_ids
        if kind is not UNSET:
            field_dict["kind"] = kind
        if ui_trigger_ids is not UNSET:
            field_dict["ui_trigger_ids"] = ui_trigger_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_execute_process_request_execution_run_args import (
            CreateExecuteProcessRequestExecutionRunArgs,
        )

        d = dict(src_dict)
        execution_run_args = CreateExecuteProcessRequestExecutionRunArgs.from_dict(d.pop("execution_run_args"))

        process_id = UUID(d.pop("process_id"))

        def _parse_project_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                project_ids_type_0 = []
                _project_ids_type_0 = data
                for project_ids_type_0_item_data in _project_ids_type_0:
                    project_ids_type_0_item = UUID(project_ids_type_0_item_data)

                    project_ids_type_0.append(project_ids_type_0_item)

                return project_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        project_ids = _parse_project_ids(d.pop("project_ids", UNSET))

        def _parse_folder_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                folder_ids_type_0 = []
                _folder_ids_type_0 = data
                for folder_ids_type_0_item_data in _folder_ids_type_0:
                    folder_ids_type_0_item = UUID(folder_ids_type_0_item_data)

                    folder_ids_type_0.append(folder_ids_type_0_item)

                return folder_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        folder_ids = _parse_folder_ids(d.pop("folder_ids", UNSET))

        def _parse_kind(data: object) -> None | UiTriggerKindChoices | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_0 = UiTriggerKindChoices(data)

                return kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UiTriggerKindChoices | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_ui_trigger_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ui_trigger_ids_type_0 = []
                _ui_trigger_ids_type_0 = data
                for ui_trigger_ids_type_0_item_data in _ui_trigger_ids_type_0:
                    ui_trigger_ids_type_0_item = UUID(ui_trigger_ids_type_0_item_data)

                    ui_trigger_ids_type_0.append(ui_trigger_ids_type_0_item)

                return ui_trigger_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        ui_trigger_ids = _parse_ui_trigger_ids(d.pop("ui_trigger_ids", UNSET))

        create_execute_process_request = cls(
            execution_run_args=execution_run_args,
            process_id=process_id,
            project_ids=project_ids,
            folder_ids=folder_ids,
            kind=kind,
            ui_trigger_ids=ui_trigger_ids,
        )

        create_execute_process_request.additional_properties = d
        return create_execute_process_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
