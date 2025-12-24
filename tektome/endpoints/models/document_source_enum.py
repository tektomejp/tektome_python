from enum import Enum


class DocumentSourceEnum(str, Enum):
    TEKTOME = "tektome"

    def __str__(self) -> str:
        return str(self.value)
