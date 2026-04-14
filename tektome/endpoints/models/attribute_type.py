from enum import Enum


class AttributeType(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    FLOAT = "float"
    INTEGER = "int"
    JSON = "json"
    STRING = "string"
    TABLE = "table"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
