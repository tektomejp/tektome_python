from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataspaceProjectAttributePostIn")


@_attrs_define
class DataspaceProjectAttributePostIn:
    """Schema for posting attributes to a project in a dataspace.

    Attributes:
        attribute_label (str):
        attribute_type (str):
        enabled (bool | Unset):  Default: True.
    """

    attribute_label: str
    attribute_type: str
    enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_label = self.attribute_label

        attribute_type = self.attribute_type

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_label": attribute_label,
                "attribute_type": attribute_type,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attribute_label = d.pop("attribute_label")

        attribute_type = d.pop("attribute_type")

        enabled = d.pop("enabled", UNSET)

        dataspace_project_attribute_post_in = cls(
            attribute_label=attribute_label,
            attribute_type=attribute_type,
            enabled=enabled,
        )

        dataspace_project_attribute_post_in.additional_properties = d
        return dataspace_project_attribute_post_in

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
