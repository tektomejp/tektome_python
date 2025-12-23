from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.date_time_condition_action import DateTimeConditionAction

T = TypeVar("T", bound="TimeSearchCondition")


@_attrs_define
class TimeSearchCondition:
    """Data Model for time conditions. Expect attribute_type to be "time"

    Attributes:
        attribute_name (str): The name of the attribute to filter on
        attribute_type (Literal['time']): The type of the attribute being filtered (time)
        action (DateTimeConditionAction): Allowed actions for date/time conditions.
            - equals (For example: 2023-01-01 equals 2023-01-01)
            - not_equals (For example: 2023-01-01 not equals 2023-01-02)
            - before (For example: 2023-01-01 before 2023-01-02)
            - after (For example: 2023-01-02 after 2023-01-01)
            - on_or_before (For example: 2023-01-01 on or before 2023-01-02)
            - on_or_after (For example: 2023-01-02 on or after 2023-01-01)
        value (str): The value to filter by
    """

    attribute_name: str
    attribute_type: Literal["time"]
    action: DateTimeConditionAction
    value: str
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

        attribute_type = cast(Literal["time"], d.pop("attribute_type"))
        if attribute_type != "time":
            raise ValueError(f"attribute_type must match const 'time', got '{attribute_type}'")

        action = DateTimeConditionAction(d.pop("action"))

        value = d.pop("value")

        time_search_condition = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            action=action,
            value=value,
        )

        time_search_condition.additional_properties = d
        return time_search_condition

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
