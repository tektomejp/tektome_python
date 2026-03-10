from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateAttributeSchemaOut")


@_attrs_define
class DateAttributeSchemaOut:
    """
    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        name (str):
        id (None | Unset | UUID):
        extraction_status (None | str | Unset):  Default: 'pending'.
        creation_method (None | str | Unset):  Default: 'automatic'.
        error_message (None | str | Unset):
        extraction_reasoning (None | str | Unset):
        is_locked (bool | Unset): Indicates whether the attribute is locked from further edits. Default: False.
        value (datetime.date | None | Unset):
    """

    created: datetime.datetime
    updated: datetime.datetime
    name: str
    id: None | Unset | UUID = UNSET
    extraction_status: None | str | Unset = "pending"
    creation_method: None | str | Unset = "automatic"
    error_message: None | str | Unset = UNSET
    extraction_reasoning: None | str | Unset = UNSET
    is_locked: bool | Unset = False
    value: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.isoformat()

        updated = self.updated.isoformat()

        name = self.name

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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

        extraction_reasoning: None | str | Unset
        if isinstance(self.extraction_reasoning, Unset):
            extraction_reasoning = UNSET
        else:
            extraction_reasoning = self.extraction_reasoning

        is_locked = self.is_locked

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, datetime.date):
            value = self.value.isoformat()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if extraction_status is not UNSET:
            field_dict["extraction_status"] = extraction_status
        if creation_method is not UNSET:
            field_dict["creation_method"] = creation_method
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if extraction_reasoning is not UNSET:
            field_dict["extraction_reasoning"] = extraction_reasoning
        if is_locked is not UNSET:
            field_dict["is_locked"] = is_locked
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        name = d.pop("name")

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

        def _parse_extraction_reasoning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extraction_reasoning = _parse_extraction_reasoning(d.pop("extraction_reasoning", UNSET))

        is_locked = d.pop("is_locked", UNSET)

        def _parse_value(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                value_type_0 = isoparse(data).date()

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        date_attribute_schema_out = cls(
            created=created,
            updated=updated,
            name=name,
            id=id,
            extraction_status=extraction_status,
            creation_method=creation_method,
            error_message=error_message,
            extraction_reasoning=extraction_reasoning,
            is_locked=is_locked,
            value=value,
        )

        date_attribute_schema_out.additional_properties = d
        return date_attribute_schema_out

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
