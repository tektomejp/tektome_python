from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type import AttributeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pdf_polygon_schema_in import PDFPolygonSchemaIn


T = TypeVar("T", bound="PDFCitationPostIn")


@_attrs_define
class PDFCitationPostIn:
    """
    Attributes:
        title (str):
        attribute_type (AttributeType): StrEnum for all available attribute types

            .. warning::
                Do not change the values of this enum, as they are used in the database.
                If you need to add a new attribute type, add a new enum value with a unique name.
        resource_id (UUID): ID of the cited PDF resource.
        polygons (list[PDFPolygonSchemaIn] | Unset): The list of polygons associated with the PDF citation.
        keywords (list[str] | Unset):
    """

    title: str
    attribute_type: AttributeType
    resource_id: UUID
    polygons: list[PDFPolygonSchemaIn] | Unset = UNSET
    keywords: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        attribute_type = self.attribute_type.value

        resource_id = str(self.resource_id)

        polygons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.polygons, Unset):
            polygons = []
            for polygons_item_data in self.polygons:
                polygons_item = polygons_item_data.to_dict()
                polygons.append(polygons_item)

        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "attribute_type": attribute_type,
                "resource_id": resource_id,
            }
        )
        if polygons is not UNSET:
            field_dict["polygons"] = polygons
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pdf_polygon_schema_in import PDFPolygonSchemaIn

        d = dict(src_dict)
        title = d.pop("title")

        attribute_type = AttributeType(d.pop("attribute_type"))

        resource_id = UUID(d.pop("resource_id"))

        _polygons = d.pop("polygons", UNSET)
        polygons: list[PDFPolygonSchemaIn] | Unset = UNSET
        if _polygons is not UNSET:
            polygons = []
            for polygons_item_data in _polygons:
                polygons_item = PDFPolygonSchemaIn.from_dict(polygons_item_data)

                polygons.append(polygons_item)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        pdf_citation_post_in = cls(
            title=title,
            attribute_type=attribute_type,
            resource_id=resource_id,
            polygons=polygons,
            keywords=keywords,
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
