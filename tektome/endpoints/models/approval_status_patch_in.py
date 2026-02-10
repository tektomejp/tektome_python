from enum import Enum


class ApprovalStatusPatchIn(str, Enum):
    APPROVED = "Approved"
    REJECTED = "Rejected"

    def __str__(self) -> str:
        return str(self.value)
