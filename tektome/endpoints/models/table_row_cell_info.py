from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.simple_attribute_type import SimpleAttributeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TableRowCellInfo")


@_attrs_define
class TableRowCellInfo:
    """A single cell from a matched table row.

    Attributes:
        column (str):
        row_index (int):
        type_ (SimpleAttributeType):
        cell_value (Any | Unset):
    """

    column: str
    row_index: int
    type_: SimpleAttributeType
    cell_value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column = self.column

        row_index = self.row_index

        type_ = self.type_.value

        cell_value = self.cell_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "column": column,
                "row_index": row_index,
                "type": type_,
            }
        )
        if cell_value is not UNSET:
            field_dict["cell_value"] = cell_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column = d.pop("column")

        row_index = d.pop("row_index")

        type_ = SimpleAttributeType(d.pop("type"))

        cell_value = d.pop("cell_value", UNSET)

        table_row_cell_info = cls(
            column=column,
            row_index=row_index,
            type_=type_,
            cell_value=cell_value,
        )

        table_row_cell_info.additional_properties = d
        return table_row_cell_info

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
