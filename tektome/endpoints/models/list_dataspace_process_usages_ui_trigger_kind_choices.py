from enum import Enum


class ListDataspaceProcessUsagesUiTriggerKindChoices(str, Enum):
    PROJECT = "project[]"
    RESOURCE = "resource[]"

    def __str__(self) -> str:
        return str(self.value)
