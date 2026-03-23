from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bim_helpers import BIMHelpers
    from ..models.bim_text_highlights import BIMTextHighlights
    from ..models.image_polygons import ImagePolygons
    from ..models.text_highlights import TextHighlights


T = TypeVar("T", bound="BIMCitationPatchInPatch")


@_attrs_define
class BIMCitationPatchInPatch:
    """
    Attributes:
        title (None | str):
        description (None | str | Unset):
        keywords (None | str | Unset):
        section_id (None | Unset | UUID):
        attribute_sources (list[str] | None | Unset):
        text_highlights (list[TextHighlights] | None | Unset):
        image_polygons (list[ImagePolygons] | None | Unset):
        bim_text_highlights (list[BIMTextHighlights] | None | Unset):
        bim_helpers (list[BIMHelpers] | None | Unset):
    """

    title: None | str
    description: None | str | Unset = UNSET
    keywords: None | str | Unset = UNSET
    section_id: None | Unset | UUID = UNSET
    attribute_sources: list[str] | None | Unset = UNSET
    text_highlights: list[TextHighlights] | None | Unset = UNSET
    image_polygons: list[ImagePolygons] | None | Unset = UNSET
    bim_text_highlights: list[BIMTextHighlights] | None | Unset = UNSET
    bim_helpers: list[BIMHelpers] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: None | str
        title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        keywords: None | str | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        else:
            keywords = self.keywords

        section_id: None | str | Unset
        if isinstance(self.section_id, Unset):
            section_id = UNSET
        elif isinstance(self.section_id, UUID):
            section_id = str(self.section_id)
        else:
            section_id = self.section_id

        attribute_sources: list[str] | None | Unset
        if isinstance(self.attribute_sources, Unset):
            attribute_sources = UNSET
        elif isinstance(self.attribute_sources, list):
            attribute_sources = self.attribute_sources

        else:
            attribute_sources = self.attribute_sources

        text_highlights: list[dict[str, Any]] | None | Unset
        if isinstance(self.text_highlights, Unset):
            text_highlights = UNSET
        elif isinstance(self.text_highlights, list):
            text_highlights = []
            for text_highlights_type_0_item_data in self.text_highlights:
                text_highlights_type_0_item = text_highlights_type_0_item_data.to_dict()
                text_highlights.append(text_highlights_type_0_item)

        else:
            text_highlights = self.text_highlights

        image_polygons: list[dict[str, Any]] | None | Unset
        if isinstance(self.image_polygons, Unset):
            image_polygons = UNSET
        elif isinstance(self.image_polygons, list):
            image_polygons = []
            for image_polygons_type_0_item_data in self.image_polygons:
                image_polygons_type_0_item = image_polygons_type_0_item_data.to_dict()
                image_polygons.append(image_polygons_type_0_item)

        else:
            image_polygons = self.image_polygons

        bim_text_highlights: list[dict[str, Any]] | None | Unset
        if isinstance(self.bim_text_highlights, Unset):
            bim_text_highlights = UNSET
        elif isinstance(self.bim_text_highlights, list):
            bim_text_highlights = []
            for bim_text_highlights_type_0_item_data in self.bim_text_highlights:
                bim_text_highlights_type_0_item = bim_text_highlights_type_0_item_data.to_dict()
                bim_text_highlights.append(bim_text_highlights_type_0_item)

        else:
            bim_text_highlights = self.bim_text_highlights

        bim_helpers: list[dict[str, Any]] | None | Unset
        if isinstance(self.bim_helpers, Unset):
            bim_helpers = UNSET
        elif isinstance(self.bim_helpers, list):
            bim_helpers = []
            for bim_helpers_type_0_item_data in self.bim_helpers:
                bim_helpers_type_0_item = bim_helpers_type_0_item_data.to_dict()
                bim_helpers.append(bim_helpers_type_0_item)

        else:
            bim_helpers = self.bim_helpers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if section_id is not UNSET:
            field_dict["section_id"] = section_id
        if attribute_sources is not UNSET:
            field_dict["attribute_sources"] = attribute_sources
        if text_highlights is not UNSET:
            field_dict["text_highlights"] = text_highlights
        if image_polygons is not UNSET:
            field_dict["image_polygons"] = image_polygons
        if bim_text_highlights is not UNSET:
            field_dict["bim_text_highlights"] = bim_text_highlights
        if bim_helpers is not UNSET:
            field_dict["bim_helpers"] = bim_helpers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bim_helpers import BIMHelpers
        from ..models.bim_text_highlights import BIMTextHighlights
        from ..models.image_polygons import ImagePolygons
        from ..models.text_highlights import TextHighlights

        d = dict(src_dict)

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_keywords(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_section_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                section_id_type_0 = UUID(data)

                return section_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        section_id = _parse_section_id(d.pop("section_id", UNSET))

        def _parse_attribute_sources(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attribute_sources_type_0 = cast(list[str], data)

                return attribute_sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        attribute_sources = _parse_attribute_sources(d.pop("attribute_sources", UNSET))

        def _parse_text_highlights(data: object) -> list[TextHighlights] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                text_highlights_type_0 = []
                _text_highlights_type_0 = data
                for text_highlights_type_0_item_data in _text_highlights_type_0:
                    text_highlights_type_0_item = TextHighlights.from_dict(text_highlights_type_0_item_data)

                    text_highlights_type_0.append(text_highlights_type_0_item)

                return text_highlights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TextHighlights] | None | Unset, data)

        text_highlights = _parse_text_highlights(d.pop("text_highlights", UNSET))

        def _parse_image_polygons(data: object) -> list[ImagePolygons] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_polygons_type_0 = []
                _image_polygons_type_0 = data
                for image_polygons_type_0_item_data in _image_polygons_type_0:
                    image_polygons_type_0_item = ImagePolygons.from_dict(image_polygons_type_0_item_data)

                    image_polygons_type_0.append(image_polygons_type_0_item)

                return image_polygons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImagePolygons] | None | Unset, data)

        image_polygons = _parse_image_polygons(d.pop("image_polygons", UNSET))

        def _parse_bim_text_highlights(data: object) -> list[BIMTextHighlights] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bim_text_highlights_type_0 = []
                _bim_text_highlights_type_0 = data
                for bim_text_highlights_type_0_item_data in _bim_text_highlights_type_0:
                    bim_text_highlights_type_0_item = BIMTextHighlights.from_dict(bim_text_highlights_type_0_item_data)

                    bim_text_highlights_type_0.append(bim_text_highlights_type_0_item)

                return bim_text_highlights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BIMTextHighlights] | None | Unset, data)

        bim_text_highlights = _parse_bim_text_highlights(d.pop("bim_text_highlights", UNSET))

        def _parse_bim_helpers(data: object) -> list[BIMHelpers] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bim_helpers_type_0 = []
                _bim_helpers_type_0 = data
                for bim_helpers_type_0_item_data in _bim_helpers_type_0:
                    bim_helpers_type_0_item = BIMHelpers.from_dict(bim_helpers_type_0_item_data)

                    bim_helpers_type_0.append(bim_helpers_type_0_item)

                return bim_helpers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BIMHelpers] | None | Unset, data)

        bim_helpers = _parse_bim_helpers(d.pop("bim_helpers", UNSET))

        bim_citation_patch_in_patch = cls(
            title=title,
            description=description,
            keywords=keywords,
            section_id=section_id,
            attribute_sources=attribute_sources,
            text_highlights=text_highlights,
            image_polygons=image_polygons,
            bim_text_highlights=bim_text_highlights,
            bim_helpers=bim_helpers,
        )

        bim_citation_patch_in_patch.additional_properties = d
        return bim_citation_patch_in_patch

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
