from enum import Enum


class Operators(str, Enum):
    VALUE_0 = ">"
    VALUE_1 = ">="
    VALUE_2 = "<"
    VALUE_3 = "<="
    VALUE_4 = "=="

    def __str__(self) -> str:
        return str(self.value)
