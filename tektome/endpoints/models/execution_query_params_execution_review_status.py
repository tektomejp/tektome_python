from enum import Enum


class ExecutionQueryParamsExecutionReviewStatus(str, Enum):
    NOT_REQUIRED = "not_required"
    PARTIALLY_REVIEWED = "partially_reviewed"
    PENDING = "pending"
    REVIEWED = "reviewed"

    def __str__(self) -> str:
        return str(self.value)
