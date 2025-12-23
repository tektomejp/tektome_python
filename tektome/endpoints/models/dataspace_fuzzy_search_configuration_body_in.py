from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataspaceFuzzySearchConfigurationBodyIn")


@_attrs_define
class DataspaceFuzzySearchConfigurationBodyIn:
    """Input schema to manipulate fuzzy search configuration in a dataspace.

    Attributes:
        excluded_project_attribute_ids (list[UUID] | Unset): List of project attribute IDs to be excluded from fuzzy
            search.
        excluded_resource_attribute_ids (list[UUID] | Unset): List of resource attribute IDs to be excluded from fuzzy
            search.
    """

    excluded_project_attribute_ids: list[UUID] | Unset = UNSET
    excluded_resource_attribute_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        excluded_project_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.excluded_project_attribute_ids, Unset):
            excluded_project_attribute_ids = []
            for excluded_project_attribute_ids_item_data in self.excluded_project_attribute_ids:
                excluded_project_attribute_ids_item = str(excluded_project_attribute_ids_item_data)
                excluded_project_attribute_ids.append(excluded_project_attribute_ids_item)

        excluded_resource_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.excluded_resource_attribute_ids, Unset):
            excluded_resource_attribute_ids = []
            for excluded_resource_attribute_ids_item_data in self.excluded_resource_attribute_ids:
                excluded_resource_attribute_ids_item = str(excluded_resource_attribute_ids_item_data)
                excluded_resource_attribute_ids.append(excluded_resource_attribute_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if excluded_project_attribute_ids is not UNSET:
            field_dict["excluded_project_attribute_ids"] = excluded_project_attribute_ids
        if excluded_resource_attribute_ids is not UNSET:
            field_dict["excluded_resource_attribute_ids"] = excluded_resource_attribute_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _excluded_project_attribute_ids = d.pop("excluded_project_attribute_ids", UNSET)
        excluded_project_attribute_ids: list[UUID] | Unset = UNSET
        if _excluded_project_attribute_ids is not UNSET:
            excluded_project_attribute_ids = []
            for excluded_project_attribute_ids_item_data in _excluded_project_attribute_ids:
                excluded_project_attribute_ids_item = UUID(excluded_project_attribute_ids_item_data)

                excluded_project_attribute_ids.append(excluded_project_attribute_ids_item)

        _excluded_resource_attribute_ids = d.pop("excluded_resource_attribute_ids", UNSET)
        excluded_resource_attribute_ids: list[UUID] | Unset = UNSET
        if _excluded_resource_attribute_ids is not UNSET:
            excluded_resource_attribute_ids = []
            for excluded_resource_attribute_ids_item_data in _excluded_resource_attribute_ids:
                excluded_resource_attribute_ids_item = UUID(excluded_resource_attribute_ids_item_data)

                excluded_resource_attribute_ids.append(excluded_resource_attribute_ids_item)

        dataspace_fuzzy_search_configuration_body_in = cls(
            excluded_project_attribute_ids=excluded_project_attribute_ids,
            excluded_resource_attribute_ids=excluded_resource_attribute_ids,
        )

        dataspace_fuzzy_search_configuration_body_in.additional_properties = d
        return dataspace_fuzzy_search_configuration_body_in

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
