from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RemoveResourceGroupPostIn")


@_attrs_define
class RemoveResourceGroupPostIn:
    """
    Attributes:
        resource_group_ids (list[UUID]):
    """

    resource_group_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_group_ids = []
        for resource_group_ids_item_data in self.resource_group_ids:
            resource_group_ids_item = str(resource_group_ids_item_data)
            resource_group_ids.append(resource_group_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_group_ids": resource_group_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_group_ids = []
        _resource_group_ids = d.pop("resource_group_ids")
        for resource_group_ids_item_data in _resource_group_ids:
            resource_group_ids_item = UUID(resource_group_ids_item_data)

            resource_group_ids.append(resource_group_ids_item)

        remove_resource_group_post_in = cls(
            resource_group_ids=resource_group_ids,
        )

        remove_resource_group_post_in.additional_properties = d
        return remove_resource_group_post_in

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
