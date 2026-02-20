from enum import Enum


class SimpleAttributeType(str, Enum):
    BOOLEAN = "boolean"
    COORDINATE = "coordinate"
    DATE = "date"
    DATETIME = "datetime"
    FLOAT = "float"
    INTEGER = "integer"
    JSON = "json"
    LIST_OBJECT = "list_object"
    MULTI_SELECT = "multi_select"
    POLYGON = "polygon"
    SINGLE_SELECT = "single_select"
    STRING = "string"
    TABLE = "table"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
