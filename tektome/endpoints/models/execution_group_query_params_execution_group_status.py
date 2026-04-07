from enum import Enum


class ExecutionGroupQueryParamsExecutionGroupStatus(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"
    INITIALIZING = "initializing"
    RUNNING = "running"
    WAITING_APPROVAL = "waiting_approval"

    def __str__(self) -> str:
        return str(self.value)
