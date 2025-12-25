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
    from ..models.chatroom_post_out_current_operations import ChatroomPostOutCurrentOperations


T = TypeVar("T", bound="ChatroomPostOut")


@_attrs_define
class ChatroomPostOut:
    """
    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        user (UUID):
        id (None | Unset | UUID):
        organization (None | Unset | UUID):
        name (str | Unset):  Default: ''.
        description (str | Unset):  Default: ''.
        status (str | Unset):  Default: 'idle'.
        current_operations (ChatroomPostOutCurrentOperations | Unset):
    """

    created: datetime.datetime
    updated: datetime.datetime
    user: UUID
    id: None | Unset | UUID = UNSET
    organization: None | Unset | UUID = UNSET
    name: str | Unset = ""
    description: str | Unset = ""
    status: str | Unset = "idle"
    current_operations: ChatroomPostOutCurrentOperations | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.isoformat()

        updated = self.updated.isoformat()

        user = str(self.user)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        organization: None | str | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        elif isinstance(self.organization, UUID):
            organization = str(self.organization)
        else:
            organization = self.organization

        name = self.name

        description = self.description

        status = self.status

        current_operations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_operations, Unset):
            current_operations = self.current_operations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
                "user": user,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if current_operations is not UNSET:
            field_dict["current_operations"] = current_operations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chatroom_post_out_current_operations import ChatroomPostOutCurrentOperations

        d = dict(src_dict)
        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        user = UUID(d.pop("user"))

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

        def _parse_organization(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_type_0 = UUID(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization = _parse_organization(d.pop("organization", UNSET))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        _current_operations = d.pop("current_operations", UNSET)
        current_operations: ChatroomPostOutCurrentOperations | Unset
        if isinstance(_current_operations, Unset):
            current_operations = UNSET
        else:
            current_operations = ChatroomPostOutCurrentOperations.from_dict(_current_operations)

        chatroom_post_out = cls(
            created=created,
            updated=updated,
            user=user,
            id=id,
            organization=organization,
            name=name,
            description=description,
            status=status,
            current_operations=current_operations,
        )

        chatroom_post_out.additional_properties = d
        return chatroom_post_out

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
