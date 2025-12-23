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
    from ..models.template_out_openflow_json import TemplateOutOpenflowJson
    from ..models.template_override_out import TemplateOverrideOut
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="TemplateOut")


@_attrs_define
class TemplateOut:
    """
    Attributes:
        created_by (None | UserMetadata):
        updated_by (None | UserMetadata):
        owner_type (str):
        override_data (None | TemplateOverrideOut):
        created (datetime.datetime):
        updated (datetime.datetime):
        name (str):
        organization (UUID):
        process_count (int | None | Unset):
        id (None | Unset | UUID):
        description (None | str | Unset):  Default: ''.
        artifact (None | Unset | UUID):
        openflow_json (TemplateOutOpenflowJson | Unset):
        is_active (bool | Unset):  Default: True.
        is_system (bool | Unset):  Default: False.
        is_available_to_all_dataspaces (bool | Unset):  Default: False.
        is_default_to_all_dataspaces (bool | Unset):  Default: False.
        is_available_to_all_projects (bool | Unset):  Default: False.
        is_default_to_all_projects (bool | Unset):  Default: False.
        type_ (str | Unset):  Default: 'general'.
        ui_trigger_name (None | str | Unset):
        ui_trigger_kind (None | str | Unset):
    """

    created_by: None | UserMetadata
    updated_by: None | UserMetadata
    owner_type: str
    override_data: None | TemplateOverrideOut
    created: datetime.datetime
    updated: datetime.datetime
    name: str
    organization: UUID
    process_count: int | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    description: None | str | Unset = ""
    artifact: None | Unset | UUID = UNSET
    openflow_json: TemplateOutOpenflowJson | Unset = UNSET
    is_active: bool | Unset = True
    is_system: bool | Unset = False
    is_available_to_all_dataspaces: bool | Unset = False
    is_default_to_all_dataspaces: bool | Unset = False
    is_available_to_all_projects: bool | Unset = False
    is_default_to_all_projects: bool | Unset = False
    type_: str | Unset = "general"
    ui_trigger_name: None | str | Unset = UNSET
    ui_trigger_kind: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_override_out import TemplateOverrideOut
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

        owner_type = self.owner_type

        override_data: dict[str, Any] | None
        if isinstance(self.override_data, TemplateOverrideOut):
            override_data = self.override_data.to_dict()
        else:
            override_data = self.override_data

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        name = self.name

        organization = str(self.organization)

        process_count: int | None | Unset
        if isinstance(self.process_count, Unset):
            process_count = UNSET
        else:
            process_count = self.process_count

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

        artifact: None | str | Unset
        if isinstance(self.artifact, Unset):
            artifact = UNSET
        elif isinstance(self.artifact, UUID):
            artifact = str(self.artifact)
        else:
            artifact = self.artifact

        openflow_json: dict[str, Any] | Unset = UNSET
        if not isinstance(self.openflow_json, Unset):
            openflow_json = self.openflow_json.to_dict()

        is_active = self.is_active

        is_system = self.is_system

        is_available_to_all_dataspaces = self.is_available_to_all_dataspaces

        is_default_to_all_dataspaces = self.is_default_to_all_dataspaces

        is_available_to_all_projects = self.is_available_to_all_projects

        is_default_to_all_projects = self.is_default_to_all_projects

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "owner_type": owner_type,
                "override_data": override_data,
                "created": created,
                "updated": updated,
                "name": name,
                "organization": organization,
            }
        )
        if process_count is not UNSET:
            field_dict["process_count"] = process_count
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if artifact is not UNSET:
            field_dict["artifact"] = artifact
        if openflow_json is not UNSET:
            field_dict["openflow_json"] = openflow_json
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
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
        if ui_trigger_name is not UNSET:
            field_dict["ui_trigger_name"] = ui_trigger_name
        if ui_trigger_kind is not UNSET:
            field_dict["ui_trigger_kind"] = ui_trigger_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_out_openflow_json import TemplateOutOpenflowJson
        from ..models.template_override_out import TemplateOverrideOut
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

        owner_type = d.pop("owner_type")

        def _parse_override_data(data: object) -> None | TemplateOverrideOut:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                override_data_type_0 = TemplateOverrideOut.from_dict(data)

                return override_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TemplateOverrideOut, data)

        override_data = _parse_override_data(d.pop("override_data"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        name = d.pop("name")

        organization = UUID(d.pop("organization"))

        def _parse_process_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        process_count = _parse_process_count(d.pop("process_count", UNSET))

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

        def _parse_artifact(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                artifact_type_0 = UUID(data)

                return artifact_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        artifact = _parse_artifact(d.pop("artifact", UNSET))

        _openflow_json = d.pop("openflow_json", UNSET)
        openflow_json: TemplateOutOpenflowJson | Unset
        if isinstance(_openflow_json, Unset):
            openflow_json = UNSET
        else:
            openflow_json = TemplateOutOpenflowJson.from_dict(_openflow_json)

        is_active = d.pop("is_active", UNSET)

        is_system = d.pop("is_system", UNSET)

        is_available_to_all_dataspaces = d.pop("is_available_to_all_dataspaces", UNSET)

        is_default_to_all_dataspaces = d.pop("is_default_to_all_dataspaces", UNSET)

        is_available_to_all_projects = d.pop("is_available_to_all_projects", UNSET)

        is_default_to_all_projects = d.pop("is_default_to_all_projects", UNSET)

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

        template_out = cls(
            created_by=created_by,
            updated_by=updated_by,
            owner_type=owner_type,
            override_data=override_data,
            created=created,
            updated=updated,
            name=name,
            organization=organization,
            process_count=process_count,
            id=id,
            description=description,
            artifact=artifact,
            openflow_json=openflow_json,
            is_active=is_active,
            is_system=is_system,
            is_available_to_all_dataspaces=is_available_to_all_dataspaces,
            is_default_to_all_dataspaces=is_default_to_all_dataspaces,
            is_available_to_all_projects=is_available_to_all_projects,
            is_default_to_all_projects=is_default_to_all_projects,
            type_=type_,
            ui_trigger_name=ui_trigger_name,
            ui_trigger_kind=ui_trigger_kind,
        )

        template_out.additional_properties = d
        return template_out

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
