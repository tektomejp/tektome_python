from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataspace_entity_type import DataspaceEntityType

T = TypeVar("T", bound="TargetTable")


@_attrs_define
class TargetTable:
    """Table-target search mode config.

    Attributes:
        table_name (str):
        table_entity_type (DataspaceEntityType):
    """

    table_name: str
    table_entity_type: DataspaceEntityType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table_name = self.table_name

        table_entity_type = self.table_entity_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "table_name": table_name,
                "table_entity_type": table_entity_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        table_name = d.pop("table_name")

        table_entity_type = DataspaceEntityType(d.pop("table_entity_type"))

        target_table = cls(
            table_name=table_name,
            table_entity_type=table_entity_type,
        )

        target_table.additional_properties = d
        return target_table

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
