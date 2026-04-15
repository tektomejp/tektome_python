from enum import Enum


class ModelTier(str, Enum):
    FAST = "fast"
    SMART = "smart"
    SMARTEST = "smartest"

    def __str__(self) -> str:
        return str(self.value)
