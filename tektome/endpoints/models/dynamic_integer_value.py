from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entity_type import EntityType

T = TypeVar("T", bound="DynamicIntegerValue")


@_attrs_define
class DynamicIntegerValue:
    """
    Attributes:
        entity (EntityType):
        entity_id (UUID): The ID of the entity to which the dynamic value belongs
        attribute_name (str): The name of the attribute to filter on
        attribute_type (Literal['integer']): The type of the attribute to filter on
    """

    entity: EntityType
    entity_id: UUID
    attribute_name: str
    attribute_type: Literal["integer"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity = self.entity.value

        entity_id = str(self.entity_id)

        attribute_name = self.attribute_name

        attribute_type = self.attribute_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity": entity,
                "entity_id": entity_id,
                "attribute_name": attribute_name,
                "attribute_type": attribute_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity = EntityType(d.pop("entity"))

        entity_id = UUID(d.pop("entity_id"))

        attribute_name = d.pop("attribute_name")

        attribute_type = cast(Literal["integer"], d.pop("attribute_type"))
        if attribute_type != "integer":
            raise ValueError(f"attribute_type must match const 'integer', got '{attribute_type}'")

        dynamic_integer_value = cls(
            entity=entity,
            entity_id=entity_id,
            attribute_name=attribute_name,
            attribute_type=attribute_type,
        )

        dynamic_integer_value.additional_properties = d
        return dynamic_integer_value

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
