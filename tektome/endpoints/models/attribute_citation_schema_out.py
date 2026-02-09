from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.attribute_citation_schema_out_value_type_7 import AttributeCitationSchemaOutValueType7


T = TypeVar("T", bound="AttributeCitationSchemaOut")


@_attrs_define
class AttributeCitationSchemaOut:
    """
    Attributes:
        name (str):
        value (AttributeCitationSchemaOutValueType7 | bool | datetime.date | datetime.datetime | float | int | list[Any]
            | str):
        is_locked (bool): Whether the attribute is locked - can't be modified
        id (UUID):
        type_ (str):
    """

    name: str
    value: (
        AttributeCitationSchemaOutValueType7 | bool | datetime.date | datetime.datetime | float | int | list[Any] | str
    )
    is_locked: bool
    id: UUID
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attribute_citation_schema_out_value_type_7 import AttributeCitationSchemaOutValueType7

        name = self.name

        value: bool | dict[str, Any] | float | int | list[Any] | str
        if isinstance(self.value, datetime.date):
            value = self.value.isoformat()
        elif isinstance(self.value, datetime.datetime):
            value = self.value.isoformat()
        elif isinstance(self.value, AttributeCitationSchemaOutValueType7):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value

        else:
            value = self.value

        is_locked = self.is_locked

        id = str(self.id)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
                "is_locked": is_locked,
                "id": id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_citation_schema_out_value_type_7 import AttributeCitationSchemaOutValueType7

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_value(
            data: object,
        ) -> (
            AttributeCitationSchemaOutValueType7
            | bool
            | datetime.date
            | datetime.datetime
            | float
            | int
            | list[Any]
            | str
        ):
            try:
                if not isinstance(data, str):
                    raise TypeError()
                value_type_4 = isoparse(data).date()

                return value_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                value_type_5 = isoparse(data)

                return value_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_7 = AttributeCitationSchemaOutValueType7.from_dict(data)

                return value_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_8 = cast(list[Any], data)

                return value_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AttributeCitationSchemaOutValueType7
                | bool
                | datetime.date
                | datetime.datetime
                | float
                | int
                | list[Any]
                | str,
                data,
            )

        value = _parse_value(d.pop("value"))

        is_locked = d.pop("is_locked")

        id = UUID(d.pop("id"))

        type_ = d.pop("type")

        attribute_citation_schema_out = cls(
            name=name,
            value=value,
            is_locked=is_locked,
            id=id,
            type_=type_,
        )

        attribute_citation_schema_out.additional_properties = d
        return attribute_citation_schema_out

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
