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
    from ..models.dataspace_required_schema import DataspaceRequiredSchema
    from ..models.dataspaces_organization_schema import DataspacesOrganizationSchema
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="DataspaceListGetOut")


@_attrs_define
class DataspaceListGetOut:
    """
    Attributes:
        core_attributes (DataspaceRequiredSchema):
        created (datetime.datetime):
        updated (datetime.datetime):
        created_by (UserMetadata):
        updated_by (UserMetadata):
        organization (DataspacesOrganizationSchema):
        entities_count (int):
        files_count (int):
        pages_count (int):
        is_external (bool): Is the dataspace external from the organization
        id (None | Unset | UUID):
        icon (None | str | Unset):
    """

    core_attributes: DataspaceRequiredSchema
    created: datetime.datetime
    updated: datetime.datetime
    created_by: UserMetadata
    updated_by: UserMetadata
    organization: DataspacesOrganizationSchema
    entities_count: int
    files_count: int
    pages_count: int
    is_external: bool
    id: None | Unset | UUID = UNSET
    icon: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        core_attributes = self.core_attributes.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        organization = self.organization.to_dict()

        entities_count = self.entities_count

        files_count = self.files_count

        pages_count = self.pages_count

        is_external = self.is_external

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "core_attributes": core_attributes,
                "created": created,
                "updated": updated,
                "created_by": created_by,
                "updated_by": updated_by,
                "organization": organization,
                "entities_count": entities_count,
                "files_count": files_count,
                "pages_count": pages_count,
                "is_external": is_external,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_required_schema import DataspaceRequiredSchema
        from ..models.dataspaces_organization_schema import DataspacesOrganizationSchema
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        core_attributes = DataspaceRequiredSchema.from_dict(d.pop("core_attributes"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        organization = DataspacesOrganizationSchema.from_dict(d.pop("organization"))

        entities_count = d.pop("entities_count")

        files_count = d.pop("files_count")

        pages_count = d.pop("pages_count")

        is_external = d.pop("is_external")

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

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        dataspace_list_get_out = cls(
            core_attributes=core_attributes,
            created=created,
            updated=updated,
            created_by=created_by,
            updated_by=updated_by,
            organization=organization,
            entities_count=entities_count,
            files_count=files_count,
            pages_count=pages_count,
            is_external=is_external,
            id=id,
            icon=icon,
        )

        dataspace_list_get_out.additional_properties = d
        return dataspace_list_get_out

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
