from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_process_post_in_execution_run_args import ExecuteProcessPostInExecutionRunArgs
    from ..models.ui_trigger_values import UITriggerValues


T = TypeVar("T", bound="ExecuteProcessPostIn")


@_attrs_define
class ExecuteProcessPostIn:
    """
    Attributes:
        execution_run_args (ExecuteProcessPostInExecutionRunArgs):
        ui_trigger_values (None | UITriggerValues | Unset):
    """

    execution_run_args: ExecuteProcessPostInExecutionRunArgs
    ui_trigger_values: None | UITriggerValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ui_trigger_values import UITriggerValues

        execution_run_args = self.execution_run_args.to_dict()

        ui_trigger_values: dict[str, Any] | None | Unset
        if isinstance(self.ui_trigger_values, Unset):
            ui_trigger_values = UNSET
        elif isinstance(self.ui_trigger_values, UITriggerValues):
            ui_trigger_values = self.ui_trigger_values.to_dict()
        else:
            ui_trigger_values = self.ui_trigger_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "execution_run_args": execution_run_args,
            }
        )
        if ui_trigger_values is not UNSET:
            field_dict["ui_trigger_values"] = ui_trigger_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_process_post_in_execution_run_args import ExecuteProcessPostInExecutionRunArgs
        from ..models.ui_trigger_values import UITriggerValues

        d = dict(src_dict)
        execution_run_args = ExecuteProcessPostInExecutionRunArgs.from_dict(d.pop("execution_run_args"))

        def _parse_ui_trigger_values(data: object) -> None | UITriggerValues | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ui_trigger_values_type_0 = UITriggerValues.from_dict(data)

                return ui_trigger_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UITriggerValues | Unset, data)

        ui_trigger_values = _parse_ui_trigger_values(d.pop("ui_trigger_values", UNSET))

        execute_process_post_in = cls(
            execution_run_args=execution_run_args,
            ui_trigger_values=ui_trigger_values,
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
