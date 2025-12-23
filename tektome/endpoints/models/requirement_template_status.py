from enum import Enum


class RequirementTemplateStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"

    def __str__(self) -> str:
        return str(self.value)
