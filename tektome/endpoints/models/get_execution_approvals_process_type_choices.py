from enum import Enum


class GetExecutionApprovalsProcessTypeChoices(str, Enum):
    GENERAL = "general"
    PROJECT_ATTRIBUTE_EXTRACTION = "project_attr_extraction"
    RESOURCE_ATTRIBUTE_EXTRACTION = "resource_attr_extraction"

    def __str__(self) -> str:
        return str(self.value)
