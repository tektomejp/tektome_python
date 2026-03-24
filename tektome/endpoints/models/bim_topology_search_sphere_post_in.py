from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.point_3d import Point3D


T = TypeVar("T", bound="BimTopologySearchSpherePostIn")


@_attrs_define
class BimTopologySearchSpherePostIn:
    """Schema for BIM topology search with sphere request.

    Attributes:
        bim_object_ids (list[str]): List of BIM object IDs to check for spatial overlap with the search volume. Must not
            contain empty or blank strings.
        center_point (Point3D):
        radius (float): Radius of the search sphere in the model's unit system. Must be greater than 0.
        strict_contains (bool | Unset): If true, only return objects fully contained within the search volume. If false,
            objects that partially overlap are also included. Default: False.
        use_vertices (bool | Unset): If true, use the object's vertex points to test overlap instead of its bounding
            box. Default: False.
    """

    bim_object_ids: list[str]
    center_point: Point3D
    radius: float
    strict_contains: bool | Unset = False
    use_vertices: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bim_object_ids = self.bim_object_ids

        center_point = self.center_point.to_dict()

        radius = self.radius

        strict_contains = self.strict_contains

        use_vertices = self.use_vertices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bim_object_ids": bim_object_ids,
                "center_point": center_point,
                "radius": radius,
            }
        )
        if strict_contains is not UNSET:
            field_dict["strict_contains"] = strict_contains
        if use_vertices is not UNSET:
            field_dict["use_vertices"] = use_vertices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.point_3d import Point3D

        d = dict(src_dict)
        bim_object_ids = cast(list[str], d.pop("bim_object_ids"))

        center_point = Point3D.from_dict(d.pop("center_point"))

        radius = d.pop("radius")

        strict_contains = d.pop("strict_contains", UNSET)

        use_vertices = d.pop("use_vertices", UNSET)

        bim_topology_search_sphere_post_in = cls(
            bim_object_ids=bim_object_ids,
            center_point=center_point,
            radius=radius,
            strict_contains=strict_contains,
            use_vertices=use_vertices,
        )

        bim_topology_search_sphere_post_in.additional_properties = d
        return bim_topology_search_sphere_post_in

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
