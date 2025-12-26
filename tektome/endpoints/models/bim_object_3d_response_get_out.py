from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bim_object_3d_item_get_out import BimObject3DItemGetOut


T = TypeVar("T", bound="BimObject3DResponseGetOut")


@_attrs_define
class BimObject3DResponseGetOut:
    """Schema for the paginated BIM object 3D response.

    Attributes:
        results (list[BimObject3DItemGetOut]):
        total (int):
        page (int):
        page_size (int):
        total_pages (int):
    """

    results: list[BimObject3DItemGetOut]
    total: int
    page: int
    page_size: int
    total_pages: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        total_pages = self.total_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "total": total,
                "page": page,
                "page_size": page_size,
                "total_pages": total_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bim_object_3d_item_get_out import BimObject3DItemGetOut

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = BimObject3DItemGetOut.from_dict(results_item_data)

            results.append(results_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        total_pages = d.pop("total_pages")

        bim_object_3d_response_get_out = cls(
            results=results,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )

        bim_object_3d_response_get_out.additional_properties = d
        return bim_object_3d_response_get_out

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
