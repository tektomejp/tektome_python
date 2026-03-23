from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FolderResourcePostIn")


@_attrs_define
class FolderResourcePostIn:
    """Schema for attaching a lawtalk resource(s) to a folder.

    Attributes:
        resource_ids (list[UUID]):
    """

    resource_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_ids = []
        for resource_ids_item_data in self.resource_ids:
            resource_ids_item = str(resource_ids_item_data)
            resource_ids.append(resource_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_ids": resource_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_ids = []
        _resource_ids = d.pop("resource_ids")
        for resource_ids_item_data in _resource_ids:
            resource_ids_item = UUID(resource_ids_item_data)

            resource_ids.append(resource_ids_item)

        folder_resource_post_in = cls(
            resource_ids=resource_ids,
        )

        folder_resource_post_in.additional_properties = d
        return folder_resource_post_in

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
