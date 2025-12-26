from enum import Enum


class DocumentExtractionStatus(str, Enum):
    DONE = "done"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"

    def __str__(self) -> str:
        return str(self.value)
