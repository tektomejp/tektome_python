from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_search_type import DocumentSearchType
from ..models.embedding_model_enum import EmbeddingModelEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentSearch")


@_attrs_define
class DocumentSearch:
    """
    Attributes:
        embedding_model (EmbeddingModelEnum):
        project_ids (list[str]):
        content (str):
        file_ids (list[str] | Unset):
        data_space_ids (list[str] | Unset):
        top_k (int | Unset):  Default: 10.
        skip (int | Unset):  Default: 0.
        sort_by_pages (bool | Unset):  Default: False.
        alpha (float | Unset):  Default: 0.5.
        type_ (DocumentSearchType | Unset):  Default: DocumentSearchType.VECTOR.
    """

    embedding_model: EmbeddingModelEnum
    project_ids: list[str]
    content: str
    file_ids: list[str] | Unset = UNSET
    data_space_ids: list[str] | Unset = UNSET
    top_k: int | Unset = 10
    skip: int | Unset = 0
    sort_by_pages: bool | Unset = False
    alpha: float | Unset = 0.5
    type_: DocumentSearchType | Unset = DocumentSearchType.VECTOR
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embedding_model = self.embedding_model.value

        project_ids = self.project_ids

        content = self.content

        file_ids: list[str] | Unset = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        data_space_ids: list[str] | Unset = UNSET
        if not isinstance(self.data_space_ids, Unset):
            data_space_ids = self.data_space_ids

        top_k = self.top_k

        skip = self.skip

        sort_by_pages = self.sort_by_pages

        alpha = self.alpha

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "embedding_model": embedding_model,
                "project_ids": project_ids,
                "content": content,
            }
        )
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids
        if data_space_ids is not UNSET:
            field_dict["data_space_ids"] = data_space_ids
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if skip is not UNSET:
            field_dict["skip"] = skip
        if sort_by_pages is not UNSET:
            field_dict["sort_by_pages"] = sort_by_pages
        if alpha is not UNSET:
            field_dict["alpha"] = alpha
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        embedding_model = EmbeddingModelEnum(d.pop("embedding_model"))

        project_ids = cast(list[str], d.pop("project_ids"))

        content = d.pop("content")

        file_ids = cast(list[str], d.pop("file_ids", UNSET))

        data_space_ids = cast(list[str], d.pop("data_space_ids", UNSET))

        top_k = d.pop("top_k", UNSET)

        skip = d.pop("skip", UNSET)

        sort_by_pages = d.pop("sort_by_pages", UNSET)

        alpha = d.pop("alpha", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: DocumentSearchType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DocumentSearchType(_type_)

        document_search = cls(
            embedding_model=embedding_model,
            project_ids=project_ids,
            content=content,
            file_ids=file_ids,
            data_space_ids=data_space_ids,
            top_k=top_k,
            skip=skip,
            sort_by_pages=sort_by_pages,
            alpha=alpha,
            type_=type_,
        )

        document_search.additional_properties = d
        return document_search

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
