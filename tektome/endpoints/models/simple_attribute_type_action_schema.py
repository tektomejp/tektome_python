from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.simple_attribute_type_action_schema_boolean_equals import SimpleAttributeTypeActionSchemaBooleanEquals
    from ..models.simple_attribute_type_action_schema_boolean_not_equals import (
        SimpleAttributeTypeActionSchemaBooleanNotEquals,
    )
    from ..models.simple_attribute_type_action_schema_date_after import SimpleAttributeTypeActionSchemaDateAfter
    from ..models.simple_attribute_type_action_schema_date_before import SimpleAttributeTypeActionSchemaDateBefore
    from ..models.simple_attribute_type_action_schema_date_equals import SimpleAttributeTypeActionSchemaDateEquals
    from ..models.simple_attribute_type_action_schema_date_not_equals import (
        SimpleAttributeTypeActionSchemaDateNotEquals,
    )
    from ..models.simple_attribute_type_action_schema_date_on_or_after import (
        SimpleAttributeTypeActionSchemaDateOnOrAfter,
    )
    from ..models.simple_attribute_type_action_schema_date_on_or_before import (
        SimpleAttributeTypeActionSchemaDateOnOrBefore,
    )
    from ..models.simple_attribute_type_action_schema_datetime_after import SimpleAttributeTypeActionSchemaDatetimeAfter
    from ..models.simple_attribute_type_action_schema_datetime_before import (
        SimpleAttributeTypeActionSchemaDatetimeBefore,
    )
    from ..models.simple_attribute_type_action_schema_datetime_equals import (
        SimpleAttributeTypeActionSchemaDatetimeEquals,
    )
    from ..models.simple_attribute_type_action_schema_datetime_not_equals import (
        SimpleAttributeTypeActionSchemaDatetimeNotEquals,
    )
    from ..models.simple_attribute_type_action_schema_datetime_on_or_after import (
        SimpleAttributeTypeActionSchemaDatetimeOnOrAfter,
    )
    from ..models.simple_attribute_type_action_schema_datetime_on_or_before import (
        SimpleAttributeTypeActionSchemaDatetimeOnOrBefore,
    )
    from ..models.simple_attribute_type_action_schema_float_equals import SimpleAttributeTypeActionSchemaFloatEquals
    from ..models.simple_attribute_type_action_schema_float_greater_than import (
        SimpleAttributeTypeActionSchemaFloatGreaterThan,
    )
    from ..models.simple_attribute_type_action_schema_float_greater_than_or_equal_to import (
        SimpleAttributeTypeActionSchemaFloatGreaterThanOrEqualTo,
    )
    from ..models.simple_attribute_type_action_schema_float_less_than import (
        SimpleAttributeTypeActionSchemaFloatLessThan,
    )
    from ..models.simple_attribute_type_action_schema_float_less_than_or_equal_to import (
        SimpleAttributeTypeActionSchemaFloatLessThanOrEqualTo,
    )
    from ..models.simple_attribute_type_action_schema_float_not_equals import (
        SimpleAttributeTypeActionSchemaFloatNotEquals,
    )
    from ..models.simple_attribute_type_action_schema_integer_equals import SimpleAttributeTypeActionSchemaIntegerEquals
    from ..models.simple_attribute_type_action_schema_integer_greater_than import (
        SimpleAttributeTypeActionSchemaIntegerGreaterThan,
    )
    from ..models.simple_attribute_type_action_schema_integer_greater_than_or_equal_to import (
        SimpleAttributeTypeActionSchemaIntegerGreaterThanOrEqualTo,
    )
    from ..models.simple_attribute_type_action_schema_integer_less_than import (
        SimpleAttributeTypeActionSchemaIntegerLessThan,
    )
    from ..models.simple_attribute_type_action_schema_integer_less_than_or_equal_to import (
        SimpleAttributeTypeActionSchemaIntegerLessThanOrEqualTo,
    )
    from ..models.simple_attribute_type_action_schema_integer_not_equals import (
        SimpleAttributeTypeActionSchemaIntegerNotEquals,
    )
    from ..models.simple_attribute_type_action_schema_string_contains import (
        SimpleAttributeTypeActionSchemaStringContains,
    )
    from ..models.simple_attribute_type_action_schema_string_exact import SimpleAttributeTypeActionSchemaStringExact
    from ..models.simple_attribute_type_action_schema_string_excludes import (
        SimpleAttributeTypeActionSchemaStringExcludes,
    )
    from ..models.simple_attribute_type_action_schema_string_includes import (
        SimpleAttributeTypeActionSchemaStringIncludes,
    )
    from ..models.simple_attribute_type_action_schema_string_matches import SimpleAttributeTypeActionSchemaStringMatches
    from ..models.simple_attribute_type_action_schema_string_means import SimpleAttributeTypeActionSchemaStringMeans
    from ..models.simple_attribute_type_action_schema_string_not_contains import (
        SimpleAttributeTypeActionSchemaStringNotContains,
    )
    from ..models.simple_attribute_type_action_schema_table_cell_matches import (
        SimpleAttributeTypeActionSchemaTableCellMatches,
    )
    from ..models.simple_attribute_type_action_schema_table_column_contains import (
        SimpleAttributeTypeActionSchemaTableColumnContains,
    )
    from ..models.simple_attribute_type_action_schema_time_after import SimpleAttributeTypeActionSchemaTimeAfter
    from ..models.simple_attribute_type_action_schema_time_before import SimpleAttributeTypeActionSchemaTimeBefore
    from ..models.simple_attribute_type_action_schema_time_equals import SimpleAttributeTypeActionSchemaTimeEquals
    from ..models.simple_attribute_type_action_schema_time_not_equals import (
        SimpleAttributeTypeActionSchemaTimeNotEquals,
    )
    from ..models.simple_attribute_type_action_schema_time_on_or_after import (
        SimpleAttributeTypeActionSchemaTimeOnOrAfter,
    )
    from ..models.simple_attribute_type_action_schema_time_on_or_before import (
        SimpleAttributeTypeActionSchemaTimeOnOrBefore,
    )


T = TypeVar("T", bound="SimpleAttributeTypeActionSchema")


@_attrs_define
class SimpleAttributeTypeActionSchema:
    """
    Attributes:
        string (list[SimpleAttributeTypeActionSchemaStringContains | SimpleAttributeTypeActionSchemaStringExact |
            SimpleAttributeTypeActionSchemaStringExcludes | SimpleAttributeTypeActionSchemaStringIncludes |
            SimpleAttributeTypeActionSchemaStringMatches | SimpleAttributeTypeActionSchemaStringMeans |
            SimpleAttributeTypeActionSchemaStringNotContains]): Action and value type for attribute type 'string'. Valid
            actions: contains, exact, excludes, includes, matches, means, not_contains. Value type: string.
        integer (list[SimpleAttributeTypeActionSchemaIntegerEquals | SimpleAttributeTypeActionSchemaIntegerGreaterThan |
            SimpleAttributeTypeActionSchemaIntegerGreaterThanOrEqualTo | SimpleAttributeTypeActionSchemaIntegerLessThan |
            SimpleAttributeTypeActionSchemaIntegerLessThanOrEqualTo | SimpleAttributeTypeActionSchemaIntegerNotEquals]):
            Action and value type for attribute type 'integer'. Valid actions: equals, greater_than,
            greater_than_or_equal_to, less_than, less_than_or_equal_to, not_equals. Value type: integer.
        float_ (list[SimpleAttributeTypeActionSchemaFloatEquals | SimpleAttributeTypeActionSchemaFloatGreaterThan |
            SimpleAttributeTypeActionSchemaFloatGreaterThanOrEqualTo | SimpleAttributeTypeActionSchemaFloatLessThan |
            SimpleAttributeTypeActionSchemaFloatLessThanOrEqualTo | SimpleAttributeTypeActionSchemaFloatNotEquals]): Action
            and value type for attribute type 'float'. Valid actions: equals, greater_than, greater_than_or_equal_to,
            less_than, less_than_or_equal_to, not_equals. Value type: float.
        boolean (list[SimpleAttributeTypeActionSchemaBooleanEquals | SimpleAttributeTypeActionSchemaBooleanNotEquals]):
            Action and value type for attribute type 'boolean'. Valid actions: equals, not_equals. Value type: boolean.
        date (list[SimpleAttributeTypeActionSchemaDateAfter | SimpleAttributeTypeActionSchemaDateBefore |
            SimpleAttributeTypeActionSchemaDateEquals | SimpleAttributeTypeActionSchemaDateNotEquals |
            SimpleAttributeTypeActionSchemaDateOnOrAfter | SimpleAttributeTypeActionSchemaDateOnOrBefore]): Action and value
            type for attribute type 'date'. Valid actions: after, before, equals, not_equals, on_or_after, on_or_before.
            Value type: date.
        datetime_ (list[SimpleAttributeTypeActionSchemaDatetimeAfter | SimpleAttributeTypeActionSchemaDatetimeBefore |
            SimpleAttributeTypeActionSchemaDatetimeEquals | SimpleAttributeTypeActionSchemaDatetimeNotEquals |
            SimpleAttributeTypeActionSchemaDatetimeOnOrAfter | SimpleAttributeTypeActionSchemaDatetimeOnOrBefore]): Action
            and value type for attribute type 'datetime'. Valid actions: after, before, equals, not_equals, on_or_after,
            on_or_before. Value type: datetime.
        time (list[SimpleAttributeTypeActionSchemaTimeAfter | SimpleAttributeTypeActionSchemaTimeBefore |
            SimpleAttributeTypeActionSchemaTimeEquals | SimpleAttributeTypeActionSchemaTimeNotEquals |
            SimpleAttributeTypeActionSchemaTimeOnOrAfter | SimpleAttributeTypeActionSchemaTimeOnOrBefore]): Action and value
            type for attribute type 'time'. Valid actions: after, before, equals, not_equals, on_or_after, on_or_before.
            Value type: time.
        table (list[SimpleAttributeTypeActionSchemaTableCellMatches |
            SimpleAttributeTypeActionSchemaTableColumnContains]): Action and value type for attribute type 'table'. Valid
            actions: cell_matches, column_contains. Value type: any.
    """

    string: list[
        SimpleAttributeTypeActionSchemaStringContains
        | SimpleAttributeTypeActionSchemaStringExact
        | SimpleAttributeTypeActionSchemaStringExcludes
        | SimpleAttributeTypeActionSchemaStringIncludes
        | SimpleAttributeTypeActionSchemaStringMatches
        | SimpleAttributeTypeActionSchemaStringMeans
        | SimpleAttributeTypeActionSchemaStringNotContains
    ]
    integer: list[
        SimpleAttributeTypeActionSchemaIntegerEquals
        | SimpleAttributeTypeActionSchemaIntegerGreaterThan
        | SimpleAttributeTypeActionSchemaIntegerGreaterThanOrEqualTo
        | SimpleAttributeTypeActionSchemaIntegerLessThan
        | SimpleAttributeTypeActionSchemaIntegerLessThanOrEqualTo
        | SimpleAttributeTypeActionSchemaIntegerNotEquals
    ]
    float_: list[
        SimpleAttributeTypeActionSchemaFloatEquals
        | SimpleAttributeTypeActionSchemaFloatGreaterThan
        | SimpleAttributeTypeActionSchemaFloatGreaterThanOrEqualTo
        | SimpleAttributeTypeActionSchemaFloatLessThan
        | SimpleAttributeTypeActionSchemaFloatLessThanOrEqualTo
        | SimpleAttributeTypeActionSchemaFloatNotEquals
    ]
    boolean: list[SimpleAttributeTypeActionSchemaBooleanEquals | SimpleAttributeTypeActionSchemaBooleanNotEquals]
    date: list[
        SimpleAttributeTypeActionSchemaDateAfter
        | SimpleAttributeTypeActionSchemaDateBefore
        | SimpleAttributeTypeActionSchemaDateEquals
        | SimpleAttributeTypeActionSchemaDateNotEquals
        | SimpleAttributeTypeActionSchemaDateOnOrAfter
        | SimpleAttributeTypeActionSchemaDateOnOrBefore
    ]
    datetime_: list[
        SimpleAttributeTypeActionSchemaDatetimeAfter
        | SimpleAttributeTypeActionSchemaDatetimeBefore
        | SimpleAttributeTypeActionSchemaDatetimeEquals
        | SimpleAttributeTypeActionSchemaDatetimeNotEquals
        | SimpleAttributeTypeActionSchemaDatetimeOnOrAfter
        | SimpleAttributeTypeActionSchemaDatetimeOnOrBefore
    ]
    time: list[
        SimpleAttributeTypeActionSchemaTimeAfter
        | SimpleAttributeTypeActionSchemaTimeBefore
        | SimpleAttributeTypeActionSchemaTimeEquals
        | SimpleAttributeTypeActionSchemaTimeNotEquals
        | SimpleAttributeTypeActionSchemaTimeOnOrAfter
        | SimpleAttributeTypeActionSchemaTimeOnOrBefore
    ]
    table: list[SimpleAttributeTypeActionSchemaTableCellMatches | SimpleAttributeTypeActionSchemaTableColumnContains]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.simple_attribute_type_action_schema_boolean_equals import (
            SimpleAttributeTypeActionSchemaBooleanEquals,
        )
        from ..models.simple_attribute_type_action_schema_date_after import SimpleAttributeTypeActionSchemaDateAfter
        from ..models.simple_attribute_type_action_schema_date_before import SimpleAttributeTypeActionSchemaDateBefore
        from ..models.simple_attribute_type_action_schema_date_equals import SimpleAttributeTypeActionSchemaDateEquals
        from ..models.simple_attribute_type_action_schema_date_not_equals import (
            SimpleAttributeTypeActionSchemaDateNotEquals,
        )
        from ..models.simple_attribute_type_action_schema_date_on_or_after import (
            SimpleAttributeTypeActionSchemaDateOnOrAfter,
        )
        from ..models.simple_attribute_type_action_schema_datetime_after import (
            SimpleAttributeTypeActionSchemaDatetimeAfter,
        )
        from ..models.simple_attribute_type_action_schema_datetime_before import (
            SimpleAttributeTypeActionSchemaDatetimeBefore,
        )
        from ..models.simple_attribute_type_action_schema_datetime_equals import (
            SimpleAttributeTypeActionSchemaDatetimeEquals,
        )
        from ..models.simple_attribute_type_action_schema_datetime_not_equals import (
            SimpleAttributeTypeActionSchemaDatetimeNotEquals,
        )
        from ..models.simple_attribute_type_action_schema_datetime_on_or_after import (
            SimpleAttributeTypeActionSchemaDatetimeOnOrAfter,
        )
        from ..models.simple_attribute_type_action_schema_float_equals import SimpleAttributeTypeActionSchemaFloatEquals
        from ..models.simple_attribute_type_action_schema_float_greater_than import (
            SimpleAttributeTypeActionSchemaFloatGreaterThan,
        )
        from ..models.simple_attribute_type_action_schema_float_greater_than_or_equal_to import (
            SimpleAttributeTypeActionSchemaFloatGreaterThanOrEqualTo,
        )
        from ..models.simple_attribute_type_action_schema_float_less_than import (
            SimpleAttributeTypeActionSchemaFloatLessThan,
        )
        from ..models.simple_attribute_type_action_schema_float_less_than_or_equal_to import (
            SimpleAttributeTypeActionSchemaFloatLessThanOrEqualTo,
        )
        from ..models.simple_attribute_type_action_schema_integer_equals import (
            SimpleAttributeTypeActionSchemaIntegerEquals,
        )
        from ..models.simple_attribute_type_action_schema_integer_greater_than import (
            SimpleAttributeTypeActionSchemaIntegerGreaterThan,
        )
        from ..models.simple_attribute_type_action_schema_integer_greater_than_or_equal_to import (
            SimpleAttributeTypeActionSchemaIntegerGreaterThanOrEqualTo,
        )
        from ..models.simple_attribute_type_action_schema_integer_less_than import (
            SimpleAttributeTypeActionSchemaIntegerLessThan,
        )
        from ..models.simple_attribute_type_action_schema_integer_less_than_or_equal_to import (
            SimpleAttributeTypeActionSchemaIntegerLessThanOrEqualTo,
        )
        from ..models.simple_attribute_type_action_schema_string_contains import (
            SimpleAttributeTypeActionSchemaStringContains,
        )
        from ..models.simple_attribute_type_action_schema_string_exact import SimpleAttributeTypeActionSchemaStringExact
        from ..models.simple_attribute_type_action_schema_string_excludes import (
            SimpleAttributeTypeActionSchemaStringExcludes,
        )
        from ..models.simple_attribute_type_action_schema_string_includes import (
            SimpleAttributeTypeActionSchemaStringIncludes,
        )
        from ..models.simple_attribute_type_action_schema_string_matches import (
            SimpleAttributeTypeActionSchemaStringMatches,
        )
        from ..models.simple_attribute_type_action_schema_string_means import SimpleAttributeTypeActionSchemaStringMeans
        from ..models.simple_attribute_type_action_schema_table_cell_matches import (
            SimpleAttributeTypeActionSchemaTableCellMatches,
        )
        from ..models.simple_attribute_type_action_schema_time_after import SimpleAttributeTypeActionSchemaTimeAfter
        from ..models.simple_attribute_type_action_schema_time_before import SimpleAttributeTypeActionSchemaTimeBefore
        from ..models.simple_attribute_type_action_schema_time_equals import SimpleAttributeTypeActionSchemaTimeEquals
        from ..models.simple_attribute_type_action_schema_time_not_equals import (
            SimpleAttributeTypeActionSchemaTimeNotEquals,
        )
        from ..models.simple_attribute_type_action_schema_time_on_or_after import (
            SimpleAttributeTypeActionSchemaTimeOnOrAfter,
        )

        string = []
        for string_item_data in self.string:
            string_item: dict[str, Any]
            if isinstance(string_item_data, SimpleAttributeTypeActionSchemaStringContains):
                string_item = string_item_data.to_dict()
            elif isinstance(string_item_data, SimpleAttributeTypeActionSchemaStringExact):
                string_item = string_item_data.to_dict()
            elif isinstance(string_item_data, SimpleAttributeTypeActionSchemaStringExcludes):
                string_item = string_item_data.to_dict()
            elif isinstance(string_item_data, SimpleAttributeTypeActionSchemaStringIncludes):
                string_item = string_item_data.to_dict()
            elif isinstance(string_item_data, SimpleAttributeTypeActionSchemaStringMatches):
                string_item = string_item_data.to_dict()
            elif isinstance(string_item_data, SimpleAttributeTypeActionSchemaStringMeans):
                string_item = string_item_data.to_dict()
            else:
                string_item = string_item_data.to_dict()

            string.append(string_item)

        integer = []
        for integer_item_data in self.integer:
            integer_item: dict[str, Any]
            if isinstance(integer_item_data, SimpleAttributeTypeActionSchemaIntegerEquals):
                integer_item = integer_item_data.to_dict()
            elif isinstance(integer_item_data, SimpleAttributeTypeActionSchemaIntegerGreaterThan):
                integer_item = integer_item_data.to_dict()
            elif isinstance(integer_item_data, SimpleAttributeTypeActionSchemaIntegerGreaterThanOrEqualTo):
                integer_item = integer_item_data.to_dict()
            elif isinstance(integer_item_data, SimpleAttributeTypeActionSchemaIntegerLessThan):
                integer_item = integer_item_data.to_dict()
            elif isinstance(integer_item_data, SimpleAttributeTypeActionSchemaIntegerLessThanOrEqualTo):
                integer_item = integer_item_data.to_dict()
            else:
                integer_item = integer_item_data.to_dict()

            integer.append(integer_item)

        float_ = []
        for float_item_data in self.float_:
            float_item: dict[str, Any]
            if isinstance(float_item_data, SimpleAttributeTypeActionSchemaFloatEquals):
                float_item = float_item_data.to_dict()
            elif isinstance(float_item_data, SimpleAttributeTypeActionSchemaFloatGreaterThan):
                float_item = float_item_data.to_dict()
            elif isinstance(float_item_data, SimpleAttributeTypeActionSchemaFloatGreaterThanOrEqualTo):
                float_item = float_item_data.to_dict()
            elif isinstance(float_item_data, SimpleAttributeTypeActionSchemaFloatLessThan):
                float_item = float_item_data.to_dict()
            elif isinstance(float_item_data, SimpleAttributeTypeActionSchemaFloatLessThanOrEqualTo):
                float_item = float_item_data.to_dict()
            else:
                float_item = float_item_data.to_dict()

            float_.append(float_item)

        boolean = []
        for boolean_item_data in self.boolean:
            boolean_item: dict[str, Any]
            if isinstance(boolean_item_data, SimpleAttributeTypeActionSchemaBooleanEquals):
                boolean_item = boolean_item_data.to_dict()
            else:
                boolean_item = boolean_item_data.to_dict()

            boolean.append(boolean_item)

        date = []
        for date_item_data in self.date:
            date_item: dict[str, Any]
            if isinstance(date_item_data, SimpleAttributeTypeActionSchemaDateAfter):
                date_item = date_item_data.to_dict()
            elif isinstance(date_item_data, SimpleAttributeTypeActionSchemaDateBefore):
                date_item = date_item_data.to_dict()
            elif isinstance(date_item_data, SimpleAttributeTypeActionSchemaDateEquals):
                date_item = date_item_data.to_dict()
            elif isinstance(date_item_data, SimpleAttributeTypeActionSchemaDateNotEquals):
                date_item = date_item_data.to_dict()
            elif isinstance(date_item_data, SimpleAttributeTypeActionSchemaDateOnOrAfter):
                date_item = date_item_data.to_dict()
            else:
                date_item = date_item_data.to_dict()

            date.append(date_item)

        datetime_ = []
        for datetime_item_data in self.datetime_:
            datetime_item: dict[str, Any]
            if isinstance(datetime_item_data, SimpleAttributeTypeActionSchemaDatetimeAfter):
                datetime_item = datetime_item_data.to_dict()
            elif isinstance(datetime_item_data, SimpleAttributeTypeActionSchemaDatetimeBefore):
                datetime_item = datetime_item_data.to_dict()
            elif isinstance(datetime_item_data, SimpleAttributeTypeActionSchemaDatetimeEquals):
                datetime_item = datetime_item_data.to_dict()
            elif isinstance(datetime_item_data, SimpleAttributeTypeActionSchemaDatetimeNotEquals):
                datetime_item = datetime_item_data.to_dict()
            elif isinstance(datetime_item_data, SimpleAttributeTypeActionSchemaDatetimeOnOrAfter):
                datetime_item = datetime_item_data.to_dict()
            else:
                datetime_item = datetime_item_data.to_dict()

            datetime_.append(datetime_item)

        time = []
        for time_item_data in self.time:
            time_item: dict[str, Any]
            if isinstance(time_item_data, SimpleAttributeTypeActionSchemaTimeAfter):
                time_item = time_item_data.to_dict()
            elif isinstance(time_item_data, SimpleAttributeTypeActionSchemaTimeBefore):
                time_item = time_item_data.to_dict()
            elif isinstance(time_item_data, SimpleAttributeTypeActionSchemaTimeEquals):
                time_item = time_item_data.to_dict()
            elif isinstance(time_item_data, SimpleAttributeTypeActionSchemaTimeNotEquals):
                time_item = time_item_data.to_dict()
            elif isinstance(time_item_data, SimpleAttributeTypeActionSchemaTimeOnOrAfter):
                time_item = time_item_data.to_dict()
            else:
                time_item = time_item_data.to_dict()

            time.append(time_item)

        table = []
        for table_item_data in self.table:
            table_item: dict[str, Any]
            if isinstance(table_item_data, SimpleAttributeTypeActionSchemaTableCellMatches):
                table_item = table_item_data.to_dict()
            else:
                table_item = table_item_data.to_dict()

            table.append(table_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "string": string,
                "integer": integer,
                "float": float_,
                "boolean": boolean,
                "date": date,
                "datetime": datetime_,
                "time": time,
                "table": table,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_attribute_type_action_schema_boolean_equals import (
            SimpleAttributeTypeActionSchemaBooleanEquals,
        )
        from ..models.simple_attribute_type_action_schema_boolean_not_equals import (
            SimpleAttributeTypeActionSchemaBooleanNotEquals,
        )
        from ..models.simple_attribute_type_action_schema_date_after import SimpleAttributeTypeActionSchemaDateAfter
        from ..models.simple_attribute_type_action_schema_date_before import SimpleAttributeTypeActionSchemaDateBefore
        from ..models.simple_attribute_type_action_schema_date_equals import SimpleAttributeTypeActionSchemaDateEquals
        from ..models.simple_attribute_type_action_schema_date_not_equals import (
            SimpleAttributeTypeActionSchemaDateNotEquals,
        )
        from ..models.simple_attribute_type_action_schema_date_on_or_after import (
            SimpleAttributeTypeActionSchemaDateOnOrAfter,
        )
        from ..models.simple_attribute_type_action_schema_date_on_or_before import (
            SimpleAttributeTypeActionSchemaDateOnOrBefore,
        )
        from ..models.simple_attribute_type_action_schema_datetime_after import (
            SimpleAttributeTypeActionSchemaDatetimeAfter,
        )
        from ..models.simple_attribute_type_action_schema_datetime_before import (
            SimpleAttributeTypeActionSchemaDatetimeBefore,
        )
        from ..models.simple_attribute_type_action_schema_datetime_equals import (
            SimpleAttributeTypeActionSchemaDatetimeEquals,
        )
        from ..models.simple_attribute_type_action_schema_datetime_not_equals import (
            SimpleAttributeTypeActionSchemaDatetimeNotEquals,
        )
        from ..models.simple_attribute_type_action_schema_datetime_on_or_after import (
            SimpleAttributeTypeActionSchemaDatetimeOnOrAfter,
        )
        from ..models.simple_attribute_type_action_schema_datetime_on_or_before import (
            SimpleAttributeTypeActionSchemaDatetimeOnOrBefore,
        )
        from ..models.simple_attribute_type_action_schema_float_equals import SimpleAttributeTypeActionSchemaFloatEquals
        from ..models.simple_attribute_type_action_schema_float_greater_than import (
            SimpleAttributeTypeActionSchemaFloatGreaterThan,
        )
        from ..models.simple_attribute_type_action_schema_float_greater_than_or_equal_to import (
            SimpleAttributeTypeActionSchemaFloatGreaterThanOrEqualTo,
        )
        from ..models.simple_attribute_type_action_schema_float_less_than import (
            SimpleAttributeTypeActionSchemaFloatLessThan,
        )
        from ..models.simple_attribute_type_action_schema_float_less_than_or_equal_to import (
            SimpleAttributeTypeActionSchemaFloatLessThanOrEqualTo,
        )
        from ..models.simple_attribute_type_action_schema_float_not_equals import (
            SimpleAttributeTypeActionSchemaFloatNotEquals,
        )
        from ..models.simple_attribute_type_action_schema_integer_equals import (
            SimpleAttributeTypeActionSchemaIntegerEquals,
        )
        from ..models.simple_attribute_type_action_schema_integer_greater_than import (
            SimpleAttributeTypeActionSchemaIntegerGreaterThan,
        )
        from ..models.simple_attribute_type_action_schema_integer_greater_than_or_equal_to import (
            SimpleAttributeTypeActionSchemaIntegerGreaterThanOrEqualTo,
        )
        from ..models.simple_attribute_type_action_schema_integer_less_than import (
            SimpleAttributeTypeActionSchemaIntegerLessThan,
        )
        from ..models.simple_attribute_type_action_schema_integer_less_than_or_equal_to import (
            SimpleAttributeTypeActionSchemaIntegerLessThanOrEqualTo,
        )
        from ..models.simple_attribute_type_action_schema_integer_not_equals import (
            SimpleAttributeTypeActionSchemaIntegerNotEquals,
        )
        from ..models.simple_attribute_type_action_schema_string_contains import (
            SimpleAttributeTypeActionSchemaStringContains,
        )
        from ..models.simple_attribute_type_action_schema_string_exact import SimpleAttributeTypeActionSchemaStringExact
        from ..models.simple_attribute_type_action_schema_string_excludes import (
            SimpleAttributeTypeActionSchemaStringExcludes,
        )
        from ..models.simple_attribute_type_action_schema_string_includes import (
            SimpleAttributeTypeActionSchemaStringIncludes,
        )
        from ..models.simple_attribute_type_action_schema_string_matches import (
            SimpleAttributeTypeActionSchemaStringMatches,
        )
        from ..models.simple_attribute_type_action_schema_string_means import SimpleAttributeTypeActionSchemaStringMeans
        from ..models.simple_attribute_type_action_schema_string_not_contains import (
            SimpleAttributeTypeActionSchemaStringNotContains,
        )
        from ..models.simple_attribute_type_action_schema_table_cell_matches import (
            SimpleAttributeTypeActionSchemaTableCellMatches,
        )
        from ..models.simple_attribute_type_action_schema_table_column_contains import (
            SimpleAttributeTypeActionSchemaTableColumnContains,
        )
        from ..models.simple_attribute_type_action_schema_time_after import SimpleAttributeTypeActionSchemaTimeAfter
        from ..models.simple_attribute_type_action_schema_time_before import SimpleAttributeTypeActionSchemaTimeBefore
        from ..models.simple_attribute_type_action_schema_time_equals import SimpleAttributeTypeActionSchemaTimeEquals
        from ..models.simple_attribute_type_action_schema_time_not_equals import (
            SimpleAttributeTypeActionSchemaTimeNotEquals,
        )
        from ..models.simple_attribute_type_action_schema_time_on_or_after import (
            SimpleAttributeTypeActionSchemaTimeOnOrAfter,
        )
        from ..models.simple_attribute_type_action_schema_time_on_or_before import (
            SimpleAttributeTypeActionSchemaTimeOnOrBefore,
        )

        d = dict(src_dict)
        string = []
        _string = d.pop("string")
        for string_item_data in _string:

            def _parse_string_item(
                data: object,
            ) -> (
                SimpleAttributeTypeActionSchemaStringContains
                | SimpleAttributeTypeActionSchemaStringExact
                | SimpleAttributeTypeActionSchemaStringExcludes
                | SimpleAttributeTypeActionSchemaStringIncludes
                | SimpleAttributeTypeActionSchemaStringMatches
                | SimpleAttributeTypeActionSchemaStringMeans
                | SimpleAttributeTypeActionSchemaStringNotContains
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    string_item_type_0 = SimpleAttributeTypeActionSchemaStringContains.from_dict(data)

                    return string_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    string_item_type_1 = SimpleAttributeTypeActionSchemaStringExact.from_dict(data)

                    return string_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    string_item_type_2 = SimpleAttributeTypeActionSchemaStringExcludes.from_dict(data)

                    return string_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    string_item_type_3 = SimpleAttributeTypeActionSchemaStringIncludes.from_dict(data)

                    return string_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    string_item_type_4 = SimpleAttributeTypeActionSchemaStringMatches.from_dict(data)

                    return string_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    string_item_type_5 = SimpleAttributeTypeActionSchemaStringMeans.from_dict(data)

                    return string_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                string_item_type_6 = SimpleAttributeTypeActionSchemaStringNotContains.from_dict(data)

                return string_item_type_6

            string_item = _parse_string_item(string_item_data)

            string.append(string_item)

        integer = []
        _integer = d.pop("integer")
        for integer_item_data in _integer:

            def _parse_integer_item(
                data: object,
            ) -> (
                SimpleAttributeTypeActionSchemaIntegerEquals
                | SimpleAttributeTypeActionSchemaIntegerGreaterThan
                | SimpleAttributeTypeActionSchemaIntegerGreaterThanOrEqualTo
                | SimpleAttributeTypeActionSchemaIntegerLessThan
                | SimpleAttributeTypeActionSchemaIntegerLessThanOrEqualTo
                | SimpleAttributeTypeActionSchemaIntegerNotEquals
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    integer_item_type_0 = SimpleAttributeTypeActionSchemaIntegerEquals.from_dict(data)

                    return integer_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    integer_item_type_1 = SimpleAttributeTypeActionSchemaIntegerGreaterThan.from_dict(data)

                    return integer_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    integer_item_type_2 = SimpleAttributeTypeActionSchemaIntegerGreaterThanOrEqualTo.from_dict(data)

                    return integer_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    integer_item_type_3 = SimpleAttributeTypeActionSchemaIntegerLessThan.from_dict(data)

                    return integer_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    integer_item_type_4 = SimpleAttributeTypeActionSchemaIntegerLessThanOrEqualTo.from_dict(data)

                    return integer_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                integer_item_type_5 = SimpleAttributeTypeActionSchemaIntegerNotEquals.from_dict(data)

                return integer_item_type_5

            integer_item = _parse_integer_item(integer_item_data)

            integer.append(integer_item)

        float_ = []
        _float_ = d.pop("float")
        for float_item_data in _float_:

            def _parse_float_item(
                data: object,
            ) -> (
                SimpleAttributeTypeActionSchemaFloatEquals
                | SimpleAttributeTypeActionSchemaFloatGreaterThan
                | SimpleAttributeTypeActionSchemaFloatGreaterThanOrEqualTo
                | SimpleAttributeTypeActionSchemaFloatLessThan
                | SimpleAttributeTypeActionSchemaFloatLessThanOrEqualTo
                | SimpleAttributeTypeActionSchemaFloatNotEquals
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    float_item_type_0 = SimpleAttributeTypeActionSchemaFloatEquals.from_dict(data)

                    return float_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    float_item_type_1 = SimpleAttributeTypeActionSchemaFloatGreaterThan.from_dict(data)

                    return float_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    float_item_type_2 = SimpleAttributeTypeActionSchemaFloatGreaterThanOrEqualTo.from_dict(data)

                    return float_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    float_item_type_3 = SimpleAttributeTypeActionSchemaFloatLessThan.from_dict(data)

                    return float_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    float_item_type_4 = SimpleAttributeTypeActionSchemaFloatLessThanOrEqualTo.from_dict(data)

                    return float_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                float_item_type_5 = SimpleAttributeTypeActionSchemaFloatNotEquals.from_dict(data)

                return float_item_type_5

            float_item = _parse_float_item(float_item_data)

            float_.append(float_item)

        boolean = []
        _boolean = d.pop("boolean")
        for boolean_item_data in _boolean:

            def _parse_boolean_item(
                data: object,
            ) -> SimpleAttributeTypeActionSchemaBooleanEquals | SimpleAttributeTypeActionSchemaBooleanNotEquals:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    boolean_item_type_0 = SimpleAttributeTypeActionSchemaBooleanEquals.from_dict(data)

                    return boolean_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                boolean_item_type_1 = SimpleAttributeTypeActionSchemaBooleanNotEquals.from_dict(data)

                return boolean_item_type_1

            boolean_item = _parse_boolean_item(boolean_item_data)

            boolean.append(boolean_item)

        date = []
        _date = d.pop("date")
        for date_item_data in _date:

            def _parse_date_item(
                data: object,
            ) -> (
                SimpleAttributeTypeActionSchemaDateAfter
                | SimpleAttributeTypeActionSchemaDateBefore
                | SimpleAttributeTypeActionSchemaDateEquals
                | SimpleAttributeTypeActionSchemaDateNotEquals
                | SimpleAttributeTypeActionSchemaDateOnOrAfter
                | SimpleAttributeTypeActionSchemaDateOnOrBefore
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    date_item_type_0 = SimpleAttributeTypeActionSchemaDateAfter.from_dict(data)

                    return date_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    date_item_type_1 = SimpleAttributeTypeActionSchemaDateBefore.from_dict(data)

                    return date_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    date_item_type_2 = SimpleAttributeTypeActionSchemaDateEquals.from_dict(data)

                    return date_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    date_item_type_3 = SimpleAttributeTypeActionSchemaDateNotEquals.from_dict(data)

                    return date_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    date_item_type_4 = SimpleAttributeTypeActionSchemaDateOnOrAfter.from_dict(data)

                    return date_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                date_item_type_5 = SimpleAttributeTypeActionSchemaDateOnOrBefore.from_dict(data)

                return date_item_type_5

            date_item = _parse_date_item(date_item_data)

            date.append(date_item)

        datetime_ = []
        _datetime_ = d.pop("datetime")
        for datetime_item_data in _datetime_:

            def _parse_datetime_item(
                data: object,
            ) -> (
                SimpleAttributeTypeActionSchemaDatetimeAfter
                | SimpleAttributeTypeActionSchemaDatetimeBefore
                | SimpleAttributeTypeActionSchemaDatetimeEquals
                | SimpleAttributeTypeActionSchemaDatetimeNotEquals
                | SimpleAttributeTypeActionSchemaDatetimeOnOrAfter
                | SimpleAttributeTypeActionSchemaDatetimeOnOrBefore
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    datetime_item_type_0 = SimpleAttributeTypeActionSchemaDatetimeAfter.from_dict(data)

                    return datetime_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    datetime_item_type_1 = SimpleAttributeTypeActionSchemaDatetimeBefore.from_dict(data)

                    return datetime_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    datetime_item_type_2 = SimpleAttributeTypeActionSchemaDatetimeEquals.from_dict(data)

                    return datetime_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    datetime_item_type_3 = SimpleAttributeTypeActionSchemaDatetimeNotEquals.from_dict(data)

                    return datetime_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    datetime_item_type_4 = SimpleAttributeTypeActionSchemaDatetimeOnOrAfter.from_dict(data)

                    return datetime_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                datetime_item_type_5 = SimpleAttributeTypeActionSchemaDatetimeOnOrBefore.from_dict(data)

                return datetime_item_type_5

            datetime_item = _parse_datetime_item(datetime_item_data)

            datetime_.append(datetime_item)

        time = []
        _time = d.pop("time")
        for time_item_data in _time:

            def _parse_time_item(
                data: object,
            ) -> (
                SimpleAttributeTypeActionSchemaTimeAfter
                | SimpleAttributeTypeActionSchemaTimeBefore
                | SimpleAttributeTypeActionSchemaTimeEquals
                | SimpleAttributeTypeActionSchemaTimeNotEquals
                | SimpleAttributeTypeActionSchemaTimeOnOrAfter
                | SimpleAttributeTypeActionSchemaTimeOnOrBefore
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    time_item_type_0 = SimpleAttributeTypeActionSchemaTimeAfter.from_dict(data)

                    return time_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    time_item_type_1 = SimpleAttributeTypeActionSchemaTimeBefore.from_dict(data)

                    return time_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    time_item_type_2 = SimpleAttributeTypeActionSchemaTimeEquals.from_dict(data)

                    return time_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    time_item_type_3 = SimpleAttributeTypeActionSchemaTimeNotEquals.from_dict(data)

                    return time_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    time_item_type_4 = SimpleAttributeTypeActionSchemaTimeOnOrAfter.from_dict(data)

                    return time_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                time_item_type_5 = SimpleAttributeTypeActionSchemaTimeOnOrBefore.from_dict(data)

                return time_item_type_5

            time_item = _parse_time_item(time_item_data)

            time.append(time_item)

        table = []
        _table = d.pop("table")
        for table_item_data in _table:

            def _parse_table_item(
                data: object,
            ) -> SimpleAttributeTypeActionSchemaTableCellMatches | SimpleAttributeTypeActionSchemaTableColumnContains:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    table_item_type_0 = SimpleAttributeTypeActionSchemaTableCellMatches.from_dict(data)

                    return table_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                table_item_type_1 = SimpleAttributeTypeActionSchemaTableColumnContains.from_dict(data)

                return table_item_type_1

            table_item = _parse_table_item(table_item_data)

            table.append(table_item)

        simple_attribute_type_action_schema = cls(
            string=string,
            integer=integer,
            float_=float_,
            boolean=boolean,
            date=date,
            datetime_=datetime_,
            time=time,
            table=table,
        )

        simple_attribute_type_action_schema.additional_properties = d
        return simple_attribute_type_action_schema

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
