from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="GenerateUsageReportPostOut")


@_attrs_define
class GenerateUsageReportPostOut:
    """
    Attributes:
        id (UUID):
        period (datetime.datetime):
        generated_on (datetime.datetime):
        tokens_used (str):
        is_current_month (bool):
        updated_by (None | UserMetadata):
    """

    id: UUID
    period: datetime.datetime
    generated_on: datetime.datetime
    tokens_used: str
    is_current_month: bool
    updated_by: None | UserMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_metadata import UserMetadata

        id = str(self.id)

        period = self.period.isoformat()

        generated_on = self.generated_on.isoformat()

        tokens_used = self.tokens_used

        is_current_month = self.is_current_month

        updated_by: dict[str, Any] | None
        if isinstance(self.updated_by, UserMetadata):
            updated_by = self.updated_by.to_dict()
        else:
            updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "period": period,
                "generated_on": generated_on,
                "tokens_used": tokens_used,
                "is_current_month": is_current_month,
                "updated_by": updated_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        period = isoparse(d.pop("period"))

        generated_on = isoparse(d.pop("generated_on"))

        tokens_used = d.pop("tokens_used")

        is_current_month = d.pop("is_current_month")

        def _parse_updated_by(data: object) -> None | UserMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_by_type_0 = UserMetadata.from_dict(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserMetadata, data)

        updated_by = _parse_updated_by(d.pop("updated_by"))

        generate_usage_report_post_out = cls(
            id=id,
            period=period,
            generated_on=generated_on,
            tokens_used=tokens_used,
            is_current_month=is_current_month,
            updated_by=updated_by,
        )

        generate_usage_report_post_out.additional_properties = d
        return generate_usage_report_post_out

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
