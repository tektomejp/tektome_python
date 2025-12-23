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
    from ..models.resource_required_schema import ResourceRequiredSchema
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="DataspaceProjectResourcesGetOut")


@_attrs_define
class DataspaceProjectResourcesGetOut:
    """Schema for retrieving resources in a dataspace project.

    Attributes:
        file (str):
        core_attributes (ResourceRequiredSchema):
        created_by (UserMetadata):
        updated_by (UserMetadata):
        created (datetime.datetime):
        updated (datetime.datetime):
        folder_id (None | Unset | UUID):
        id (None | Unset | UUID):
    """

    file: str
    core_attributes: ResourceRequiredSchema
    created_by: UserMetadata
    updated_by: UserMetadata
    created: datetime.datetime
    updated: datetime.datetime
    folder_id: None | Unset | UUID = UNSET
    id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        core_attributes = self.core_attributes.to_dict()

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        folder_id: None | str | Unset
        if isinstance(self.folder_id, Unset):
            folder_id = UNSET
        elif isinstance(self.folder_id, UUID):
            folder_id = str(self.folder_id)
        else:
            folder_id = self.folder_id

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
                "file": file,
                "core_attributes": core_attributes,
                "created_by": created_by,
                "updated_by": updated_by,
                "created": created,
                "updated": updated,
            }
        )
        if folder_id is not UNSET:
            field_dict["folder_id"] = folder_id
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_required_schema import ResourceRequiredSchema
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        file = d.pop("file")

        core_attributes = ResourceRequiredSchema.from_dict(d.pop("core_attributes"))

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        def _parse_folder_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                folder_id_type_0 = UUID(data)

                return folder_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        folder_id = _parse_folder_id(d.pop("folder_id", UNSET))

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

        dataspace_project_resources_get_out = cls(
            file=file,
            core_attributes=core_attributes,
            created_by=created_by,
            updated_by=updated_by,
            created=created,
            updated=updated,
            folder_id=folder_id,
            id=id,
        )

        dataspace_project_resources_get_out.additional_properties = d
        return dataspace_project_resources_get_out

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
