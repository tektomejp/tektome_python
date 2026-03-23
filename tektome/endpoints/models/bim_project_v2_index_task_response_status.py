from enum import Enum


class BimProjectV2IndexTaskResponseStatus(str, Enum):
    ALREADY_RUNNING = "already_running"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
