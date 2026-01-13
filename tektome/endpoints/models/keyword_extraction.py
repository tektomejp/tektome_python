from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_extraction_return_mode import KeywordExtractionReturnMode
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
        return_mode (str): The mode to determine the form of keywords to return.
            - SURFACE: Return surface forms of keywords.
            - ROOT: Return root/lemma forms of keywords (or surface in case of measurements).
            - INFLECTIONS: Return all inflected forms of keywords (just surface in case of measurements).

        Attributes:
            text (str):
            return_mode (KeywordExtractionReturnMode | Unset):  Default: KeywordExtractionReturnMode.SURFACE.
    """

    text: str
    return_mode: KeywordExtractionReturnMode | Unset = KeywordExtractionReturnMode.SURFACE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        return_mode: str | Unset = UNSET
        if not isinstance(self.return_mode, Unset):
            return_mode = self.return_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if return_mode is not UNSET:
            field_dict["return_mode"] = return_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        _return_mode = d.pop("return_mode", UNSET)
        return_mode: KeywordExtractionReturnMode | Unset
        if isinstance(_return_mode, Unset):
            return_mode = UNSET
        else:
            return_mode = KeywordExtractionReturnMode(_return_mode)

        keyword_extraction = cls(
            text=text,
            return_mode=return_mode,
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
