from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.table import Table


T = TypeVar("T", bound="TableAttributeSchemaIn")


@_attrs_define
class TableAttributeSchemaIn:
    """
    Attributes:
        name (str):
        value (Table): Data model representing a table with columns and rows.
            Includes validation to ensure data integrity based on column definitions.

            Attributes:
                columns (list[TableColumn]): List of column definitions.
                rows (list[list[TableCell]]): List of rows, each containing a list of table cells.

            Methods:
                validate_table: Validates the table structure and data integrity after initialization.

            Requirement:
                - At least one column must be defined.
                - Column names must be unique.
                - Each row must conform to the column definitions in terms of data types and nullability.
    """

    name: str
    value: Table
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table import Table

        d = dict(src_dict)
        name = d.pop("name")

        value = Table.from_dict(d.pop("value"))

        table_attribute_schema_in = cls(
            name=name,
            value=value,
        )

        table_attribute_schema_in.additional_properties = d
        return table_attribute_schema_in

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
