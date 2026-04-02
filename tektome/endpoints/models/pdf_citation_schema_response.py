from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pdf_citation_annotated_polygon_schema_response import PDFCitationAnnotatedPolygonSchemaResponse
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="PDFCitationSchemaResponse")


@_attrs_define
class PDFCitationSchemaResponse:
    """
    Attributes:
        polygons (list[PDFCitationAnnotatedPolygonSchemaResponse]):
        created_by (UserMetadata):
        updated_by (UserMetadata):
        created (datetime.datetime):
        updated (datetime.datetime):
        resource (UUID):
        citation_type (Literal['pdf_citation'] | Unset):  Default: 'pdf_citation'.
        id (None | Unset | UUID):
        title (str | Unset):  Default: ''.
        keywords (list[Any] | Unset): List of keywords that may or may not be present in the cited resource.
        overlay_html (None | str | Unset): Custom HTML content rendered as an overlay panel on the viewer (e.g. floating
            info panel on BIM/PDF viewer). Limited to 1MB in size. Note that this is unsanitized data.
    """

    polygons: list[PDFCitationAnnotatedPolygonSchemaResponse]
    created_by: UserMetadata
    updated_by: UserMetadata
    created: datetime.datetime
    updated: datetime.datetime
    resource: UUID
    citation_type: Literal["pdf_citation"] | Unset = "pdf_citation"
    id: None | Unset | UUID = UNSET
    title: str | Unset = ""
    keywords: list[Any] | Unset = UNSET
    overlay_html: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        polygons = []
        for polygons_item_data in self.polygons:
            polygons_item = polygons_item_data.to_dict()
            polygons.append(polygons_item)

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        resource = str(self.resource)

        citation_type = self.citation_type

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        title = self.title

        keywords: list[Any] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        overlay_html: None | str | Unset
        if isinstance(self.overlay_html, Unset):
            overlay_html = UNSET
        else:
            overlay_html = self.overlay_html

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "polygons": polygons,
                "created_by": created_by,
                "updated_by": updated_by,
                "created": created,
                "updated": updated,
                "resource": resource,
            }
        )
        if citation_type is not UNSET:
            field_dict["citation_type"] = citation_type
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if overlay_html is not UNSET:
            field_dict["overlay_html"] = overlay_html

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pdf_citation_annotated_polygon_schema_response import PDFCitationAnnotatedPolygonSchemaResponse
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        polygons = []
        _polygons = d.pop("polygons")
        for polygons_item_data in _polygons:
            polygons_item = PDFCitationAnnotatedPolygonSchemaResponse.from_dict(polygons_item_data)

            polygons.append(polygons_item)

        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        resource = UUID(d.pop("resource"))

        citation_type = cast(Literal["pdf_citation"] | Unset, d.pop("citation_type", UNSET))
        if citation_type != "pdf_citation" and not isinstance(citation_type, Unset):
            raise ValueError(f"citation_type must match const 'pdf_citation', got '{citation_type}'")

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        title = d.pop("title", UNSET)

        keywords = cast(list[Any], d.pop("keywords", UNSET))

        def _parse_overlay_html(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overlay_html = _parse_overlay_html(d.pop("overlay_html", UNSET))

        pdf_citation_schema_response = cls(
            polygons=polygons,
            created_by=created_by,
            updated_by=updated_by,
            created=created,
            updated=updated,
            resource=resource,
            citation_type=citation_type,
            id=id,
            title=title,
            keywords=keywords,
            overlay_html=overlay_html,
        )

        pdf_citation_schema_response.additional_properties = d
        return pdf_citation_schema_response

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
