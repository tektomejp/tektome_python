from enum import Enum


class ApprovalStatus(str, Enum):
    APPROVED = "Approved"
    AUTO_APPROVED = "Auto Approved"
    PENDING = "Pending"
    REJECTED = "Rejected"

    def __str__(self) -> str:
        return str(self.value)
