from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_attribute_type_enum import FileAttributeTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="TableColumn")


@_attrs_define
class TableColumn:
    """
    Attributes:
        name (str):
        prompt (str | Unset):  Default: ''.
        type_ (FileAttributeTypeEnum | Unset):  Default: FileAttributeTypeEnum.STRING.
        primary_key (bool | Unset):  Default: False.
    """

    name: str
    prompt: str | Unset = ""
    type_: FileAttributeTypeEnum | Unset = FileAttributeTypeEnum.STRING
    primary_key: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        prompt = self.prompt

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        primary_key = self.primary_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if type_ is not UNSET:
            field_dict["type"] = type_
        if primary_key is not UNSET:
            field_dict["primary_key"] = primary_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        prompt = d.pop("prompt", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: FileAttributeTypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FileAttributeTypeEnum(_type_)

        primary_key = d.pop("primary_key", UNSET)

        table_column = cls(
            name=name,
            prompt=prompt,
            type_=type_,
            primary_key=primary_key,
        )

        table_column.additional_properties = d
        return table_column

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
