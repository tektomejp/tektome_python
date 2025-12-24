from enum import Enum


class DocumentExtractorEnum(str, Enum):
    AZURE_FORM_RECOGNIZER = "azure_form_recognizer"

    def __str__(self) -> str:
        return str(self.value)
