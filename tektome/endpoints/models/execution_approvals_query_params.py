from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_category_types import ApprovalCategoryTypes
from ..models.approval_status import ApprovalStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionApprovalsQueryParams")


@_attrs_define
class ExecutionApprovalsQueryParams:
    """Query parameters for retrieving execution approvals

    Attributes:
        execution_id (None | Unset | UUID):
        execution_group_id (None | Unset | UUID):
        status (ApprovalStatus | None | Unset):
        category (ApprovalCategoryTypes | None | Unset):
    """

    execution_id: None | Unset | UUID = UNSET
    execution_group_id: None | Unset | UUID = UNSET
    status: ApprovalStatus | None | Unset = UNSET
    category: ApprovalCategoryTypes | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id: None | str | Unset
        if isinstance(self.execution_id, Unset):
            execution_id = UNSET
        elif isinstance(self.execution_id, UUID):
            execution_id = str(self.execution_id)
        else:
            execution_id = self.execution_id

        execution_group_id: None | str | Unset
        if isinstance(self.execution_group_id, Unset):
            execution_group_id = UNSET
        elif isinstance(self.execution_group_id, UUID):
            execution_group_id = str(self.execution_group_id)
        else:
            execution_group_id = self.execution_group_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ApprovalStatus):
            status = self.status.value
        else:
            status = self.status

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, ApprovalCategoryTypes):
            category = self.category.value
        else:
            category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_id is not UNSET:
            field_dict["execution_id"] = execution_id
        if execution_group_id is not UNSET:
            field_dict["execution_group_id"] = execution_group_id
        if status is not UNSET:
            field_dict["status"] = status
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_execution_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execution_id_type_0 = UUID(data)

                return execution_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        execution_id = _parse_execution_id(d.pop("execution_id", UNSET))

        def _parse_execution_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execution_group_id_type_0 = UUID(data)

                return execution_group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        execution_group_id = _parse_execution_group_id(d.pop("execution_group_id", UNSET))

        def _parse_status(data: object) -> ApprovalStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = ApprovalStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

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

        execution_approvals_query_params = cls(
            execution_id=execution_id,
            execution_group_id=execution_group_id,
            status=status,
            category=category,
        )

        execution_approvals_query_params.additional_properties = d
        return execution_approvals_query_params

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
