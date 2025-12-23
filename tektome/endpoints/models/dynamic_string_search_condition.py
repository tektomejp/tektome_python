from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.string_condition_action import StringConditionAction

if TYPE_CHECKING:
    from ..models.dynamic_string_value import DynamicStringValue


T = TypeVar("T", bound="DynamicStringSearchCondition")


@_attrs_define
class DynamicStringSearchCondition:
    """
    Attributes:
        attribute_name (str): The name of the attribute to filter on
        attribute_type (Literal['string']): The type of the attribute being filtered (string)
        action (StringConditionAction): Allowed actions for string conditions.
            - includes (For example: "foo" includes "foobar", treated as filtering)
            - excludes (For example: "foo" excludes "foobar", treated as filtering)
            - matches (For example: "foobar" could match "foobar", "barbaz" but not "bazqux", treated as querying)
            - means (For example: "royal" could mean "king & queen", "monarch", "sovereign", treated as querying)
        value (DynamicStringValue): Dynamic value for string attributes.
    """

    attribute_name: str
    attribute_type: Literal["string"]
    action: StringConditionAction
    value: DynamicStringValue
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_name = self.attribute_name

        attribute_type = self.attribute_type

        action = self.action.value

        value = self.value.to_dict()

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
        from ..models.dynamic_string_value import DynamicStringValue

        d = dict(src_dict)
        attribute_name = d.pop("attribute_name")

        attribute_type = cast(Literal["string"], d.pop("attribute_type"))
        if attribute_type != "string":
            raise ValueError(f"attribute_type must match const 'string', got '{attribute_type}'")

        action = StringConditionAction(d.pop("action"))

        value = DynamicStringValue.from_dict(d.pop("value"))

        dynamic_string_search_condition = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            action=action,
            value=value,
        )

        dynamic_string_search_condition.additional_properties = d
        return dynamic_string_search_condition

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
