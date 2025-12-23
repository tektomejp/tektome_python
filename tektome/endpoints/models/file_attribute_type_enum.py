from enum import Enum


class FileAttributeTypeEnum(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    FLOAT = "float"
    INT = "int"
    JSON = "json"
    STRING = "string"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
