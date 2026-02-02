from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SimpleAttributeTypeActionSchemaIntegerGreaterThanOrEqualTo")


@_attrs_define
class SimpleAttributeTypeActionSchemaIntegerGreaterThanOrEqualTo:
    """
    Attributes:
        action (Literal['greater_than_or_equal_to']):
        value_type (Literal['integer']):
    """

    action: Literal["greater_than_or_equal_to"]
    value_type: Literal["integer"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        value_type = self.value_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "value_type": value_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = cast(Literal["greater_than_or_equal_to"], d.pop("action"))
        if action != "greater_than_or_equal_to":
            raise ValueError(f"action must match const 'greater_than_or_equal_to', got '{action}'")

        value_type = cast(Literal["integer"], d.pop("value_type"))
        if value_type != "integer":
            raise ValueError(f"value_type must match const 'integer', got '{value_type}'")

        simple_attribute_type_action_schema_integer_greater_than_or_equal_to = cls(
            action=action,
            value_type=value_type,
        )

        simple_attribute_type_action_schema_integer_greater_than_or_equal_to.additional_properties = d
        return simple_attribute_type_action_schema_integer_greater_than_or_equal_to

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
