from enum import Enum


class AttributeDataSnapshotState(str, Enum):
    INITIAL = "initial"
    REVIEWED = "reviewed"

    def __str__(self) -> str:
        return str(self.value)
