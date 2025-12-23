from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RequirementTemplateContainerPath")


@_attrs_define
class RequirementTemplateContainerPath:
    """Serializer for Requirement Template Path.

    Attributes:
        requirement_template_container_id (UUID):
    """

    requirement_template_container_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requirement_template_container_id = str(self.requirement_template_container_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requirement_template_container_id": requirement_template_container_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requirement_template_container_id = UUID(d.pop("requirement_template_container_id"))

        requirement_template_container_path = cls(
            requirement_template_container_id=requirement_template_container_id,
        )

        requirement_template_container_path.additional_properties = d
        return requirement_template_container_path

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
