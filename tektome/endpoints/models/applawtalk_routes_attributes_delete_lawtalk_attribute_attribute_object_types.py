from enum import Enum


class ApplawtalkRoutesAttributesDeleteLawtalkAttributeAttributeObjectTypes(str, Enum):
    PROJECT = "project"
    REQUIREMENT = "requirement"
    RESOURCE = "resource"
    RESOURCE_GROUP = "resource-group"

    def __str__(self) -> str:
        return str(self.value)
