from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute_patch_in_patch_value_type_7 import AttributePatchInPatchValueType7


T = TypeVar("T", bound="AttributePatchInPatch")


@_attrs_define
class AttributePatchInPatch:
    """
    Attributes:
        name (None | str | Unset):
        value (AttributePatchInPatchValueType7 | bool | datetime.date | datetime.datetime | float | int | list[Any] |
            None | str | Unset):
        is_locked (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    value: (
        AttributePatchInPatchValueType7
        | bool
        | datetime.date
        | datetime.datetime
        | float
        | int
        | list[Any]
        | None
        | str
        | Unset
    ) = UNSET
    is_locked: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attribute_patch_in_patch_value_type_7 import AttributePatchInPatchValueType7

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        value: bool | dict[str, Any] | float | int | list[Any] | None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, datetime.date):
            value = self.value.isoformat()
        elif isinstance(self.value, datetime.datetime):
            value = self.value.isoformat()
        elif isinstance(self.value, AttributePatchInPatchValueType7):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value

        else:
            value = self.value

        is_locked: bool | None | Unset
        if isinstance(self.is_locked, Unset):
            is_locked = UNSET
        else:
            is_locked = self.is_locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if is_locked is not UNSET:
            field_dict["is_locked"] = is_locked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_patch_in_patch_value_type_7 import AttributePatchInPatchValueType7

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_value(
            data: object,
        ) -> (
            AttributePatchInPatchValueType7
            | bool
            | datetime.date
            | datetime.datetime
            | float
            | int
            | list[Any]
            | None
            | str
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
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
                value_type_7 = AttributePatchInPatchValueType7.from_dict(data)

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
                AttributePatchInPatchValueType7
                | bool
                | datetime.date
                | datetime.datetime
                | float
                | int
                | list[Any]
                | None
                | str
                | Unset,
                data,
            )

        value = _parse_value(d.pop("value", UNSET))

        def _parse_is_locked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_locked = _parse_is_locked(d.pop("is_locked", UNSET))

        attribute_patch_in_patch = cls(
            name=name,
            value=value,
            is_locked=is_locked,
        )

        attribute_patch_in_patch.additional_properties = d
        return attribute_patch_in_patch

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
