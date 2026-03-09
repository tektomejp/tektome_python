from enum import Enum


class StringConditionAction(str, Enum):
    CONTAINS = "contains"
    EXACT = "exact"
    EXCLUDES = "excludes"
    INCLUDES = "includes"
    MATCHES = "matches"
    MEANS = "means"
    NOT_CONTAINS = "not_contains"

    def __str__(self) -> str:
        return str(self.value)
