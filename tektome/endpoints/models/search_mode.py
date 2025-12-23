from enum import Enum


class SearchMode(str, Enum):
    BLEND = "blend"
    EXACT = "exact"
    HYBRID = "hybrid"
    SIMPLE = "simple"
    VECTOR = "vector"

    def __str__(self) -> str:
        return str(self.value)
