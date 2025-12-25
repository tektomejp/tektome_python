from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reference_notes_query_sort import ReferenceNotesQuerySort
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferenceNotesQuery")


@_attrs_define
class ReferenceNotesQuery:
    """
    Attributes:
        sort (ReferenceNotesQuerySort | Unset):  Default: ReferenceNotesQuerySort.ASC.
    """

    sort: ReferenceNotesQuerySort | Unset = ReferenceNotesQuerySort.ASC
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sort: str | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _sort = d.pop("sort", UNSET)
        sort: ReferenceNotesQuerySort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = ReferenceNotesQuerySort(_sort)

        reference_notes_query = cls(
            sort=sort,
        )

        reference_notes_query.additional_properties = d
        return reference_notes_query

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
