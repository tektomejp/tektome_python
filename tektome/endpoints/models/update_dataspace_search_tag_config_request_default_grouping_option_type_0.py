from enum import Enum


class UpdateDataspaceSearchTagConfigRequestDefaultGroupingOptionType0(str, Enum):
    PROJECT = "project"
    RESOURCE = "resource"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
