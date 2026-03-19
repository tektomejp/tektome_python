from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transaction_types import TransactionTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentRecordPatchInPatch")


@_attrs_define
class PaymentRecordPatchInPatch:
    """
    Attributes:
        transaction_type (None | TransactionTypes | Unset):
        credits_amount (float | None | str | Unset):
        notes (None | str | Unset):
    """

    transaction_type: None | TransactionTypes | Unset = UNSET
    credits_amount: float | None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_type: None | str | Unset
        if isinstance(self.transaction_type, Unset):
            transaction_type = UNSET
        elif isinstance(self.transaction_type, TransactionTypes):
            transaction_type = self.transaction_type.value
        else:
            transaction_type = self.transaction_type

        credits_amount: float | None | str | Unset
        if isinstance(self.credits_amount, Unset):
            credits_amount = UNSET
        else:
            credits_amount = self.credits_amount

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_type is not UNSET:
            field_dict["transaction_type"] = transaction_type
        if credits_amount is not UNSET:
            field_dict["credits_amount"] = credits_amount
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_transaction_type(data: object) -> None | TransactionTypes | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transaction_type_type_0 = TransactionTypes(data)

                return transaction_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionTypes | Unset, data)

        transaction_type = _parse_transaction_type(d.pop("transaction_type", UNSET))

        def _parse_credits_amount(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        credits_amount = _parse_credits_amount(d.pop("credits_amount", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        payment_record_patch_in_patch = cls(
            transaction_type=transaction_type,
            credits_amount=credits_amount,
            notes=notes,
        )

        payment_record_patch_in_patch.additional_properties = d
        return payment_record_patch_in_patch

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
