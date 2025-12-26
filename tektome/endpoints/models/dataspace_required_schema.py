from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataspaceRequiredSchema")


@_attrs_define
class DataspaceRequiredSchema:
    """
    Attributes:
        name (str | Unset):  Default: ''.
        primary_entity (str | Unset):  Default: ''.
    """

    name: str | Unset = ""
    primary_entity: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        primary_entity = self.primary_entity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if primary_entity is not UNSET:
            field_dict["primary_entity"] = primary_entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        primary_entity = d.pop("primary_entity", UNSET)

        dataspace_required_schema = cls(
            name=name,
            primary_entity=primary_entity,
        )

        dataspace_required_schema.additional_properties = d
        return dataspace_required_schema

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
