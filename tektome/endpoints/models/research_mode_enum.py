from enum import Enum


class ResearchModeEnum(str, Enum):
    AUTO_CAPTURE = "auto_capture"
    DEEP_RESEARCH = "deep_research"

    def __str__(self) -> str:
        return str(self.value)
