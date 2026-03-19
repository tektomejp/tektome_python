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
    from ..models.requirement_template_resources_get_out import RequirementTemplateResourcesGetOut
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="RequirementTemplateContainerGetOut")


@_attrs_define
class RequirementTemplateContainerGetOut:
    """Serializer for Requirement Template Output.

    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        name (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        public_resource_groups (list[RequirementTemplateResourcesGetOut] | Unset):
        requirements_count (int | Unset):  Default: 0.
        is_updated_since_last_seen (bool | None | Unset):
        is_template_new_since_last_seen (bool | None | Unset):
        id (None | Unset | UUID):
        description (None | str | Unset):
        status (str | Unset):  Default: 'draft'.
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    name: str
    created: datetime.datetime
    updated: datetime.datetime
    public_resource_groups: list[RequirementTemplateResourcesGetOut] | Unset = UNSET
    requirements_count: int | Unset = 0
    is_updated_since_last_seen: bool | None | Unset = UNSET
    is_template_new_since_last_seen: bool | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    status: str | Unset = "draft"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        name = self.name

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        public_resource_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.public_resource_groups, Unset):
            public_resource_groups = []
            for public_resource_groups_item_data in self.public_resource_groups:
                public_resource_groups_item = public_resource_groups_item_data.to_dict()
                public_resource_groups.append(public_resource_groups_item)

        requirements_count = self.requirements_count

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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "name": name,
                "created": created,
                "updated": updated,
            }
        )
        if public_resource_groups is not UNSET:
            field_dict["public_resource_groups"] = public_resource_groups
        if requirements_count is not UNSET:
            field_dict["requirements_count"] = requirements_count
        if is_updated_since_last_seen is not UNSET:
            field_dict["is_updated_since_last_seen"] = is_updated_since_last_seen
        if is_template_new_since_last_seen is not UNSET:
            field_dict["is_template_new_since_last_seen"] = is_template_new_since_last_seen
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.requirement_template_resources_get_out import RequirementTemplateResourcesGetOut
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        name = d.pop("name")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        _public_resource_groups = d.pop("public_resource_groups", UNSET)
        public_resource_groups: list[RequirementTemplateResourcesGetOut] | Unset = UNSET
        if _public_resource_groups is not UNSET:
            public_resource_groups = []
            for public_resource_groups_item_data in _public_resource_groups:
                public_resource_groups_item = RequirementTemplateResourcesGetOut.from_dict(
                    public_resource_groups_item_data
                )

                public_resource_groups.append(public_resource_groups_item)

        requirements_count = d.pop("requirements_count", UNSET)

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        status = d.pop("status", UNSET)

        requirement_template_container_get_out = cls(
            created_by=created_by,
            updated_by=updated_by,
            name=name,
            created=created,
            updated=updated,
            public_resource_groups=public_resource_groups,
            requirements_count=requirements_count,
            is_updated_since_last_seen=is_updated_since_last_seen,
            is_template_new_since_last_seen=is_template_new_since_last_seen,
            id=id,
            description=description,
            status=status,
        )

        requirement_template_container_get_out.additional_properties = d
        return requirement_template_container_get_out

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
