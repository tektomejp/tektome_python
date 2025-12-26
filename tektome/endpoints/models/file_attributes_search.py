from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.embedding_model_enum import EmbeddingModelEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileAttributesSearch")


@_attrs_define
class FileAttributesSearch:
    """
    Attributes:
        project_ids (list[str]):
        data_space_id (str):
        attribute_id (str):
        content (str):
        embedding_model (EmbeddingModelEnum):
        file_ids (list[str] | Unset):
        top_k (int | Unset):  Default: 10.
    """

    project_ids: list[str]
    data_space_id: str
    attribute_id: str
    content: str
    embedding_model: EmbeddingModelEnum
    file_ids: list[str] | Unset = UNSET
    top_k: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_ids = self.project_ids

        data_space_id = self.data_space_id

        attribute_id = self.attribute_id

        content = self.content

        embedding_model = self.embedding_model.value

        file_ids: list[str] | Unset = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        top_k = self.top_k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_ids": project_ids,
                "data_space_id": data_space_id,
                "attribute_id": attribute_id,
                "content": content,
                "embedding_model": embedding_model,
            }
        )
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids
        if top_k is not UNSET:
            field_dict["top_k"] = top_k

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_ids = cast(list[str], d.pop("project_ids"))

        data_space_id = d.pop("data_space_id")

        attribute_id = d.pop("attribute_id")

        content = d.pop("content")

        embedding_model = EmbeddingModelEnum(d.pop("embedding_model"))

        file_ids = cast(list[str], d.pop("file_ids", UNSET))

        top_k = d.pop("top_k", UNSET)

        file_attributes_search = cls(
            project_ids=project_ids,
            data_space_id=data_space_id,
            attribute_id=attribute_id,
            content=content,
            embedding_model=embedding_model,
            file_ids=file_ids,
            top_k=top_k,
        )

        file_attributes_search.additional_properties = d
        return file_attributes_search

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
