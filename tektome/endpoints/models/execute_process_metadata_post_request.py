from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecuteProcessMetadataPostRequest")


@_attrs_define
class ExecuteProcessMetadataPostRequest:
    """
    Attributes:
        project_ids (list[UUID] | Unset):
        folder_ids (list[UUID] | Unset):
        resource_ids (list[UUID] | Unset):
        should_use_dataspace (bool | Unset): Whether to get all metadata from the dataspace. Default: False.
    """

    project_ids: list[UUID] | Unset = UNSET
    folder_ids: list[UUID] | Unset = UNSET
    resource_ids: list[UUID] | Unset = UNSET
    should_use_dataspace: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_ids: list[str] | Unset = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = []
            for project_ids_item_data in self.project_ids:
                project_ids_item = str(project_ids_item_data)
                project_ids.append(project_ids_item)

        folder_ids: list[str] | Unset = UNSET
        if not isinstance(self.folder_ids, Unset):
            folder_ids = []
            for folder_ids_item_data in self.folder_ids:
                folder_ids_item = str(folder_ids_item_data)
                folder_ids.append(folder_ids_item)

        resource_ids: list[str] | Unset = UNSET
        if not isinstance(self.resource_ids, Unset):
            resource_ids = []
            for resource_ids_item_data in self.resource_ids:
                resource_ids_item = str(resource_ids_item_data)
                resource_ids.append(resource_ids_item)

        should_use_dataspace = self.should_use_dataspace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_ids is not UNSET:
            field_dict["project_ids"] = project_ids
        if folder_ids is not UNSET:
            field_dict["folder_ids"] = folder_ids
        if resource_ids is not UNSET:
            field_dict["resource_ids"] = resource_ids
        if should_use_dataspace is not UNSET:
            field_dict["should_use_dataspace"] = should_use_dataspace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _project_ids = d.pop("project_ids", UNSET)
        project_ids: list[UUID] | Unset = UNSET
        if _project_ids is not UNSET:
            project_ids = []
            for project_ids_item_data in _project_ids:
                project_ids_item = UUID(project_ids_item_data)

                project_ids.append(project_ids_item)

        _folder_ids = d.pop("folder_ids", UNSET)
        folder_ids: list[UUID] | Unset = UNSET
        if _folder_ids is not UNSET:
            folder_ids = []
            for folder_ids_item_data in _folder_ids:
                folder_ids_item = UUID(folder_ids_item_data)

                folder_ids.append(folder_ids_item)

        _resource_ids = d.pop("resource_ids", UNSET)
        resource_ids: list[UUID] | Unset = UNSET
        if _resource_ids is not UNSET:
            resource_ids = []
            for resource_ids_item_data in _resource_ids:
                resource_ids_item = UUID(resource_ids_item_data)

                resource_ids.append(resource_ids_item)

        should_use_dataspace = d.pop("should_use_dataspace", UNSET)

        execute_process_metadata_post_request = cls(
            project_ids=project_ids,
            folder_ids=folder_ids,
            resource_ids=resource_ids,
            should_use_dataspace=should_use_dataspace,
        )

        execute_process_metadata_post_request.additional_properties = d
        return execute_process_metadata_post_request

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
