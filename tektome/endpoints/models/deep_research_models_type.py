from enum import Enum


class DeepResearchModelsType(str, Enum):
    GEMINI_3_PRO_PREVIEW = "gemini-3-pro-preview"
    O3_DEEP_RESEARCH = "o3-deep-research"
    O4_MINI_DEEP_RESEARCH = "o4-mini-deep-research"

    def __str__(self) -> str:
        return str(self.value)
