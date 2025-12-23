from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_type_choices import ProcessTypeChoices
from ..models.ui_trigger_kind_choices import UiTriggerKindChoices
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_override_input_schema import TemplateOverrideInputSchema


T = TypeVar("T", bound="ProcessPostIn")


@_attrs_define
class ProcessPostIn:
    """
    Attributes:
        name (str): The name of the process.
        description (str): A brief description of the process.
        template_id (UUID): The template to register this process from.
        is_active (bool | Unset): Whether the template is active. Default: True.
        type_ (ProcessTypeChoices | Unset):  Default: ProcessTypeChoices.GENERAL.
        ui_trigger_name (None | str | Unset): The name of the UI trigger associated with the template.
        ui_trigger_kind (None | UiTriggerKindChoices | Unset): The kind of the UI trigger associated with the template.
            Possible values are defined in UiTriggerKindChoices.
        project_attribute_ids (list[UUID] | Unset): The ID list of project attributes linked to an
            ENTITY_ATTRIBUTE_EXTRACTION
        resource_attribute_ids (list[UUID] | Unset): The ID list of resource attributes linked to an
            FILE_ATTRIBUTE_EXTRACTION
        input_schema_patch (None | TemplateOverrideInputSchema | Unset): Overrides the original template's input schema.
    """

    name: str
    description: str
    template_id: UUID
    is_active: bool | Unset = True
    type_: ProcessTypeChoices | Unset = ProcessTypeChoices.GENERAL
    ui_trigger_name: None | str | Unset = UNSET
    ui_trigger_kind: None | UiTriggerKindChoices | Unset = UNSET
    project_attribute_ids: list[UUID] | Unset = UNSET
    resource_attribute_ids: list[UUID] | Unset = UNSET
    input_schema_patch: None | TemplateOverrideInputSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_override_input_schema import TemplateOverrideInputSchema

        name = self.name

        description = self.description

        template_id = str(self.template_id)

        is_active = self.is_active

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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

        project_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.project_attribute_ids, Unset):
            project_attribute_ids = []
            for project_attribute_ids_item_data in self.project_attribute_ids:
                project_attribute_ids_item = str(project_attribute_ids_item_data)
                project_attribute_ids.append(project_attribute_ids_item)

        resource_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.resource_attribute_ids, Unset):
            resource_attribute_ids = []
            for resource_attribute_ids_item_data in self.resource_attribute_ids:
                resource_attribute_ids_item = str(resource_attribute_ids_item_data)
                resource_attribute_ids.append(resource_attribute_ids_item)

        input_schema_patch: dict[str, Any] | None | Unset
        if isinstance(self.input_schema_patch, Unset):
            input_schema_patch = UNSET
        elif isinstance(self.input_schema_patch, TemplateOverrideInputSchema):
            input_schema_patch = self.input_schema_patch.to_dict()
        else:
            input_schema_patch = self.input_schema_patch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "template_id": template_id,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ui_trigger_name is not UNSET:
            field_dict["ui_trigger_name"] = ui_trigger_name
        if ui_trigger_kind is not UNSET:
            field_dict["ui_trigger_kind"] = ui_trigger_kind
        if project_attribute_ids is not UNSET:
            field_dict["project_attribute_ids"] = project_attribute_ids
        if resource_attribute_ids is not UNSET:
            field_dict["resource_attribute_ids"] = resource_attribute_ids
        if input_schema_patch is not UNSET:
            field_dict["input_schema_patch"] = input_schema_patch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_override_input_schema import TemplateOverrideInputSchema

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        template_id = UUID(d.pop("template_id"))

        is_active = d.pop("is_active", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ProcessTypeChoices | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ProcessTypeChoices(_type_)

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

        _project_attribute_ids = d.pop("project_attribute_ids", UNSET)
        project_attribute_ids: list[UUID] | Unset = UNSET
        if _project_attribute_ids is not UNSET:
            project_attribute_ids = []
            for project_attribute_ids_item_data in _project_attribute_ids:
                project_attribute_ids_item = UUID(project_attribute_ids_item_data)

                project_attribute_ids.append(project_attribute_ids_item)

        _resource_attribute_ids = d.pop("resource_attribute_ids", UNSET)
        resource_attribute_ids: list[UUID] | Unset = UNSET
        if _resource_attribute_ids is not UNSET:
            resource_attribute_ids = []
            for resource_attribute_ids_item_data in _resource_attribute_ids:
                resource_attribute_ids_item = UUID(resource_attribute_ids_item_data)

                resource_attribute_ids.append(resource_attribute_ids_item)

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

        process_post_in = cls(
            name=name,
            description=description,
            template_id=template_id,
            is_active=is_active,
            type_=type_,
            ui_trigger_name=ui_trigger_name,
            ui_trigger_kind=ui_trigger_kind,
            project_attribute_ids=project_attribute_ids,
            resource_attribute_ids=resource_attribute_ids,
            input_schema_patch=input_schema_patch,
        )

        process_post_in.additional_properties = d
        return process_post_in

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
