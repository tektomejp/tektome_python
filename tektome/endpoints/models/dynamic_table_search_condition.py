from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.simple_attribute_type import SimpleAttributeType
from ..models.table_condition_action import TableConditionAction

if TYPE_CHECKING:
    from ..models.cell_coordinate import CellCoordinate
    from ..models.dynamic_boolean_value import DynamicBooleanValue
    from ..models.dynamic_date_time_value import DynamicDateTimeValue
    from ..models.dynamic_date_value import DynamicDateValue
    from ..models.dynamic_float_value import DynamicFloatValue
    from ..models.dynamic_integer_value import DynamicIntegerValue
    from ..models.dynamic_string_value import DynamicStringValue
    from ..models.dynamic_time_value import DynamicTimeValue


T = TypeVar("T", bound="DynamicTableSearchCondition")


@_attrs_define
class DynamicTableSearchCondition:
    """
    Attributes:
        attribute_name (str): The name of the attribute to filter on
        attribute_type (Literal['table']): The type of the attribute being filtered (table)
        action (TableConditionAction): Allowed actions for table conditions.
            - column_contains (For example: column "age" contains value 30)
            - cell_matches (For example: cell at (column "age", row 0) matches value 30)
        key (CellCoordinate | int | str): The key to filter by (e.g., column name, row index, or cell coordinate)
        value (DynamicBooleanValue | DynamicDateTimeValue | DynamicDateValue | DynamicFloatValue | DynamicIntegerValue |
            DynamicStringValue | DynamicTimeValue): The dynamic value type to filter by
        value_type (SimpleAttributeType):
    """

    attribute_name: str
    attribute_type: Literal["table"]
    action: TableConditionAction
    key: CellCoordinate | int | str
    value: (
        DynamicBooleanValue
        | DynamicDateTimeValue
        | DynamicDateValue
        | DynamicFloatValue
        | DynamicIntegerValue
        | DynamicStringValue
        | DynamicTimeValue
    )
    value_type: SimpleAttributeType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cell_coordinate import CellCoordinate
        from ..models.dynamic_boolean_value import DynamicBooleanValue
        from ..models.dynamic_date_time_value import DynamicDateTimeValue
        from ..models.dynamic_date_value import DynamicDateValue
        from ..models.dynamic_float_value import DynamicFloatValue
        from ..models.dynamic_integer_value import DynamicIntegerValue
        from ..models.dynamic_string_value import DynamicStringValue

        attribute_name = self.attribute_name

        attribute_type = self.attribute_type

        action = self.action.value

        key: dict[str, Any] | int | str
        if isinstance(self.key, CellCoordinate):
            key = self.key.to_dict()
        else:
            key = self.key

        value: dict[str, Any]
        if isinstance(self.value, DynamicStringValue):
            value = self.value.to_dict()
        elif isinstance(self.value, DynamicIntegerValue):
            value = self.value.to_dict()
        elif isinstance(self.value, DynamicFloatValue):
            value = self.value.to_dict()
        elif isinstance(self.value, DynamicBooleanValue):
            value = self.value.to_dict()
        elif isinstance(self.value, DynamicDateValue):
            value = self.value.to_dict()
        elif isinstance(self.value, DynamicDateTimeValue):
            value = self.value.to_dict()
        else:
            value = self.value.to_dict()

        value_type = self.value_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_name": attribute_name,
                "attribute_type": attribute_type,
                "action": action,
                "key": key,
                "value": value,
                "value_type": value_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cell_coordinate import CellCoordinate
        from ..models.dynamic_boolean_value import DynamicBooleanValue
        from ..models.dynamic_date_time_value import DynamicDateTimeValue
        from ..models.dynamic_date_value import DynamicDateValue
        from ..models.dynamic_float_value import DynamicFloatValue
        from ..models.dynamic_integer_value import DynamicIntegerValue
        from ..models.dynamic_string_value import DynamicStringValue
        from ..models.dynamic_time_value import DynamicTimeValue

        d = dict(src_dict)
        attribute_name = d.pop("attribute_name")

        attribute_type = cast(Literal["table"], d.pop("attribute_type"))
        if attribute_type != "table":
            raise ValueError(f"attribute_type must match const 'table', got '{attribute_type}'")

        action = TableConditionAction(d.pop("action"))

        def _parse_key(data: object) -> CellCoordinate | int | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                key_type_2 = CellCoordinate.from_dict(data)

                return key_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CellCoordinate | int | str, data)

        key = _parse_key(d.pop("key"))

        def _parse_value(
            data: object,
        ) -> (
            DynamicBooleanValue
            | DynamicDateTimeValue
            | DynamicDateValue
            | DynamicFloatValue
            | DynamicIntegerValue
            | DynamicStringValue
            | DynamicTimeValue
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = DynamicStringValue.from_dict(data)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = DynamicIntegerValue.from_dict(data)

                return value_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_2 = DynamicFloatValue.from_dict(data)

                return value_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_3 = DynamicBooleanValue.from_dict(data)

                return value_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_4 = DynamicDateValue.from_dict(data)

                return value_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_5 = DynamicDateTimeValue.from_dict(data)

                return value_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            value_type_6 = DynamicTimeValue.from_dict(data)

            return value_type_6

        value = _parse_value(d.pop("value"))

        value_type = SimpleAttributeType(d.pop("value_type"))

        dynamic_table_search_condition = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            action=action,
            key=key,
            value=value,
            value_type=value_type,
        )

        dynamic_table_search_condition.additional_properties = d
        return dynamic_table_search_condition

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
