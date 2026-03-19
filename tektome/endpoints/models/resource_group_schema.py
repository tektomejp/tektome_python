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
    from ..models.attribute_schema import AttributeSchema
    from ..models.folder_schema import FolderSchema
    from ..models.lawtalk_resource_group_required_schema import LawtalkResourceGroupRequiredSchema
    from ..models.resource_schema_2 import ResourceSchema2
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="ResourceGroupSchema")


@_attrs_define
class ResourceGroupSchema:
    """
    Attributes:
        lawtalk_attributes (list[AttributeSchema]):
        core_attributes (LawtalkResourceGroupRequiredSchema):
        file_count (int):
        root_folder (FolderSchema):
        created_by (UserMetadata):
        updated_by (UserMetadata):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        resources (list[ResourceSchema2] | Unset):
    """

    lawtalk_attributes: list[AttributeSchema]
    core_attributes: LawtalkResourceGroupRequiredSchema
    file_count: int
    root_folder: FolderSchema
    created_by: UserMetadata
    updated_by: UserMetadata
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    resources: list[ResourceSchema2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lawtalk_attributes = []
        for lawtalk_attributes_item_data in self.lawtalk_attributes:
            lawtalk_attributes_item = lawtalk_attributes_item_data.to_dict()
            lawtalk_attributes.append(lawtalk_attributes_item)

        core_attributes = self.core_attributes.to_dict()

        file_count = self.file_count

        root_folder = self.root_folder.to_dict()

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        resources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()
                resources.append(resources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lawtalk_attributes": lawtalk_attributes,
                "core_attributes": core_attributes,
                "file_count": file_count,
                "root_folder": root_folder,
                "created_by": created_by,
                "updated_by": updated_by,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_schema import AttributeSchema
        from ..models.folder_schema import FolderSchema
        from ..models.lawtalk_resource_group_required_schema import LawtalkResourceGroupRequiredSchema
        from ..models.resource_schema_2 import ResourceSchema2
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        lawtalk_attributes = []
        _lawtalk_attributes = d.pop("lawtalk_attributes")
        for lawtalk_attributes_item_data in _lawtalk_attributes:
            lawtalk_attributes_item = AttributeSchema.from_dict(lawtalk_attributes_item_data)

            lawtalk_attributes.append(lawtalk_attributes_item)

        core_attributes = LawtalkResourceGroupRequiredSchema.from_dict(d.pop("core_attributes"))

        file_count = d.pop("file_count")

        root_folder = FolderSchema.from_dict(d.pop("root_folder"))

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

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

        _resources = d.pop("resources", UNSET)
        resources: list[ResourceSchema2] | Unset = UNSET
        if _resources is not UNSET:
            resources = []
            for resources_item_data in _resources:
                resources_item = ResourceSchema2.from_dict(resources_item_data)

                resources.append(resources_item)

        resource_group_schema = cls(
            lawtalk_attributes=lawtalk_attributes,
            core_attributes=core_attributes,
            file_count=file_count,
            root_folder=root_folder,
            created_by=created_by,
            updated_by=updated_by,
            created=created,
            updated=updated,
            id=id,
            resources=resources,
        )

        resource_group_schema.additional_properties = d
        return resource_group_schema

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
