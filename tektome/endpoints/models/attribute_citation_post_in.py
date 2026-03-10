from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type import AttributeType

T = TypeVar("T", bound="AttributeCitationPostIn")


@_attrs_define
class AttributeCitationPostIn:
    """
    Attributes:
        title (str):
        attribute_type (AttributeType): StrEnum for all available attribute types

            .. warning::
                Do not change the values of this enum, as they are used in the database.
                If you need to add a new attribute type, add a new enum value with a unique name.
        cited_attribute_type (AttributeType): StrEnum for all available attribute types

            .. warning::
                Do not change the values of this enum, as they are used in the database.
                If you need to add a new attribute type, add a new enum value with a unique name.
        cited_attribute_id (UUID):
    """

    title: str
    attribute_type: AttributeType
    cited_attribute_type: AttributeType
    cited_attribute_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        attribute_type = self.attribute_type.value

        cited_attribute_type = self.cited_attribute_type.value

        cited_attribute_id = str(self.cited_attribute_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "attribute_type": attribute_type,
                "cited_attribute_type": cited_attribute_type,
                "cited_attribute_id": cited_attribute_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        attribute_type = AttributeType(d.pop("attribute_type"))

        cited_attribute_type = AttributeType(d.pop("cited_attribute_type"))

        cited_attribute_id = UUID(d.pop("cited_attribute_id"))

        attribute_citation_post_in = cls(
            title=title,
            attribute_type=attribute_type,
            cited_attribute_type=cited_attribute_type,
            cited_attribute_id=cited_attribute_id,
        )

        attribute_citation_post_in.additional_properties = d
        return attribute_citation_post_in

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
