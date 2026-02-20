from enum import Enum


class TableColumnType(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    FLOAT = "float"
    INTEGER = "integer"
    JSON = "json"
    MULTI_SELECT = "multi_select"
    SINGLE_SELECT = "single_select"
    STRING = "string"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
