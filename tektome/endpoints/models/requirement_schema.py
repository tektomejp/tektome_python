from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_entry_schema import ApprovalEntrySchema
    from ..models.lawtalk_requirement_required_schema import LawtalkRequirementRequiredSchema
    from ..models.requirement_schema_section_changes_since_last_summary import (
        RequirementSchemaSectionChangesSinceLastSummary,
    )
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="RequirementSchema")


@_attrs_define
class RequirementSchema:
    """
    Attributes:
        core_attributes (LawtalkRequirementRequiredSchema):
        created_by (UserMetadata):
        updated_by (UserMetadata):
        saved_items (int):
        approvals (list[ApprovalEntrySchema]):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        section_changes_since_last_summary (RequirementSchemaSectionChangesSinceLastSummary | Unset):
    """

    core_attributes: LawtalkRequirementRequiredSchema
    created_by: UserMetadata
    updated_by: UserMetadata
    saved_items: int
    approvals: list[ApprovalEntrySchema]
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    section_changes_since_last_summary: RequirementSchemaSectionChangesSinceLastSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        core_attributes = self.core_attributes.to_dict()

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        saved_items = self.saved_items

        approvals = []
        for approvals_item_data in self.approvals:
            approvals_item = approvals_item_data.to_dict()
            approvals.append(approvals_item)

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        section_changes_since_last_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.section_changes_since_last_summary, Unset):
            section_changes_since_last_summary = self.section_changes_since_last_summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "core_attributes": core_attributes,
                "created_by": created_by,
                "updated_by": updated_by,
                "saved_items": saved_items,
                "approvals": approvals,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if section_changes_since_last_summary is not UNSET:
            field_dict["section_changes_since_last_summary"] = section_changes_since_last_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_entry_schema import ApprovalEntrySchema
        from ..models.lawtalk_requirement_required_schema import LawtalkRequirementRequiredSchema
        from ..models.requirement_schema_section_changes_since_last_summary import (
            RequirementSchemaSectionChangesSinceLastSummary,
        )
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        core_attributes = LawtalkRequirementRequiredSchema.from_dict(d.pop("core_attributes"))

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        saved_items = d.pop("saved_items")

        approvals = []
        _approvals = d.pop("approvals")
        for approvals_item_data in _approvals:
            approvals_item = ApprovalEntrySchema.from_dict(approvals_item_data)

            approvals.append(approvals_item)

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        _section_changes_since_last_summary = d.pop("section_changes_since_last_summary", UNSET)
        section_changes_since_last_summary: RequirementSchemaSectionChangesSinceLastSummary | Unset
        if isinstance(_section_changes_since_last_summary, Unset):
            section_changes_since_last_summary = UNSET
        else:
            section_changes_since_last_summary = RequirementSchemaSectionChangesSinceLastSummary.from_dict(
                _section_changes_since_last_summary
            )

        requirement_schema = cls(
            core_attributes=core_attributes,
            created_by=created_by,
            updated_by=updated_by,
            saved_items=saved_items,
            approvals=approvals,
            created=created,
            updated=updated,
            id=id,
            section_changes_since_last_summary=section_changes_since_last_summary,
        )

        requirement_schema.additional_properties = d
        return requirement_schema

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
