from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResourceAttributeInputPayload")


@_attrs_define
class ResourceAttributeInputPayload:
    """Filter fields for attribute candidates — always present.

    Attributes:
        attribute_id (UUID):
        kind (str):
        resource_id (UUID):
    """

    attribute_id: UUID
    kind: str
    resource_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_id = str(self.attribute_id)

        kind = self.kind

        resource_id = str(self.resource_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_id": attribute_id,
                "kind": kind,
                "resource_id": resource_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attribute_id = UUID(d.pop("attribute_id"))

        kind = d.pop("kind")

        resource_id = UUID(d.pop("resource_id"))

        resource_attribute_input_payload = cls(
            attribute_id=attribute_id,
            kind=kind,
            resource_id=resource_id,
        )

        resource_attribute_input_payload.additional_properties = d
        return resource_attribute_input_payload

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
