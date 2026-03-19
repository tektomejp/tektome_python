from enum import Enum


class DateTimeConditionAction(str, Enum):
    AFTER = "after"
    BEFORE = "before"
    EQUALS = "equals"
    NOT_EQUALS = "not_equals"
    ON_OR_AFTER = "on_or_after"
    ON_OR_BEFORE = "on_or_before"

    def __str__(self) -> str:
        return str(self.value)
