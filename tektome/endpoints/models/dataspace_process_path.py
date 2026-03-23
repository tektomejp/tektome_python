from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DataspaceProcessPath")


@_attrs_define
class DataspaceProcessPath:
    """Schema for accessing processes in a dataspace.

    Attributes:
        dataspace_id (UUID):
        process_id (UUID): The ID of an existing process.
    """

    dataspace_id: UUID
    process_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataspace_id = str(self.dataspace_id)

        process_id = str(self.process_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataspace_id": dataspace_id,
                "process_id": process_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataspace_id = UUID(d.pop("dataspace_id"))

        process_id = UUID(d.pop("process_id"))

        dataspace_process_path = cls(
            dataspace_id=dataspace_id,
            process_id=process_id,
        )

        dataspace_process_path.additional_properties = d
        return dataspace_process_path

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
