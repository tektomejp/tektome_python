from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.affected_requirement_out import AffectedRequirementOut


T = TypeVar("T", bound="ResourceGroupCheckDeleteOut")


@_attrs_define
class ResourceGroupCheckDeleteOut:
    """
    Attributes:
        can_delete (bool):
        has_nested_items (bool):
        folder_count (int):
        resource_count (int):
        resources_in_use_count (int):
        affected_requirements (list[AffectedRequirementOut]):
        deep_research_notes_count (int):
    """

    can_delete: bool
    has_nested_items: bool
    folder_count: int
    resource_count: int
    resources_in_use_count: int
    affected_requirements: list[AffectedRequirementOut]
    deep_research_notes_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_delete = self.can_delete

        has_nested_items = self.has_nested_items

        folder_count = self.folder_count

        resource_count = self.resource_count

        resources_in_use_count = self.resources_in_use_count

        affected_requirements = []
        for affected_requirements_item_data in self.affected_requirements:
            affected_requirements_item = affected_requirements_item_data.to_dict()
            affected_requirements.append(affected_requirements_item)

        deep_research_notes_count = self.deep_research_notes_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "can_delete": can_delete,
                "has_nested_items": has_nested_items,
                "folder_count": folder_count,
                "resource_count": resource_count,
                "resources_in_use_count": resources_in_use_count,
                "affected_requirements": affected_requirements,
                "deep_research_notes_count": deep_research_notes_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.affected_requirement_out import AffectedRequirementOut

        d = dict(src_dict)
        can_delete = d.pop("can_delete")

        has_nested_items = d.pop("has_nested_items")

        folder_count = d.pop("folder_count")

        resource_count = d.pop("resource_count")

        resources_in_use_count = d.pop("resources_in_use_count")

        affected_requirements = []
        _affected_requirements = d.pop("affected_requirements")
        for affected_requirements_item_data in _affected_requirements:
            affected_requirements_item = AffectedRequirementOut.from_dict(affected_requirements_item_data)

            affected_requirements.append(affected_requirements_item)

        deep_research_notes_count = d.pop("deep_research_notes_count")

        resource_group_check_delete_out = cls(
            can_delete=can_delete,
            has_nested_items=has_nested_items,
            folder_count=folder_count,
            resource_count=resource_count,
            resources_in_use_count=resources_in_use_count,
            affected_requirements=affected_requirements,
            deep_research_notes_count=deep_research_notes_count,
        )

        resource_group_check_delete_out.additional_properties = d
        return resource_group_check_delete_out

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
