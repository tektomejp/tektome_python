from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ArtifactPostIn")


@_attrs_define
class ArtifactPostIn:
    """
    Attributes:
        name (str):
        extension (str):
        description (str):
        content (str):
    """

    name: str
    extension: str
    description: str
    content: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        extension = self.extension

        description = self.description

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "extension": extension,
                "description": description,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        extension = d.pop("extension")

        description = d.pop("description")

        content = d.pop("content")

        artifact_post_in = cls(
            name=name,
            extension=extension,
            description=description,
            content=content,
        )

        artifact_post_in.additional_properties = d
        return artifact_post_in

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
