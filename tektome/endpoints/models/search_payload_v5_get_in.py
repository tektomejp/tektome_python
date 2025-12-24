from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchPayloadV5GetIn")


@_attrs_define
class SearchPayloadV5GetIn:
    """
    Attributes:
        query (str):
        keywords (list[str] | Unset):
        resource_group_ids (list[UUID] | Unset):
        top_k (int | Unset):  Default: 30.
        skip (int | Unset):  Default: 0.
        sort_by_pages (bool | Unset):  Default: False.
    """

    query: str
    keywords: list[str] | Unset = UNSET
    resource_group_ids: list[UUID] | Unset = UNSET
    top_k: int | Unset = 30
    skip: int | Unset = 0
    sort_by_pages: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        resource_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.resource_group_ids, Unset):
            resource_group_ids = []
            for resource_group_ids_item_data in self.resource_group_ids:
                resource_group_ids_item = str(resource_group_ids_item_data)
                resource_group_ids.append(resource_group_ids_item)

        top_k = self.top_k

        skip = self.skip

        sort_by_pages = self.sort_by_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if resource_group_ids is not UNSET:
            field_dict["resource_group_ids"] = resource_group_ids
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if skip is not UNSET:
            field_dict["skip"] = skip
        if sort_by_pages is not UNSET:
            field_dict["sort_by_pages"] = sort_by_pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        keywords = cast(list[str], d.pop("keywords", UNSET))

        _resource_group_ids = d.pop("resource_group_ids", UNSET)
        resource_group_ids: list[UUID] | Unset = UNSET
        if _resource_group_ids is not UNSET:
            resource_group_ids = []
            for resource_group_ids_item_data in _resource_group_ids:
                resource_group_ids_item = UUID(resource_group_ids_item_data)

                resource_group_ids.append(resource_group_ids_item)

        top_k = d.pop("top_k", UNSET)

        skip = d.pop("skip", UNSET)

        sort_by_pages = d.pop("sort_by_pages", UNSET)

        search_payload_v5_get_in = cls(
            query=query,
            keywords=keywords,
            resource_group_ids=resource_group_ids,
            top_k=top_k,
            skip=skip,
            sort_by_pages=sort_by_pages,
        )

        search_payload_v5_get_in.additional_properties = d
        return search_payload_v5_get_in

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
