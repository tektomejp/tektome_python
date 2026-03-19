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
    from ..models.requirement_template_get_out_requirement_item_attribute_table_type_0 import (
        RequirementTemplateGetOutRequirementItemAttributeTableType0,
    )
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="RequirementTemplateGetOut")


@_attrs_define
class RequirementTemplateGetOut:
    """Serializer for retrieving a Requirement Template.

    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        title (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        item_count (int | Unset):  Default: 0.
        usage_count (int | Unset):  Default: 0.
        ref_notes_count (int | Unset):  Default: 0.
        research_templates_count (int | Unset):  Default: 0.
        is_updated_since_last_seen (bool | None | Unset):
        is_template_new_since_last_seen (bool | None | Unset):
        id (None | Unset | UUID):
        status (str | Unset):  Default: 'draft'.
        requirement_item_attribute_table (None | RequirementTemplateGetOutRequirementItemAttributeTableType0 | Unset):
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    title: str
    created: datetime.datetime
    updated: datetime.datetime
    item_count: int | Unset = 0
    usage_count: int | Unset = 0
    ref_notes_count: int | Unset = 0
    research_templates_count: int | Unset = 0
    is_updated_since_last_seen: bool | None | Unset = UNSET
    is_template_new_since_last_seen: bool | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    status: str | Unset = "draft"
    requirement_item_attribute_table: None | RequirementTemplateGetOutRequirementItemAttributeTableType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.requirement_template_get_out_requirement_item_attribute_table_type_0 import (
            RequirementTemplateGetOutRequirementItemAttributeTableType0,
        )

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        title = self.title

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        item_count = self.item_count

        usage_count = self.usage_count

        ref_notes_count = self.ref_notes_count

        research_templates_count = self.research_templates_count

        is_updated_since_last_seen: bool | None | Unset
        if isinstance(self.is_updated_since_last_seen, Unset):
            is_updated_since_last_seen = UNSET
        else:
            is_updated_since_last_seen = self.is_updated_since_last_seen

        is_template_new_since_last_seen: bool | None | Unset
        if isinstance(self.is_template_new_since_last_seen, Unset):
            is_template_new_since_last_seen = UNSET
        else:
            is_template_new_since_last_seen = self.is_template_new_since_last_seen

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        status = self.status

        requirement_item_attribute_table: dict[str, Any] | None | Unset
        if isinstance(self.requirement_item_attribute_table, Unset):
            requirement_item_attribute_table = UNSET
        elif isinstance(
            self.requirement_item_attribute_table, RequirementTemplateGetOutRequirementItemAttributeTableType0
        ):
            requirement_item_attribute_table = self.requirement_item_attribute_table.to_dict()
        else:
            requirement_item_attribute_table = self.requirement_item_attribute_table

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "title": title,
                "created": created,
                "updated": updated,
            }
        )
        if item_count is not UNSET:
            field_dict["item_count"] = item_count
        if usage_count is not UNSET:
            field_dict["usage_count"] = usage_count
        if ref_notes_count is not UNSET:
            field_dict["ref_notes_count"] = ref_notes_count
        if research_templates_count is not UNSET:
            field_dict["research_templates_count"] = research_templates_count
        if is_updated_since_last_seen is not UNSET:
            field_dict["is_updated_since_last_seen"] = is_updated_since_last_seen
        if is_template_new_since_last_seen is not UNSET:
            field_dict["is_template_new_since_last_seen"] = is_template_new_since_last_seen
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if requirement_item_attribute_table is not UNSET:
            field_dict["requirement_item_attribute_table"] = requirement_item_attribute_table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.requirement_template_get_out_requirement_item_attribute_table_type_0 import (
            RequirementTemplateGetOutRequirementItemAttributeTableType0,
        )
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        title = d.pop("title")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        item_count = d.pop("item_count", UNSET)

        usage_count = d.pop("usage_count", UNSET)

        ref_notes_count = d.pop("ref_notes_count", UNSET)

        research_templates_count = d.pop("research_templates_count", UNSET)

        def _parse_is_updated_since_last_seen(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_updated_since_last_seen = _parse_is_updated_since_last_seen(d.pop("is_updated_since_last_seen", UNSET))

        def _parse_is_template_new_since_last_seen(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_template_new_since_last_seen = _parse_is_template_new_since_last_seen(
            d.pop("is_template_new_since_last_seen", UNSET)
        )

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

        status = d.pop("status", UNSET)

        def _parse_requirement_item_attribute_table(
            data: object,
        ) -> None | RequirementTemplateGetOutRequirementItemAttributeTableType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                requirement_item_attribute_table_type_0 = (
                    RequirementTemplateGetOutRequirementItemAttributeTableType0.from_dict(data)
                )

                return requirement_item_attribute_table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RequirementTemplateGetOutRequirementItemAttributeTableType0 | Unset, data)

        requirement_item_attribute_table = _parse_requirement_item_attribute_table(
            d.pop("requirement_item_attribute_table", UNSET)
        )

        requirement_template_get_out = cls(
            created_by=created_by,
            updated_by=updated_by,
            title=title,
            created=created,
            updated=updated,
            item_count=item_count,
            usage_count=usage_count,
            ref_notes_count=ref_notes_count,
            research_templates_count=research_templates_count,
            is_updated_since_last_seen=is_updated_since_last_seen,
            is_template_new_since_last_seen=is_template_new_since_last_seen,
            id=id,
            status=status,
            requirement_item_attribute_table=requirement_item_attribute_table,
        )

        requirement_template_get_out.additional_properties = d
        return requirement_template_get_out

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
