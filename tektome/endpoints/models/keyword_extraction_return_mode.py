from enum import Enum


class KeywordExtractionReturnMode(str, Enum):
    INFLECTIONS = "INFLECTIONS"
    ROOT = "ROOT"
    SURFACE = "SURFACE"

    def __str__(self) -> str:
        return str(self.value)
