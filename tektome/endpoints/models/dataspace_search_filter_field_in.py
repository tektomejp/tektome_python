from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataspaceSearchFilterFieldIn")


@_attrs_define
class DataspaceSearchFilterFieldIn:
    """Input schema for DataspaceSearchFilterField

    Attributes:
        name (str): Name of the search filter field.
        operator (str):
        description (None | str | Unset):
        recommended_values (list[str] | Unset): List of recommended values for the search filter field.
        project_attribute_ids (list[UUID] | Unset): List of project attribute IDs associated with the search filter
            field.
        resource_attribute_ids (list[UUID] | Unset): List of resource attribute IDs associated with the search filter
            field.
    """

    name: str
    operator: str
    description: None | str | Unset = UNSET
    recommended_values: list[str] | Unset = UNSET
    project_attribute_ids: list[UUID] | Unset = UNSET
    resource_attribute_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        operator = self.operator

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        recommended_values: list[str] | Unset = UNSET
        if not isinstance(self.recommended_values, Unset):
            recommended_values = self.recommended_values

        project_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.project_attribute_ids, Unset):
            project_attribute_ids = []
            for project_attribute_ids_item_data in self.project_attribute_ids:
                project_attribute_ids_item = str(project_attribute_ids_item_data)
                project_attribute_ids.append(project_attribute_ids_item)

        resource_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.resource_attribute_ids, Unset):
            resource_attribute_ids = []
            for resource_attribute_ids_item_data in self.resource_attribute_ids:
                resource_attribute_ids_item = str(resource_attribute_ids_item_data)
                resource_attribute_ids.append(resource_attribute_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "operator": operator,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if recommended_values is not UNSET:
            field_dict["recommended_values"] = recommended_values
        if project_attribute_ids is not UNSET:
            field_dict["project_attribute_ids"] = project_attribute_ids
        if resource_attribute_ids is not UNSET:
            field_dict["resource_attribute_ids"] = resource_attribute_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        operator = d.pop("operator")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        recommended_values = cast(list[str], d.pop("recommended_values", UNSET))

        _project_attribute_ids = d.pop("project_attribute_ids", UNSET)
        project_attribute_ids: list[UUID] | Unset = UNSET
        if _project_attribute_ids is not UNSET:
            project_attribute_ids = []
            for project_attribute_ids_item_data in _project_attribute_ids:
                project_attribute_ids_item = UUID(project_attribute_ids_item_data)

                project_attribute_ids.append(project_attribute_ids_item)

        _resource_attribute_ids = d.pop("resource_attribute_ids", UNSET)
        resource_attribute_ids: list[UUID] | Unset = UNSET
        if _resource_attribute_ids is not UNSET:
            resource_attribute_ids = []
            for resource_attribute_ids_item_data in _resource_attribute_ids:
                resource_attribute_ids_item = UUID(resource_attribute_ids_item_data)

                resource_attribute_ids.append(resource_attribute_ids_item)

        dataspace_search_filter_field_in = cls(
            name=name,
            operator=operator,
            description=description,
            recommended_values=recommended_values,
            project_attribute_ids=project_attribute_ids,
            resource_attribute_ids=resource_attribute_ids,
        )

        dataspace_search_filter_field_in.additional_properties = d
        return dataspace_search_filter_field_in

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
