from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_process_types import ExecutionProcessTypes
from ..models.process_usage_query_ui_trigger_kind_choices import ProcessUsageQueryUiTriggerKindChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessUsageQuery")


@_attrs_define
class ProcessUsageQuery:
    """
    Attributes:
        process_type (ExecutionProcessTypes | None | Unset): Filter process usage by process type. Possible values are
            defined in ExecutionProcessTypes.
        ui_trigger_kinds (list[ProcessUsageQueryUiTriggerKindChoices] | Unset): Filter process usage by UI trigger kind.
            Possible values are defined in UiTriggerKindChoices.
    """

    process_type: ExecutionProcessTypes | None | Unset = UNSET
    ui_trigger_kinds: list[ProcessUsageQueryUiTriggerKindChoices] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_type: None | str | Unset
        if isinstance(self.process_type, Unset):
            process_type = UNSET
        elif isinstance(self.process_type, ExecutionProcessTypes):
            process_type = self.process_type.value
        else:
            process_type = self.process_type

        ui_trigger_kinds: list[str] | Unset = UNSET
        if not isinstance(self.ui_trigger_kinds, Unset):
            ui_trigger_kinds = []
            for ui_trigger_kinds_item_data in self.ui_trigger_kinds:
                ui_trigger_kinds_item = ui_trigger_kinds_item_data.value
                ui_trigger_kinds.append(ui_trigger_kinds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if process_type is not UNSET:
            field_dict["process_type"] = process_type
        if ui_trigger_kinds is not UNSET:
            field_dict["ui_trigger_kinds"] = ui_trigger_kinds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_process_type(data: object) -> ExecutionProcessTypes | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                process_type_type_0 = ExecutionProcessTypes(data)

                return process_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExecutionProcessTypes | None | Unset, data)

        process_type = _parse_process_type(d.pop("process_type", UNSET))

        _ui_trigger_kinds = d.pop("ui_trigger_kinds", UNSET)
        ui_trigger_kinds: list[ProcessUsageQueryUiTriggerKindChoices] | Unset = UNSET
        if _ui_trigger_kinds is not UNSET:
            ui_trigger_kinds = []
            for ui_trigger_kinds_item_data in _ui_trigger_kinds:
                ui_trigger_kinds_item = ProcessUsageQueryUiTriggerKindChoices(ui_trigger_kinds_item_data)

                ui_trigger_kinds.append(ui_trigger_kinds_item)

        process_usage_query = cls(
            process_type=process_type,
            ui_trigger_kinds=ui_trigger_kinds,
        )

        process_usage_query.additional_properties = d
        return process_usage_query

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
