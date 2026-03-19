from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.table_column_mapping_entity_type import TableColumnMappingEntityType

T = TypeVar("T", bound="TableColumnMapping")


@_attrs_define
class TableColumnMapping:
    """Maps a table attribute column to a search filter field.

    Attributes:
        entity_type (TableColumnMappingEntityType):
        attribute_config_id (UUID):
        column_name (str):
    """

    entity_type: TableColumnMappingEntityType
    attribute_config_id: UUID
    column_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_type = self.entity_type.value

        attribute_config_id = str(self.attribute_config_id)

        column_name = self.column_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity_type": entity_type,
                "attribute_config_id": attribute_config_id,
                "column_name": column_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_type = TableColumnMappingEntityType(d.pop("entity_type"))

        attribute_config_id = UUID(d.pop("attribute_config_id"))

        column_name = d.pop("column_name")

        table_column_mapping = cls(
            entity_type=entity_type,
            attribute_config_id=attribute_config_id,
            column_name=column_name,
        )

        table_column_mapping.additional_properties = d
        return table_column_mapping

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
