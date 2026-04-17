from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_filter_request_ui_trigger_kind_choices import ProcessFilterRequestUiTriggerKindChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessFilterRequest")


@_attrs_define
class ProcessFilterRequest:
    """
    Attributes:
        ui_trigger_name (None | str | Unset): Filter processes by UI trigger name.
        ui_trigger_kinds (list[ProcessFilterRequestUiTriggerKindChoices] | Unset): Filter processes by UI trigger kind.
            Possible values are defined in UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the process to search for.
        template_id (None | Unset | UUID): Filter processes by the associated process template ID.
    """

    ui_trigger_name: None | str | Unset = UNSET
    ui_trigger_kinds: list[ProcessFilterRequestUiTriggerKindChoices] | Unset = UNSET
    name: None | str | Unset = UNSET
    template_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ui_trigger_name: None | str | Unset
        if isinstance(self.ui_trigger_name, Unset):
            ui_trigger_name = UNSET
        else:
            ui_trigger_name = self.ui_trigger_name

        ui_trigger_kinds: list[str] | Unset = UNSET
        if not isinstance(self.ui_trigger_kinds, Unset):
            ui_trigger_kinds = []
            for ui_trigger_kinds_item_data in self.ui_trigger_kinds:
                ui_trigger_kinds_item = ui_trigger_kinds_item_data.value
                ui_trigger_kinds.append(ui_trigger_kinds_item)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        template_id: None | str | Unset
        if isinstance(self.template_id, Unset):
            template_id = UNSET
        elif isinstance(self.template_id, UUID):
            template_id = str(self.template_id)
        else:
            template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ui_trigger_name is not UNSET:
            field_dict["ui_trigger_name"] = ui_trigger_name
        if ui_trigger_kinds is not UNSET:
            field_dict["ui_trigger_kinds"] = ui_trigger_kinds
        if name is not UNSET:
            field_dict["name"] = name
        if template_id is not UNSET:
            field_dict["template_id"] = template_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ui_trigger_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ui_trigger_name = _parse_ui_trigger_name(d.pop("ui_trigger_name", UNSET))

        _ui_trigger_kinds = d.pop("ui_trigger_kinds", UNSET)
        ui_trigger_kinds: list[ProcessFilterRequestUiTriggerKindChoices] | Unset = UNSET
        if _ui_trigger_kinds is not UNSET:
            ui_trigger_kinds = []
            for ui_trigger_kinds_item_data in _ui_trigger_kinds:
                ui_trigger_kinds_item = ProcessFilterRequestUiTriggerKindChoices(ui_trigger_kinds_item_data)

                ui_trigger_kinds.append(ui_trigger_kinds_item)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_template_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                template_id_type_0 = UUID(data)

                return template_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        template_id = _parse_template_id(d.pop("template_id", UNSET))

        process_filter_request = cls(
            ui_trigger_name=ui_trigger_name,
            ui_trigger_kinds=ui_trigger_kinds,
            name=name,
            template_id=template_id,
        )

        process_filter_request.additional_properties = d
        return process_filter_request

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
