from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RequirementResearchTemplatePath")


@_attrs_define
class RequirementResearchTemplatePath:
    """Path parameters for Requirement Research Template operations.

    requirement_id: UUID The unique identifier of the requirement.
    research_template_id: UUID The unique identifier of the research template.

        Attributes:
            research_template_id (UUID):
            requirement_id (UUID):
    """

    research_template_id: UUID
    requirement_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        research_template_id = str(self.research_template_id)

        requirement_id = str(self.requirement_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "research_template_id": research_template_id,
                "requirement_id": requirement_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        research_template_id = UUID(d.pop("research_template_id"))

        requirement_id = UUID(d.pop("requirement_id"))

        requirement_research_template_path = cls(
            research_template_id=research_template_id,
            requirement_id=requirement_id,
        )

        requirement_research_template_path.additional_properties = d
        return requirement_research_template_path

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
