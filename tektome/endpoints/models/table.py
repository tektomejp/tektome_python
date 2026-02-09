from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.table_cell import TableCell
    from ..models.table_column import TableColumn


T = TypeVar("T", bound="Table")


@_attrs_define
class Table:
    """Data model representing a table with columns and rows.

    Attributes:
        columns: Column definitions (must have unique names, at least one required).
        rows: List of rows, each row is a list of cells matching column order.
        version: Optimistic locking version for structural changes only.

    Version is used to detect conflicts when rows are inserted, deleted, or reordered.
    Cell value updates use last-write-wins semantics and don't require version checks,
    since they don't affect other cells or row indices.

        Attributes:
            columns (list[TableColumn]):
            rows (list[list[TableCell]]):
            version (int | None | Unset):
    """

    columns: list[TableColumn]
    rows: list[list[TableCell]]
    version: int | None | Unset = UNSET
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

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columns": columns,
                "rows": rows,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version

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

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        table = cls(
            columns=columns,
            rows=rows,
            version=version,
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
