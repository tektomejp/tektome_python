from enum import Enum


class SectionTablePathMode(str, Enum):
    CELL = "cell"
    COLUMN = "column"
    ROW = "row"

    def __str__(self) -> str:
        return str(self.value)
