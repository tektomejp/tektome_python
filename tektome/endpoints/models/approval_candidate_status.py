from enum import Enum


class ApprovalCandidateStatus(str, Enum):
    DISCARDED = "Discarded"
    SELECTED = "Selected"
    UNSELECTED = "Unselected"

    def __str__(self) -> str:
        return str(self.value)
