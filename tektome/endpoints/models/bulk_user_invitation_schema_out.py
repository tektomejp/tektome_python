from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_invitation_skipped_schema import UserInvitationSkippedSchema
    from ..models.user_invitation_success_schema import UserInvitationSuccessSchema


T = TypeVar("T", bound="BulkUserInvitationSchemaOut")


@_attrs_define
class BulkUserInvitationSchemaOut:
    """
    Attributes:
        added (list[UserInvitationSuccessSchema] | Unset):
        skipped (list[UserInvitationSkippedSchema] | Unset):
    """

    added: list[UserInvitationSuccessSchema] | Unset = UNSET
    skipped: list[UserInvitationSkippedSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.added, Unset):
            added = []
            for added_item_data in self.added:
                added_item = added_item_data.to_dict()
                added.append(added_item)

        skipped: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skipped, Unset):
            skipped = []
            for skipped_item_data in self.skipped:
                skipped_item = skipped_item_data.to_dict()
                skipped.append(skipped_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added is not UNSET:
            field_dict["added"] = added
        if skipped is not UNSET:
            field_dict["skipped"] = skipped

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_invitation_skipped_schema import UserInvitationSkippedSchema
        from ..models.user_invitation_success_schema import UserInvitationSuccessSchema

        d = dict(src_dict)
        _added = d.pop("added", UNSET)
        added: list[UserInvitationSuccessSchema] | Unset = UNSET
        if _added is not UNSET:
            added = []
            for added_item_data in _added:
                added_item = UserInvitationSuccessSchema.from_dict(added_item_data)

                added.append(added_item)

        _skipped = d.pop("skipped", UNSET)
        skipped: list[UserInvitationSkippedSchema] | Unset = UNSET
        if _skipped is not UNSET:
            skipped = []
            for skipped_item_data in _skipped:
                skipped_item = UserInvitationSkippedSchema.from_dict(skipped_item_data)

                skipped.append(skipped_item)

        bulk_user_invitation_schema_out = cls(
            added=added,
            skipped=skipped,
        )

        bulk_user_invitation_schema_out.additional_properties = d
        return bulk_user_invitation_schema_out

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
