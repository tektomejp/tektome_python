from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChunkHit")


@_attrs_define
class ChunkHit:
    """A single OCR chunk hit within a page.

    Attributes:
        chunk_id (UUID):
        text (str):
        highlight (str):
        score (float):
    """

    chunk_id: UUID
    text: str
    highlight: str
    score: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chunk_id = str(self.chunk_id)

        text = self.text

        highlight = self.highlight

        score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunk_id": chunk_id,
                "text": text,
                "highlight": highlight,
                "score": score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chunk_id = UUID(d.pop("chunk_id"))

        text = d.pop("text")

        highlight = d.pop("highlight")

        score = d.pop("score")

        chunk_hit = cls(
            chunk_id=chunk_id,
            text=text,
            highlight=highlight,
            score=score,
        )

        chunk_hit.additional_properties = d
        return chunk_hit

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
