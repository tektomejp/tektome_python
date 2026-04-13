from enum import Enum


class RECIPESCHOICES(str, Enum):
    CONCERT_V1 = "concert-v1"
    MAGI_V1 = "magi-v1"
    TABLE_V1 = "table_v1"
    V1 = "v1"

    def __str__(self) -> str:
        return str(self.value)
