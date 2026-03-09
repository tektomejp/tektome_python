from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataspace_entity_type import DataspaceEntityType

T = TypeVar("T", bound="DataspaceAttributeCategoryAttributePath")


@_attrs_define
class DataspaceAttributeCategoryAttributePath:
    """Path schema for endpoints that use attribute_category with attribute_id.

    Attributes:
        dataspace_id (UUID):
        attribute_category (DataspaceEntityType):
        attribute_id (UUID):
    """

    dataspace_id: UUID
    attribute_category: DataspaceEntityType
    attribute_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataspace_id = str(self.dataspace_id)

        attribute_category = self.attribute_category.value

        attribute_id = str(self.attribute_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataspace_id": dataspace_id,
                "attribute_category": attribute_category,
                "attribute_id": attribute_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataspace_id = UUID(d.pop("dataspace_id"))

        attribute_category = DataspaceEntityType(d.pop("attribute_category"))

        attribute_id = UUID(d.pop("attribute_id"))

        dataspace_attribute_category_attribute_path = cls(
            dataspace_id=dataspace_id,
            attribute_category=attribute_category,
            attribute_id=attribute_id,
        )

        dataspace_attribute_category_attribute_path.additional_properties = d
        return dataspace_attribute_category_attribute_path

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
