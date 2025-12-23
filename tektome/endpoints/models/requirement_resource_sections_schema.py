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
    from ..models.requirement_lawtalk_resource_group_schema import RequirementLawtalkResourceGroupSchema
    from ..models.requirement_lawtalk_resource_metadata_schema import RequirementLawtalkResourceMetadataSchema
    from ..models.requirement_resource_capture_section_component_schema import (
        RequirementResourceCaptureSectionComponentSchema,
    )
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="RequirementResourceSectionsSchema")


@_attrs_define
class RequirementResourceSectionsSchema:
    """
    Attributes:
        resource (RequirementLawtalkResourceMetadataSchema):
        resource_group (RequirementLawtalkResourceGroupSchema):
        captures (list[RequirementResourceCaptureSectionComponentSchema]):
        value (None | str):
        status (None | str):
        created_by (UserMetadata):
        updated_by (UserMetadata):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
    """

    resource: RequirementLawtalkResourceMetadataSchema
    resource_group: RequirementLawtalkResourceGroupSchema
    captures: list[RequirementResourceCaptureSectionComponentSchema]
    value: None | str
    status: None | str
    created_by: UserMetadata
    updated_by: UserMetadata
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource.to_dict()

        resource_group = self.resource_group.to_dict()

        captures = []
        for captures_item_data in self.captures:
            captures_item = captures_item_data.to_dict()
            captures.append(captures_item)

        value: None | str
        value = self.value

        status: None | str
        status = self.status

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "resource_group": resource_group,
                "captures": captures,
                "value": value,
                "status": status,
                "created_by": created_by,
                "updated_by": updated_by,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.requirement_lawtalk_resource_group_schema import RequirementLawtalkResourceGroupSchema
        from ..models.requirement_lawtalk_resource_metadata_schema import RequirementLawtalkResourceMetadataSchema
        from ..models.requirement_resource_capture_section_component_schema import (
            RequirementResourceCaptureSectionComponentSchema,
        )
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        resource = RequirementLawtalkResourceMetadataSchema.from_dict(d.pop("resource"))

        resource_group = RequirementLawtalkResourceGroupSchema.from_dict(d.pop("resource_group"))

        captures = []
        _captures = d.pop("captures")
        for captures_item_data in _captures:
            captures_item = RequirementResourceCaptureSectionComponentSchema.from_dict(captures_item_data)

            captures.append(captures_item)

        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

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

        requirement_resource_sections_schema = cls(
            resource=resource,
            resource_group=resource_group,
            captures=captures,
            value=value,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
            created=created,
            updated=updated,
            id=id,
        )

        requirement_resource_sections_schema.additional_properties = d
        return requirement_resource_sections_schema

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
