from enum import Enum


class ExecutionApprovalsQueryParamsProcessTypeChoices(str, Enum):
    GENERAL = "general"
    PROJECT_ATTR_EXTRACTION = "project_attr_extraction"
    RESOURCE_ATTR_EXTRACTION = "resource_attr_extraction"

    def __str__(self) -> str:
        return str(self.value)
