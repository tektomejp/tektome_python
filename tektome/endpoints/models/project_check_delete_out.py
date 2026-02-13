from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProjectCheckDeleteOut")


@_attrs_define
class ProjectCheckDeleteOut:
    """
    Attributes:
        can_delete (bool):
        has_nested_items (bool):
        requirement_count (int):
        resource_group_count (int):
        folder_count (int):
        resource_count (int):
        member_count (int):
    """

    can_delete: bool
    has_nested_items: bool
    requirement_count: int
    resource_group_count: int
    folder_count: int
    resource_count: int
    member_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_delete = self.can_delete

        has_nested_items = self.has_nested_items

        requirement_count = self.requirement_count

        resource_group_count = self.resource_group_count

        folder_count = self.folder_count

        resource_count = self.resource_count

        member_count = self.member_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "can_delete": can_delete,
                "has_nested_items": has_nested_items,
                "requirement_count": requirement_count,
                "resource_group_count": resource_group_count,
                "folder_count": folder_count,
                "resource_count": resource_count,
                "member_count": member_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_delete = d.pop("can_delete")

        has_nested_items = d.pop("has_nested_items")

        requirement_count = d.pop("requirement_count")

        resource_group_count = d.pop("resource_group_count")

        folder_count = d.pop("folder_count")

        resource_count = d.pop("resource_count")

        member_count = d.pop("member_count")

        project_check_delete_out = cls(
            can_delete=can_delete,
            has_nested_items=has_nested_items,
            requirement_count=requirement_count,
            resource_group_count=resource_group_count,
            folder_count=folder_count,
            resource_count=resource_count,
            member_count=member_count,
        )

        project_check_delete_out.additional_properties = d
        return project_check_delete_out

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
