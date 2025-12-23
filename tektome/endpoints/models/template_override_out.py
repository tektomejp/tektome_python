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
    from ..models.template_override_out_input_schema_patch_type_0 import TemplateOverrideOutInputSchemaPatchType0


T = TypeVar("T", bound="TemplateOverrideOut")


@_attrs_define
class TemplateOverrideOut:
    """
    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        template (UUID):
        organization (UUID):
        id (None | Unset | UUID):
        created_by (None | Unset | UUID):
        updated_by (None | Unset | UUID):
        is_active (bool | Unset):  Default: True.
        is_modified (bool | Unset):  Default: False.
        dataspace (None | Unset | UUID):
        project (None | Unset | UUID):
        ui_trigger_name (None | str | Unset):
        ui_trigger_kind (None | str | Unset):
        input_schema_patch (None | TemplateOverrideOutInputSchemaPatchType0 | Unset):
    """

    created: datetime.datetime
    updated: datetime.datetime
    template: UUID
    organization: UUID
    id: None | Unset | UUID = UNSET
    created_by: None | Unset | UUID = UNSET
    updated_by: None | Unset | UUID = UNSET
    is_active: bool | Unset = True
    is_modified: bool | Unset = False
    dataspace: None | Unset | UUID = UNSET
    project: None | Unset | UUID = UNSET
    ui_trigger_name: None | str | Unset = UNSET
    ui_trigger_kind: None | str | Unset = UNSET
    input_schema_patch: None | TemplateOverrideOutInputSchemaPatchType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_override_out_input_schema_patch_type_0 import TemplateOverrideOutInputSchemaPatchType0

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        template = str(self.template)

        organization = str(self.organization)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UUID):
            updated_by = str(self.updated_by)
        else:
            updated_by = self.updated_by

        is_active = self.is_active

        is_modified = self.is_modified

        dataspace: None | str | Unset
        if isinstance(self.dataspace, Unset):
            dataspace = UNSET
        elif isinstance(self.dataspace, UUID):
            dataspace = str(self.dataspace)
        else:
            dataspace = self.dataspace

        project: None | str | Unset
        if isinstance(self.project, Unset):
            project = UNSET
        elif isinstance(self.project, UUID):
            project = str(self.project)
        else:
            project = self.project

        ui_trigger_name: None | str | Unset
        if isinstance(self.ui_trigger_name, Unset):
            ui_trigger_name = UNSET
        else:
            ui_trigger_name = self.ui_trigger_name

        ui_trigger_kind: None | str | Unset
        if isinstance(self.ui_trigger_kind, Unset):
            ui_trigger_kind = UNSET
        else:
            ui_trigger_kind = self.ui_trigger_kind

        input_schema_patch: dict[str, Any] | None | Unset
        if isinstance(self.input_schema_patch, Unset):
            input_schema_patch = UNSET
        elif isinstance(self.input_schema_patch, TemplateOverrideOutInputSchemaPatchType0):
            input_schema_patch = self.input_schema_patch.to_dict()
        else:
            input_schema_patch = self.input_schema_patch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
                "template": template,
                "organization": organization,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_modified is not UNSET:
            field_dict["is_modified"] = is_modified
        if dataspace is not UNSET:
            field_dict["dataspace"] = dataspace
        if project is not UNSET:
            field_dict["project"] = project
        if ui_trigger_name is not UNSET:
            field_dict["ui_trigger_name"] = ui_trigger_name
        if ui_trigger_kind is not UNSET:
            field_dict["ui_trigger_kind"] = ui_trigger_kind
        if input_schema_patch is not UNSET:
            field_dict["input_schema_patch"] = input_schema_patch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_override_out_input_schema_patch_type_0 import TemplateOverrideOutInputSchemaPatchType0

        d = dict(src_dict)
        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        template = UUID(d.pop("template"))

        organization = UUID(d.pop("organization"))

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

        def _parse_created_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_by_type_0 = UUID(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        is_active = d.pop("is_active", UNSET)

        is_modified = d.pop("is_modified", UNSET)

        def _parse_dataspace(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dataspace_type_0 = UUID(data)

                return dataspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dataspace = _parse_dataspace(d.pop("dataspace", UNSET))

        def _parse_project(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_type_0 = UUID(data)

                return project_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        project = _parse_project(d.pop("project", UNSET))

        def _parse_ui_trigger_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ui_trigger_name = _parse_ui_trigger_name(d.pop("ui_trigger_name", UNSET))

        def _parse_ui_trigger_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ui_trigger_kind = _parse_ui_trigger_kind(d.pop("ui_trigger_kind", UNSET))

        def _parse_input_schema_patch(data: object) -> None | TemplateOverrideOutInputSchemaPatchType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_schema_patch_type_0 = TemplateOverrideOutInputSchemaPatchType0.from_dict(data)

                return input_schema_patch_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TemplateOverrideOutInputSchemaPatchType0 | Unset, data)

        input_schema_patch = _parse_input_schema_patch(d.pop("input_schema_patch", UNSET))

        template_override_out = cls(
            created=created,
            updated=updated,
            template=template,
            organization=organization,
            id=id,
            created_by=created_by,
            updated_by=updated_by,
            is_active=is_active,
            is_modified=is_modified,
            dataspace=dataspace,
            project=project,
            ui_trigger_name=ui_trigger_name,
            ui_trigger_kind=ui_trigger_kind,
            input_schema_patch=input_schema_patch,
        )

        template_override_out.additional_properties = d
        return template_override_out

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
