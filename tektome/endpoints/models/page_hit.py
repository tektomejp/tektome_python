from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_hit import ChunkHit


T = TypeVar("T", bound="PageHit")


@_attrs_define
class PageHit:
    """A single page hit within a resource.

    Attributes:
        page_id (UUID):
        page_number (int):
        chunks (list[ChunkHit] | Unset):
    """

    page_id: UUID
    page_number: int
    chunks: list[ChunkHit] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_id = str(self.page_id)

        page_number = self.page_number

        chunks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.chunks, Unset):
            chunks = []
            for chunks_item_data in self.chunks:
                chunks_item = chunks_item_data.to_dict()
                chunks.append(chunks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page_id": page_id,
                "page_number": page_number,
            }
        )
        if chunks is not UNSET:
            field_dict["chunks"] = chunks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chunk_hit import ChunkHit

        d = dict(src_dict)
        page_id = UUID(d.pop("page_id"))

        page_number = d.pop("page_number")

        _chunks = d.pop("chunks", UNSET)
        chunks: list[ChunkHit] | Unset = UNSET
        if _chunks is not UNSET:
            chunks = []
            for chunks_item_data in _chunks:
                chunks_item = ChunkHit.from_dict(chunks_item_data)

                chunks.append(chunks_item)

        page_hit = cls(
            page_id=page_id,
            page_number=page_number,
            chunks=chunks,
        )

        page_hit.additional_properties = d
        return page_hit

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
