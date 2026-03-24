from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataspace_counts_get_out import DataspaceCountsGetOut
    from ..models.folder_resource_counts_out import FolderResourceCountsOut
    from ..models.project_resource_counts_out import ProjectResourceCountsOut


T = TypeVar("T", bound="ResourceCountsPostOut")


@_attrs_define
class ResourceCountsPostOut:
    """
    Attributes:
        folders_resource_counts (FolderResourceCountsOut):
        projects_resource_counts (ProjectResourceCountsOut):
        dataspace_counts (DataspaceCountsGetOut):
    """

    folders_resource_counts: FolderResourceCountsOut
    projects_resource_counts: ProjectResourceCountsOut
    dataspace_counts: DataspaceCountsGetOut
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folders_resource_counts = self.folders_resource_counts.to_dict()

        projects_resource_counts = self.projects_resource_counts.to_dict()

        dataspace_counts = self.dataspace_counts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folders_resource_counts": folders_resource_counts,
                "projects_resource_counts": projects_resource_counts,
                "dataspace_counts": dataspace_counts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_counts_get_out import DataspaceCountsGetOut
        from ..models.folder_resource_counts_out import FolderResourceCountsOut
        from ..models.project_resource_counts_out import ProjectResourceCountsOut

        d = dict(src_dict)
        folders_resource_counts = FolderResourceCountsOut.from_dict(d.pop("folders_resource_counts"))

        projects_resource_counts = ProjectResourceCountsOut.from_dict(d.pop("projects_resource_counts"))

        dataspace_counts = DataspaceCountsGetOut.from_dict(d.pop("dataspace_counts"))

        resource_counts_post_out = cls(
            folders_resource_counts=folders_resource_counts,
            projects_resource_counts=projects_resource_counts,
            dataspace_counts=dataspace_counts,
        )

        resource_counts_post_out.additional_properties = d
        return resource_counts_post_out

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
