from enum import Enum


class CitationKind(str, Enum):
    CITED_BIM_RESOURCES = "cited_bim_resources"
    CITED_BOOLEAN_ATTRIBUTES = "cited_boolean_attributes"
    CITED_FLOAT_ATTRIBUTES = "cited_float_attributes"
    CITED_IMAGE_RESOURCES = "cited_image_resources"
    CITED_INTEGER_ATTRIBUTES = "cited_integer_attributes"
    CITED_PDF_RESOURCES = "cited_pdf_resources"
    CITED_RAW_TEXT_RESOURCES = "cited_raw_text_resources"
    CITED_STRING_ATTRIBUTES = "cited_string_attributes"

    def __str__(self) -> str:
        return str(self.value)
