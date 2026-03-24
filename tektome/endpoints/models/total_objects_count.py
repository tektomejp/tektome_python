from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TotalObjectsCount")


@_attrs_define
class TotalObjectsCount:
    """Aggregated counts of matched objects across the entire search result.

    Attributes:
        pages_count (int | Unset): Total number of pages that matched the keyword search across all resources Default:
            0.
        resources_count (int | Unset): Total number of resources that matched the search conditions Default: 0.
        projects_count (int | Unset): Total number of projects that matched the search conditions Default: 0.
    """

    pages_count: int | Unset = 0
    resources_count: int | Unset = 0
    projects_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pages_count = self.pages_count

        resources_count = self.resources_count

        projects_count = self.projects_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pages_count is not UNSET:
            field_dict["pages_count"] = pages_count
        if resources_count is not UNSET:
            field_dict["resources_count"] = resources_count
        if projects_count is not UNSET:
            field_dict["projects_count"] = projects_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pages_count = d.pop("pages_count", UNSET)

        resources_count = d.pop("resources_count", UNSET)

        projects_count = d.pop("projects_count", UNSET)

        total_objects_count = cls(
            pages_count=pages_count,
            resources_count=resources_count,
            projects_count=projects_count,
        )

        total_objects_count.additional_properties = d
        return total_objects_count

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
