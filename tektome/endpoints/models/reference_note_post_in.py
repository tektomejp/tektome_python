from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reference_note_sources import ReferenceNoteSources
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferenceNotePostIn")


@_attrs_define
class ReferenceNotePostIn:
    """Schema for creating a reference note.

    Attributes:
        title (str):
        content (str):
        creation_source (ReferenceNoteSources | Unset):  Default: ReferenceNoteSources.MANUAL.
    """

    title: str
    content: str
    creation_source: ReferenceNoteSources | Unset = ReferenceNoteSources.MANUAL
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        content = self.content

        creation_source: str | Unset = UNSET
        if not isinstance(self.creation_source, Unset):
            creation_source = self.creation_source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "content": content,
            }
        )
        if creation_source is not UNSET:
            field_dict["creation_source"] = creation_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        content = d.pop("content")

        _creation_source = d.pop("creation_source", UNSET)
        creation_source: ReferenceNoteSources | Unset
        if isinstance(_creation_source, Unset):
            creation_source = UNSET
        else:
            creation_source = ReferenceNoteSources(_creation_source)

        reference_note_post_in = cls(
            title=title,
            content=content,
            creation_source=creation_source,
        )

        reference_note_post_in.additional_properties = d
        return reference_note_post_in

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
