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


T = TypeVar("T", bound="ProcessPostInPatch")


@_attrs_define
class ProcessPostInPatch:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        is_active (bool | None | Unset):
        template_id (None | Unset | UUID):
        type_ (None | ProcessTypeChoices | Unset):
        ui_trigger_name (None | str | Unset): The name of the UI trigger associated with the template.
        ui_trigger_kind (None | UiTriggerKindChoices | Unset): The kind of the UI trigger associated with the template.
            Possible values are defined in UiTriggerKindChoices.
        project_attribute_ids (list[UUID] | None | Unset):
        resource_attribute_ids (list[UUID] | None | Unset):
        input_schema_patch (None | TemplateOverrideInputSchema | Unset): Overrides the original template's input schema.
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    template_id: None | Unset | UUID = UNSET
    type_: None | ProcessTypeChoices | Unset = UNSET
    ui_trigger_name: None | str | Unset = UNSET
    ui_trigger_kind: None | UiTriggerKindChoices | Unset = UNSET
    project_attribute_ids: list[UUID] | None | Unset = UNSET
    resource_attribute_ids: list[UUID] | None | Unset = UNSET
    input_schema_patch: None | TemplateOverrideInputSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_override_input_schema import TemplateOverrideInputSchema

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        template_id: None | str | Unset
        if isinstance(self.template_id, Unset):
            template_id = UNSET
        elif isinstance(self.template_id, UUID):
            template_id = str(self.template_id)
        else:
            template_id = self.template_id

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, ProcessTypeChoices):
            type_ = self.type_.value
        else:
            type_ = self.type_

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

        project_attribute_ids: list[str] | None | Unset
        if isinstance(self.project_attribute_ids, Unset):
            project_attribute_ids = UNSET
        elif isinstance(self.project_attribute_ids, list):
            project_attribute_ids = []
            for project_attribute_ids_type_0_item_data in self.project_attribute_ids:
                project_attribute_ids_type_0_item = str(project_attribute_ids_type_0_item_data)
                project_attribute_ids.append(project_attribute_ids_type_0_item)

        else:
            project_attribute_ids = self.project_attribute_ids

        resource_attribute_ids: list[str] | None | Unset
        if isinstance(self.resource_attribute_ids, Unset):
            resource_attribute_ids = UNSET
        elif isinstance(self.resource_attribute_ids, list):
            resource_attribute_ids = []
            for resource_attribute_ids_type_0_item_data in self.resource_attribute_ids:
                resource_attribute_ids_type_0_item = str(resource_attribute_ids_type_0_item_data)
                resource_attribute_ids.append(resource_attribute_ids_type_0_item)

        else:
            resource_attribute_ids = self.resource_attribute_ids

        input_schema_patch: dict[str, Any] | None | Unset
        if isinstance(self.input_schema_patch, Unset):
            input_schema_patch = UNSET
        elif isinstance(self.input_schema_patch, TemplateOverrideInputSchema):
            input_schema_patch = self.input_schema_patch.to_dict()
        else:
            input_schema_patch = self.input_schema_patch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

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

        def _parse_project_attribute_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                project_attribute_ids_type_0 = []
                _project_attribute_ids_type_0 = data
                for project_attribute_ids_type_0_item_data in _project_attribute_ids_type_0:
                    project_attribute_ids_type_0_item = UUID(project_attribute_ids_type_0_item_data)

                    project_attribute_ids_type_0.append(project_attribute_ids_type_0_item)

                return project_attribute_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        project_attribute_ids = _parse_project_attribute_ids(d.pop("project_attribute_ids", UNSET))

        def _parse_resource_attribute_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resource_attribute_ids_type_0 = []
                _resource_attribute_ids_type_0 = data
                for resource_attribute_ids_type_0_item_data in _resource_attribute_ids_type_0:
                    resource_attribute_ids_type_0_item = UUID(resource_attribute_ids_type_0_item_data)

                    resource_attribute_ids_type_0.append(resource_attribute_ids_type_0_item)

                return resource_attribute_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        resource_attribute_ids = _parse_resource_attribute_ids(d.pop("resource_attribute_ids", UNSET))

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

        process_post_in_patch = cls(
            name=name,
            description=description,
            is_active=is_active,
            template_id=template_id,
            type_=type_,
            ui_trigger_name=ui_trigger_name,
            ui_trigger_kind=ui_trigger_kind,
            project_attribute_ids=project_attribute_ids,
            resource_attribute_ids=resource_attribute_ids,
            input_schema_patch=input_schema_patch,
        )

        process_post_in_patch.additional_properties = d
        return process_post_in_patch

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
