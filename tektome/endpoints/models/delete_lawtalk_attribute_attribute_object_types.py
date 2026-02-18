from enum import Enum


class DeleteLawtalkAttributeAttributeObjectTypes(str, Enum):
    FOLDER = "folder"
    PROJECT = "project"
    REQUIREMENT = "requirement"
    RESOURCE = "resource"
    RESOURCE_GROUP = "resource-group"

    def __str__(self) -> str:
        return str(self.value)
