from enum import Enum


class ExecutionGroupQueryParamsExecutionReviewStatus(str, Enum):
    NOT_REQUIRED = "not_required"
    PARTIALLY_REVIEWED = "partially_reviewed"
    PENDING = "pending"
    REVIEWED = "reviewed"

    def __str__(self) -> str:
        return str(self.value)
