from enum import Enum


class DeleteTableAttributeRowAttributeObjectTypes(str, Enum):
    FOLDER = "folder"
    PROJECT = "project"
    RESOURCE = "resource"
    RESOURCE_GROUP = "resource-group"
    SECTION = "section"

    def __str__(self) -> str:
        return str(self.value)
