from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BimSearchDetailPostIn")


@_attrs_define
class BimSearchDetailPostIn:
    """Schema for BIM search query payload.

    Attributes:
        element_id (None | str | Unset):
        content_query (None | str | Unset):
        exact_match (bool | None | Unset):
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
    """

    element_id: None | str | Unset = UNSET
    content_query: None | str | Unset = UNSET
    exact_match: bool | None | Unset = UNSET
    limit: int | Unset = 10
    page: int | Unset = 1
    page_size: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_id: None | str | Unset
        if isinstance(self.element_id, Unset):
            element_id = UNSET
        else:
            element_id = self.element_id

        content_query: None | str | Unset
        if isinstance(self.content_query, Unset):
            content_query = UNSET
        else:
            content_query = self.content_query

        exact_match: bool | None | Unset
        if isinstance(self.exact_match, Unset):
            exact_match = UNSET
        else:
            exact_match = self.exact_match

        limit = self.limit

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if element_id is not UNSET:
            field_dict["element_id"] = element_id
        if content_query is not UNSET:
            field_dict["content_query"] = content_query
        if exact_match is not UNSET:
            field_dict["exact_match"] = exact_match
        if limit is not UNSET:
            field_dict["limit"] = limit
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_element_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        element_id = _parse_element_id(d.pop("element_id", UNSET))

        def _parse_content_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_query = _parse_content_query(d.pop("content_query", UNSET))

        def _parse_exact_match(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exact_match = _parse_exact_match(d.pop("exact_match", UNSET))

        limit = d.pop("limit", UNSET)

        page = d.pop("page", UNSET)

        page_size = d.pop("page_size", UNSET)

        bim_search_detail_post_in = cls(
            element_id=element_id,
            content_query=content_query,
            exact_match=exact_match,
            limit=limit,
            page=page,
            page_size=page_size,
        )

        bim_search_detail_post_in.additional_properties = d
        return bim_search_detail_post_in

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
