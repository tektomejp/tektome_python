from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_resource_user_aids_pdf_get_out_page_polygons import GetResourceUserAidsPDFGetOutPagePolygons
    from ..models.get_resource_user_aids_pdf_get_out_text_highlights_type_0 import (
        GetResourceUserAidsPDFGetOutTextHighlightsType0,
    )


T = TypeVar("T", bound="GetResourceUserAidsPDFGetOut")


@_attrs_define
class GetResourceUserAidsPDFGetOut:
    """
    Attributes:
        title (str): Title of the citation
        text_highlights (GetResourceUserAidsPDFGetOutTextHighlightsType0 | None): Text highlights as UUID mapped to list
            of highlights.
        page_polygons (GetResourceUserAidsPDFGetOutPagePolygons): Polygon highlights as Page UUID mapped to list of
            polygons.
    """

    title: str
    text_highlights: GetResourceUserAidsPDFGetOutTextHighlightsType0 | None
    page_polygons: GetResourceUserAidsPDFGetOutPagePolygons
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_resource_user_aids_pdf_get_out_text_highlights_type_0 import (
            GetResourceUserAidsPDFGetOutTextHighlightsType0,
        )

        title = self.title

        text_highlights: dict[str, Any] | None
        if isinstance(self.text_highlights, GetResourceUserAidsPDFGetOutTextHighlightsType0):
            text_highlights = self.text_highlights.to_dict()
        else:
            text_highlights = self.text_highlights

        page_polygons = self.page_polygons.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "text_highlights": text_highlights,
                "page_polygons": page_polygons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_resource_user_aids_pdf_get_out_page_polygons import GetResourceUserAidsPDFGetOutPagePolygons
        from ..models.get_resource_user_aids_pdf_get_out_text_highlights_type_0 import (
            GetResourceUserAidsPDFGetOutTextHighlightsType0,
        )

        d = dict(src_dict)
        title = d.pop("title")

        def _parse_text_highlights(data: object) -> GetResourceUserAidsPDFGetOutTextHighlightsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                text_highlights_type_0 = GetResourceUserAidsPDFGetOutTextHighlightsType0.from_dict(data)

                return text_highlights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetResourceUserAidsPDFGetOutTextHighlightsType0 | None, data)

        text_highlights = _parse_text_highlights(d.pop("text_highlights"))

        page_polygons = GetResourceUserAidsPDFGetOutPagePolygons.from_dict(d.pop("page_polygons"))

        get_resource_user_aids_pdf_get_out = cls(
            title=title,
            text_highlights=text_highlights,
            page_polygons=page_polygons,
        )

        get_resource_user_aids_pdf_get_out.additional_properties = d
        return get_resource_user_aids_pdf_get_out

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
