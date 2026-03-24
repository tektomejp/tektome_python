from enum import Enum


class DuplicateStrategy(str, Enum):
    FORBID = "forbid"
    OVERWRITE = "overwrite"
    SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
