from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BimElementLinkParentChildren")


@_attrs_define
class BimElementLinkParentChildren:
    """Schema for linking parent-children BIM objects.

    Attributes:
        parent (str):
        children (list[str]):
    """

    parent: str
    children: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent = self.parent

        children = self.children

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent": parent,
                "children": children,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent = d.pop("parent")

        children = cast(list[str], d.pop("children"))

        bim_element_link_parent_children = cls(
            parent=parent,
            children=children,
        )

        bim_element_link_parent_children.additional_properties = d
        return bim_element_link_parent_children

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
