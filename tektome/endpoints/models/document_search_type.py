from enum import Enum


class DocumentSearchType(str, Enum):
    BLEND = "blend"
    EXACT = "exact"
    HYBRID = "hybrid"
    VECTOR = "vector"

    def __str__(self) -> str:
        return str(self.value)
