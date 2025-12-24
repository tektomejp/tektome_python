from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.period_types import PeriodTypes

T = TypeVar("T", bound="LLMUsageReportQuery")


@_attrs_define
class LLMUsageReportQuery:
    """
    Attributes:
        organization_id (UUID):
        period_type (PeriodTypes):
    """

    organization_id: UUID
    period_type: PeriodTypes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id = str(self.organization_id)

        period_type = self.period_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_id": organization_id,
                "period_type": period_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_id = UUID(d.pop("organization_id"))

        period_type = PeriodTypes(d.pop("period_type"))

        llm_usage_report_query = cls(
            organization_id=organization_id,
            period_type=period_type,
        )

        llm_usage_report_query.additional_properties = d
        return llm_usage_report_query

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
