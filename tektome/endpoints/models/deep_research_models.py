from enum import Enum


class DeepResearchModels(str, Enum):
    GEMINI_3_PRO_PREVIEW = "gemini-3-pro-preview"
    O_3_DEEP_RESEARCH = "o3-deep-research"
    O_4_MINI_DEEP_RESEARCH = "o4-mini-deep-research"

    def __str__(self) -> str:
        return str(self.value)
