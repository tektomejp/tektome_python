from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SimpleAttributeTypeActionSchemaDatetimeOnOrAfter")


@_attrs_define
class SimpleAttributeTypeActionSchemaDatetimeOnOrAfter:
    """
    Attributes:
        action (Literal['on_or_after']):
        value_type (Literal['datetime']):
    """

    action: Literal["on_or_after"]
    value_type: Literal["datetime"]
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
        action = cast(Literal["on_or_after"], d.pop("action"))
        if action != "on_or_after":
            raise ValueError(f"action must match const 'on_or_after', got '{action}'")

        value_type = cast(Literal["datetime"], d.pop("value_type"))
        if value_type != "datetime":
            raise ValueError(f"value_type must match const 'datetime', got '{value_type}'")

        simple_attribute_type_action_schema_datetime_on_or_after = cls(
            action=action,
            value_type=value_type,
        )

        simple_attribute_type_action_schema_datetime_on_or_after.additional_properties = d
        return simple_attribute_type_action_schema_datetime_on_or_after

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
