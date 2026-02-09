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
    from ..models.resource_metadata_required_schema import ResourceMetadataRequiredSchema
    from ..models.resource_required_schema import ResourceRequiredSchema
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="ResourceChildren")


@_attrs_define
class ResourceChildren:
    """
    Attributes:
        core_attributes (ResourceRequiredSchema):
        core_attributes_metadata (ResourceMetadataRequiredSchema):
        created (datetime.datetime):
        updated (datetime.datetime):
        file (str):
        created_by (UserMetadata):
        updated_by (UserMetadata):
        id (None | Unset | UUID):
        is_public (bool | Unset):  Default: False.
        initialization_status (None | str | Unset):
        bim_project_id (None | Unset | UUID):
    """

    core_attributes: ResourceRequiredSchema
    core_attributes_metadata: ResourceMetadataRequiredSchema
    created: datetime.datetime
    updated: datetime.datetime
    file: str
    created_by: UserMetadata
    updated_by: UserMetadata
    id: None | Unset | UUID = UNSET
    is_public: bool | Unset = False
    initialization_status: None | str | Unset = UNSET
    bim_project_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        core_attributes = self.core_attributes.to_dict()

        core_attributes_metadata = self.core_attributes_metadata.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        file = self.file

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_public = self.is_public

        initialization_status: None | str | Unset
        if isinstance(self.initialization_status, Unset):
            initialization_status = UNSET
        else:
            initialization_status = self.initialization_status

        bim_project_id: None | str | Unset
        if isinstance(self.bim_project_id, Unset):
            bim_project_id = UNSET
        elif isinstance(self.bim_project_id, UUID):
            bim_project_id = str(self.bim_project_id)
        else:
            bim_project_id = self.bim_project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "core_attributes": core_attributes,
                "core_attributes_metadata": core_attributes_metadata,
                "created": created,
                "updated": updated,
                "file": file,
                "created_by": created_by,
                "updated_by": updated_by,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if initialization_status is not UNSET:
            field_dict["initialization_status"] = initialization_status
        if bim_project_id is not UNSET:
            field_dict["bim_project_id"] = bim_project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_metadata_required_schema import ResourceMetadataRequiredSchema
        from ..models.resource_required_schema import ResourceRequiredSchema
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        core_attributes = ResourceRequiredSchema.from_dict(d.pop("core_attributes"))

        core_attributes_metadata = ResourceMetadataRequiredSchema.from_dict(d.pop("core_attributes_metadata"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        file = d.pop("file")

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

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

        is_public = d.pop("is_public", UNSET)

        def _parse_initialization_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initialization_status = _parse_initialization_status(d.pop("initialization_status", UNSET))

        def _parse_bim_project_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bim_project_id_type_0 = UUID(data)

                return bim_project_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bim_project_id = _parse_bim_project_id(d.pop("bim_project_id", UNSET))

        resource_children = cls(
            core_attributes=core_attributes,
            core_attributes_metadata=core_attributes_metadata,
            created=created,
            updated=updated,
            file=file,
            created_by=created_by,
            updated_by=updated_by,
            id=id,
            is_public=is_public,
            initialization_status=initialization_status,
            bim_project_id=bim_project_id,
        )

        resource_children.additional_properties = d
        return resource_children

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
