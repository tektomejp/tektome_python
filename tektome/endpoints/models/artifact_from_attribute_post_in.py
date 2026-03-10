from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArtifactFromAttributePostIn")


@_attrs_define
class ArtifactFromAttributePostIn:
    """
    Attributes:
        path (str):
        attribute_id (UUID):
        description (str | Unset):  Default: ''.
    """

    path: str
    attribute_id: UUID
    description: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        attribute_id = str(self.attribute_id)

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "attribute_id": attribute_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        attribute_id = UUID(d.pop("attribute_id"))

        description = d.pop("description", UNSET)

        artifact_from_attribute_post_in = cls(
            path=path,
            attribute_id=attribute_id,
            description=description,
        )

        artifact_from_attribute_post_in.additional_properties = d
        return artifact_from_attribute_post_in

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
