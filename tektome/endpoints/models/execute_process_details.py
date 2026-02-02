from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_process_file_attribute_details import ExecuteProcessFileAttributeDetails


T = TypeVar("T", bound="ExecuteProcessDetails")


@_attrs_define
class ExecuteProcessDetails:
    """Validation schema for UI trigger details in individual process execution payload

    Attributes:
        id (UUID):
        name (str):
        file_attributes (list[ExecuteProcessFileAttributeDetails] | Unset):
    """

    id: UUID
    name: str
    file_attributes: list[ExecuteProcessFileAttributeDetails] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        file_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.file_attributes, Unset):
            file_attributes = []
            for file_attributes_item_data in self.file_attributes:
                file_attributes_item = file_attributes_item_data.to_dict()
                file_attributes.append(file_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if file_attributes is not UNSET:
            field_dict["file_attributes"] = file_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_process_file_attribute_details import ExecuteProcessFileAttributeDetails

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        _file_attributes = d.pop("file_attributes", UNSET)
        file_attributes: list[ExecuteProcessFileAttributeDetails] | Unset = UNSET
        if _file_attributes is not UNSET:
            file_attributes = []
            for file_attributes_item_data in _file_attributes:
                file_attributes_item = ExecuteProcessFileAttributeDetails.from_dict(file_attributes_item_data)

                file_attributes.append(file_attributes_item)

        execute_process_details = cls(
            id=id,
            name=name,
            file_attributes=file_attributes,
        )

        execute_process_details.additional_properties = d
        return execute_process_details

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
