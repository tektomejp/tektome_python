from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AttributeMetadata")


@_attrs_define
class AttributeMetadata:
    """
    Attributes:
        id (UUID):
        is_locked (bool):
        value (Any):
        citations_count (int):
    """

    id: UUID
    is_locked: bool
    value: Any
    citations_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        is_locked = self.is_locked

        value = self.value

        citations_count = self.citations_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "is_locked": is_locked,
                "value": value,
                "citations_count": citations_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        is_locked = d.pop("is_locked")

        value = d.pop("value")

        citations_count = d.pop("citations_count")

        attribute_metadata = cls(
            id=id,
            is_locked=is_locked,
            value=value,
            citations_count=citations_count,
        )

        attribute_metadata.additional_properties = d
        return attribute_metadata

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
