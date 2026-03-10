from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.polygon_highlight import PolygonHighlight


T = TypeVar("T", bound="ImagePolygons")


@_attrs_define
class ImagePolygons:
    """
    Attributes:
        image_uuid (str):
            UUID of the image on which to draw polygons.
            This could be an isolated image resource or the page UUID of a page in a document, e.g. to highlight parts of a
            diagram that is not captured in the OCR text.
        polygons (list[PolygonHighlight]): List of polygons to be drawn on the image
    """

    image_uuid: str
    polygons: list[PolygonHighlight]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_uuid = self.image_uuid

        polygons = []
        for polygons_item_data in self.polygons:
            polygons_item = polygons_item_data.to_dict()
            polygons.append(polygons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_uuid": image_uuid,
                "polygons": polygons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polygon_highlight import PolygonHighlight

        d = dict(src_dict)
        image_uuid = d.pop("image_uuid")

        polygons = []
        _polygons = d.pop("polygons")
        for polygons_item_data in _polygons:
            polygons_item = PolygonHighlight.from_dict(polygons_item_data)

            polygons.append(polygons_item)

        image_polygons = cls(
            image_uuid=image_uuid,
            polygons=polygons,
        )

        image_polygons.additional_properties = d
        return image_polygons

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
