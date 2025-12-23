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
    from ..models.dataspace_project_attribute_post_out import DataspaceProjectAttributePostOut
    from ..models.dataspace_resource_file_attribute_post_out import DataspaceResourceFileAttributePostOut
    from ..models.process_out_input_schema_patch_type_0 import ProcessOutInputSchemaPatchType0
    from ..models.process_out_openflow_json import ProcessOutOpenflowJson
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="ProcessOut")


@_attrs_define
class ProcessOut:
    """
    Attributes:
        created_by (None | UserMetadata):
        updated_by (None | UserMetadata):
        created (datetime.datetime):
        updated (datetime.datetime):
        name (str):
        organization (UUID):
        project_attributes (list[DataspaceProjectAttributePostOut] | Unset):
        resource_attributes (list[DataspaceResourceFileAttributePostOut] | Unset):
        id (None | Unset | UUID):
        description (None | str | Unset):  Default: ''.
        openflow_json (ProcessOutOpenflowJson | Unset):
        is_active (bool | Unset):  Default: True.
        template (None | Unset | UUID):
        dataspace (None | Unset | UUID):
        project (None | Unset | UUID):
        type_ (str | Unset):  Default: 'general'.
        ui_trigger_name (None | str | Unset):
        ui_trigger_kind (None | str | Unset):
        input_schema_patch (None | ProcessOutInputSchemaPatchType0 | Unset):
    """

    created_by: None | UserMetadata
    updated_by: None | UserMetadata
    created: datetime.datetime
    updated: datetime.datetime
    name: str
    organization: UUID
    project_attributes: list[DataspaceProjectAttributePostOut] | Unset = UNSET
    resource_attributes: list[DataspaceResourceFileAttributePostOut] | Unset = UNSET
    id: None | Unset | UUID = UNSET
    description: None | str | Unset = ""
    openflow_json: ProcessOutOpenflowJson | Unset = UNSET
    is_active: bool | Unset = True
    template: None | Unset | UUID = UNSET
    dataspace: None | Unset | UUID = UNSET
    project: None | Unset | UUID = UNSET
    type_: str | Unset = "general"
    ui_trigger_name: None | str | Unset = UNSET
    ui_trigger_kind: None | str | Unset = UNSET
    input_schema_patch: None | ProcessOutInputSchemaPatchType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.process_out_input_schema_patch_type_0 import ProcessOutInputSchemaPatchType0
        from ..models.user_metadata import UserMetadata

        created_by: dict[str, Any] | None
        if isinstance(self.created_by, UserMetadata):
            created_by = self.created_by.to_dict()
        else:
            created_by = self.created_by

        updated_by: dict[str, Any] | None
        if isinstance(self.updated_by, UserMetadata):
            updated_by = self.updated_by.to_dict()
        else:
            updated_by = self.updated_by

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        name = self.name

        organization = str(self.organization)

        project_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.project_attributes, Unset):
            project_attributes = []
            for project_attributes_item_data in self.project_attributes:
                project_attributes_item = project_attributes_item_data.to_dict()
                project_attributes.append(project_attributes_item)

        resource_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resource_attributes, Unset):
            resource_attributes = []
            for resource_attributes_item_data in self.resource_attributes:
                resource_attributes_item = resource_attributes_item_data.to_dict()
                resource_attributes.append(resource_attributes_item)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        openflow_json: dict[str, Any] | Unset = UNSET
        if not isinstance(self.openflow_json, Unset):
            openflow_json = self.openflow_json.to_dict()

        is_active = self.is_active

        template: None | str | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        elif isinstance(self.template, UUID):
            template = str(self.template)
        else:
            template = self.template

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

        type_ = self.type_

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
        elif isinstance(self.input_schema_patch, ProcessOutInputSchemaPatchType0):
            input_schema_patch = self.input_schema_patch.to_dict()
        else:
            input_schema_patch = self.input_schema_patch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "created": created,
                "updated": updated,
                "name": name,
                "organization": organization,
            }
        )
        if project_attributes is not UNSET:
            field_dict["project_attributes"] = project_attributes
        if resource_attributes is not UNSET:
            field_dict["resource_attributes"] = resource_attributes
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if openflow_json is not UNSET:
            field_dict["openflow_json"] = openflow_json
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if template is not UNSET:
            field_dict["template"] = template
        if dataspace is not UNSET:
            field_dict["dataspace"] = dataspace
        if project is not UNSET:
            field_dict["project"] = project
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ui_trigger_name is not UNSET:
            field_dict["ui_trigger_name"] = ui_trigger_name
        if ui_trigger_kind is not UNSET:
            field_dict["ui_trigger_kind"] = ui_trigger_kind
        if input_schema_patch is not UNSET:
            field_dict["input_schema_patch"] = input_schema_patch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_project_attribute_post_out import DataspaceProjectAttributePostOut
        from ..models.dataspace_resource_file_attribute_post_out import DataspaceResourceFileAttributePostOut
        from ..models.process_out_input_schema_patch_type_0 import ProcessOutInputSchemaPatchType0
        from ..models.process_out_openflow_json import ProcessOutOpenflowJson
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)

        def _parse_created_by(data: object) -> None | UserMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_type_0 = UserMetadata.from_dict(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserMetadata, data)

        created_by = _parse_created_by(d.pop("created_by"))

        def _parse_updated_by(data: object) -> None | UserMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_by_type_0 = UserMetadata.from_dict(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserMetadata, data)

        updated_by = _parse_updated_by(d.pop("updated_by"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        name = d.pop("name")

        organization = UUID(d.pop("organization"))

        _project_attributes = d.pop("project_attributes", UNSET)
        project_attributes: list[DataspaceProjectAttributePostOut] | Unset = UNSET
        if _project_attributes is not UNSET:
            project_attributes = []
            for project_attributes_item_data in _project_attributes:
                project_attributes_item = DataspaceProjectAttributePostOut.from_dict(project_attributes_item_data)

                project_attributes.append(project_attributes_item)

        _resource_attributes = d.pop("resource_attributes", UNSET)
        resource_attributes: list[DataspaceResourceFileAttributePostOut] | Unset = UNSET
        if _resource_attributes is not UNSET:
            resource_attributes = []
            for resource_attributes_item_data in _resource_attributes:
                resource_attributes_item = DataspaceResourceFileAttributePostOut.from_dict(
                    resource_attributes_item_data
                )

                resource_attributes.append(resource_attributes_item)

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _openflow_json = d.pop("openflow_json", UNSET)
        openflow_json: ProcessOutOpenflowJson | Unset
        if isinstance(_openflow_json, Unset):
            openflow_json = UNSET
        else:
            openflow_json = ProcessOutOpenflowJson.from_dict(_openflow_json)

        is_active = d.pop("is_active", UNSET)

        def _parse_template(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                template_type_0 = UUID(data)

                return template_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        template = _parse_template(d.pop("template", UNSET))

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

        type_ = d.pop("type", UNSET)

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

        def _parse_input_schema_patch(data: object) -> None | ProcessOutInputSchemaPatchType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_schema_patch_type_0 = ProcessOutInputSchemaPatchType0.from_dict(data)

                return input_schema_patch_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProcessOutInputSchemaPatchType0 | Unset, data)

        input_schema_patch = _parse_input_schema_patch(d.pop("input_schema_patch", UNSET))

        process_out = cls(
            created_by=created_by,
            updated_by=updated_by,
            created=created,
            updated=updated,
            name=name,
            organization=organization,
            project_attributes=project_attributes,
            resource_attributes=resource_attributes,
            id=id,
            description=description,
            openflow_json=openflow_json,
            is_active=is_active,
            template=template,
            dataspace=dataspace,
            project=project,
            type_=type_,
            ui_trigger_name=ui_trigger_name,
            ui_trigger_kind=ui_trigger_kind,
            input_schema_patch=input_schema_patch,
        )

        process_out.additional_properties = d
        return process_out

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
