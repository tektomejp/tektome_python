from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SectionParagraphPath")


@_attrs_define
class SectionParagraphPath:
    """Represents a path to paragraphs in a section.
    Example: { <page_id: 1>: [0,1,2] }
    Refers to the first three paragraphs in the page id 1.

        Attributes:
            page_id (UUID):
            paragraph_indices (list[int] | Unset): List of paragraph indices in the page
    """

    page_id: UUID
    paragraph_indices: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_id = str(self.page_id)

        paragraph_indices: list[int] | Unset = UNSET
        if not isinstance(self.paragraph_indices, Unset):
            paragraph_indices = self.paragraph_indices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page_id": page_id,
            }
        )
        if paragraph_indices is not UNSET:
            field_dict["paragraph_indices"] = paragraph_indices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_id = UUID(d.pop("page_id"))

        paragraph_indices = cast(list[int], d.pop("paragraph_indices", UNSET))

        section_paragraph_path = cls(
            page_id=page_id,
            paragraph_indices=paragraph_indices,
        )

        section_paragraph_path.additional_properties = d
        return section_paragraph_path

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
