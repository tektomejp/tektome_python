from enum import Enum


class SimulateTaskResultStatus(str, Enum):
    FAILURE = "FAILURE"
    PENDING = "PENDING"
    RETRY = "RETRY"
    STARTED = "STARTED"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
