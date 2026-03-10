from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TextHighlights")


@_attrs_define
class TextHighlights:
    """
    Attributes:
        text_part_uuid (str):
            UUID of the text part to be highlighted in a PDF document or Raw Text resource.
            This could be a text chunk, table, page, or even the entire document.
            The highlights will only applied to the specified text part, so try to be reasonable in choosing the specificity
            if the text part level.
        highlights (list[str]): List of text highlights on the page; can be keywords or quotations
    """

    text_part_uuid: str
    highlights: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text_part_uuid = self.text_part_uuid

        highlights = self.highlights

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text_part_uuid": text_part_uuid,
                "highlights": highlights,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text_part_uuid = d.pop("text_part_uuid")

        highlights = cast(list[str], d.pop("highlights"))

        text_highlights = cls(
            text_part_uuid=text_part_uuid,
            highlights=highlights,
        )

        text_highlights.additional_properties = d
        return text_highlights

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
