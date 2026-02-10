from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.execution_attribute_metadata import ExecutionAttributeMetadata


T = TypeVar("T", bound="ExecuteProcessMetadataGetOut")


@_attrs_define
class ExecuteProcessMetadataGetOut:
    """Schema for execution metadata response.

    Attributes:
        empty_values (ExecutionAttributeMetadata): Schema for execution attribute.
        locked_values (ExecutionAttributeMetadata): Schema for execution attribute.
        existing_values (ExecutionAttributeMetadata): Schema for execution attribute.
    """

    empty_values: ExecutionAttributeMetadata
    locked_values: ExecutionAttributeMetadata
    existing_values: ExecutionAttributeMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        empty_values = self.empty_values.to_dict()

        locked_values = self.locked_values.to_dict()

        existing_values = self.existing_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "empty_values": empty_values,
                "locked_values": locked_values,
                "existing_values": existing_values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_attribute_metadata import ExecutionAttributeMetadata

        d = dict(src_dict)
        empty_values = ExecutionAttributeMetadata.from_dict(d.pop("empty_values"))

        locked_values = ExecutionAttributeMetadata.from_dict(d.pop("locked_values"))

        existing_values = ExecutionAttributeMetadata.from_dict(d.pop("existing_values"))

        execute_process_metadata_get_out = cls(
            empty_values=empty_values,
            locked_values=locked_values,
            existing_values=existing_values,
        )

        execute_process_metadata_get_out.additional_properties = d
        return execute_process_metadata_get_out

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
