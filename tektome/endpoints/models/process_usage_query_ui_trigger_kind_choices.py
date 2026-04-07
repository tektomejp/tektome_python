from enum import Enum


class ProcessUsageQueryUiTriggerKindChoices(str, Enum):
    PROJECT = "project"
    PROJECTS = "project[]"
    RESOURCE = "resource"
    RESOURCES = "resource[]"

    def __str__(self) -> str:
        return str(self.value)
