from enum import Enum


class ModelHint(str, Enum):
    OPUS = "pro"
    SONNET = "fast"

    def __str__(self) -> str:
        return str(self.value)
