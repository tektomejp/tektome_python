from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BimKeyValueSearchPostIn")


@_attrs_define
class BimKeyValueSearchPostIn:
    """Schema for key-value search in BIM file_content JSON.

    Supports wildcard patterns using '*':
    - key="*" matches any key name
    - value="prefix*" matches values starting with "prefix"
    - value="*suffix" matches values ending with "suffix"
    - value="*middle*" matches values containing "middle"

        Attributes:
            key (str): Key to search for (supports * wildcard)
            value (str): Value to search for (supports * wildcard)
            fields (list[str] | None | Unset): Fields to return from file_content (default: ['id', 'name'])
            page (int | Unset):  Default: 1.
            page_size (int | Unset):  Default: 10.
    """

    key: str
    value: str
    fields: list[str] | None | Unset = UNSET
    page: int | Unset = 1
    page_size: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        fields: list[str] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = self.fields

        else:
            fields = self.fields

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value")

        def _parse_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = cast(list[str], data)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))

        page = d.pop("page", UNSET)

        page_size = d.pop("page_size", UNSET)

        bim_key_value_search_post_in = cls(
            key=key,
            value=value,
            fields=fields,
            page=page,
            page_size=page_size,
        )

        bim_key_value_search_post_in.additional_properties = d
        return bim_key_value_search_post_in

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
