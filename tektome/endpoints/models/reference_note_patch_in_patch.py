from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reference_note_sources import ReferenceNoteSources
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferenceNotePatchInPatch")


@_attrs_define
class ReferenceNotePatchInPatch:
    """
    Attributes:
        title (None | str | Unset):
        creation_source (None | ReferenceNoteSources | Unset):
    """

    title: None | str | Unset = UNSET
    creation_source: None | ReferenceNoteSources | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        creation_source: None | str | Unset
        if isinstance(self.creation_source, Unset):
            creation_source = UNSET
        elif isinstance(self.creation_source, ReferenceNoteSources):
            creation_source = self.creation_source.value
        else:
            creation_source = self.creation_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if creation_source is not UNSET:
            field_dict["creation_source"] = creation_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_creation_source(data: object) -> None | ReferenceNoteSources | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_source_type_0 = ReferenceNoteSources(data)

                return creation_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReferenceNoteSources | Unset, data)

        creation_source = _parse_creation_source(d.pop("creation_source", UNSET))

        reference_note_patch_in_patch = cls(
            title=title,
            creation_source=creation_source,
        )

        reference_note_patch_in_patch.additional_properties = d
        return reference_note_patch_in_patch

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
