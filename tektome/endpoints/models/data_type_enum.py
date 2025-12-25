from enum import Enum


class DataTypeEnum(str, Enum):
    TEXT_BASED_DATA = "text_based_data"

    def __str__(self) -> str:
        return str(self.value)
