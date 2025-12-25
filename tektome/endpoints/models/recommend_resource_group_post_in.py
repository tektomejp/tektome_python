from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecommendResourceGroupPostIn")


@_attrs_define
class RecommendResourceGroupPostIn:
    """
    Attributes:
        project_id (None | Unset | UUID):
        location (None | str | Unset):
        structures (list[str] | None | Unset):
        building_types (list[str] | None | Unset):
        floors_above_ground (int | None | Unset):
        floors_below_ground (int | None | Unset):
        height (float | None | Unset):
        land_area (float | None | Unset):
        building_area (float | None | Unset):
        page (int | Unset):  Default: 1.
        top_k (int | Unset):  Default: 1000.
    """

    project_id: None | Unset | UUID = UNSET
    location: None | str | Unset = UNSET
    structures: list[str] | None | Unset = UNSET
    building_types: list[str] | None | Unset = UNSET
    floors_above_ground: int | None | Unset = UNSET
    floors_below_ground: int | None | Unset = UNSET
    height: float | None | Unset = UNSET
    land_area: float | None | Unset = UNSET
    building_area: float | None | Unset = UNSET
    page: int | Unset = 1
    top_k: int | Unset = 1000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        structures: list[str] | None | Unset
        if isinstance(self.structures, Unset):
            structures = UNSET
        elif isinstance(self.structures, list):
            structures = self.structures

        else:
            structures = self.structures

        building_types: list[str] | None | Unset
        if isinstance(self.building_types, Unset):
            building_types = UNSET
        elif isinstance(self.building_types, list):
            building_types = self.building_types

        else:
            building_types = self.building_types

        floors_above_ground: int | None | Unset
        if isinstance(self.floors_above_ground, Unset):
            floors_above_ground = UNSET
        else:
            floors_above_ground = self.floors_above_ground

        floors_below_ground: int | None | Unset
        if isinstance(self.floors_below_ground, Unset):
            floors_below_ground = UNSET
        else:
            floors_below_ground = self.floors_below_ground

        height: float | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        land_area: float | None | Unset
        if isinstance(self.land_area, Unset):
            land_area = UNSET
        else:
            land_area = self.land_area

        building_area: float | None | Unset
        if isinstance(self.building_area, Unset):
            building_area = UNSET
        else:
            building_area = self.building_area

        page = self.page

        top_k = self.top_k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if location is not UNSET:
            field_dict["location"] = location
        if structures is not UNSET:
            field_dict["structures"] = structures
        if building_types is not UNSET:
            field_dict["building_types"] = building_types
        if floors_above_ground is not UNSET:
            field_dict["floors_above_ground"] = floors_above_ground
        if floors_below_ground is not UNSET:
            field_dict["floors_below_ground"] = floors_below_ground
        if height is not UNSET:
            field_dict["height"] = height
        if land_area is not UNSET:
            field_dict["land_area"] = land_area
        if building_area is not UNSET:
            field_dict["building_area"] = building_area
        if page is not UNSET:
            field_dict["page"] = page
        if top_k is not UNSET:
            field_dict["top_k"] = top_k

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_project_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_0 = UUID(data)

                return project_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_structures(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                structures_type_0 = cast(list[str], data)

                return structures_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        structures = _parse_structures(d.pop("structures", UNSET))

        def _parse_building_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                building_types_type_0 = cast(list[str], data)

                return building_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        building_types = _parse_building_types(d.pop("building_types", UNSET))

        def _parse_floors_above_ground(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        floors_above_ground = _parse_floors_above_ground(d.pop("floors_above_ground", UNSET))

        def _parse_floors_below_ground(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        floors_below_ground = _parse_floors_below_ground(d.pop("floors_below_ground", UNSET))

        def _parse_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_land_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        land_area = _parse_land_area(d.pop("land_area", UNSET))

        def _parse_building_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        building_area = _parse_building_area(d.pop("building_area", UNSET))

        page = d.pop("page", UNSET)

        top_k = d.pop("top_k", UNSET)

        recommend_resource_group_post_in = cls(
            project_id=project_id,
            location=location,
            structures=structures,
            building_types=building_types,
            floors_above_ground=floors_above_ground,
            floors_below_ground=floors_below_ground,
            height=height,
            land_area=land_area,
            building_area=building_area,
            page=page,
            top_k=top_k,
        )

        recommend_resource_group_post_in.additional_properties = d
        return recommend_resource_group_post_in

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
