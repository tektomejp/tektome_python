from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExecutionPathParams")


@_attrs_define
class ExecutionPathParams:
    """
    Attributes:
        dataspace_id (UUID):
        execution_id (UUID): The UUID of the execution to cancel
    """

    dataspace_id: UUID
    execution_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataspace_id = str(self.dataspace_id)

        execution_id = str(self.execution_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataspace_id": dataspace_id,
                "execution_id": execution_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataspace_id = UUID(d.pop("dataspace_id"))

        execution_id = UUID(d.pop("execution_id"))

        execution_path_params = cls(
            dataspace_id=dataspace_id,
            execution_id=execution_id,
        )

        execution_path_params.additional_properties = d
        return execution_path_params

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
