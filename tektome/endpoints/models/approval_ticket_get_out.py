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
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="ApprovalTicketGetOut")


@_attrs_define
class ApprovalTicketGetOut:
    """Serializer for ApprovalTicket details

    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        category (str): The category of the approval ticket
        execution (UUID): The execution associated with this approval ticket
        process (UUID): The process associated with this approval ticket
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        status (str | Unset): The status of the approval ticket Default: 'pending'.
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    category: str
    execution: UUID
    process: UUID
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    status: str | Unset = "pending"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        category = self.category

        execution = str(self.execution)

        process = str(self.process)

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "category": category,
                "execution": execution,
                "process": process,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        category = d.pop("category")

        execution = UUID(d.pop("execution"))

        process = UUID(d.pop("process"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

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

        approval_ticket_get_out = cls(
            created_by=created_by,
            updated_by=updated_by,
            category=category,
            execution=execution,
            process=process,
            created=created,
            updated=updated,
            id=id,
            status=status,
        )

        approval_ticket_get_out.additional_properties = d
        return approval_ticket_get_out

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
