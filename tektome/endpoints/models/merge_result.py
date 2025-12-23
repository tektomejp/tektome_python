from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merge_result_search_results_item import MergeResultSearchResultsItem


T = TypeVar("T", bound="MergeResult")


@_attrs_define
class MergeResult:
    """
    Attributes:
        search_results (list[MergeResultSearchResultsItem]):
        sort_by_pages (bool | Unset):  Default: False.
    """

    search_results: list[MergeResultSearchResultsItem]
    sort_by_pages: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_results = []
        for search_results_item_data in self.search_results:
            search_results_item = search_results_item_data.to_dict()
            search_results.append(search_results_item)

        sort_by_pages = self.sort_by_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "search_results": search_results,
            }
        )
        if sort_by_pages is not UNSET:
            field_dict["sort_by_pages"] = sort_by_pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.merge_result_search_results_item import MergeResultSearchResultsItem

        d = dict(src_dict)
        search_results = []
        _search_results = d.pop("search_results")
        for search_results_item_data in _search_results:
            search_results_item = MergeResultSearchResultsItem.from_dict(search_results_item_data)

            search_results.append(search_results_item)

        sort_by_pages = d.pop("sort_by_pages", UNSET)

        merge_result = cls(
            search_results=search_results,
            sort_by_pages=sort_by_pages,
        )

        merge_result.additional_properties = d
        return merge_result

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
