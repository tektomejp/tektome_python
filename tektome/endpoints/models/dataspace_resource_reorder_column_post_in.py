from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DataspaceResourceReorderColumnPostIn")


@_attrs_define
class DataspaceResourceReorderColumnPostIn:
    """Schema for reordering columns in a dataspace project's resource.

    Attributes:
        column_id (UUID):
        new_index (int):
    """

    column_id: UUID
    new_index: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column_id = str(self.column_id)

        new_index = self.new_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "column_id": column_id,
                "new_index": new_index,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column_id = UUID(d.pop("column_id"))

        new_index = d.pop("new_index")

        dataspace_resource_reorder_column_post_in = cls(
            column_id=column_id,
            new_index=new_index,
        )

        dataspace_resource_reorder_column_post_in.additional_properties = d
        return dataspace_resource_reorder_column_post_in

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
