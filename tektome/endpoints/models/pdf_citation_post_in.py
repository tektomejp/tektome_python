from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.literal_attribute_type import LiteralAttributeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_polygons import ImagePolygons
    from ..models.text_highlights import TextHighlights


T = TypeVar("T", bound="PDFCitationPostIn")


@_attrs_define
class PDFCitationPostIn:
    """
    Attributes:
        title (str):
        extracted_attribute_id (UUID):
        extracted_attribute_type (LiteralAttributeType):
        section_id (UUID):
        attribute_sources (list[UUID]):
        text_highlights (list[TextHighlights]):
        image_polygons (list[ImagePolygons]):
        description (None | str | Unset):
    """

    title: str
    extracted_attribute_id: UUID
    extracted_attribute_type: LiteralAttributeType
    section_id: UUID
    attribute_sources: list[UUID]
    text_highlights: list[TextHighlights]
    image_polygons: list[ImagePolygons]
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        extracted_attribute_id = str(self.extracted_attribute_id)

        extracted_attribute_type = self.extracted_attribute_type.value

        section_id = str(self.section_id)

        attribute_sources = []
        for attribute_sources_item_data in self.attribute_sources:
            attribute_sources_item = str(attribute_sources_item_data)
            attribute_sources.append(attribute_sources_item)

        text_highlights = []
        for text_highlights_item_data in self.text_highlights:
            text_highlights_item = text_highlights_item_data.to_dict()
            text_highlights.append(text_highlights_item)

        image_polygons = []
        for image_polygons_item_data in self.image_polygons:
            image_polygons_item = image_polygons_item_data.to_dict()
            image_polygons.append(image_polygons_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "extracted_attribute_id": extracted_attribute_id,
                "extracted_attribute_type": extracted_attribute_type,
                "section_id": section_id,
                "attribute_sources": attribute_sources,
                "text_highlights": text_highlights,
                "image_polygons": image_polygons,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_polygons import ImagePolygons
        from ..models.text_highlights import TextHighlights

        d = dict(src_dict)
        title = d.pop("title")

        extracted_attribute_id = UUID(d.pop("extracted_attribute_id"))

        extracted_attribute_type = LiteralAttributeType(d.pop("extracted_attribute_type"))

        section_id = UUID(d.pop("section_id"))

        attribute_sources = []
        _attribute_sources = d.pop("attribute_sources")
        for attribute_sources_item_data in _attribute_sources:
            attribute_sources_item = UUID(attribute_sources_item_data)

            attribute_sources.append(attribute_sources_item)

        text_highlights = []
        _text_highlights = d.pop("text_highlights")
        for text_highlights_item_data in _text_highlights:
            text_highlights_item = TextHighlights.from_dict(text_highlights_item_data)

            text_highlights.append(text_highlights_item)

        image_polygons = []
        _image_polygons = d.pop("image_polygons")
        for image_polygons_item_data in _image_polygons:
            image_polygons_item = ImagePolygons.from_dict(image_polygons_item_data)

            image_polygons.append(image_polygons_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        pdf_citation_post_in = cls(
            title=title,
            extracted_attribute_id=extracted_attribute_id,
            extracted_attribute_type=extracted_attribute_type,
            section_id=section_id,
            attribute_sources=attribute_sources,
            text_highlights=text_highlights,
            image_polygons=image_polygons,
            description=description,
        )

        pdf_citation_post_in.additional_properties = d
        return pdf_citation_post_in

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
