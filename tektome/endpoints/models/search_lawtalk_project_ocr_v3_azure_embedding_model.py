from enum import Enum


class SearchLawtalkProjectOcrV3AzureEmbeddingModel(str, Enum):
    AZURETEXT_EMBEDDING_3_LARGE = "azure/text-embedding-3-large"
    AZURETEXT_EMBEDDING_3_SMALL = "azure/text-embedding-3-small"
    AZURETEXT_EMBEDDING_ADA_002 = "azure/text-embedding-ada-002"

    def __str__(self) -> str:
        return str(self.value)
