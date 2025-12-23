from enum import Enum


class NumericConditionAction(str, Enum):
    EQUALS = "equals"
    GREATER_THAN = "greater_than"
    GREATER_THAN_OR_EQUAL_TO = "greater_than_or_equal_to"
    LESS_THAN = "less_than"
    LESS_THAN_OR_EQUAL_TO = "less_than_or_equal_to"
    NOT_EQUALS = "not_equals"

    def __str__(self) -> str:
        return str(self.value)
