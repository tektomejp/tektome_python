from enum import Enum


class ArtifactTemplateGroupKind(str, Enum):
    ARTIFACT = "artifact"
    SKILL = "skill"

    def __str__(self) -> str:
        return str(self.value)
