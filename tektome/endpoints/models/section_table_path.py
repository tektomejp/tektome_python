from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.section_table_path_mode import SectionTablePathMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SectionTablePath")


@_attrs_define
class SectionTablePath:
    """Represents a path to tables in a section.
    Example: { <page_id: 1>: {table_index: 0, row_index: 1} }
    Refers to the entire second row in the first table of the page id 1.

        Attributes:
            page_id (UUID):
            table_index (int):
            row_index (int | None | Unset): Index of the row in the table
            column_index (int | None | Unset): Index of the column in the table
            mode (SectionTablePathMode | Unset): Mode of the table path: 'row' for entire row, 'column' for entire column,
                'cell' for specific cell Default: SectionTablePathMode.CELL.
    """

    page_id: UUID
    table_index: int
    row_index: int | None | Unset = UNSET
    column_index: int | None | Unset = UNSET
    mode: SectionTablePathMode | Unset = SectionTablePathMode.CELL
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_id = str(self.page_id)

        table_index = self.table_index

        row_index: int | None | Unset
        if isinstance(self.row_index, Unset):
            row_index = UNSET
        else:
            row_index = self.row_index

        column_index: int | None | Unset
        if isinstance(self.column_index, Unset):
            column_index = UNSET
        else:
            column_index = self.column_index

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page_id": page_id,
                "table_index": table_index,
            }
        )
        if row_index is not UNSET:
            field_dict["row_index"] = row_index
        if column_index is not UNSET:
            field_dict["column_index"] = column_index
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_id = UUID(d.pop("page_id"))

        table_index = d.pop("table_index")

        def _parse_row_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_index = _parse_row_index(d.pop("row_index", UNSET))

        def _parse_column_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        column_index = _parse_column_index(d.pop("column_index", UNSET))

        _mode = d.pop("mode", UNSET)
        mode: SectionTablePathMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = SectionTablePathMode(_mode)

        section_table_path = cls(
            page_id=page_id,
            table_index=table_index,
            row_index=row_index,
            column_index=column_index,
            mode=mode,
        )

        section_table_path.additional_properties = d
        return section_table_path

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
