from enum import Enum


class ResourceGlobOutInitializationStatusType0(str, Enum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    QUERYING = "QUERYING"
    TIMEOUT = "TIMEOUT"

    def __str__(self) -> str:
        return str(self.value)
