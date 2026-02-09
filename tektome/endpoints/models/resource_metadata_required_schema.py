from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attribute_metadata import AttributeMetadata


T = TypeVar("T", bound="ResourceMetadataRequiredSchema")


@_attrs_define
class ResourceMetadataRequiredSchema:
    """
    Attributes:
        name (AttributeMetadata):
        kind (AttributeMetadata):
        description (AttributeMetadata):
    """

    name: AttributeMetadata
    kind: AttributeMetadata
    description: AttributeMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.to_dict()

        kind = self.kind.to_dict()

        description = self.description.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "kind": kind,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_metadata import AttributeMetadata

        d = dict(src_dict)
        name = AttributeMetadata.from_dict(d.pop("name"))

        kind = AttributeMetadata.from_dict(d.pop("kind"))

        description = AttributeMetadata.from_dict(d.pop("description"))

        resource_metadata_required_schema = cls(
            name=name,
            kind=kind,
            description=description,
        )

        resource_metadata_required_schema.additional_properties = d
        return resource_metadata_required_schema

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
