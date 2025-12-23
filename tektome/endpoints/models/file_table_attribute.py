from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.table_column import TableColumn


T = TypeVar("T", bound="FileTableAttribute")


@_attrs_define
class FileTableAttribute:
    """
    Attributes:
        name (str):
        prompt (str):
        columns (list[TableColumn]):
        id (UUID | Unset):
    """

    name: str
    prompt: str
    columns: list[TableColumn]
    id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        prompt = self.prompt

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "prompt": prompt,
                "columns": columns,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_column import TableColumn

        d = dict(src_dict)
        name = d.pop("name")

        prompt = d.pop("prompt")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = TableColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        file_table_attribute = cls(
            name=name,
            prompt=prompt,
            columns=columns,
            id=id,
        )

        file_table_attribute.additional_properties = d
        return file_table_attribute

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
