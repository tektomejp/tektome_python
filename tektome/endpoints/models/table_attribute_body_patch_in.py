from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.table_cell_update import TableCellUpdate


T = TypeVar("T", bound="TableAttributeBodyPatchIn")


@_attrs_define
class TableAttributeBodyPatchIn:
    """
    Attributes:
        name (str):
        cells (list[TableCellUpdate]):
        version (int | None | Unset):
    """

    name: str
    cells: list[TableCellUpdate]
    version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        cells = []
        for cells_item_data in self.cells:
            cells_item = cells_item_data.to_dict()
            cells.append(cells_item)

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "cells": cells,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_cell_update import TableCellUpdate

        d = dict(src_dict)
        name = d.pop("name")

        cells = []
        _cells = d.pop("cells")
        for cells_item_data in _cells:
            cells_item = TableCellUpdate.from_dict(cells_item_data)

            cells.append(cells_item)

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        table_attribute_body_patch_in = cls(
            name=name,
            cells=cells,
            version=version,
        )

        table_attribute_body_patch_in.additional_properties = d
        return table_attribute_body_patch_in

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
