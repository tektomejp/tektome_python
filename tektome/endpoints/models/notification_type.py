from enum import Enum


class NotificationType(str, Enum):
    AGGREGATE_APPROVAL_AVAILABLE = "aggregate_approval_available"
    AGGREGATE_APPROVAL_REQUIRED = "aggregate_approval_required"
    APPROVAL_AVAILABLE = "approval_available"
    APPROVAL_REQUIRED = "approval_required"
    EXECUTION_CANCELLED = "execution_cancelled"
    EXECUTION_GROUP_CANCELLED = "execution_group_cancelled"
    EXECUTION_GROUP_COMPLETED = "execution_group_completed"
    EXECUTION_GROUP_COMPLETED_REVIEW_PENDING = "execution_group_completed_review_pending"
    EXECUTION_GROUP_FAILED = "execution_group_failed"
    EXECUTION_GROUP_STARTED = "execution_group_started"
    FILE_UPLOAD_STARTED = "file_upload_started"
    FILE_UPLOAD_WILL_START = "file_upload_will_start"
    IMPORT_COMPLETED = "import_completed"
    IMPORT_FAILED = "import_failed"

    def __str__(self) -> str:
        return str(self.value)
