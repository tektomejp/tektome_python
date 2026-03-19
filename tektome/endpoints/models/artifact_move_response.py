from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArtifactMoveResponse")


@_attrs_define
class ArtifactMoveResponse:
    """
    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        chatroom (UUID):
        path (str):
        id (None | Unset | UUID):
        created_by (None | Unset | UUID):
        updated_by (None | Unset | UUID):
        description (None | str | Unset):  Default: ''.
        content (None | str | Unset):  Default: ''.
        status (str | Unset):  Default: 'pending'.
        read_only (bool | Unset):  Default: False.
        job_id (None | Unset | UUID):
        imported_resource (None | Unset | UUID):
        imported_attribute_content_type (int | None | Unset):
        imported_attribute_object_id (None | Unset | UUID):
    """

    created: datetime.datetime
    updated: datetime.datetime
    chatroom: UUID
    path: str
    id: None | Unset | UUID = UNSET
    created_by: None | Unset | UUID = UNSET
    updated_by: None | Unset | UUID = UNSET
    description: None | str | Unset = ""
    content: None | str | Unset = ""
    status: str | Unset = "pending"
    read_only: bool | Unset = False
    job_id: None | Unset | UUID = UNSET
    imported_resource: None | Unset | UUID = UNSET
    imported_attribute_content_type: int | None | Unset = UNSET
    imported_attribute_object_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.isoformat()

        updated = self.updated.isoformat()

        chatroom = str(self.chatroom)

        path = self.path

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UUID):
            updated_by = str(self.updated_by)
        else:
            updated_by = self.updated_by

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        status = self.status

        read_only = self.read_only

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        elif isinstance(self.job_id, UUID):
            job_id = str(self.job_id)
        else:
            job_id = self.job_id

        imported_resource: None | str | Unset
        if isinstance(self.imported_resource, Unset):
            imported_resource = UNSET
        elif isinstance(self.imported_resource, UUID):
            imported_resource = str(self.imported_resource)
        else:
            imported_resource = self.imported_resource

        imported_attribute_content_type: int | None | Unset
        if isinstance(self.imported_attribute_content_type, Unset):
            imported_attribute_content_type = UNSET
        else:
            imported_attribute_content_type = self.imported_attribute_content_type

        imported_attribute_object_id: None | str | Unset
        if isinstance(self.imported_attribute_object_id, Unset):
            imported_attribute_object_id = UNSET
        elif isinstance(self.imported_attribute_object_id, UUID):
            imported_attribute_object_id = str(self.imported_attribute_object_id)
        else:
            imported_attribute_object_id = self.imported_attribute_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
                "chatroom": chatroom,
                "path": path,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if description is not UNSET:
            field_dict["description"] = description
        if content is not UNSET:
            field_dict["content"] = content
        if status is not UNSET:
            field_dict["status"] = status
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if imported_resource is not UNSET:
            field_dict["imported_resource"] = imported_resource
        if imported_attribute_content_type is not UNSET:
            field_dict["imported_attribute_content_type"] = imported_attribute_content_type
        if imported_attribute_object_id is not UNSET:
            field_dict["imported_attribute_object_id"] = imported_attribute_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        chatroom = UUID(d.pop("chatroom"))

        path = d.pop("path")

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

        def _parse_created_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_by_type_0 = UUID(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        status = d.pop("status", UNSET)

        read_only = d.pop("read_only", UNSET)

        def _parse_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_id_type_0 = UUID(data)

                return job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

        def _parse_imported_resource(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                imported_resource_type_0 = UUID(data)

                return imported_resource_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        imported_resource = _parse_imported_resource(d.pop("imported_resource", UNSET))

        def _parse_imported_attribute_content_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        imported_attribute_content_type = _parse_imported_attribute_content_type(
            d.pop("imported_attribute_content_type", UNSET)
        )

        def _parse_imported_attribute_object_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                imported_attribute_object_id_type_0 = UUID(data)

                return imported_attribute_object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        imported_attribute_object_id = _parse_imported_attribute_object_id(d.pop("imported_attribute_object_id", UNSET))

        artifact_move_response = cls(
            created=created,
            updated=updated,
            chatroom=chatroom,
            path=path,
            id=id,
            created_by=created_by,
            updated_by=updated_by,
            description=description,
            content=content,
            status=status,
            read_only=read_only,
            job_id=job_id,
            imported_resource=imported_resource,
            imported_attribute_content_type=imported_attribute_content_type,
            imported_attribute_object_id=imported_attribute_object_id,
        )

        artifact_move_response.additional_properties = d
        return artifact_move_response

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
