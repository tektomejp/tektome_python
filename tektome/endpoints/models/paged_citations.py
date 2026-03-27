from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attribute_citations_response import AttributeCitationsResponse
    from ..models.bim_citations_response import BIMCitationsResponse
    from ..models.image_citations_response import ImageCitationsResponse
    from ..models.pdf_citations_response import PDFCitationsResponse
    from ..models.raw_text_citations_response import RawTextCitationsResponse


T = TypeVar("T", bound="PagedCitations")


@_attrs_define
class PagedCitations:
    """
    Attributes:
        count (int):
        total_page (int):
        items (list[AttributeCitationsResponse | BIMCitationsResponse | ImageCitationsResponse | PDFCitationsResponse |
            RawTextCitationsResponse]):
    """

    count: int
    total_page: int
    items: list[
        AttributeCitationsResponse
        | BIMCitationsResponse
        | ImageCitationsResponse
        | PDFCitationsResponse
        | RawTextCitationsResponse
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bim_citations_response import BIMCitationsResponse
        from ..models.image_citations_response import ImageCitationsResponse
        from ..models.pdf_citations_response import PDFCitationsResponse
        from ..models.raw_text_citations_response import RawTextCitationsResponse

        count = self.count

        total_page = self.total_page

        items = []
        for items_item_data in self.items:
            items_item: dict[str, Any]
            if isinstance(items_item_data, PDFCitationsResponse):
                items_item = items_item_data.to_dict()
            elif isinstance(items_item_data, RawTextCitationsResponse):
                items_item = items_item_data.to_dict()
            elif isinstance(items_item_data, BIMCitationsResponse):
                items_item = items_item_data.to_dict()
            elif isinstance(items_item_data, ImageCitationsResponse):
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
        from ..models.attribute_citations_response import AttributeCitationsResponse
        from ..models.bim_citations_response import BIMCitationsResponse
        from ..models.image_citations_response import ImageCitationsResponse
        from ..models.pdf_citations_response import PDFCitationsResponse
        from ..models.raw_text_citations_response import RawTextCitationsResponse

        d = dict(src_dict)
        count = d.pop("count")

        total_page = d.pop("total_page")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:

            def _parse_items_item(
                data: object,
            ) -> (
                AttributeCitationsResponse
                | BIMCitationsResponse
                | ImageCitationsResponse
                | PDFCitationsResponse
                | RawTextCitationsResponse
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_citations_type_0 = PDFCitationsResponse.from_dict(data)

                    return componentsschemas_citations_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_citations_type_1 = RawTextCitationsResponse.from_dict(data)

                    return componentsschemas_citations_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_citations_type_2 = BIMCitationsResponse.from_dict(data)

                    return componentsschemas_citations_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_citations_type_3 = ImageCitationsResponse.from_dict(data)

                    return componentsschemas_citations_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_citations_type_4 = AttributeCitationsResponse.from_dict(data)

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
