from enum import Enum


class ExecutionQueryParamsExecutionStatus(str, Enum):
    AUTO_APPROVED = "auto_approved"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"
    WAITING_APPROVAL = "waiting_approval"

    def __str__(self) -> str:
        return str(self.value)
