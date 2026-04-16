from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type import AttributeType

T = TypeVar("T", bound="CreatePDFCitationPolygonAnnotationRequest")


@_attrs_define
class CreatePDFCitationPolygonAnnotationRequest:
    """
    Attributes:
        page_id (UUID): ID of the page the polygon belongs to. Required if polygon_type is 'pdf'.
        attribute_type (AttributeType): StrEnum for all available attribute types

            .. warning::
                Do not change the values of this enum, as they are used in the database.
                If you need to add a new attribute type, add a new enum value with a unique name.
        bounding_geometry (list[list[float]]): List of coordinates defining the polygon. Each coordinate is a list of
            two floats [x, y].
    """

    page_id: UUID
    attribute_type: AttributeType
    bounding_geometry: list[list[float]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_id = str(self.page_id)

        attribute_type = self.attribute_type.value

        bounding_geometry = []
        for bounding_geometry_item_data in self.bounding_geometry:
            bounding_geometry_item = []
            for bounding_geometry_item_item_data in bounding_geometry_item_data:
                bounding_geometry_item_item: float
                bounding_geometry_item_item = bounding_geometry_item_item_data
                bounding_geometry_item.append(bounding_geometry_item_item)

            bounding_geometry.append(bounding_geometry_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page_id": page_id,
                "attribute_type": attribute_type,
                "bounding_geometry": bounding_geometry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_id = UUID(d.pop("page_id"))

        attribute_type = AttributeType(d.pop("attribute_type"))

        bounding_geometry = []
        _bounding_geometry = d.pop("bounding_geometry")
        for bounding_geometry_item_data in _bounding_geometry:
            bounding_geometry_item = []
            _bounding_geometry_item = bounding_geometry_item_data
            for bounding_geometry_item_item_data in _bounding_geometry_item:

                def _parse_bounding_geometry_item_item(data: object) -> float:
                    return cast(float, data)

                bounding_geometry_item_item = _parse_bounding_geometry_item_item(bounding_geometry_item_item_data)

                bounding_geometry_item.append(bounding_geometry_item_item)

            bounding_geometry.append(bounding_geometry_item)

        create_pdf_citation_polygon_annotation_request = cls(
            page_id=page_id,
            attribute_type=attribute_type,
            bounding_geometry=bounding_geometry,
        )

        create_pdf_citation_polygon_annotation_request.additional_properties = d
        return create_pdf_citation_polygon_annotation_request

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
