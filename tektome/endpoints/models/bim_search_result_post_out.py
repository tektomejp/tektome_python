from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bim_search_item_result_post_out import BimSearchItemResultPostOut


T = TypeVar("T", bound="BimSearchResultPostOut")


@_attrs_define
class BimSearchResultPostOut:
    """
    Attributes:
        results (list[BimSearchItemResultPostOut]):
        total (int):
        page (int):
        page_size (int):
    """

    results: list[BimSearchItemResultPostOut]
    total: int
    page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "total": total,
                "page": page,
                "page_size": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bim_search_item_result_post_out import BimSearchItemResultPostOut

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = BimSearchItemResultPostOut.from_dict(results_item_data)

            results.append(results_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        bim_search_result_post_out = cls(
            results=results,
            total=total,
            page=page,
            page_size=page_size,
        )

        bim_search_result_post_out.additional_properties = d
        return bim_search_result_post_out

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
