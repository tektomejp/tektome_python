from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_embedding_model import AzureEmbeddingModel
from ..models.search_mode import SearchMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchDocumentPostIn")


@_attrs_define
class SearchDocumentPostIn:
    """
    Attributes:
        embedding_model (AzureEmbeddingModel): List of available embedding models which compatible with litellm

            the exahustive list of models can be found at https://models.litellm.ai/
        query_content (str):
        data_space_ids (list[str] | Unset):
        project_ids (list[str] | Unset):
        file_ids (list[str] | Unset):
        query_type (SearchMode | Unset):  Default: SearchMode.VECTOR.
        top_k (int | Unset):  Default: 10.
        skip (int | Unset):  Default: 0.
        sort_by_pages (bool | Unset):  Default: False.
        alpha (float | Unset):  Default: 0.5.
    """

    embedding_model: AzureEmbeddingModel
    query_content: str
    data_space_ids: list[str] | Unset = UNSET
    project_ids: list[str] | Unset = UNSET
    file_ids: list[str] | Unset = UNSET
    query_type: SearchMode | Unset = SearchMode.VECTOR
    top_k: int | Unset = 10
    skip: int | Unset = 0
    sort_by_pages: bool | Unset = False
    alpha: float | Unset = 0.5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embedding_model = self.embedding_model.value

        query_content = self.query_content

        data_space_ids: list[str] | Unset = UNSET
        if not isinstance(self.data_space_ids, Unset):
            data_space_ids = self.data_space_ids

        project_ids: list[str] | Unset = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = self.project_ids

        file_ids: list[str] | Unset = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        query_type: str | Unset = UNSET
        if not isinstance(self.query_type, Unset):
            query_type = self.query_type.value

        top_k = self.top_k

        skip = self.skip

        sort_by_pages = self.sort_by_pages

        alpha = self.alpha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "embedding_model": embedding_model,
                "query_content": query_content,
            }
        )
        if data_space_ids is not UNSET:
            field_dict["data_space_ids"] = data_space_ids
        if project_ids is not UNSET:
            field_dict["project_ids"] = project_ids
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids
        if query_type is not UNSET:
            field_dict["query_type"] = query_type
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if skip is not UNSET:
            field_dict["skip"] = skip
        if sort_by_pages is not UNSET:
            field_dict["sort_by_pages"] = sort_by_pages
        if alpha is not UNSET:
            field_dict["alpha"] = alpha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        embedding_model = AzureEmbeddingModel(d.pop("embedding_model"))

        query_content = d.pop("query_content")

        data_space_ids = cast(list[str], d.pop("data_space_ids", UNSET))

        project_ids = cast(list[str], d.pop("project_ids", UNSET))

        file_ids = cast(list[str], d.pop("file_ids", UNSET))

        _query_type = d.pop("query_type", UNSET)
        query_type: SearchMode | Unset
        if isinstance(_query_type, Unset):
            query_type = UNSET
        else:
            query_type = SearchMode(_query_type)

        top_k = d.pop("top_k", UNSET)

        skip = d.pop("skip", UNSET)

        sort_by_pages = d.pop("sort_by_pages", UNSET)

        alpha = d.pop("alpha", UNSET)

        search_document_post_in = cls(
            embedding_model=embedding_model,
            query_content=query_content,
            data_space_ids=data_space_ids,
            project_ids=project_ids,
            file_ids=file_ids,
            query_type=query_type,
            top_k=top_k,
            skip=skip,
            sort_by_pages=sort_by_pages,
            alpha=alpha,
        )

        search_document_post_in.additional_properties = d
        return search_document_post_in

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
