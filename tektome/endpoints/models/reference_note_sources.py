from enum import Enum


class ReferenceNoteSources(str, Enum):
    DEEP_RESEARCH = "deep_research"
    MANUAL = "manual"
    TEMPLATE = "template"

    def __str__(self) -> str:
        return str(self.value)
