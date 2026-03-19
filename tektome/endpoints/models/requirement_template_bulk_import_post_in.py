from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RequirementTemplateBulkImportPostIn")


@_attrs_define
class RequirementTemplateBulkImportPostIn:
    """Serializer for Requirement Template Bulk Import.

    Attributes:
        project_id (UUID):
        requirement_templates_ids (list[UUID]):
    """

    project_id: UUID
    requirement_templates_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = str(self.project_id)

        requirement_templates_ids = []
        for requirement_templates_ids_item_data in self.requirement_templates_ids:
            requirement_templates_ids_item = str(requirement_templates_ids_item_data)
            requirement_templates_ids.append(requirement_templates_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "requirement_templates_ids": requirement_templates_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = UUID(d.pop("project_id"))

        requirement_templates_ids = []
        _requirement_templates_ids = d.pop("requirement_templates_ids")
        for requirement_templates_ids_item_data in _requirement_templates_ids:
            requirement_templates_ids_item = UUID(requirement_templates_ids_item_data)

            requirement_templates_ids.append(requirement_templates_ids_item)

        requirement_template_bulk_import_post_in = cls(
            project_id=project_id,
            requirement_templates_ids=requirement_templates_ids,
        )

        requirement_template_bulk_import_post_in.additional_properties = d
        return requirement_template_bulk_import_post_in

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
