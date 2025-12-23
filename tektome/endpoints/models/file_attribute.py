from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_attribute_type_enum import FileAttributeTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileAttribute")


@_attrs_define
class FileAttribute:
    """
    Attributes:
        name (str):
        prompt (str):
        id (UUID | Unset):
        type_ (FileAttributeTypeEnum | Unset):  Default: FileAttributeTypeEnum.STRING.
    """

    name: str
    prompt: str
    id: UUID | Unset = UNSET
    type_: FileAttributeTypeEnum | Unset = FileAttributeTypeEnum.STRING
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        prompt = self.prompt

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "prompt": prompt,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        prompt = d.pop("prompt")

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _type_ = d.pop("type", UNSET)
        type_: FileAttributeTypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FileAttributeTypeEnum(_type_)

        file_attribute = cls(
            name=name,
            prompt=prompt,
            id=id,
            type_=type_,
        )

        file_attribute.additional_properties = d
        return file_attribute

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
