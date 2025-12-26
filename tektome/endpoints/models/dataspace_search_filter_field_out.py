from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataspace_project_attribute_schema_out import DataspaceProjectAttributeSchemaOut
    from ..models.dataspace_resource_file_attribute_schema_out import DataspaceResourceFileAttributeSchemaOut
    from ..models.dataspace_search_filter_field_out_recommended_values_type_0 import (
        DataspaceSearchFilterFieldOutRecommendedValuesType0,
    )
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="DataspaceSearchFilterFieldOut")


@_attrs_define
class DataspaceSearchFilterFieldOut:
    """Schema for the response of posting resource file attributes to a project in a dataspace.

    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        project_attributes (list[DataspaceProjectAttributeSchemaOut]):
        resource_attributes (list[DataspaceResourceFileAttributeSchemaOut]):
        name (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        description (None | str | Unset):
        operator (None | str | Unset):
        recommended_values (DataspaceSearchFilterFieldOutRecommendedValuesType0 | None | Unset):
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    project_attributes: list[DataspaceProjectAttributeSchemaOut]
    resource_attributes: list[DataspaceResourceFileAttributeSchemaOut]
    name: str
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    operator: None | str | Unset = UNSET
    recommended_values: DataspaceSearchFilterFieldOutRecommendedValuesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dataspace_search_filter_field_out_recommended_values_type_0 import (
            DataspaceSearchFilterFieldOutRecommendedValuesType0,
        )

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        project_attributes = []
        for project_attributes_item_data in self.project_attributes:
            project_attributes_item = project_attributes_item_data.to_dict()
            project_attributes.append(project_attributes_item)

        resource_attributes = []
        for resource_attributes_item_data in self.resource_attributes:
            resource_attributes_item = resource_attributes_item_data.to_dict()
            resource_attributes.append(resource_attributes_item)

        name = self.name

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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

        recommended_values: dict[str, Any] | None | Unset
        if isinstance(self.recommended_values, Unset):
            recommended_values = UNSET
        elif isinstance(self.recommended_values, DataspaceSearchFilterFieldOutRecommendedValuesType0):
            recommended_values = self.recommended_values.to_dict()
        else:
            recommended_values = self.recommended_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "project_attributes": project_attributes,
                "resource_attributes": resource_attributes,
                "name": name,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if operator is not UNSET:
            field_dict["operator"] = operator
        if recommended_values is not UNSET:
            field_dict["recommended_values"] = recommended_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_project_attribute_schema_out import DataspaceProjectAttributeSchemaOut
        from ..models.dataspace_resource_file_attribute_schema_out import DataspaceResourceFileAttributeSchemaOut
        from ..models.dataspace_search_filter_field_out_recommended_values_type_0 import (
            DataspaceSearchFilterFieldOutRecommendedValuesType0,
        )
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        project_attributes = []
        _project_attributes = d.pop("project_attributes")
        for project_attributes_item_data in _project_attributes:
            project_attributes_item = DataspaceProjectAttributeSchemaOut.from_dict(project_attributes_item_data)

            project_attributes.append(project_attributes_item)

        resource_attributes = []
        _resource_attributes = d.pop("resource_attributes")
        for resource_attributes_item_data in _resource_attributes:
            resource_attributes_item = DataspaceResourceFileAttributeSchemaOut.from_dict(resource_attributes_item_data)

            resource_attributes.append(resource_attributes_item)

        name = d.pop("name")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

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

        def _parse_recommended_values(
            data: object,
        ) -> DataspaceSearchFilterFieldOutRecommendedValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                recommended_values_type_0 = DataspaceSearchFilterFieldOutRecommendedValuesType0.from_dict(data)

                return recommended_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataspaceSearchFilterFieldOutRecommendedValuesType0 | None | Unset, data)

        recommended_values = _parse_recommended_values(d.pop("recommended_values", UNSET))

        dataspace_search_filter_field_out = cls(
            created_by=created_by,
            updated_by=updated_by,
            project_attributes=project_attributes,
            resource_attributes=resource_attributes,
            name=name,
            created=created,
            updated=updated,
            id=id,
            description=description,
            operator=operator,
            recommended_values=recommended_values,
        )

        dataspace_search_filter_field_out.additional_properties = d
        return dataspace_search_filter_field_out

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
