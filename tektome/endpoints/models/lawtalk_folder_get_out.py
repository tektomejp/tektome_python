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
    from ..models.folder_level_metadata import FolderLevelMetadata
    from ..models.folder_required_schema import FolderRequiredSchema
    from ..models.resource_schema_2 import ResourceSchema2


T = TypeVar("T", bound="LawtalkFolderGetOut")


@_attrs_define
class LawtalkFolderGetOut:
    """
    Attributes:
        core_attributes (FolderRequiredSchema): Folder required schema
        resources (list[ResourceSchema2]):
        children (list[FolderLevelMetadata]):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
    """

    core_attributes: FolderRequiredSchema
    resources: list[ResourceSchema2]
    children: list[FolderLevelMetadata]
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        core_attributes = self.core_attributes.to_dict()

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "core_attributes": core_attributes,
                "resources": resources,
                "children": children,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.folder_level_metadata import FolderLevelMetadata
        from ..models.folder_required_schema import FolderRequiredSchema
        from ..models.resource_schema_2 import ResourceSchema2

        d = dict(src_dict)
        core_attributes = FolderRequiredSchema.from_dict(d.pop("core_attributes"))

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = ResourceSchema2.from_dict(resources_item_data)

            resources.append(resources_item)

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = FolderLevelMetadata.from_dict(children_item_data)

            children.append(children_item)

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

        lawtalk_folder_get_out = cls(
            core_attributes=core_attributes,
            resources=resources,
            children=children,
            created=created,
            updated=updated,
            id=id,
        )

        lawtalk_folder_get_out.additional_properties = d
        return lawtalk_folder_get_out

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
