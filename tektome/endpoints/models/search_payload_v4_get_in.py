from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchPayloadV4GetIn")


@_attrs_define
class SearchPayloadV4GetIn:
    """
    Attributes:
        query (str):
        keyword (None | str | Unset):
        top_k (int | Unset):  Default: 30.
        skip (int | Unset):  Default: 0.
        sort_by_pages (bool | Unset):  Default: False.
        debug (bool | Unset):  Default: False.
    """

    query: str
    keyword: None | str | Unset = UNSET
    top_k: int | Unset = 30
    skip: int | Unset = 0
    sort_by_pages: bool | Unset = False
    debug: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        keyword: None | str | Unset
        if isinstance(self.keyword, Unset):
            keyword = UNSET
        else:
            keyword = self.keyword

        top_k = self.top_k

        skip = self.skip

        sort_by_pages = self.sort_by_pages

        debug = self.debug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if skip is not UNSET:
            field_dict["skip"] = skip
        if sort_by_pages is not UNSET:
            field_dict["sort_by_pages"] = sort_by_pages
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        def _parse_keyword(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keyword = _parse_keyword(d.pop("keyword", UNSET))

        top_k = d.pop("top_k", UNSET)

        skip = d.pop("skip", UNSET)

        sort_by_pages = d.pop("sort_by_pages", UNSET)

        debug = d.pop("debug", UNSET)

        search_payload_v4_get_in = cls(
            query=query,
            keyword=keyword,
            top_k=top_k,
            skip=skip,
            sort_by_pages=sort_by_pages,
            debug=debug,
        )

        search_payload_v4_get_in.additional_properties = d
        return search_payload_v4_get_in

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
