from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.resource_glob_out_initialization_status_type_0 import ResourceGlobOutInitializationStatusType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_out import UserOut


T = TypeVar("T", bound="ResourceGlobOut")


@_attrs_define
class ResourceGlobOut:
    """
    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        resource_id (None | Unset | UUID):
        name (None | str | Unset):
        kind (None | str | Unset):
        description (None | str | Unset):
        bim_project_id (None | Unset | UUID):
        initialization_status (None | ResourceGlobOutInitializationStatusType0 | Unset):
        created_by (None | Unset | UserOut):
        updated_by (None | Unset | UserOut):
        id (None | Unset | UUID):
        path (None | str | Unset): Full path including filename. None = unmigrated row.
    """

    created: datetime.datetime
    updated: datetime.datetime
    resource_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    bim_project_id: None | Unset | UUID = UNSET
    initialization_status: None | ResourceGlobOutInitializationStatusType0 | Unset = UNSET
    created_by: None | Unset | UserOut = UNSET
    updated_by: None | Unset | UserOut = UNSET
    id: None | Unset | UUID = UNSET
    path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_out import UserOut

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        elif isinstance(self.resource_id, UUID):
            resource_id = str(self.resource_id)
        else:
            resource_id = self.resource_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        bim_project_id: None | str | Unset
        if isinstance(self.bim_project_id, Unset):
            bim_project_id = UNSET
        elif isinstance(self.bim_project_id, UUID):
            bim_project_id = str(self.bim_project_id)
        else:
            bim_project_id = self.bim_project_id

        initialization_status: None | str | Unset
        if isinstance(self.initialization_status, Unset):
            initialization_status = UNSET
        elif isinstance(self.initialization_status, ResourceGlobOutInitializationStatusType0):
            initialization_status = self.initialization_status.value
        else:
            initialization_status = self.initialization_status

        created_by: dict[str, Any] | None | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UserOut):
            created_by = self.created_by.to_dict()
        else:
            created_by = self.created_by

        updated_by: dict[str, Any] | None | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UserOut):
            updated_by = self.updated_by.to_dict()
        else:
            updated_by = self.updated_by

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
            }
        )
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if description is not UNSET:
            field_dict["description"] = description
        if bim_project_id is not UNSET:
            field_dict["bim_project_id"] = bim_project_id
        if initialization_status is not UNSET:
            field_dict["initialization_status"] = initialization_status
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if id is not UNSET:
            field_dict["id"] = id
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_out import UserOut

        d = dict(src_dict)
        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        def _parse_resource_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resource_id_type_0 = UUID(data)

                return resource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        resource_id = _parse_resource_id(d.pop("resource_id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_initialization_status(data: object) -> None | ResourceGlobOutInitializationStatusType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                initialization_status_type_0 = ResourceGlobOutInitializationStatusType0(data)

                return initialization_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResourceGlobOutInitializationStatusType0 | Unset, data)

        initialization_status = _parse_initialization_status(d.pop("initialization_status", UNSET))

        def _parse_created_by(data: object) -> None | Unset | UserOut:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_type_0 = UserOut.from_dict(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserOut, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> None | Unset | UserOut:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_by_type_0 = UserOut.from_dict(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserOut, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

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

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        resource_glob_out = cls(
            created=created,
            updated=updated,
            resource_id=resource_id,
            name=name,
            kind=kind,
            description=description,
            bim_project_id=bim_project_id,
            initialization_status=initialization_status,
            created_by=created_by,
            updated_by=updated_by,
            id=id,
            path=path,
        )

        resource_glob_out.additional_properties = d
        return resource_glob_out

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
