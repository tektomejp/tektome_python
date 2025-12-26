from enum import Enum


class EmbeddingModelEnum(str, Enum):
    AZURE_OPENAI_TEXT_EMBEDDING_3_LARGE = "azure-openai-text-embedding-3-large"
    AZURE_OPENAI_TEXT_EMBEDDING_3_SMALL = "azure-openai-text-embedding-3-small"
    AZURE_OPENAI_TEXT_EMBEDDING_ADA_002 = "azure-openai-text-embedding-ada-002"

    def __str__(self) -> str:
        return str(self.value)
