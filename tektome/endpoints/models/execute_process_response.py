from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecuteProcessResponse")


@_attrs_define
class ExecuteProcessResponse:
    """
    Attributes:
        execution_group_id (UUID):
        execution_ids (list[UUID] | Unset):
    """

    execution_group_id: UUID
    execution_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_group_id = str(self.execution_group_id)

        execution_ids: list[str] | Unset = UNSET
        if not isinstance(self.execution_ids, Unset):
            execution_ids = []
            for execution_ids_item_data in self.execution_ids:
                execution_ids_item = str(execution_ids_item_data)
                execution_ids.append(execution_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "execution_group_id": execution_group_id,
            }
        )
        if execution_ids is not UNSET:
            field_dict["execution_ids"] = execution_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_group_id = UUID(d.pop("execution_group_id"))

        _execution_ids = d.pop("execution_ids", UNSET)
        execution_ids: list[UUID] | Unset = UNSET
        if _execution_ids is not UNSET:
            execution_ids = []
            for execution_ids_item_data in _execution_ids:
                execution_ids_item = UUID(execution_ids_item_data)

                execution_ids.append(execution_ids_item)

        execute_process_response = cls(
            execution_group_id=execution_group_id,
            execution_ids=execution_ids,
        )

        execute_process_response.additional_properties = d
        return execute_process_response

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
