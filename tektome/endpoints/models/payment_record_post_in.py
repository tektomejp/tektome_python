from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transaction_types import TransactionTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentRecordPostIn")


@_attrs_define
class PaymentRecordPostIn:
    """Schema for creating a new payment record.

    Attributes:
        transaction_type (TransactionTypes):
        credits_amount (float | str):
        notes (None | str | Unset):
    """

    transaction_type: TransactionTypes
    credits_amount: float | str
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_type = self.transaction_type.value

        credits_amount: float | str
        credits_amount = self.credits_amount

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transaction_type": transaction_type,
                "credits_amount": credits_amount,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transaction_type = TransactionTypes(d.pop("transaction_type"))

        def _parse_credits_amount(data: object) -> float | str:
            return cast(float | str, data)

        credits_amount = _parse_credits_amount(d.pop("credits_amount"))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        payment_record_post_in = cls(
            transaction_type=transaction_type,
            credits_amount=credits_amount,
            notes=notes,
        )

        payment_record_post_in.additional_properties = d
        return payment_record_post_in

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
