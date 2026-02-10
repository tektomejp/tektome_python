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
    from ..models.notification_get_out_metadata import NotificationGetOutMetadata


T = TypeVar("T", bound="NotificationGetOut")


@_attrs_define
class NotificationGetOut:
    """Output schema for notification.

    Attributes:
        type_ (str): The type of notification
        title (str): The title of the notification
        body (str): The body/description of the notification
        entity_type (str): The type of entity this notification relates to
        entity_id (UUID): The ID of the related entity
        created (datetime.datetime):
        updated (datetime.datetime):
        organization_id (None | Unset | UUID):
        dataspace_id (None | Unset | UUID):
        id (None | Unset | UUID):
        status (str | Unset): The read status of the notification Default: 'unread'.
        metadata (NotificationGetOutMetadata | Unset): Additional context data (entity IDs, counts, etc.)
    """

    type_: str
    title: str
    body: str
    entity_type: str
    entity_id: UUID
    created: datetime.datetime
    updated: datetime.datetime
    organization_id: None | Unset | UUID = UNSET
    dataspace_id: None | Unset | UUID = UNSET
    id: None | Unset | UUID = UNSET
    status: str | Unset = "unread"
    metadata: NotificationGetOutMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        title = self.title

        body = self.body

        entity_type = self.entity_type

        entity_id = str(self.entity_id)

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        dataspace_id: None | str | Unset
        if isinstance(self.dataspace_id, Unset):
            dataspace_id = UNSET
        elif isinstance(self.dataspace_id, UUID):
            dataspace_id = str(self.dataspace_id)
        else:
            dataspace_id = self.dataspace_id

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        status = self.status

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
                "body": body,
                "entity_type": entity_type,
                "entity_id": entity_id,
                "created": created,
                "updated": updated,
            }
        )
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if dataspace_id is not UNSET:
            field_dict["dataspace_id"] = dataspace_id
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_get_out_metadata import NotificationGetOutMetadata

        d = dict(src_dict)
        type_ = d.pop("type")

        title = d.pop("title")

        body = d.pop("body")

        entity_type = d.pop("entity_type")

        entity_id = UUID(d.pop("entity_id"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)

                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        def _parse_dataspace_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dataspace_id_type_0 = UUID(data)

                return dataspace_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dataspace_id = _parse_dataspace_id(d.pop("dataspace_id", UNSET))

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

        _metadata = d.pop("metadata", UNSET)
        metadata: NotificationGetOutMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = NotificationGetOutMetadata.from_dict(_metadata)

        notification_get_out = cls(
            type_=type_,
            title=title,
            body=body,
            entity_type=entity_type,
            entity_id=entity_id,
            created=created,
            updated=updated,
            organization_id=organization_id,
            dataspace_id=dataspace_id,
            id=id,
            status=status,
            metadata=metadata,
        )

        notification_get_out.additional_properties = d
        return notification_get_out

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
