from enum import Enum


class RECIPESCHOICES(str, Enum):
    AUTO_CAPTURE_V0 = "auto-capture-v0"
    AUTO_CAPTURE_V1 = "auto-capture-v1"
    DEEP_RESEARCH_V0 = "deep-research-v0"
    DEEP_RESEARCH_V1 = "deep-research-v1"
    TEKTOME_OS_V1 = "tektome-os-v1"
    V1 = "v1"

    def __str__(self) -> str:
        return str(self.value)
