from enum import Enum


class BooleanConditionAction(str, Enum):
    EQUALS = "equals"
    NOT_EQUALS = "not_equals"

    def __str__(self) -> str:
        return str(self.value)
