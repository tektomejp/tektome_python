from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.all_attributes_schema_response import AllAttributesSchemaResponse


T = TypeVar("T", bound="AttributeExtractionResponse")


@_attrs_define
class AttributeExtractionResponse:
    """
    Attributes:
        created (AllAttributesSchemaResponse):
        updated (AllAttributesSchemaResponse):
    """

    created: AllAttributesSchemaResponse
    updated: AllAttributesSchemaResponse
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.to_dict()

        updated = self.updated.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.all_attributes_schema_response import AllAttributesSchemaResponse

        d = dict(src_dict)
        created = AllAttributesSchemaResponse.from_dict(d.pop("created"))

        updated = AllAttributesSchemaResponse.from_dict(d.pop("updated"))

        attribute_extraction_response = cls(
            created=created,
            updated=updated,
        )

        attribute_extraction_response.additional_properties = d
        return attribute_extraction_response

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
