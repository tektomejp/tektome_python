from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LawtalkRequirementRequiredSchema")


@_attrs_define
class LawtalkRequirementRequiredSchema:
    """
    Attributes:
        name (str | Unset):  Default: ''.
        summary (str | Unset):  Default: ''.
        question (str | Unset):  Default: ''.
        keywords (str | Unset):  Default: ''.
    """

    name: str | Unset = ""
    summary: str | Unset = ""
    question: str | Unset = ""
    keywords: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        summary = self.summary

        question = self.question

        keywords = self.keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if summary is not UNSET:
            field_dict["summary"] = summary
        if question is not UNSET:
            field_dict["question"] = question
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        summary = d.pop("summary", UNSET)

        question = d.pop("question", UNSET)

        keywords = d.pop("keywords", UNSET)

        lawtalk_requirement_required_schema = cls(
            name=name,
            summary=summary,
            question=question,
            keywords=keywords,
        )

        lawtalk_requirement_required_schema.additional_properties = d
        return lawtalk_requirement_required_schema

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
