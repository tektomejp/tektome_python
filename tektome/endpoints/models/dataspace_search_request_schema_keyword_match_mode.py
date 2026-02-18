from enum import Enum


class DataspaceSearchRequestSchemaKeywordMatchMode(str, Enum):
    ALL = "all"
    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)
