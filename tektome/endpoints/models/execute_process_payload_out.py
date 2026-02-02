from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.execute_process_details import ExecuteProcessDetails
    from ..models.execute_process_payload_out_execution_run_args import ExecuteProcessPayloadOutExecutionRunArgs
    from ..models.execute_process_ui_trigger_details import ExecuteProcessUITriggerDetails


T = TypeVar("T", bound="ExecuteProcessPayloadOut")


@_attrs_define
class ExecuteProcessPayloadOut:
    """Validation schema for individual process execution payload

    Attributes:
        execution_run_args (ExecuteProcessPayloadOutExecutionRunArgs):
        process_details (ExecuteProcessDetails): Validation schema for UI trigger details in individual process
            execution payload
        ui_trigger_details (list[ExecuteProcessUITriggerDetails]):
    """

    execution_run_args: ExecuteProcessPayloadOutExecutionRunArgs
    process_details: ExecuteProcessDetails
    ui_trigger_details: list[ExecuteProcessUITriggerDetails]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_run_args = self.execution_run_args.to_dict()

        process_details = self.process_details.to_dict()

        ui_trigger_details = []
        for ui_trigger_details_item_data in self.ui_trigger_details:
            ui_trigger_details_item = ui_trigger_details_item_data.to_dict()
            ui_trigger_details.append(ui_trigger_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "execution_run_args": execution_run_args,
                "process_details": process_details,
                "ui_trigger_details": ui_trigger_details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_process_details import ExecuteProcessDetails
        from ..models.execute_process_payload_out_execution_run_args import ExecuteProcessPayloadOutExecutionRunArgs
        from ..models.execute_process_ui_trigger_details import ExecuteProcessUITriggerDetails

        d = dict(src_dict)
        execution_run_args = ExecuteProcessPayloadOutExecutionRunArgs.from_dict(d.pop("execution_run_args"))

        process_details = ExecuteProcessDetails.from_dict(d.pop("process_details"))

        ui_trigger_details = []
        _ui_trigger_details = d.pop("ui_trigger_details")
        for ui_trigger_details_item_data in _ui_trigger_details:
            ui_trigger_details_item = ExecuteProcessUITriggerDetails.from_dict(ui_trigger_details_item_data)

            ui_trigger_details.append(ui_trigger_details_item)

        execute_process_payload_out = cls(
            execution_run_args=execution_run_args,
            process_details=process_details,
            ui_trigger_details=ui_trigger_details,
        )

        execute_process_payload_out.additional_properties = d
        return execute_process_payload_out

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
