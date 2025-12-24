from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResourceIfcBimProjectCreationPostOut")


@_attrs_define
class ResourceIfcBimProjectCreationPostOut:
    """Output schema for BIM resource creation endpoint

    Attributes:
        task_id (UUID):
        resource_id (UUID):
        bim_project_id (UUID):
        file_name (str):
        created (Any):
        updated (Any):
    """

    task_id: UUID
    resource_id: UUID
    bim_project_id: UUID
    file_name: str
    created: Any
    updated: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = str(self.task_id)

        resource_id = str(self.resource_id)

        bim_project_id = str(self.bim_project_id)

        file_name = self.file_name

        created = self.created

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
                "resource_id": resource_id,
                "bim_project_id": bim_project_id,
                "file_name": file_name,
                "created": created,
                "updated": updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = UUID(d.pop("task_id"))

        resource_id = UUID(d.pop("resource_id"))

        bim_project_id = UUID(d.pop("bim_project_id"))

        file_name = d.pop("file_name")

        created = d.pop("created")

        updated = d.pop("updated")

        resource_ifc_bim_project_creation_post_out = cls(
            task_id=task_id,
            resource_id=resource_id,
            bim_project_id=bim_project_id,
            file_name=file_name,
            created=created,
            updated=updated,
        )

        resource_ifc_bim_project_creation_post_out.additional_properties = d
        return resource_ifc_bim_project_creation_post_out

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
