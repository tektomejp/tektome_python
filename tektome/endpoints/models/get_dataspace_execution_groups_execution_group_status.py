from enum import Enum


class GetDataspaceExecutionGroupsExecutionGroupStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    INITIALIZING = "initializing"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
