from enum import Enum


class FileDataSnapshotState(str, Enum):
    INITIAL = "initial"
    REVIEWED = "reviewed"

    def __str__(self) -> str:
        return str(self.value)
