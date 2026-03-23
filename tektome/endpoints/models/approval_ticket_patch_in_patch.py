from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_category_types import ApprovalCategoryTypes
from ..models.approval_status_patch_in import ApprovalStatusPatchIn
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalTicketPatchInPatch")


@_attrs_define
class ApprovalTicketPatchInPatch:
    """
    Attributes:
        category (ApprovalCategoryTypes | None | Unset):
        status (ApprovalStatusPatchIn | None | Unset):
    """

    category: ApprovalCategoryTypes | None | Unset = UNSET
    status: ApprovalStatusPatchIn | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, ApprovalCategoryTypes):
            category = self.category.value
        else:
            category = self.category

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ApprovalStatusPatchIn):
            status = self.status.value
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_category(data: object) -> ApprovalCategoryTypes | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_0 = ApprovalCategoryTypes(data)

                return category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalCategoryTypes | None | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_status(data: object) -> ApprovalStatusPatchIn | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = ApprovalStatusPatchIn(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalStatusPatchIn | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        approval_ticket_patch_in_patch = cls(
            category=category,
            status=status,
        )

        approval_ticket_patch_in_patch.additional_properties = d
        return approval_ticket_patch_in_patch

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
