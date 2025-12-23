from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.table_cell import TableCell
    from ..models.table_column import TableColumn


T = TypeVar("T", bound="Table")


@_attrs_define
class Table:
    """Data model representing a table with columns and rows.
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

        Attributes:
            columns (list[TableColumn]):
            rows (list[list[TableCell]]):
    """

    columns: list[TableColumn]
    rows: list[list[TableCell]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        rows = []
        for rows_item_data in self.rows:
            rows_item = []
            for rows_item_item_data in rows_item_data:
                rows_item_item = rows_item_item_data.to_dict()
                rows_item.append(rows_item_item)

            rows.append(rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columns": columns,
                "rows": rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_cell import TableCell
        from ..models.table_column import TableColumn

        d = dict(src_dict)
        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = TableColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = []
            _rows_item = rows_item_data
            for rows_item_item_data in _rows_item:
                rows_item_item = TableCell.from_dict(rows_item_item_data)

                rows_item.append(rows_item_item)

            rows.append(rows_item)

        table = cls(
            columns=columns,
            rows=rows,
        )

        table.additional_properties = d
        return table

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
