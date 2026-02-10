from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.entity_search_result_hit import EntitySearchResultHit


T = TypeVar("T", bound="PaginatedSearchResultHits")


@_attrs_define
class PaginatedSearchResultHits:
    """Paginated search result hits

    Attributes:
        items (list[EntitySearchResultHit]):
        count (int):
        total_page (int):
        page (int):
        page_size (int):
    """

    items: list[EntitySearchResultHit]
    count: int
    total_page: int
    page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        count = self.count

        total_page = self.total_page

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "count": count,
                "total_page": total_page,
                "page": page,
                "page_size": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_search_result_hit import EntitySearchResultHit

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = EntitySearchResultHit.from_dict(items_item_data)

            items.append(items_item)

        count = d.pop("count")

        total_page = d.pop("total_page")

        page = d.pop("page")

        page_size = d.pop("page_size")

        paginated_search_result_hits = cls(
            items=items,
            count=count,
            total_page=total_page,
            page=page,
            page_size=page_size,
        )

        paginated_search_result_hits.additional_properties = d
        return paginated_search_result_hits

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
