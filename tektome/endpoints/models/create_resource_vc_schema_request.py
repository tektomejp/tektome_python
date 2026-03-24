from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateResourceVCSchemaRequest")


@_attrs_define
class CreateResourceVCSchemaRequest:
    """Input Schema for looking up multiple Resource Version Control

    Attributes:
        resource_vc_ids (list[UUID]):
    """

    resource_vc_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_vc_ids = []
        for resource_vc_ids_item_data in self.resource_vc_ids:
            resource_vc_ids_item = str(resource_vc_ids_item_data)
            resource_vc_ids.append(resource_vc_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_vc_ids": resource_vc_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_vc_ids = []
        _resource_vc_ids = d.pop("resource_vc_ids")
        for resource_vc_ids_item_data in _resource_vc_ids:
            resource_vc_ids_item = UUID(resource_vc_ids_item_data)

            resource_vc_ids.append(resource_vc_ids_item)

        create_resource_vc_schema_request = cls(
            resource_vc_ids=resource_vc_ids,
        )

        create_resource_vc_schema_request.additional_properties = d
        return create_resource_vc_schema_request

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
