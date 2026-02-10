from enum import Enum


class AttributeExtractionStatusChoices(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    COMPLETED_NOT_FOUND = "completed_not_found"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"
    PENDING_APPROVAL = "pending_approval"

    def __str__(self) -> str:
        return str(self.value)
