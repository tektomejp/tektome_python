from enum import Enum


class ExecutionApprovalsQueryParamsApprovalStatus(str, Enum):
    APPROVED = "approved"
    AUTO_APPROVED = "auto_approved"
    DISABLED = "disabled"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
