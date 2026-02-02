from enum import Enum


class GetExecuteProcessMetadataExecuteMetadataKind(str, Enum):
    PROJECT = "project"
    RESOURCE = "resource"

    def __str__(self) -> str:
        return str(self.value)
