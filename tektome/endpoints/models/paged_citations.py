from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attribute_citations_get_out import AttributeCitationsGetOut
    from ..models.bim_citations_get_out import BIMCitationsGetOut
    from ..models.image_citations_get_out import ImageCitationsGetOut
    from ..models.pdf_citations_get_out import PDFCitationsGetOut
    from ..models.raw_text_citations_get_out import RawTextCitationsGetOut


T = TypeVar("T", bound="PagedCitations")


@_attrs_define
class PagedCitations:
    """
    Attributes:
        count (int):
        total_page (int):
        items (list[AttributeCitationsGetOut | BIMCitationsGetOut | ImageCitationsGetOut | PDFCitationsGetOut |
            RawTextCitationsGetOut]):
    """

    count: int
    total_page: int
    items: list[
        AttributeCitationsGetOut
        | BIMCitationsGetOut
        | ImageCitationsGetOut
        | PDFCitationsGetOut
        | RawTextCitationsGetOut
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bim_citations_get_out import BIMCitationsGetOut
        from ..models.image_citations_get_out import ImageCitationsGetOut
        from ..models.pdf_citations_get_out import PDFCitationsGetOut
        from ..models.raw_text_citations_get_out import RawTextCitationsGetOut

        count = self.count

        total_page = self.total_page

        items = []
        for items_item_data in self.items:
            items_item: dict[str, Any]
            if isinstance(items_item_data, PDFCitationsGetOut):
                items_item = items_item_data.to_dict()
            elif isinstance(items_item_data, RawTextCitationsGetOut):
                items_item = items_item_data.to_dict()
            elif isinstance(items_item_data, BIMCitationsGetOut):
                items_item = items_item_data.to_dict()
            elif isinstance(items_item_data, ImageCitationsGetOut):
                items_item = items_item_data.to_dict()
            else:
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
        from ..models.attribute_citations_get_out import AttributeCitationsGetOut
        from ..models.bim_citations_get_out import BIMCitationsGetOut
        from ..models.image_citations_get_out import ImageCitationsGetOut
        from ..models.pdf_citations_get_out import PDFCitationsGetOut
        from ..models.raw_text_citations_get_out import RawTextCitationsGetOut

        d = dict(src_dict)
        count = d.pop("count")

        total_page = d.pop("total_page")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:

            def _parse_items_item(
                data: object,
            ) -> (
                AttributeCitationsGetOut
                | BIMCitationsGetOut
                | ImageCitationsGetOut
                | PDFCitationsGetOut
                | RawTextCitationsGetOut
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_citations_type_0 = PDFCitationsGetOut.from_dict(data)

                    return componentsschemas_citations_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_citations_type_1 = RawTextCitationsGetOut.from_dict(data)

                    return componentsschemas_citations_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_citations_type_2 = BIMCitationsGetOut.from_dict(data)

                    return componentsschemas_citations_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_citations_type_3 = ImageCitationsGetOut.from_dict(data)

                    return componentsschemas_citations_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_citations_type_4 = AttributeCitationsGetOut.from_dict(data)

                return componentsschemas_citations_type_4

            items_item = _parse_items_item(items_item_data)

            items.append(items_item)

        paged_citations = cls(
            count=count,
            total_page=total_page,
            items=items,
        )

        paged_citations.additional_properties = d
        return paged_citations

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
