from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataspace_entity_type import DataspaceEntityType

T = TypeVar("T", bound="TableResultInfo")


@_attrs_define
class TableResultInfo:
    """Summary info about a table in search results.

    Attributes:
        table_name (str):
        table_entity_type (DataspaceEntityType):
        total_tables_count (int):
    """

    table_name: str
    table_entity_type: DataspaceEntityType
    total_tables_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table_name = self.table_name

        table_entity_type = self.table_entity_type.value

        total_tables_count = self.total_tables_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "table_name": table_name,
                "table_entity_type": table_entity_type,
                "total_tables_count": total_tables_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        table_name = d.pop("table_name")

        table_entity_type = DataspaceEntityType(d.pop("table_entity_type"))

        total_tables_count = d.pop("total_tables_count")

        table_result_info = cls(
            table_name=table_name,
            table_entity_type=table_entity_type,
            total_tables_count=total_tables_count,
        )

        table_result_info.additional_properties = d
        return table_result_info

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
