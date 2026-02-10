from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ui_trigger_kind_choices import UiTriggerKindChoices
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_process_post_in_execution_run_args import ExecuteProcessPostInExecutionRunArgs


T = TypeVar("T", bound="ExecuteProcessPostIn")


@_attrs_define
class ExecuteProcessPostIn:
    """
    Attributes:
        execution_run_args (ExecuteProcessPostInExecutionRunArgs):
        process_id (UUID):
        kind (None | UiTriggerKindChoices | Unset):
        ui_trigger_ids (list[UUID] | None | Unset):
    """

    execution_run_args: ExecuteProcessPostInExecutionRunArgs
    process_id: UUID
    kind: None | UiTriggerKindChoices | Unset = UNSET
    ui_trigger_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_run_args = self.execution_run_args.to_dict()

        process_id = str(self.process_id)

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
        if kind is not UNSET:
            field_dict["kind"] = kind
        if ui_trigger_ids is not UNSET:
            field_dict["ui_trigger_ids"] = ui_trigger_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_process_post_in_execution_run_args import ExecuteProcessPostInExecutionRunArgs

        d = dict(src_dict)
        execution_run_args = ExecuteProcessPostInExecutionRunArgs.from_dict(d.pop("execution_run_args"))

        process_id = UUID(d.pop("process_id"))

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

        execute_process_post_in = cls(
            execution_run_args=execution_run_args,
            process_id=process_id,
            kind=kind,
            ui_trigger_ids=ui_trigger_ids,
        )

        execute_process_post_in.additional_properties = d
        return execute_process_post_in

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
