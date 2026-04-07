from enum import Enum


class AzureEmbeddingModel(str, Enum):
    AZURE_TEXT_EMBEDDING_3_LARGE = "azure/text-embedding-3-large"
    AZURE_TEXT_EMBEDDING_3_SMALL = "azure/text-embedding-3-small"
    AZURE_TEXT_EMBEDDING_ADA_002 = "azure/text-embedding-ada-002"

    def __str__(self) -> str:
        return str(self.value)
