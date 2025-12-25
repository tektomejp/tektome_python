from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AggregatedUsageByModel")


@_attrs_define
class AggregatedUsageByModel:
    """
    Attributes:
        model (str):
        total_request_tokens (int):
        total_response_tokens (int):
        total_cost_sum (float):
        total_tokens_sum (float):
    """

    model: str
    total_request_tokens: int
    total_response_tokens: int
    total_cost_sum: float
    total_tokens_sum: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        total_request_tokens = self.total_request_tokens

        total_response_tokens = self.total_response_tokens

        total_cost_sum = self.total_cost_sum

        total_tokens_sum = self.total_tokens_sum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "total_request_tokens": total_request_tokens,
                "total_response_tokens": total_response_tokens,
                "total_cost_sum": total_cost_sum,
                "total_tokens_sum": total_tokens_sum,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        total_request_tokens = d.pop("total_request_tokens")

        total_response_tokens = d.pop("total_response_tokens")

        total_cost_sum = d.pop("total_cost_sum")

        total_tokens_sum = d.pop("total_tokens_sum")

        aggregated_usage_by_model = cls(
            model=model,
            total_request_tokens=total_request_tokens,
            total_response_tokens=total_response_tokens,
            total_cost_sum=total_cost_sum,
            total_tokens_sum=total_tokens_sum,
        )

        aggregated_usage_by_model.additional_properties = d
        return aggregated_usage_by_model

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
