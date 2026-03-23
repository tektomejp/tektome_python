from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_process_details import ExecuteProcessDetails
    from ..models.execute_process_ui_trigger_details import ExecuteProcessUITriggerDetails
    from ..models.execution_get_out_execution_run_args import ExecutionGetOutExecutionRunArgs


T = TypeVar("T", bound="ExecutionGetOut")


@_attrs_define
class ExecutionGetOut:
    """Serializer for Execution metadata details

    Attributes:
        execution_run_args (ExecutionGetOutExecutionRunArgs):
        process_details (ExecuteProcessDetails): Validation schema for UI trigger details in individual process
            execution payload
        auto_approved_output (bool):
        created (datetime.datetime):
        updated (datetime.datetime):
        ui_trigger_details (list[ExecuteProcessUITriggerDetails] | Unset):
        memo (None | str | Unset): Memo for the execution group
        id (None | Unset | UUID):
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
    """

    execution_run_args: ExecutionGetOutExecutionRunArgs
    process_details: ExecuteProcessDetails
    auto_approved_output: bool
    created: datetime.datetime
    updated: datetime.datetime
    ui_trigger_details: list[ExecuteProcessUITriggerDetails] | Unset = UNSET
    memo: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_run_args = self.execution_run_args.to_dict()

        process_details = self.process_details.to_dict()

        auto_approved_output = self.auto_approved_output

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        ui_trigger_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ui_trigger_details, Unset):
            ui_trigger_details = []
            for ui_trigger_details_item_data in self.ui_trigger_details:
                ui_trigger_details_item = ui_trigger_details_item_data.to_dict()
                ui_trigger_details.append(ui_trigger_details_item)

        memo: None | str | Unset
        if isinstance(self.memo, Unset):
            memo = UNSET
        else:
            memo = self.memo

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "execution_run_args": execution_run_args,
                "process_details": process_details,
                "auto_approved_output": auto_approved_output,
                "created": created,
                "updated": updated,
            }
        )
        if ui_trigger_details is not UNSET:
            field_dict["ui_trigger_details"] = ui_trigger_details
        if memo is not UNSET:
            field_dict["memo"] = memo
        if id is not UNSET:
            field_dict["id"] = id
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_process_details import ExecuteProcessDetails
        from ..models.execute_process_ui_trigger_details import ExecuteProcessUITriggerDetails
        from ..models.execution_get_out_execution_run_args import ExecutionGetOutExecutionRunArgs

        d = dict(src_dict)
        execution_run_args = ExecutionGetOutExecutionRunArgs.from_dict(d.pop("execution_run_args"))

        process_details = ExecuteProcessDetails.from_dict(d.pop("process_details"))

        auto_approved_output = d.pop("auto_approved_output")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        _ui_trigger_details = d.pop("ui_trigger_details", UNSET)
        ui_trigger_details: list[ExecuteProcessUITriggerDetails] | Unset = UNSET
        if _ui_trigger_details is not UNSET:
            ui_trigger_details = []
            for ui_trigger_details_item_data in _ui_trigger_details:
                ui_trigger_details_item = ExecuteProcessUITriggerDetails.from_dict(ui_trigger_details_item_data)

                ui_trigger_details.append(ui_trigger_details_item)

        def _parse_memo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        memo = _parse_memo(d.pop("memo", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        execution_get_out = cls(
            execution_run_args=execution_run_args,
            process_details=process_details,
            auto_approved_output=auto_approved_output,
            created=created,
            updated=updated,
            ui_trigger_details=ui_trigger_details,
            memo=memo,
            id=id,
            start_time=start_time,
            end_time=end_time,
        )

        execution_get_out.additional_properties = d
        return execution_get_out

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
