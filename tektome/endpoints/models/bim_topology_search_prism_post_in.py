from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.point_2d import Point2D


T = TypeVar("T", bound="BimTopologySearchPrismPostIn")


@_attrs_define
class BimTopologySearchPrismPostIn:
    """Schema for BIM topology search with prism request.

    Attributes:
        bim_object_ids (list[str]): List of BIM object IDs to check for spatial overlap with the search volume. Must not
            contain empty or blank strings.
        base_outline (list[Point2D]): Ordered list of 2D points defining the horizontal footprint of the prism. Must
            form a valid, non-self-intersecting polygon with at least 3 distinct points and a non-zero area.
        strict_contains (bool | Unset): If true, only return objects fully contained within the search volume. If false,
            objects that partially overlap are also included. Default: False.
        use_vertices (bool | Unset): If true, use the object's vertex points to test overlap instead of its bounding
            box. Default: False.
        z_min (float | None | Unset): Lower elevation bound of the prism. If omitted, the prism extends downward without
            limit. Must be strictly less than z_max when both are provided.
        z_max (float | None | Unset): Upper elevation bound of the prism. If omitted, the prism extends upward without
            limit. Must be strictly greater than z_min when both are provided.
    """

    bim_object_ids: list[str]
    base_outline: list[Point2D]
    strict_contains: bool | Unset = False
    use_vertices: bool | Unset = False
    z_min: float | None | Unset = UNSET
    z_max: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bim_object_ids = self.bim_object_ids

        base_outline = []
        for base_outline_item_data in self.base_outline:
            base_outline_item = base_outline_item_data.to_dict()
            base_outline.append(base_outline_item)

        strict_contains = self.strict_contains

        use_vertices = self.use_vertices

        z_min: float | None | Unset
        if isinstance(self.z_min, Unset):
            z_min = UNSET
        else:
            z_min = self.z_min

        z_max: float | None | Unset
        if isinstance(self.z_max, Unset):
            z_max = UNSET
        else:
            z_max = self.z_max

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bim_object_ids": bim_object_ids,
                "base_outline": base_outline,
            }
        )
        if strict_contains is not UNSET:
            field_dict["strict_contains"] = strict_contains
        if use_vertices is not UNSET:
            field_dict["use_vertices"] = use_vertices
        if z_min is not UNSET:
            field_dict["z_min"] = z_min
        if z_max is not UNSET:
            field_dict["z_max"] = z_max

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.point_2d import Point2D

        d = dict(src_dict)
        bim_object_ids = cast(list[str], d.pop("bim_object_ids"))

        base_outline = []
        _base_outline = d.pop("base_outline")
        for base_outline_item_data in _base_outline:
            base_outline_item = Point2D.from_dict(base_outline_item_data)

            base_outline.append(base_outline_item)

        strict_contains = d.pop("strict_contains", UNSET)

        use_vertices = d.pop("use_vertices", UNSET)

        def _parse_z_min(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        z_min = _parse_z_min(d.pop("z_min", UNSET))

        def _parse_z_max(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        z_max = _parse_z_max(d.pop("z_max", UNSET))

        bim_topology_search_prism_post_in = cls(
            bim_object_ids=bim_object_ids,
            base_outline=base_outline,
            strict_contains=strict_contains,
            use_vertices=use_vertices,
            z_min=z_min,
            z_max=z_max,
        )

        bim_topology_search_prism_post_in.additional_properties = d
        return bim_topology_search_prism_post_in

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
