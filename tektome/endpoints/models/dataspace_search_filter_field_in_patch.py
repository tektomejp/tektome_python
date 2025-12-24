from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataspaceSearchFilterFieldInPatch")


@_attrs_define
class DataspaceSearchFilterFieldInPatch:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        operator (None | str | Unset):
        recommended_values (list[str] | None | Unset):
        project_attribute_ids (list[UUID] | None | Unset):
        resource_attribute_ids (list[UUID] | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    operator: None | str | Unset = UNSET
    recommended_values: list[str] | None | Unset = UNSET
    project_attribute_ids: list[UUID] | None | Unset = UNSET
    resource_attribute_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        operator: None | str | Unset
        if isinstance(self.operator, Unset):
            operator = UNSET
        else:
            operator = self.operator

        recommended_values: list[str] | None | Unset
        if isinstance(self.recommended_values, Unset):
            recommended_values = UNSET
        elif isinstance(self.recommended_values, list):
            recommended_values = self.recommended_values

        else:
            recommended_values = self.recommended_values

        project_attribute_ids: list[str] | None | Unset
        if isinstance(self.project_attribute_ids, Unset):
            project_attribute_ids = UNSET
        elif isinstance(self.project_attribute_ids, list):
            project_attribute_ids = []
            for project_attribute_ids_type_0_item_data in self.project_attribute_ids:
                project_attribute_ids_type_0_item = str(project_attribute_ids_type_0_item_data)
                project_attribute_ids.append(project_attribute_ids_type_0_item)

        else:
            project_attribute_ids = self.project_attribute_ids

        resource_attribute_ids: list[str] | None | Unset
        if isinstance(self.resource_attribute_ids, Unset):
            resource_attribute_ids = UNSET
        elif isinstance(self.resource_attribute_ids, list):
            resource_attribute_ids = []
            for resource_attribute_ids_type_0_item_data in self.resource_attribute_ids:
                resource_attribute_ids_type_0_item = str(resource_attribute_ids_type_0_item_data)
                resource_attribute_ids.append(resource_attribute_ids_type_0_item)

        else:
            resource_attribute_ids = self.resource_attribute_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if operator is not UNSET:
            field_dict["operator"] = operator
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_operator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operator = _parse_operator(d.pop("operator", UNSET))

        def _parse_recommended_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recommended_values_type_0 = cast(list[str], data)

                return recommended_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        recommended_values = _parse_recommended_values(d.pop("recommended_values", UNSET))

        def _parse_project_attribute_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                project_attribute_ids_type_0 = []
                _project_attribute_ids_type_0 = data
                for project_attribute_ids_type_0_item_data in _project_attribute_ids_type_0:
                    project_attribute_ids_type_0_item = UUID(project_attribute_ids_type_0_item_data)

                    project_attribute_ids_type_0.append(project_attribute_ids_type_0_item)

                return project_attribute_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        project_attribute_ids = _parse_project_attribute_ids(d.pop("project_attribute_ids", UNSET))

        def _parse_resource_attribute_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resource_attribute_ids_type_0 = []
                _resource_attribute_ids_type_0 = data
                for resource_attribute_ids_type_0_item_data in _resource_attribute_ids_type_0:
                    resource_attribute_ids_type_0_item = UUID(resource_attribute_ids_type_0_item_data)

                    resource_attribute_ids_type_0.append(resource_attribute_ids_type_0_item)

                return resource_attribute_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        resource_attribute_ids = _parse_resource_attribute_ids(d.pop("resource_attribute_ids", UNSET))

        dataspace_search_filter_field_in_patch = cls(
            name=name,
            description=description,
            operator=operator,
            recommended_values=recommended_values,
            project_attribute_ids=project_attribute_ids,
            resource_attribute_ids=resource_attribute_ids,
        )

        dataspace_search_filter_field_in_patch.additional_properties = d
        return dataspace_search_filter_field_in_patch

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
