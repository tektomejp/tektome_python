from enum import Enum


class ListCoreProjectProcessesUiTriggerKindChoices(str, Enum):
    PROJECT = "project[]"
    RESOURCE = "resource[]"

    def __str__(self) -> str:
        return str(self.value)
