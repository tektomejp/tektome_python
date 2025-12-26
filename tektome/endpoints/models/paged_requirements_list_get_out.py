from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.requirements_list_get_out import RequirementsListGetOut


T = TypeVar("T", bound="PagedRequirementsListGetOut")


@_attrs_define
class PagedRequirementsListGetOut:
    """
    Attributes:
        count (int):
        total_page (int):
        items (list[RequirementsListGetOut]):
    """

    count: int
    total_page: int
    items: list[RequirementsListGetOut]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        total_page = self.total_page

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "total_page": total_page,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.requirements_list_get_out import RequirementsListGetOut

        d = dict(src_dict)
        count = d.pop("count")

        total_page = d.pop("total_page")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = RequirementsListGetOut.from_dict(items_item_data)

            items.append(items_item)

        paged_requirements_list_get_out = cls(
            count=count,
            total_page=total_page,
            items=items,
        )

        paged_requirements_list_get_out.additional_properties = d
        return paged_requirements_list_get_out

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
