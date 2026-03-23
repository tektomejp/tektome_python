from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BimProjectV2IndexTaskQuery")


@_attrs_define
class BimProjectV2IndexTaskQuery:
    """Query options for BIM project-wide V2 indexing task trigger.

    Attributes:
        batch_size (int | Unset): Batch size for chunked indexing. Must be between 1 and 500. Default: 500.
        concurrency (int | Unset): Number of batches to process in parallel. Must be at least 1. Default: 1.
    """

    batch_size: int | Unset = 500
    concurrency: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_size = self.batch_size

        concurrency = self.concurrency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_size is not UNSET:
            field_dict["batch_size"] = batch_size
        if concurrency is not UNSET:
            field_dict["concurrency"] = concurrency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        batch_size = d.pop("batch_size", UNSET)

        concurrency = d.pop("concurrency", UNSET)

        bim_project_v2_index_task_query = cls(
            batch_size=batch_size,
            concurrency=concurrency,
        )

        bim_project_v2_index_task_query.additional_properties = d
        return bim_project_v2_index_task_query

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
