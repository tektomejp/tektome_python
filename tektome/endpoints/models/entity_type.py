from enum import Enum


class EntityType(str, Enum):
    PROJECT = "project"
    RESOURCE = "resource"
    RESOURCE_GROUP = "resource_group"

    def __str__(self) -> str:
        return str(self.value)
