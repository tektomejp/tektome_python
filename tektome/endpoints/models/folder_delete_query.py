from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FolderDeleteQuery")


@_attrs_define
class FolderDeleteQuery:
    """
    Attributes:
        include_resources (bool | Unset):  Default: False.
        force (bool | Unset):  Default: False.
    """

    include_resources: bool | Unset = False
    force: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_resources = self.include_resources

        force = self.force

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_resources is not UNSET:
            field_dict["include_resources"] = include_resources
        if force is not UNSET:
            field_dict["force"] = force

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_resources = d.pop("include_resources", UNSET)

        force = d.pop("force", UNSET)

        folder_delete_query = cls(
            include_resources=include_resources,
            force=force,
        )

        folder_delete_query.additional_properties = d
        return folder_delete_query

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
