from enum import Enum


class GetGeneralDataspaceAttributeDataspaceEntityType(str, Enum):
    PROJECT = "project"
    RESOURCE = "resource"

    def __str__(self) -> str:
        return str(self.value)
