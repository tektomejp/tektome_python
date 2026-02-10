from enum import Enum


class CandidateItemKind(str, Enum):
    BOOLEAN_ATTRIBUTES = "boolean_attributes"
    FILE_UPLOAD = "file_upload"
    FLOAT_ATTRIBUTES = "float_attributes"
    INTEGER_ATTRIBUTES = "integer_attributes"
    STRING_ATTRIBUTES = "string_attributes"

    def __str__(self) -> str:
        return str(self.value)
