from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.numeric_condition_action import NumericConditionAction

T = TypeVar("T", bound="FloatSearchCondition")


@_attrs_define
class FloatSearchCondition:
    """Data Model for float conditions. Expect attribute_type to be "float"

    Attributes:
        attribute_name (str): The name of the attribute to filter on
        attribute_type (Literal['float']): The type of the attribute being filtered (float)
        action (NumericConditionAction): Allowed actions for numeric conditions.

            - equals (For example: 5 equals 5)
            - not_equals (For example: 5 not equals 3)
            - greater_than (For example: 5 greater than 3)
            - less_than (For example: 3 less than 5)
            - greater_than_or_equal_to (For example: 5 greater than or equal to 5)
            - less_than_or_equal_to (For example: 3 less than or equal to 5)
        value (float): The value to filter by
    """

    attribute_name: str
    attribute_type: Literal["float"]
    action: NumericConditionAction
    value: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_name = self.attribute_name

        attribute_type = self.attribute_type

        action = self.action.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_name": attribute_name,
                "attribute_type": attribute_type,
                "action": action,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attribute_name = d.pop("attribute_name")

        attribute_type = cast(Literal["float"], d.pop("attribute_type"))
        if attribute_type != "float":
            raise ValueError(f"attribute_type must match const 'float', got '{attribute_type}'")

        action = NumericConditionAction(d.pop("action"))

        value = d.pop("value")

        float_search_condition = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            action=action,
            value=value,
        )

        float_search_condition.additional_properties = d
        return float_search_condition

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
