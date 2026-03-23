from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateCaptureSectionComponentPostIn")


@_attrs_define
class CreateCaptureSectionComponentPostIn:
    """
    Attributes:
        resource_id (UUID):
        page_number (int):
        bounding_geometry (list[list[float]]):
    """

    resource_id: UUID
    page_number: int
    bounding_geometry: list[list[float]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = str(self.resource_id)

        page_number = self.page_number

        bounding_geometry = []
        for bounding_geometry_item_data in self.bounding_geometry:
            bounding_geometry_item = bounding_geometry_item_data

            bounding_geometry.append(bounding_geometry_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_id": resource_id,
                "page_number": page_number,
                "bounding_geometry": bounding_geometry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_id = UUID(d.pop("resource_id"))

        page_number = d.pop("page_number")

        bounding_geometry = []
        _bounding_geometry = d.pop("bounding_geometry")
        for bounding_geometry_item_data in _bounding_geometry:
            bounding_geometry_item = cast(list[float], bounding_geometry_item_data)

            bounding_geometry.append(bounding_geometry_item)

        create_capture_section_component_post_in = cls(
            resource_id=resource_id,
            page_number=page_number,
            bounding_geometry=bounding_geometry,
        )

        create_capture_section_component_post_in.additional_properties = d
        return create_capture_section_component_post_in

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
