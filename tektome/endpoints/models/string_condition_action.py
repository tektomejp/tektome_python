from enum import Enum


class StringConditionAction(str, Enum):
    EXCLUDES = "excludes"
    INCLUDES = "includes"
    MATCHES = "matches"
    MEANS = "means"

    def __str__(self) -> str:
        return str(self.value)
