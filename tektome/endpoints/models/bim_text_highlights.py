from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BIMTextHighlights")


@_attrs_define
class BIMTextHighlights:
    """
    Attributes:
        bim_object_uuid (str): UUID of the BIM object to be highlighted (not the BIM project)
        highlights (list[str]): List of text highlights on the JSON-representation of the BIM object; can be keywords or
            quotations
    """

    bim_object_uuid: str
    highlights: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bim_object_uuid = self.bim_object_uuid

        highlights = self.highlights

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bim_object_uuid": bim_object_uuid,
                "highlights": highlights,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bim_object_uuid = d.pop("bim_object_uuid")

        highlights = cast(list[str], d.pop("highlights"))

        bim_text_highlights = cls(
            bim_object_uuid=bim_object_uuid,
            highlights=highlights,
        )

        bim_text_highlights.additional_properties = d
        return bim_text_highlights

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
