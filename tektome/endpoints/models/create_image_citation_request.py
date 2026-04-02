from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type import AttributeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateImageCitationRequest")


@_attrs_define
class CreateImageCitationRequest:
    """
    Attributes:
        title (str):
        attribute_type (AttributeType): StrEnum for all available attribute types

            .. warning::
                Do not change the values of this enum, as they are used in the database.
                If you need to add a new attribute type, add a new enum value with a unique name.
        bounding_geometry (list[list[list[float]]]): List of coordinates defining the polygon within the image only.
        image_resource_id (UUID): ID of the cited image resource.
        overlay_html (None | str | Unset):
        keywords (list[str] | Unset):
    """

    title: str
    attribute_type: AttributeType
    bounding_geometry: list[list[list[float]]]
    image_resource_id: UUID
    overlay_html: None | str | Unset = UNSET
    keywords: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        attribute_type = self.attribute_type.value

        bounding_geometry = []
        for bounding_geometry_item_data in self.bounding_geometry:
            bounding_geometry_item = []
            for bounding_geometry_item_item_data in bounding_geometry_item_data:
                bounding_geometry_item_item = []
                for bounding_geometry_item_item_item_data in bounding_geometry_item_item_data:
                    bounding_geometry_item_item_item: float
                    bounding_geometry_item_item_item = bounding_geometry_item_item_item_data
                    bounding_geometry_item_item.append(bounding_geometry_item_item_item)

                bounding_geometry_item.append(bounding_geometry_item_item)

            bounding_geometry.append(bounding_geometry_item)

        image_resource_id = str(self.image_resource_id)

        overlay_html: None | str | Unset
        if isinstance(self.overlay_html, Unset):
            overlay_html = UNSET
        else:
            overlay_html = self.overlay_html

        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "attribute_type": attribute_type,
                "bounding_geometry": bounding_geometry,
                "image_resource_id": image_resource_id,
            }
        )
        if overlay_html is not UNSET:
            field_dict["overlay_html"] = overlay_html
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        attribute_type = AttributeType(d.pop("attribute_type"))

        bounding_geometry = []
        _bounding_geometry = d.pop("bounding_geometry")
        for bounding_geometry_item_data in _bounding_geometry:
            bounding_geometry_item = []
            _bounding_geometry_item = bounding_geometry_item_data
            for bounding_geometry_item_item_data in _bounding_geometry_item:
                bounding_geometry_item_item = []
                _bounding_geometry_item_item = bounding_geometry_item_item_data
                for bounding_geometry_item_item_item_data in _bounding_geometry_item_item:

                    def _parse_bounding_geometry_item_item_item(data: object) -> float:
                        return cast(float, data)

                    bounding_geometry_item_item_item = _parse_bounding_geometry_item_item_item(
                        bounding_geometry_item_item_item_data
                    )

                    bounding_geometry_item_item.append(bounding_geometry_item_item_item)

                bounding_geometry_item.append(bounding_geometry_item_item)

            bounding_geometry.append(bounding_geometry_item)

        image_resource_id = UUID(d.pop("image_resource_id"))

        def _parse_overlay_html(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overlay_html = _parse_overlay_html(d.pop("overlay_html", UNSET))

        keywords = cast(list[str], d.pop("keywords", UNSET))

        create_image_citation_request = cls(
            title=title,
            attribute_type=attribute_type,
            bounding_geometry=bounding_geometry,
            image_resource_id=image_resource_id,
            overlay_html=overlay_html,
            keywords=keywords,
        )

        create_image_citation_request.additional_properties = d
        return create_image_citation_request

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
