from enum import Enum


class BulkReviewPostInAction(str, Enum):
    APPROVED = "approved"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
