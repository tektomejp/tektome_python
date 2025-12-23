from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Section")


@_attrs_define
class Section:
    """
    Attributes:
        id (str):
        index_name (str):
        title (str):
        page (int):
        resource_group_id (str):
        resource_id (str):
        score (float):
        max_score (float):
        chunk_ids (list[str]):
        chunk_indexes (list[int]):
        chunk_scores (list[float]):
        chunk_highlights (list[list[str]]):
        text_highlights (list[str]):
    """

    id: str
    index_name: str
    title: str
    page: int
    resource_group_id: str
    resource_id: str
    score: float
    max_score: float
    chunk_ids: list[str]
    chunk_indexes: list[int]
    chunk_scores: list[float]
    chunk_highlights: list[list[str]]
    text_highlights: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        index_name = self.index_name

        title = self.title

        page = self.page

        resource_group_id = self.resource_group_id

        resource_id = self.resource_id

        score = self.score

        max_score = self.max_score

        chunk_ids = self.chunk_ids

        chunk_indexes = self.chunk_indexes

        chunk_scores = self.chunk_scores

        chunk_highlights = []
        for chunk_highlights_item_data in self.chunk_highlights:
            chunk_highlights_item = chunk_highlights_item_data

            chunk_highlights.append(chunk_highlights_item)

        text_highlights = self.text_highlights

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "index_name": index_name,
                "title": title,
                "page": page,
                "resource_group_id": resource_group_id,
                "resource_id": resource_id,
                "score": score,
                "max_score": max_score,
                "chunk_ids": chunk_ids,
                "chunk_indexes": chunk_indexes,
                "chunk_scores": chunk_scores,
                "chunk_highlights": chunk_highlights,
                "text_highlights": text_highlights,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        index_name = d.pop("index_name")

        title = d.pop("title")

        page = d.pop("page")

        resource_group_id = d.pop("resource_group_id")

        resource_id = d.pop("resource_id")

        score = d.pop("score")

        max_score = d.pop("max_score")

        chunk_ids = cast(list[str], d.pop("chunk_ids"))

        chunk_indexes = cast(list[int], d.pop("chunk_indexes"))

        chunk_scores = cast(list[float], d.pop("chunk_scores"))

        chunk_highlights = []
        _chunk_highlights = d.pop("chunk_highlights")
        for chunk_highlights_item_data in _chunk_highlights:
            chunk_highlights_item = cast(list[str], chunk_highlights_item_data)

            chunk_highlights.append(chunk_highlights_item)

        text_highlights = cast(list[str], d.pop("text_highlights"))

        section = cls(
            id=id,
            index_name=index_name,
            title=title,
            page=page,
            resource_group_id=resource_group_id,
            resource_id=resource_id,
            score=score,
            max_score=max_score,
            chunk_ids=chunk_ids,
            chunk_indexes=chunk_indexes,
            chunk_scores=chunk_scores,
            chunk_highlights=chunk_highlights,
            text_highlights=text_highlights,
        )

        section.additional_properties = d
        return section

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
