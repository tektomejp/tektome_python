from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute_get_out_value_type_7 import AttributeGetOutValueType7


T = TypeVar("T", bound="AttributeGetOut")


@_attrs_define
class AttributeGetOut:
    """Schema for getting an attribute.

    Attributes:
        name (str):
        value (AttributeGetOutValueType7 | bool | datetime.date | datetime.datetime | float | int | list[Any] | str):
        is_locked (bool): Whether the attribute is locked - can't be modified
        id (UUID):
        type_ (str):
        extraction_status (None | str | Unset):
        creation_method (None | str | Unset):
        error_message (None | str | Unset):
    """

    name: str
    value: AttributeGetOutValueType7 | bool | datetime.date | datetime.datetime | float | int | list[Any] | str
    is_locked: bool
    id: UUID
    type_: str
    extraction_status: None | str | Unset = UNSET
    creation_method: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attribute_get_out_value_type_7 import AttributeGetOutValueType7

        name = self.name

        value: bool | dict[str, Any] | float | int | list[Any] | str
        if isinstance(self.value, datetime.date):
            value = self.value.isoformat()
        elif isinstance(self.value, datetime.datetime):
            value = self.value.isoformat()
        elif isinstance(self.value, AttributeGetOutValueType7):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value

        else:
            value = self.value

        is_locked = self.is_locked

        id = str(self.id)

        type_ = self.type_

        extraction_status: None | str | Unset
        if isinstance(self.extraction_status, Unset):
            extraction_status = UNSET
        else:
            extraction_status = self.extraction_status

        creation_method: None | str | Unset
        if isinstance(self.creation_method, Unset):
            creation_method = UNSET
        else:
            creation_method = self.creation_method

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

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
        if extraction_status is not UNSET:
            field_dict["extraction_status"] = extraction_status
        if creation_method is not UNSET:
            field_dict["creation_method"] = creation_method
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_get_out_value_type_7 import AttributeGetOutValueType7

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_value(
            data: object,
        ) -> AttributeGetOutValueType7 | bool | datetime.date | datetime.datetime | float | int | list[Any] | str:
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
                value_type_7 = AttributeGetOutValueType7.from_dict(data)

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
                AttributeGetOutValueType7 | bool | datetime.date | datetime.datetime | float | int | list[Any] | str,
                data,
            )

        value = _parse_value(d.pop("value"))

        is_locked = d.pop("is_locked")

        id = UUID(d.pop("id"))

        type_ = d.pop("type")

        def _parse_extraction_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extraction_status = _parse_extraction_status(d.pop("extraction_status", UNSET))

        def _parse_creation_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        creation_method = _parse_creation_method(d.pop("creation_method", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        attribute_get_out = cls(
            name=name,
            value=value,
            is_locked=is_locked,
            id=id,
            type_=type_,
            extraction_status=extraction_status,
            creation_method=creation_method,
            error_message=error_message,
        )

        attribute_get_out.additional_properties = d
        return attribute_get_out

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
