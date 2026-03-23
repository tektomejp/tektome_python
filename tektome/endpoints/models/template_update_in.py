from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_type_choices import ProcessTypeChoices
from ..models.ui_trigger_kind_choices import UiTriggerKindChoices
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_override_input_schema import TemplateOverrideInputSchema


T = TypeVar("T", bound="TemplateUpdateIn")


@_attrs_define
class TemplateUpdateIn:
    """Schema for updating an existing template.

    Attributes:
        name (str): The name of the template.
        description (str): A brief description of the template.
        ui_trigger_name (None | str | Unset): The name of the UI trigger associated with the template.
        ui_trigger_kind (None | UiTriggerKindChoices | Unset): The kind of the UI trigger associated with the template.
            Possible values are defined in UiTriggerKindChoices.
        is_active (bool | Unset): Whether the template is active. Default: True.
        input_schema_patch (None | TemplateOverrideInputSchema | Unset): Overrides the original template's input schema.
        is_available_to_all_dataspaces (bool | Unset): Whether the template is available to all dataspaces. Default:
            False.
        is_default_to_all_dataspaces (bool | Unset): Whether the template is default to all dataspaces. Default: False.
        is_available_to_all_projects (bool | Unset): Whether the template is available to all projects. Default: False.
        is_default_to_all_projects (bool | Unset): Whether the template is default to all projects. Default: False.
        type_ (ProcessTypeChoices | Unset):  Default: ProcessTypeChoices.GENERAL.
    """

    name: str
    description: str
    ui_trigger_name: None | str | Unset = UNSET
    ui_trigger_kind: None | UiTriggerKindChoices | Unset = UNSET
    is_active: bool | Unset = True
    input_schema_patch: None | TemplateOverrideInputSchema | Unset = UNSET
    is_available_to_all_dataspaces: bool | Unset = False
    is_default_to_all_dataspaces: bool | Unset = False
    is_available_to_all_projects: bool | Unset = False
    is_default_to_all_projects: bool | Unset = False
    type_: ProcessTypeChoices | Unset = ProcessTypeChoices.GENERAL
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_override_input_schema import TemplateOverrideInputSchema

        name = self.name

        description = self.description

        ui_trigger_name: None | str | Unset
        if isinstance(self.ui_trigger_name, Unset):
            ui_trigger_name = UNSET
        else:
            ui_trigger_name = self.ui_trigger_name

        ui_trigger_kind: None | str | Unset
        if isinstance(self.ui_trigger_kind, Unset):
            ui_trigger_kind = UNSET
        elif isinstance(self.ui_trigger_kind, UiTriggerKindChoices):
            ui_trigger_kind = self.ui_trigger_kind.value
        else:
            ui_trigger_kind = self.ui_trigger_kind

        is_active = self.is_active

        input_schema_patch: dict[str, Any] | None | Unset
        if isinstance(self.input_schema_patch, Unset):
            input_schema_patch = UNSET
        elif isinstance(self.input_schema_patch, TemplateOverrideInputSchema):
            input_schema_patch = self.input_schema_patch.to_dict()
        else:
            input_schema_patch = self.input_schema_patch

        is_available_to_all_dataspaces = self.is_available_to_all_dataspaces

        is_default_to_all_dataspaces = self.is_default_to_all_dataspaces

        is_available_to_all_projects = self.is_available_to_all_projects

        is_default_to_all_projects = self.is_default_to_all_projects

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
            }
        )
        if ui_trigger_name is not UNSET:
            field_dict["ui_trigger_name"] = ui_trigger_name
        if ui_trigger_kind is not UNSET:
            field_dict["ui_trigger_kind"] = ui_trigger_kind
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if input_schema_patch is not UNSET:
            field_dict["input_schema_patch"] = input_schema_patch
        if is_available_to_all_dataspaces is not UNSET:
            field_dict["is_available_to_all_dataspaces"] = is_available_to_all_dataspaces
        if is_default_to_all_dataspaces is not UNSET:
            field_dict["is_default_to_all_dataspaces"] = is_default_to_all_dataspaces
        if is_available_to_all_projects is not UNSET:
            field_dict["is_available_to_all_projects"] = is_available_to_all_projects
        if is_default_to_all_projects is not UNSET:
            field_dict["is_default_to_all_projects"] = is_default_to_all_projects
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_override_input_schema import TemplateOverrideInputSchema

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        def _parse_ui_trigger_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ui_trigger_name = _parse_ui_trigger_name(d.pop("ui_trigger_name", UNSET))

        def _parse_ui_trigger_kind(data: object) -> None | UiTriggerKindChoices | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ui_trigger_kind_type_0 = UiTriggerKindChoices(data)

                return ui_trigger_kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UiTriggerKindChoices | Unset, data)

        ui_trigger_kind = _parse_ui_trigger_kind(d.pop("ui_trigger_kind", UNSET))

        is_active = d.pop("is_active", UNSET)

        def _parse_input_schema_patch(data: object) -> None | TemplateOverrideInputSchema | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_schema_patch_type_0 = TemplateOverrideInputSchema.from_dict(data)

                return input_schema_patch_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TemplateOverrideInputSchema | Unset, data)

        input_schema_patch = _parse_input_schema_patch(d.pop("input_schema_patch", UNSET))

        is_available_to_all_dataspaces = d.pop("is_available_to_all_dataspaces", UNSET)

        is_default_to_all_dataspaces = d.pop("is_default_to_all_dataspaces", UNSET)

        is_available_to_all_projects = d.pop("is_available_to_all_projects", UNSET)

        is_default_to_all_projects = d.pop("is_default_to_all_projects", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ProcessTypeChoices | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ProcessTypeChoices(_type_)

        template_update_in = cls(
            name=name,
            description=description,
            ui_trigger_name=ui_trigger_name,
            ui_trigger_kind=ui_trigger_kind,
            is_active=is_active,
            input_schema_patch=input_schema_patch,
            is_available_to_all_dataspaces=is_available_to_all_dataspaces,
            is_default_to_all_dataspaces=is_default_to_all_dataspaces,
            is_available_to_all_projects=is_available_to_all_projects,
            is_default_to_all_projects=is_default_to_all_projects,
            type_=type_,
        )

        template_update_in.additional_properties = d
        return template_update_in

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
