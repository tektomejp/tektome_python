from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FieldConditionInput")


@_attrs_define
class FieldConditionInput:
    """Input schema for a single field-based condition.

    The field_id references a DataspaceSearchFilterField which contains
    the attribute_name and attribute_type mapping.

        Attributes:
            field_id (UUID): UUID of the DataspaceSearchFilterField
            action (str): The action/operator to perform (e.g., contains, equals, greater_than)
            value (Any): The value to search for
    """

    field_id: UUID
    action: str
    value: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = str(self.field_id)

        action = self.action

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_id": field_id,
                "action": action,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = UUID(d.pop("field_id"))

        action = d.pop("action")

        value = d.pop("value")

        field_condition_input = cls(
            field_id=field_id,
            action=action,
            value=value,
        )

        field_condition_input.additional_properties = d
        return field_condition_input

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
