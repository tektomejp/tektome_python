from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkMoveFolderResourcesSchema")


@_attrs_define
class BulkMoveFolderResourcesSchema:
    """Schema for bulk move folders and resources by their IDs.

    Attributes:
        ids (list[UUID]):
        destination_folder_id (UUID):
    """

    ids: list[UUID]
    destination_folder_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = []
        for ids_item_data in self.ids:
            ids_item = str(ids_item_data)
            ids.append(ids_item)

        destination_folder_id = str(self.destination_folder_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
                "destination_folder_id": destination_folder_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = []
        _ids = d.pop("ids")
        for ids_item_data in _ids:
            ids_item = UUID(ids_item_data)

            ids.append(ids_item)

        destination_folder_id = UUID(d.pop("destination_folder_id"))

        bulk_move_folder_resources_schema = cls(
            ids=ids,
            destination_folder_id=destination_folder_id,
        )

        bulk_move_folder_resources_schema.additional_properties = d
        return bulk_move_folder_resources_schema

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
