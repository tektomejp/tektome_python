from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_type_choices import ProcessTypeChoices
from ..models.template_admin_filter_in_ui_trigger_kind_choices import TemplateAdminFilterInUiTriggerKindChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateAdminFilterIn")


@_attrs_define
class TemplateAdminFilterIn:
    """
    Attributes:
        ui_trigger_name (None | str | Unset): Filter templates by UI trigger name.
        ui_trigger_kinds (list[TemplateAdminFilterInUiTriggerKindChoices] | Unset): Filter templates by UI trigger kind.
            Possible values are defined in UiTriggerKindChoices.
        name (None | str | Unset): The name (or part of the name) of the template to search for.
        type_ (None | ProcessTypeChoices | Unset): Filter templates by type. Possible values are defined in
            ProcessTypeChoices.
        for_import (bool | None | Unset): If true, only return templates that can be imported. Otherwise, return all
            available templates, either default or imported.
    """

    ui_trigger_name: None | str | Unset = UNSET
    ui_trigger_kinds: list[TemplateAdminFilterInUiTriggerKindChoices] | Unset = UNSET
    name: None | str | Unset = UNSET
    type_: None | ProcessTypeChoices | Unset = UNSET
    for_import: bool | None | Unset = UNSET
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

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, ProcessTypeChoices):
            type_ = self.type_.value
        else:
            type_ = self.type_

        for_import: bool | None | Unset
        if isinstance(self.for_import, Unset):
            for_import = UNSET
        else:
            for_import = self.for_import

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ui_trigger_name is not UNSET:
            field_dict["ui_trigger_name"] = ui_trigger_name
        if ui_trigger_kinds is not UNSET:
            field_dict["ui_trigger_kinds"] = ui_trigger_kinds
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if for_import is not UNSET:
            field_dict["for_import"] = for_import

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
        ui_trigger_kinds: list[TemplateAdminFilterInUiTriggerKindChoices] | Unset = UNSET
        if _ui_trigger_kinds is not UNSET:
            ui_trigger_kinds = []
            for ui_trigger_kinds_item_data in _ui_trigger_kinds:
                ui_trigger_kinds_item = TemplateAdminFilterInUiTriggerKindChoices(ui_trigger_kinds_item_data)

                ui_trigger_kinds.append(ui_trigger_kinds_item)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_type_(data: object) -> None | ProcessTypeChoices | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = ProcessTypeChoices(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProcessTypeChoices | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_for_import(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        for_import = _parse_for_import(d.pop("for_import", UNSET))

        template_admin_filter_in = cls(
            ui_trigger_name=ui_trigger_name,
            ui_trigger_kinds=ui_trigger_kinds,
            name=name,
            type_=type_,
            for_import=for_import,
        )

        template_admin_filter_in.additional_properties = d
        return template_admin_filter_in

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
