from enum import Enum


class TableConditionAction(str, Enum):
    CELL_MATCHES = "cell_matches"
    COLUMN_CONTAINS = "column_contains"

    def __str__(self) -> str:
        return str(self.value)
