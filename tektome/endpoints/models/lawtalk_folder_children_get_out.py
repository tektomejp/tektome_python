from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.folder_required_schema import FolderRequiredSchema
    from ..models.lawtalk_resource_children import LawtalkResourceChildren
    from ..models.resource_folder_children_schema import ResourceFolderChildrenSchema


T = TypeVar("T", bound="LawtalkFolderChildrenGetOut")


@_attrs_define
class LawtalkFolderChildrenGetOut:
    """
    Attributes:
        core_attributes (FolderRequiredSchema): Folder required schema
        resources (list[LawtalkResourceChildren]):
        folders (list[ResourceFolderChildrenSchema]):
        count (int):
        total_page (int):
    """

    core_attributes: FolderRequiredSchema
    resources: list[LawtalkResourceChildren]
    folders: list[ResourceFolderChildrenSchema]
    count: int
    total_page: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        core_attributes = self.core_attributes.to_dict()

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        folders = []
        for folders_item_data in self.folders:
            folders_item = folders_item_data.to_dict()
            folders.append(folders_item)

        count = self.count

        total_page = self.total_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "core_attributes": core_attributes,
                "resources": resources,
                "folders": folders,
                "count": count,
                "total_page": total_page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.folder_required_schema import FolderRequiredSchema
        from ..models.lawtalk_resource_children import LawtalkResourceChildren
        from ..models.resource_folder_children_schema import ResourceFolderChildrenSchema

        d = dict(src_dict)
        core_attributes = FolderRequiredSchema.from_dict(d.pop("core_attributes"))

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = LawtalkResourceChildren.from_dict(resources_item_data)

            resources.append(resources_item)

        folders = []
        _folders = d.pop("folders")
        for folders_item_data in _folders:
            folders_item = ResourceFolderChildrenSchema.from_dict(folders_item_data)

            folders.append(folders_item)

        count = d.pop("count")

        total_page = d.pop("total_page")

        lawtalk_folder_children_get_out = cls(
            core_attributes=core_attributes,
            resources=resources,
            folders=folders,
            count=count,
            total_page=total_page,
        )

        lawtalk_folder_children_get_out.additional_properties = d
        return lawtalk_folder_children_get_out

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
