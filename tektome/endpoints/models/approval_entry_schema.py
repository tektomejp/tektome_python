from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.approval_user_schema import ApprovalUserSchema


T = TypeVar("T", bound="ApprovalEntrySchema")


@_attrs_define
class ApprovalEntrySchema:
    """Schema for a single approval entry within the JSONField.

    Attributes:
        user_id (UUID):
        approved_at (datetime.datetime):
        user (ApprovalUserSchema | None):
    """

    user_id: UUID
    approved_at: datetime.datetime
    user: ApprovalUserSchema | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.approval_user_schema import ApprovalUserSchema

        user_id = str(self.user_id)

        approved_at = self.approved_at.isoformat()

        user: dict[str, Any] | None
        if isinstance(self.user, ApprovalUserSchema):
            user = self.user.to_dict()
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "approved_at": approved_at,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_user_schema import ApprovalUserSchema

        d = dict(src_dict)
        user_id = UUID(d.pop("user_id"))

        approved_at = isoparse(d.pop("approved_at"))

        def _parse_user(data: object) -> ApprovalUserSchema | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = ApprovalUserSchema.from_dict(data)

                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalUserSchema | None, data)

        user = _parse_user(d.pop("user"))

        approval_entry_schema = cls(
            user_id=user_id,
            approved_at=approved_at,
            user=user,
        )

        approval_entry_schema.additional_properties = d
        return approval_entry_schema

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
