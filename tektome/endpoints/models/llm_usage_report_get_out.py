from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LLMUsageReportGetOut")


@_attrs_define
class LLMUsageReportGetOut:
    """
    Attributes:
        generated_on (datetime.datetime):
        tokens_used (str):
        period (datetime.datetime):
        id (None | Unset | UUID):
    """

    generated_on: datetime.datetime
    tokens_used: str
    period: datetime.datetime
    id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        generated_on = self.generated_on.isoformat()

        tokens_used = self.tokens_used

        period = self.period.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "generated_on": generated_on,
                "tokens_used": tokens_used,
                "period": period,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        generated_on = isoparse(d.pop("generated_on"))

        tokens_used = d.pop("tokens_used")

        period = isoparse(d.pop("period"))

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

        llm_usage_report_get_out = cls(
            generated_on=generated_on,
            tokens_used=tokens_used,
            period=period,
            id=id,
        )

        llm_usage_report_get_out.additional_properties = d
        return llm_usage_report_get_out

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
