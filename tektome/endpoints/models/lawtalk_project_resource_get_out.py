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
    from ..models.attribute_schema import AttributeSchema
    from ..models.lawtalk_resource_required_schema import LawtalkResourceRequiredSchema
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="LawtalkProjectResourceGetOut")


@_attrs_define
class LawtalkProjectResourceGetOut:
    """
    Attributes:
        file (str):
        lawtalk_attributes (list[AttributeSchema]):
        core_attributes (LawtalkResourceRequiredSchema):
        created_by (UserMetadata):
        updated_by (UserMetadata):
        created (datetime.datetime):
        updated (datetime.datetime):
        initialization_status (None | str | Unset):
        folder_id (None | Unset | UUID):
        id (None | Unset | UUID):
        is_public (bool | Unset):  Default: False.
    """

    file: str
    lawtalk_attributes: list[AttributeSchema]
    core_attributes: LawtalkResourceRequiredSchema
    created_by: UserMetadata
    updated_by: UserMetadata
    created: datetime.datetime
    updated: datetime.datetime
    initialization_status: None | str | Unset = UNSET
    folder_id: None | Unset | UUID = UNSET
    id: None | Unset | UUID = UNSET
    is_public: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        lawtalk_attributes = []
        for lawtalk_attributes_item_data in self.lawtalk_attributes:
            lawtalk_attributes_item = lawtalk_attributes_item_data.to_dict()
            lawtalk_attributes.append(lawtalk_attributes_item)

        core_attributes = self.core_attributes.to_dict()

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        initialization_status: None | str | Unset
        if isinstance(self.initialization_status, Unset):
            initialization_status = UNSET
        else:
            initialization_status = self.initialization_status

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

        is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "lawtalk_attributes": lawtalk_attributes,
                "core_attributes": core_attributes,
                "created_by": created_by,
                "updated_by": updated_by,
                "created": created,
                "updated": updated,
            }
        )
        if initialization_status is not UNSET:
            field_dict["initialization_status"] = initialization_status
        if folder_id is not UNSET:
            field_dict["folder_id"] = folder_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_public is not UNSET:
            field_dict["is_public"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_schema import AttributeSchema
        from ..models.lawtalk_resource_required_schema import LawtalkResourceRequiredSchema
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        file = d.pop("file")

        lawtalk_attributes = []
        _lawtalk_attributes = d.pop("lawtalk_attributes")
        for lawtalk_attributes_item_data in _lawtalk_attributes:
            lawtalk_attributes_item = AttributeSchema.from_dict(lawtalk_attributes_item_data)

            lawtalk_attributes.append(lawtalk_attributes_item)

        core_attributes = LawtalkResourceRequiredSchema.from_dict(d.pop("core_attributes"))

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        def _parse_initialization_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initialization_status = _parse_initialization_status(d.pop("initialization_status", UNSET))

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

        is_public = d.pop("is_public", UNSET)

        lawtalk_project_resource_get_out = cls(
            file=file,
            lawtalk_attributes=lawtalk_attributes,
            core_attributes=core_attributes,
            created_by=created_by,
            updated_by=updated_by,
            created=created,
            updated=updated,
            initialization_status=initialization_status,
            folder_id=folder_id,
            id=id,
            is_public=is_public,
        )

        lawtalk_project_resource_get_out.additional_properties = d
        return lawtalk_project_resource_get_out

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
