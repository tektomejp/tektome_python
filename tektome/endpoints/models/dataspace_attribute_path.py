from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataspace_attribute_object_types import DataspaceAttributeObjectTypes

T = TypeVar("T", bound="DataspaceAttributePath")


@_attrs_define
class DataspaceAttributePath:
    """
    Attributes:
        object_type (DataspaceAttributeObjectTypes):
        object_id (UUID):
    """

    object_type: DataspaceAttributeObjectTypes
    object_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_type = self.object_type.value

        object_id = str(self.object_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_type": object_type,
                "object_id": object_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_type = DataspaceAttributeObjectTypes(d.pop("object_type"))

        object_id = UUID(d.pop("object_id"))

        dataspace_attribute_path = cls(
            object_type=object_type,
            object_id=object_id,
        )

        dataspace_attribute_path.additional_properties = d
        return dataspace_attribute_path

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
