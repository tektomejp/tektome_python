from enum import Enum


class AttributeType(str, Enum):
    BOOLEAN_ATTRIBUTES = "boolean_attributes"
    COORDINATE_ATTRIBUTES = "coordinate_attributes"
    DATETIME_ATTRIBUTES = "datetime_attributes"
    DATE_ATTRIBUTES = "date_attributes"
    FLOAT_ATTRIBUTES = "float_attributes"
    INTEGER_ATTRIBUTES = "integer_attributes"
    JSON_ATTRIBUTES = "json_attributes"
    LIST_OBJECT_ATTRIBUTES = "list_object_attributes"
    MULTI_SELECT_ATTRIBUTES = "multi_select_attributes"
    POLYGON_ATTRIBUTES = "polygon_attributes"
    SINGLE_SELECT_ATTRIBUTES = "single_select_attributes"
    STRING_ATTRIBUTES = "string_attributes"
    TABLE_ATTRIBUTES = "table_attributes"
    TIME_ATTRIBUTES = "time_attributes"

    def __str__(self) -> str:
        return str(self.value)
