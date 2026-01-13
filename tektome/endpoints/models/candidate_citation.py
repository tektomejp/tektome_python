from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.citation_kind import CitationKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.candidate_citation_bim_helpers_type_0 import CandidateCitationBimHelpersType0
    from ..models.candidate_citation_highlights_type_0 import CandidateCitationHighlightsType0
    from ..models.candidate_citation_polygons_type_0 import CandidateCitationPolygonsType0


T = TypeVar("T", bound="CandidateCitation")


@_attrs_define
class CandidateCitation:
    """
    Attributes:
        title (str): Citation title.
        kind (CitationKind):
        resource_id (None | Unset | UUID): ID of the cited resource of type Resource
        image_id (None | Unset | UUID): ID of the cited image of type Resource
        polygons (CandidateCitationPolygonsType0 | None | Unset):
        highlights (CandidateCitationHighlightsType0 | None | Unset):
        bim_project_id (None | Unset | UUID):
        bim_helpers (CandidateCitationBimHelpersType0 | None | Unset):
    """

    title: str
    kind: CitationKind
    resource_id: None | Unset | UUID = UNSET
    image_id: None | Unset | UUID = UNSET
    polygons: CandidateCitationPolygonsType0 | None | Unset = UNSET
    highlights: CandidateCitationHighlightsType0 | None | Unset = UNSET
    bim_project_id: None | Unset | UUID = UNSET
    bim_helpers: CandidateCitationBimHelpersType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.candidate_citation_bim_helpers_type_0 import CandidateCitationBimHelpersType0
        from ..models.candidate_citation_highlights_type_0 import CandidateCitationHighlightsType0
        from ..models.candidate_citation_polygons_type_0 import CandidateCitationPolygonsType0

        title = self.title

        kind = self.kind.value

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        elif isinstance(self.resource_id, UUID):
            resource_id = str(self.resource_id)
        else:
            resource_id = self.resource_id

        image_id: None | str | Unset
        if isinstance(self.image_id, Unset):
            image_id = UNSET
        elif isinstance(self.image_id, UUID):
            image_id = str(self.image_id)
        else:
            image_id = self.image_id

        polygons: dict[str, Any] | None | Unset
        if isinstance(self.polygons, Unset):
            polygons = UNSET
        elif isinstance(self.polygons, CandidateCitationPolygonsType0):
            polygons = self.polygons.to_dict()
        else:
            polygons = self.polygons

        highlights: dict[str, Any] | None | Unset
        if isinstance(self.highlights, Unset):
            highlights = UNSET
        elif isinstance(self.highlights, CandidateCitationHighlightsType0):
            highlights = self.highlights.to_dict()
        else:
            highlights = self.highlights

        bim_project_id: None | str | Unset
        if isinstance(self.bim_project_id, Unset):
            bim_project_id = UNSET
        elif isinstance(self.bim_project_id, UUID):
            bim_project_id = str(self.bim_project_id)
        else:
            bim_project_id = self.bim_project_id

        bim_helpers: dict[str, Any] | None | Unset
        if isinstance(self.bim_helpers, Unset):
            bim_helpers = UNSET
        elif isinstance(self.bim_helpers, CandidateCitationBimHelpersType0):
            bim_helpers = self.bim_helpers.to_dict()
        else:
            bim_helpers = self.bim_helpers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "kind": kind,
            }
        )
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if image_id is not UNSET:
            field_dict["image_id"] = image_id
        if polygons is not UNSET:
            field_dict["polygons"] = polygons
        if highlights is not UNSET:
            field_dict["highlights"] = highlights
        if bim_project_id is not UNSET:
            field_dict["bim_project_id"] = bim_project_id
        if bim_helpers is not UNSET:
            field_dict["bim_helpers"] = bim_helpers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.candidate_citation_bim_helpers_type_0 import CandidateCitationBimHelpersType0
        from ..models.candidate_citation_highlights_type_0 import CandidateCitationHighlightsType0
        from ..models.candidate_citation_polygons_type_0 import CandidateCitationPolygonsType0

        d = dict(src_dict)
        title = d.pop("title")

        kind = CitationKind(d.pop("kind"))

        def _parse_resource_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resource_id_type_0 = UUID(data)

                return resource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        resource_id = _parse_resource_id(d.pop("resource_id", UNSET))

        def _parse_image_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                image_id_type_0 = UUID(data)

                return image_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        image_id = _parse_image_id(d.pop("image_id", UNSET))

        def _parse_polygons(data: object) -> CandidateCitationPolygonsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                polygons_type_0 = CandidateCitationPolygonsType0.from_dict(data)

                return polygons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CandidateCitationPolygonsType0 | None | Unset, data)

        polygons = _parse_polygons(d.pop("polygons", UNSET))

        def _parse_highlights(data: object) -> CandidateCitationHighlightsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                highlights_type_0 = CandidateCitationHighlightsType0.from_dict(data)

                return highlights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CandidateCitationHighlightsType0 | None | Unset, data)

        highlights = _parse_highlights(d.pop("highlights", UNSET))

        def _parse_bim_project_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bim_project_id_type_0 = UUID(data)

                return bim_project_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bim_project_id = _parse_bim_project_id(d.pop("bim_project_id", UNSET))

        def _parse_bim_helpers(data: object) -> CandidateCitationBimHelpersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bim_helpers_type_0 = CandidateCitationBimHelpersType0.from_dict(data)

                return bim_helpers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CandidateCitationBimHelpersType0 | None | Unset, data)

        bim_helpers = _parse_bim_helpers(d.pop("bim_helpers", UNSET))

        candidate_citation = cls(
            title=title,
            kind=kind,
            resource_id=resource_id,
            image_id=image_id,
            polygons=polygons,
            highlights=highlights,
            bim_project_id=bim_project_id,
            bim_helpers=bim_helpers,
        )

        candidate_citation.additional_properties = d
        return candidate_citation

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
