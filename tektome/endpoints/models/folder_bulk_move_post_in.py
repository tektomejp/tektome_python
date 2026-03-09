from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FolderBulkMovePostIn")


@_attrs_define
class FolderBulkMovePostIn:
    """Schema for bulk moving folders and resources to a target folder.

    Attributes:
        folder_id (UUID):
        folder_ids (list[UUID] | Unset):
        resource_ids (list[UUID] | Unset):
        check_collisions (bool | Unset):  Default: True.
    """

    folder_id: UUID
    folder_ids: list[UUID] | Unset = UNSET
    resource_ids: list[UUID] | Unset = UNSET
    check_collisions: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folder_id = str(self.folder_id)

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

        check_collisions = self.check_collisions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folder_id": folder_id,
            }
        )
        if folder_ids is not UNSET:
            field_dict["folder_ids"] = folder_ids
        if resource_ids is not UNSET:
            field_dict["resource_ids"] = resource_ids
        if check_collisions is not UNSET:
            field_dict["check_collisions"] = check_collisions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        folder_id = UUID(d.pop("folder_id"))

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

        check_collisions = d.pop("check_collisions", UNSET)

        folder_bulk_move_post_in = cls(
            folder_id=folder_id,
            folder_ids=folder_ids,
            resource_ids=resource_ids,
            check_collisions=check_collisions,
        )

        folder_bulk_move_post_in.additional_properties = d
        return folder_bulk_move_post_in

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
