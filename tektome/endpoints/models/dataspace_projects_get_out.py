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
    from ..models.required_core_project_attributes import RequiredCoreProjectAttributes
    from ..models.required_core_project_metadata_attributes import RequiredCoreProjectMetadataAttributes
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="DataspaceProjectsGetOut")


@_attrs_define
class DataspaceProjectsGetOut:
    """
    Attributes:
        core_attributes (RequiredCoreProjectAttributes):
        core_attributes_metadata (RequiredCoreProjectMetadataAttributes):
        root_folder_id (UUID):
        created_by (UserMetadata):
        created (datetime.datetime):
        updated (datetime.datetime):
        files_count (int):
        pages_count (int):
        id (None | Unset | UUID):
    """

    core_attributes: RequiredCoreProjectAttributes
    core_attributes_metadata: RequiredCoreProjectMetadataAttributes
    root_folder_id: UUID
    created_by: UserMetadata
    created: datetime.datetime
    updated: datetime.datetime
    files_count: int
    pages_count: int
    id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        core_attributes = self.core_attributes.to_dict()

        core_attributes_metadata = self.core_attributes_metadata.to_dict()

        root_folder_id = str(self.root_folder_id)

        created_by = self.created_by.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        files_count = self.files_count

        pages_count = self.pages_count

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
                "core_attributes": core_attributes,
                "core_attributes_metadata": core_attributes_metadata,
                "root_folder_id": root_folder_id,
                "created_by": created_by,
                "created": created,
                "updated": updated,
                "files_count": files_count,
                "pages_count": pages_count,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.required_core_project_attributes import RequiredCoreProjectAttributes
        from ..models.required_core_project_metadata_attributes import RequiredCoreProjectMetadataAttributes
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        core_attributes = RequiredCoreProjectAttributes.from_dict(d.pop("core_attributes"))

        core_attributes_metadata = RequiredCoreProjectMetadataAttributes.from_dict(d.pop("core_attributes_metadata"))

        root_folder_id = UUID(d.pop("root_folder_id"))

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        files_count = d.pop("files_count")

        pages_count = d.pop("pages_count")

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

        dataspace_projects_get_out = cls(
            core_attributes=core_attributes,
            core_attributes_metadata=core_attributes_metadata,
            root_folder_id=root_folder_id,
            created_by=created_by,
            created=created,
            updated=updated,
            files_count=files_count,
            pages_count=pages_count,
            id=id,
        )

        dataspace_projects_get_out.additional_properties = d
        return dataspace_projects_get_out

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
