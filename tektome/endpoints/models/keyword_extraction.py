from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordExtraction")


@_attrs_define
class KeywordExtraction:
    """Schema for keyword extraction requests.

    This schema defines the structure for keyword extraction operations,
    allowing users to specify the text to analyze and whether to include
    word inflections in the extraction process.

    Attributes:
        text (str): The input text from which keywords will be extracted.
        include_inflections (bool): Flag indicating whether to include word
            inflections (different forms of the same word) in the keyword
            extraction results. Defaults to False.

        Attributes:
            text (str):
            include_inflections (bool | Unset):  Default: False.
    """

    text: str
    include_inflections: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        include_inflections = self.include_inflections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if include_inflections is not UNSET:
            field_dict["include_inflections"] = include_inflections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        include_inflections = d.pop("include_inflections", UNSET)

        keyword_extraction = cls(
            text=text,
            include_inflections=include_inflections,
        )

        keyword_extraction.additional_properties = d
        return keyword_extraction

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
