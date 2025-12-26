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


T = TypeVar("T", bound="PaymentRecordOutBase")


@_attrs_define
class PaymentRecordOutBase:
    """
    Attributes:
        supporting_file (str):
        created_by (UserMetadata):
        updated_by (UserMetadata):
        transaction_type (str):
        credits_amount (float | str):
        original_file_name (str):
        reference_id (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        notes (None | str | Unset):
        deleted (datetime.datetime | None | Unset):
    """

    supporting_file: str
    created_by: UserMetadata
    updated_by: UserMetadata
    transaction_type: str
    credits_amount: float | str
    original_file_name: str
    reference_id: str
    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    notes: None | str | Unset = UNSET
    deleted: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        supporting_file = self.supporting_file

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        transaction_type = self.transaction_type

        credits_amount: float | str
        credits_amount = self.credits_amount

        original_file_name = self.original_file_name

        reference_id = self.reference_id

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        deleted: None | str | Unset
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        elif isinstance(self.deleted, datetime.datetime):
            deleted = self.deleted.isoformat()
        else:
            deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "supporting_file": supporting_file,
                "created_by": created_by,
                "updated_by": updated_by,
                "transaction_type": transaction_type,
                "credits_amount": credits_amount,
                "original_file_name": original_file_name,
                "reference_id": reference_id,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        supporting_file = d.pop("supporting_file")

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        transaction_type = d.pop("transaction_type")

        def _parse_credits_amount(data: object) -> float | str:
            return cast(float | str, data)

        credits_amount = _parse_credits_amount(d.pop("credits_amount"))

        original_file_name = d.pop("original_file_name")

        reference_id = d.pop("reference_id")

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

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_deleted(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_type_0 = isoparse(data)

                return deleted_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        payment_record_out_base = cls(
            supporting_file=supporting_file,
            created_by=created_by,
            updated_by=updated_by,
            transaction_type=transaction_type,
            credits_amount=credits_amount,
            original_file_name=original_file_name,
            reference_id=reference_id,
            created=created,
            updated=updated,
            id=id,
            notes=notes,
            deleted=deleted,
        )

        payment_record_out_base.additional_properties = d
        return payment_record_out_base

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
