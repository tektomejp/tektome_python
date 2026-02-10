from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.attribute_extraction_status_choices import AttributeExtractionStatusChoices
from ..models.attribute_type import AttributeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_attribute_post_in_value_type_7 import ResourceAttributePostInValueType7


T = TypeVar("T", bound="ResourceAttributePostIn")


@_attrs_define
class ResourceAttributePostIn:
    """
    Attributes:
        name (str):
        value (bool | datetime.date | datetime.datetime | float | int | list[Any] | ResourceAttributePostInValueType7 |
            str):
        type_ (AttributeType): StrEnum for all available attribute types

            .. warning::
                Do not change the values of this enum, as they are used in the database.
                If you need to add a new attribute type, add a new enum value with a unique name.
        is_locked (bool | Unset):  Default: False.
        entity_id (None | Unset | UUID):
        extraction_status (AttributeExtractionStatusChoices | Unset):  Default:
            AttributeExtractionStatusChoices.PENDING_APPROVAL.
    """

    name: str
    value: bool | datetime.date | datetime.datetime | float | int | list[Any] | ResourceAttributePostInValueType7 | str
    type_: AttributeType
    is_locked: bool | Unset = False
    entity_id: None | Unset | UUID = UNSET
    extraction_status: AttributeExtractionStatusChoices | Unset = AttributeExtractionStatusChoices.PENDING_APPROVAL
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resource_attribute_post_in_value_type_7 import ResourceAttributePostInValueType7

        name = self.name

        value: bool | dict[str, Any] | float | int | list[Any] | str
        if isinstance(self.value, datetime.date):
            value = self.value.isoformat()
        elif isinstance(self.value, datetime.datetime):
            value = self.value.isoformat()
        elif isinstance(self.value, ResourceAttributePostInValueType7):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value

        else:
            value = self.value

        type_ = self.type_.value

        is_locked = self.is_locked

        entity_id: None | str | Unset
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        elif isinstance(self.entity_id, UUID):
            entity_id = str(self.entity_id)
        else:
            entity_id = self.entity_id

        extraction_status: str | Unset = UNSET
        if not isinstance(self.extraction_status, Unset):
            extraction_status = self.extraction_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
                "type": type_,
            }
        )
        if is_locked is not UNSET:
            field_dict["is_locked"] = is_locked
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if extraction_status is not UNSET:
            field_dict["extraction_status"] = extraction_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_attribute_post_in_value_type_7 import ResourceAttributePostInValueType7

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_value(
            data: object,
        ) -> (
            bool | datetime.date | datetime.datetime | float | int | list[Any] | ResourceAttributePostInValueType7 | str
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
                value_type_7 = ResourceAttributePostInValueType7.from_dict(data)

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
                bool
                | datetime.date
                | datetime.datetime
                | float
                | int
                | list[Any]
                | ResourceAttributePostInValueType7
                | str,
                data,
            )

        value = _parse_value(d.pop("value"))

        type_ = AttributeType(d.pop("type"))

        is_locked = d.pop("is_locked", UNSET)

        def _parse_entity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entity_id_type_0 = UUID(data)

                return entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

        _extraction_status = d.pop("extraction_status", UNSET)
        extraction_status: AttributeExtractionStatusChoices | Unset
        if isinstance(_extraction_status, Unset):
            extraction_status = UNSET
        else:
            extraction_status = AttributeExtractionStatusChoices(_extraction_status)

        resource_attribute_post_in = cls(
            name=name,
            value=value,
            type_=type_,
            is_locked=is_locked,
            entity_id=entity_id,
            extraction_status=extraction_status,
        )

        resource_attribute_post_in.additional_properties = d
        return resource_attribute_post_in

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
