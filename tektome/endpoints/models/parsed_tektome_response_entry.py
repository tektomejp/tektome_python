from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.parsed_tektome_response_entry_resource_text_highlights import (
        ParsedTektomeResponseEntryResourceTextHighlights,
    )
    from ..models.resource_group import ResourceGroup
    from ..models.section import Section


T = TypeVar("T", bound="ParsedTektomeResponseEntry")


@_attrs_define
class ParsedTektomeResponseEntry:
    """
    Attributes:
        resource_group (ResourceGroup):
        sections (list[Section]):
        resource_text_highlights (ParsedTektomeResponseEntryResourceTextHighlights):
    """

    resource_group: ResourceGroup
    sections: list[Section]
    resource_text_highlights: ParsedTektomeResponseEntryResourceTextHighlights
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_group = self.resource_group.to_dict()

        sections = []
        for sections_item_data in self.sections:
            sections_item = sections_item_data.to_dict()
            sections.append(sections_item)

        resource_text_highlights = self.resource_text_highlights.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_group": resource_group,
                "sections": sections,
                "resource_text_highlights": resource_text_highlights,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parsed_tektome_response_entry_resource_text_highlights import (
            ParsedTektomeResponseEntryResourceTextHighlights,
        )
        from ..models.resource_group import ResourceGroup
        from ..models.section import Section

        d = dict(src_dict)
        resource_group = ResourceGroup.from_dict(d.pop("resource_group"))

        sections = []
        _sections = d.pop("sections")
        for sections_item_data in _sections:
            sections_item = Section.from_dict(sections_item_data)

            sections.append(sections_item)

        resource_text_highlights = ParsedTektomeResponseEntryResourceTextHighlights.from_dict(
            d.pop("resource_text_highlights")
        )

        parsed_tektome_response_entry = cls(
            resource_group=resource_group,
            sections=sections,
            resource_text_highlights=resource_text_highlights,
        )

        parsed_tektome_response_entry.additional_properties = d
        return parsed_tektome_response_entry

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
