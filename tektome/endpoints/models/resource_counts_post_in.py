from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceCountsPostIn")


@_attrs_define
class ResourceCountsPostIn:
    """
    Attributes:
        folder_ids (list[UUID] | Unset):
        project_ids (list[UUID] | Unset):
    """

    folder_ids: list[UUID] | Unset = UNSET
    project_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folder_ids: list[str] | Unset = UNSET
        if not isinstance(self.folder_ids, Unset):
            folder_ids = []
            for folder_ids_item_data in self.folder_ids:
                folder_ids_item = str(folder_ids_item_data)
                folder_ids.append(folder_ids_item)

        project_ids: list[str] | Unset = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = []
            for project_ids_item_data in self.project_ids:
                project_ids_item = str(project_ids_item_data)
                project_ids.append(project_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if folder_ids is not UNSET:
            field_dict["folder_ids"] = folder_ids
        if project_ids is not UNSET:
            field_dict["project_ids"] = project_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _folder_ids = d.pop("folder_ids", UNSET)
        folder_ids: list[UUID] | Unset = UNSET
        if _folder_ids is not UNSET:
            folder_ids = []
            for folder_ids_item_data in _folder_ids:
                folder_ids_item = UUID(folder_ids_item_data)

                folder_ids.append(folder_ids_item)

        _project_ids = d.pop("project_ids", UNSET)
        project_ids: list[UUID] | Unset = UNSET
        if _project_ids is not UNSET:
            project_ids = []
            for project_ids_item_data in _project_ids:
                project_ids_item = UUID(project_ids_item_data)

                project_ids.append(project_ids_item)

        resource_counts_post_in = cls(
            folder_ids=folder_ids,
            project_ids=project_ids,
        )

        resource_counts_post_in.additional_properties = d
        return resource_counts_post_in

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
