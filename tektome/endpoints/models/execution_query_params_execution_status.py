from enum import Enum


class ExecutionQueryParamsExecutionStatus(str, Enum):
    AUTO_APPROVED = "auto_approved"
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
