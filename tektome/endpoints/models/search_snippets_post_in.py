from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_embedding_model import AzureEmbeddingModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchSnippetsPostIn")


@_attrs_define
class SearchSnippetsPostIn:
    """
    Attributes:
        embedding_model (AzureEmbeddingModel): List of available embedding models which compatible with litellm

            the exahustive list of models can be found at https://models.litellm.ai/
        query (None | str | Unset):
        keyword (None | str | Unset):
        top_k (int | Unset):  Default: 10.
        sort_by_pages (bool | Unset):  Default: False.
        vector_project (None | str | Unset):
        vector_data_space (None | str | Unset):
    """

    embedding_model: AzureEmbeddingModel
    query: None | str | Unset = UNSET
    keyword: None | str | Unset = UNSET
    top_k: int | Unset = 10
    sort_by_pages: bool | Unset = False
    vector_project: None | str | Unset = UNSET
    vector_data_space: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embedding_model = self.embedding_model.value

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        keyword: None | str | Unset
        if isinstance(self.keyword, Unset):
            keyword = UNSET
        else:
            keyword = self.keyword

        top_k = self.top_k

        sort_by_pages = self.sort_by_pages

        vector_project: None | str | Unset
        if isinstance(self.vector_project, Unset):
            vector_project = UNSET
        else:
            vector_project = self.vector_project

        vector_data_space: None | str | Unset
        if isinstance(self.vector_data_space, Unset):
            vector_data_space = UNSET
        else:
            vector_data_space = self.vector_data_space

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "embedding_model": embedding_model,
            }
        )
        if query is not UNSET:
            field_dict["query"] = query
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if sort_by_pages is not UNSET:
            field_dict["sort_by_pages"] = sort_by_pages
        if vector_project is not UNSET:
            field_dict["vector_project"] = vector_project
        if vector_data_space is not UNSET:
            field_dict["vector_data_space"] = vector_data_space

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        embedding_model = AzureEmbeddingModel(d.pop("embedding_model"))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_keyword(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keyword = _parse_keyword(d.pop("keyword", UNSET))

        top_k = d.pop("top_k", UNSET)

        sort_by_pages = d.pop("sort_by_pages", UNSET)

        def _parse_vector_project(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vector_project = _parse_vector_project(d.pop("vector_project", UNSET))

        def _parse_vector_data_space(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vector_data_space = _parse_vector_data_space(d.pop("vector_data_space", UNSET))

        search_snippets_post_in = cls(
            embedding_model=embedding_model,
            query=query,
            keyword=keyword,
            top_k=top_k,
            sort_by_pages=sort_by_pages,
            vector_project=vector_project,
            vector_data_space=vector_data_space,
        )

        search_snippets_post_in.additional_properties = d
        return search_snippets_post_in

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
