from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TektomeResponseEntry")


@_attrs_define
class TektomeResponseEntry:
    """
    Attributes:
        data_space_id (str):
        project_id (str):
        file_id (str):
        file_name (str):
        chunk_id (list[str]):
        page_number (list[int]):
        score (list[float]):
        max_score (float):
    """

    data_space_id: str
    project_id: str
    file_id: str
    file_name: str
    chunk_id: list[str]
    page_number: list[int]
    score: list[float]
    max_score: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_space_id = self.data_space_id

        project_id = self.project_id

        file_id = self.file_id

        file_name = self.file_name

        chunk_id = self.chunk_id

        page_number = self.page_number

        score = self.score

        max_score = self.max_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_space_id": data_space_id,
                "project_id": project_id,
                "file_id": file_id,
                "file_name": file_name,
                "chunk_id": chunk_id,
                "page_number": page_number,
                "score": score,
                "max_score": max_score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_space_id = d.pop("data_space_id")

        project_id = d.pop("project_id")

        file_id = d.pop("file_id")

        file_name = d.pop("file_name")

        chunk_id = cast(list[str], d.pop("chunk_id"))

        page_number = cast(list[int], d.pop("page_number"))

        score = cast(list[float], d.pop("score"))

        max_score = d.pop("max_score")

        tektome_response_entry = cls(
            data_space_id=data_space_id,
            project_id=project_id,
            file_id=file_id,
            file_name=file_name,
            chunk_id=chunk_id,
            page_number=page_number,
            score=score,
            max_score=max_score,
        )

        tektome_response_entry.additional_properties = d
        return tektome_response_entry

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
