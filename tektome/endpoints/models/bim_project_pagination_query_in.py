from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BimProjectPaginationQueryIn")


@_attrs_define
class BimProjectPaginationQueryIn:
    """Query schema for BIM project list/stat endpoints with bounded pagination.

    Reuses the shared `page` and `page_size` validation rules from
    `BoundedPaginationQueryIn`.

        Attributes:
            page (int | Unset):  Default: 1.
            page_size (int | Unset):  Default: 100.
    """

    page: int | Unset = 1
    page_size: int | Unset = 100
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page = d.pop("page", UNSET)

        page_size = d.pop("page_size", UNSET)

        bim_project_pagination_query_in = cls(
            page=page,
            page_size=page_size,
        )

        bim_project_pagination_query_in.additional_properties = d
        return bim_project_pagination_query_in

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
