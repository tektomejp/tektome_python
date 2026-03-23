from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DataspaceCountsGetOut")


@_attrs_define
class DataspaceCountsGetOut:
    """
    Attributes:
        projects_count (int):
        resources_count (int):
    """

    projects_count: int
    resources_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects_count = self.projects_count

        resources_count = self.resources_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projects_count": projects_count,
                "resources_count": resources_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        projects_count = d.pop("projects_count")

        resources_count = d.pop("resources_count")

        dataspace_counts_get_out = cls(
            projects_count=projects_count,
            resources_count=resources_count,
        )

        dataspace_counts_get_out.additional_properties = d
        return dataspace_counts_get_out

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
