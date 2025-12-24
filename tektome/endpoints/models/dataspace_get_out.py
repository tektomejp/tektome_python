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
    from ..models.dataspace_required_schema import DataspaceRequiredSchema
    from ..models.dataspace_resource_file_attribute_post_out import DataspaceResourceFileAttributePostOut
    from ..models.dataspaces_organization_schema import DataspacesOrganizationSchema


T = TypeVar("T", bound="DataspaceGetOut")


@_attrs_define
class DataspaceGetOut:
    """
    Attributes:
        core_attributes (DataspaceRequiredSchema):
        created (datetime.datetime):
        updated (datetime.datetime):
        organization (DataspacesOrganizationSchema):
        is_external (bool): Is the dataspace external from the organization
        id (None | Unset | UUID):
        created_by (None | Unset | UUID):
        updated_by (None | Unset | UUID):
        icon (None | str | Unset):
        core_project_attr_config (list[DataspaceProjectAttributePostOut] | Unset):
        core_resource_file_attr_config (list[DataspaceResourceFileAttributePostOut] | Unset):
    """

    core_attributes: DataspaceRequiredSchema
    created: datetime.datetime
    updated: datetime.datetime
    organization: DataspacesOrganizationSchema
    is_external: bool
    id: None | Unset | UUID = UNSET
    created_by: None | Unset | UUID = UNSET
    updated_by: None | Unset | UUID = UNSET
    icon: None | str | Unset = UNSET
    core_project_attr_config: list[DataspaceProjectAttributePostOut] | Unset = UNSET
    core_resource_file_attr_config: list[DataspaceResourceFileAttributePostOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        core_attributes = self.core_attributes.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        organization = self.organization.to_dict()

        is_external = self.is_external

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

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        core_project_attr_config: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.core_project_attr_config, Unset):
            core_project_attr_config = []
            for core_project_attr_config_item_data in self.core_project_attr_config:
                core_project_attr_config_item = core_project_attr_config_item_data.to_dict()
                core_project_attr_config.append(core_project_attr_config_item)

        core_resource_file_attr_config: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.core_resource_file_attr_config, Unset):
            core_resource_file_attr_config = []
            for core_resource_file_attr_config_item_data in self.core_resource_file_attr_config:
                core_resource_file_attr_config_item = core_resource_file_attr_config_item_data.to_dict()
                core_resource_file_attr_config.append(core_resource_file_attr_config_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "core_attributes": core_attributes,
                "created": created,
                "updated": updated,
                "organization": organization,
                "is_external": is_external,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if icon is not UNSET:
            field_dict["icon"] = icon
        if core_project_attr_config is not UNSET:
            field_dict["core_project_attr_config"] = core_project_attr_config
        if core_resource_file_attr_config is not UNSET:
            field_dict["core_resource_file_attr_config"] = core_resource_file_attr_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_project_attribute_post_out import DataspaceProjectAttributePostOut
        from ..models.dataspace_required_schema import DataspaceRequiredSchema
        from ..models.dataspace_resource_file_attribute_post_out import DataspaceResourceFileAttributePostOut
        from ..models.dataspaces_organization_schema import DataspacesOrganizationSchema

        d = dict(src_dict)
        core_attributes = DataspaceRequiredSchema.from_dict(d.pop("core_attributes"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        organization = DataspacesOrganizationSchema.from_dict(d.pop("organization"))

        is_external = d.pop("is_external")

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

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        _core_project_attr_config = d.pop("core_project_attr_config", UNSET)
        core_project_attr_config: list[DataspaceProjectAttributePostOut] | Unset = UNSET
        if _core_project_attr_config is not UNSET:
            core_project_attr_config = []
            for core_project_attr_config_item_data in _core_project_attr_config:
                core_project_attr_config_item = DataspaceProjectAttributePostOut.from_dict(
                    core_project_attr_config_item_data
                )

                core_project_attr_config.append(core_project_attr_config_item)

        _core_resource_file_attr_config = d.pop("core_resource_file_attr_config", UNSET)
        core_resource_file_attr_config: list[DataspaceResourceFileAttributePostOut] | Unset = UNSET
        if _core_resource_file_attr_config is not UNSET:
            core_resource_file_attr_config = []
            for core_resource_file_attr_config_item_data in _core_resource_file_attr_config:
                core_resource_file_attr_config_item = DataspaceResourceFileAttributePostOut.from_dict(
                    core_resource_file_attr_config_item_data
                )

                core_resource_file_attr_config.append(core_resource_file_attr_config_item)

        dataspace_get_out = cls(
            core_attributes=core_attributes,
            created=created,
            updated=updated,
            organization=organization,
            is_external=is_external,
            id=id,
            created_by=created_by,
            updated_by=updated_by,
            icon=icon,
            core_project_attr_config=core_project_attr_config,
            core_resource_file_attr_config=core_resource_file_attr_config,
        )

        dataspace_get_out.additional_properties = d
        return dataspace_get_out

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
