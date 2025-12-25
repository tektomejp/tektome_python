from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.operators_type_1 import OperatorsType1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coordinate import Coordinate


T = TypeVar("T", bound="JapanProjectAttributes")


@_attrs_define
class JapanProjectAttributes:
    """
    Attributes:
        name (str):
        planned_construction_start_date (datetime.date):
        street_address (str):
        coordinates (Coordinate):
        state (str):
        country (Literal['japan'] | Unset):  Default: 'japan'.
        structures (list[str] | None | Unset):
        site_area (float | None | Unset):
        site_area_operator (None | OperatorsType1 | Unset):
        floors_above_ground (int | None | Unset):
        floors_above_ground_operator (None | OperatorsType1 | Unset):
        floors_below_ground (int | None | Unset):
        floors_below_ground_operator (None | OperatorsType1 | Unset):
        height (float | None | Unset):
        height_operator (None | OperatorsType1 | Unset):
        other_details (None | str | Unset):
        fire_prevention_area (None | str | Unset):
        other_areas (None | str | Unset):
        area_of_use (None | str | Unset):
        construction_type (None | str | Unset):
        fire_resistance_type (None | str | Unset):
        fire_use_type (None | str | Unset):
        total_floor_area (float | None | Unset):
        total_floor_area_operator (None | OperatorsType1 | Unset):
        specified_area_ratio (float | None | Unset):
        specified_area_ratio_operator (None | OperatorsType1 | Unset):
        designated_building_coverage_ratio (float | None | Unset):
        designated_building_coverage_ratio_operator (None | OperatorsType1 | Unset):
        building_area (float | None | Unset):
        building_area_operator (None | OperatorsType1 | Unset):
        floor_area (float | None | Unset):
        floor_area_operator (None | OperatorsType1 | Unset):
        building_uses (list[str] | None | Unset):
        partial_structures (list[str] | None | Unset):
    """

    name: str
    planned_construction_start_date: datetime.date
    street_address: str
    coordinates: Coordinate
    state: str
    country: Literal["japan"] | Unset = "japan"
    structures: list[str] | None | Unset = UNSET
    site_area: float | None | Unset = UNSET
    site_area_operator: None | OperatorsType1 | Unset = UNSET
    floors_above_ground: int | None | Unset = UNSET
    floors_above_ground_operator: None | OperatorsType1 | Unset = UNSET
    floors_below_ground: int | None | Unset = UNSET
    floors_below_ground_operator: None | OperatorsType1 | Unset = UNSET
    height: float | None | Unset = UNSET
    height_operator: None | OperatorsType1 | Unset = UNSET
    other_details: None | str | Unset = UNSET
    fire_prevention_area: None | str | Unset = UNSET
    other_areas: None | str | Unset = UNSET
    area_of_use: None | str | Unset = UNSET
    construction_type: None | str | Unset = UNSET
    fire_resistance_type: None | str | Unset = UNSET
    fire_use_type: None | str | Unset = UNSET
    total_floor_area: float | None | Unset = UNSET
    total_floor_area_operator: None | OperatorsType1 | Unset = UNSET
    specified_area_ratio: float | None | Unset = UNSET
    specified_area_ratio_operator: None | OperatorsType1 | Unset = UNSET
    designated_building_coverage_ratio: float | None | Unset = UNSET
    designated_building_coverage_ratio_operator: None | OperatorsType1 | Unset = UNSET
    building_area: float | None | Unset = UNSET
    building_area_operator: None | OperatorsType1 | Unset = UNSET
    floor_area: float | None | Unset = UNSET
    floor_area_operator: None | OperatorsType1 | Unset = UNSET
    building_uses: list[str] | None | Unset = UNSET
    partial_structures: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        planned_construction_start_date = self.planned_construction_start_date.isoformat()

        street_address = self.street_address

        coordinates = self.coordinates.to_dict()

        state = self.state

        country = self.country

        structures: list[str] | None | Unset
        if isinstance(self.structures, Unset):
            structures = UNSET
        elif isinstance(self.structures, list):
            structures = self.structures

        else:
            structures = self.structures

        site_area: float | None | Unset
        if isinstance(self.site_area, Unset):
            site_area = UNSET
        else:
            site_area = self.site_area

        site_area_operator: None | str | Unset
        if isinstance(self.site_area_operator, Unset):
            site_area_operator = UNSET
        elif isinstance(self.site_area_operator, OperatorsType1):
            site_area_operator = self.site_area_operator.value
        else:
            site_area_operator = self.site_area_operator

        floors_above_ground: int | None | Unset
        if isinstance(self.floors_above_ground, Unset):
            floors_above_ground = UNSET
        else:
            floors_above_ground = self.floors_above_ground

        floors_above_ground_operator: None | str | Unset
        if isinstance(self.floors_above_ground_operator, Unset):
            floors_above_ground_operator = UNSET
        elif isinstance(self.floors_above_ground_operator, OperatorsType1):
            floors_above_ground_operator = self.floors_above_ground_operator.value
        else:
            floors_above_ground_operator = self.floors_above_ground_operator

        floors_below_ground: int | None | Unset
        if isinstance(self.floors_below_ground, Unset):
            floors_below_ground = UNSET
        else:
            floors_below_ground = self.floors_below_ground

        floors_below_ground_operator: None | str | Unset
        if isinstance(self.floors_below_ground_operator, Unset):
            floors_below_ground_operator = UNSET
        elif isinstance(self.floors_below_ground_operator, OperatorsType1):
            floors_below_ground_operator = self.floors_below_ground_operator.value
        else:
            floors_below_ground_operator = self.floors_below_ground_operator

        height: float | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        height_operator: None | str | Unset
        if isinstance(self.height_operator, Unset):
            height_operator = UNSET
        elif isinstance(self.height_operator, OperatorsType1):
            height_operator = self.height_operator.value
        else:
            height_operator = self.height_operator

        other_details: None | str | Unset
        if isinstance(self.other_details, Unset):
            other_details = UNSET
        else:
            other_details = self.other_details

        fire_prevention_area: None | str | Unset
        if isinstance(self.fire_prevention_area, Unset):
            fire_prevention_area = UNSET
        else:
            fire_prevention_area = self.fire_prevention_area

        other_areas: None | str | Unset
        if isinstance(self.other_areas, Unset):
            other_areas = UNSET
        else:
            other_areas = self.other_areas

        area_of_use: None | str | Unset
        if isinstance(self.area_of_use, Unset):
            area_of_use = UNSET
        else:
            area_of_use = self.area_of_use

        construction_type: None | str | Unset
        if isinstance(self.construction_type, Unset):
            construction_type = UNSET
        else:
            construction_type = self.construction_type

        fire_resistance_type: None | str | Unset
        if isinstance(self.fire_resistance_type, Unset):
            fire_resistance_type = UNSET
        else:
            fire_resistance_type = self.fire_resistance_type

        fire_use_type: None | str | Unset
        if isinstance(self.fire_use_type, Unset):
            fire_use_type = UNSET
        else:
            fire_use_type = self.fire_use_type

        total_floor_area: float | None | Unset
        if isinstance(self.total_floor_area, Unset):
            total_floor_area = UNSET
        else:
            total_floor_area = self.total_floor_area

        total_floor_area_operator: None | str | Unset
        if isinstance(self.total_floor_area_operator, Unset):
            total_floor_area_operator = UNSET
        elif isinstance(self.total_floor_area_operator, OperatorsType1):
            total_floor_area_operator = self.total_floor_area_operator.value
        else:
            total_floor_area_operator = self.total_floor_area_operator

        specified_area_ratio: float | None | Unset
        if isinstance(self.specified_area_ratio, Unset):
            specified_area_ratio = UNSET
        else:
            specified_area_ratio = self.specified_area_ratio

        specified_area_ratio_operator: None | str | Unset
        if isinstance(self.specified_area_ratio_operator, Unset):
            specified_area_ratio_operator = UNSET
        elif isinstance(self.specified_area_ratio_operator, OperatorsType1):
            specified_area_ratio_operator = self.specified_area_ratio_operator.value
        else:
            specified_area_ratio_operator = self.specified_area_ratio_operator

        designated_building_coverage_ratio: float | None | Unset
        if isinstance(self.designated_building_coverage_ratio, Unset):
            designated_building_coverage_ratio = UNSET
        else:
            designated_building_coverage_ratio = self.designated_building_coverage_ratio

        designated_building_coverage_ratio_operator: None | str | Unset
        if isinstance(self.designated_building_coverage_ratio_operator, Unset):
            designated_building_coverage_ratio_operator = UNSET
        elif isinstance(self.designated_building_coverage_ratio_operator, OperatorsType1):
            designated_building_coverage_ratio_operator = self.designated_building_coverage_ratio_operator.value
        else:
            designated_building_coverage_ratio_operator = self.designated_building_coverage_ratio_operator

        building_area: float | None | Unset
        if isinstance(self.building_area, Unset):
            building_area = UNSET
        else:
            building_area = self.building_area

        building_area_operator: None | str | Unset
        if isinstance(self.building_area_operator, Unset):
            building_area_operator = UNSET
        elif isinstance(self.building_area_operator, OperatorsType1):
            building_area_operator = self.building_area_operator.value
        else:
            building_area_operator = self.building_area_operator

        floor_area: float | None | Unset
        if isinstance(self.floor_area, Unset):
            floor_area = UNSET
        else:
            floor_area = self.floor_area

        floor_area_operator: None | str | Unset
        if isinstance(self.floor_area_operator, Unset):
            floor_area_operator = UNSET
        elif isinstance(self.floor_area_operator, OperatorsType1):
            floor_area_operator = self.floor_area_operator.value
        else:
            floor_area_operator = self.floor_area_operator

        building_uses: list[str] | None | Unset
        if isinstance(self.building_uses, Unset):
            building_uses = UNSET
        elif isinstance(self.building_uses, list):
            building_uses = self.building_uses

        else:
            building_uses = self.building_uses

        partial_structures: list[str] | None | Unset
        if isinstance(self.partial_structures, Unset):
            partial_structures = UNSET
        elif isinstance(self.partial_structures, list):
            partial_structures = self.partial_structures

        else:
            partial_structures = self.partial_structures

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "planned_construction_start_date": planned_construction_start_date,
                "street_address": street_address,
                "coordinates": coordinates,
                "state": state,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country
        if structures is not UNSET:
            field_dict["structures"] = structures
        if site_area is not UNSET:
            field_dict["site_area"] = site_area
        if site_area_operator is not UNSET:
            field_dict["site_area_operator"] = site_area_operator
        if floors_above_ground is not UNSET:
            field_dict["floors_above_ground"] = floors_above_ground
        if floors_above_ground_operator is not UNSET:
            field_dict["floors_above_ground_operator"] = floors_above_ground_operator
        if floors_below_ground is not UNSET:
            field_dict["floors_below_ground"] = floors_below_ground
        if floors_below_ground_operator is not UNSET:
            field_dict["floors_below_ground_operator"] = floors_below_ground_operator
        if height is not UNSET:
            field_dict["height"] = height
        if height_operator is not UNSET:
            field_dict["height_operator"] = height_operator
        if other_details is not UNSET:
            field_dict["other_details"] = other_details
        if fire_prevention_area is not UNSET:
            field_dict["fire_prevention_area"] = fire_prevention_area
        if other_areas is not UNSET:
            field_dict["other_areas"] = other_areas
        if area_of_use is not UNSET:
            field_dict["area_of_use"] = area_of_use
        if construction_type is not UNSET:
            field_dict["construction_type"] = construction_type
        if fire_resistance_type is not UNSET:
            field_dict["fire_resistance_type"] = fire_resistance_type
        if fire_use_type is not UNSET:
            field_dict["fire_use_type"] = fire_use_type
        if total_floor_area is not UNSET:
            field_dict["total_floor_area"] = total_floor_area
        if total_floor_area_operator is not UNSET:
            field_dict["total_floor_area_operator"] = total_floor_area_operator
        if specified_area_ratio is not UNSET:
            field_dict["specified_area_ratio"] = specified_area_ratio
        if specified_area_ratio_operator is not UNSET:
            field_dict["specified_area_ratio_operator"] = specified_area_ratio_operator
        if designated_building_coverage_ratio is not UNSET:
            field_dict["designated_building_coverage_ratio"] = designated_building_coverage_ratio
        if designated_building_coverage_ratio_operator is not UNSET:
            field_dict["designated_building_coverage_ratio_operator"] = designated_building_coverage_ratio_operator
        if building_area is not UNSET:
            field_dict["building_area"] = building_area
        if building_area_operator is not UNSET:
            field_dict["building_area_operator"] = building_area_operator
        if floor_area is not UNSET:
            field_dict["floor_area"] = floor_area
        if floor_area_operator is not UNSET:
            field_dict["floor_area_operator"] = floor_area_operator
        if building_uses is not UNSET:
            field_dict["building_uses"] = building_uses
        if partial_structures is not UNSET:
            field_dict["partial_structures"] = partial_structures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coordinate import Coordinate

        d = dict(src_dict)
        name = d.pop("name")

        planned_construction_start_date = isoparse(d.pop("planned_construction_start_date")).date()

        street_address = d.pop("street_address")

        coordinates = Coordinate.from_dict(d.pop("coordinates"))

        state = d.pop("state")

        country = cast(Literal["japan"] | Unset, d.pop("country", UNSET))
        if country != "japan" and not isinstance(country, Unset):
            raise ValueError(f"country must match const 'japan', got '{country}'")

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

        def _parse_site_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        site_area = _parse_site_area(d.pop("site_area", UNSET))

        def _parse_site_area_operator(data: object) -> None | OperatorsType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_operators_type_1 = OperatorsType1(data)

                return componentsschemas_operators_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OperatorsType1 | Unset, data)

        site_area_operator = _parse_site_area_operator(d.pop("site_area_operator", UNSET))

        def _parse_floors_above_ground(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        floors_above_ground = _parse_floors_above_ground(d.pop("floors_above_ground", UNSET))

        def _parse_floors_above_ground_operator(data: object) -> None | OperatorsType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_operators_type_1 = OperatorsType1(data)

                return componentsschemas_operators_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OperatorsType1 | Unset, data)

        floors_above_ground_operator = _parse_floors_above_ground_operator(d.pop("floors_above_ground_operator", UNSET))

        def _parse_floors_below_ground(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        floors_below_ground = _parse_floors_below_ground(d.pop("floors_below_ground", UNSET))

        def _parse_floors_below_ground_operator(data: object) -> None | OperatorsType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_operators_type_1 = OperatorsType1(data)

                return componentsschemas_operators_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OperatorsType1 | Unset, data)

        floors_below_ground_operator = _parse_floors_below_ground_operator(d.pop("floors_below_ground_operator", UNSET))

        def _parse_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_height_operator(data: object) -> None | OperatorsType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_operators_type_1 = OperatorsType1(data)

                return componentsschemas_operators_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OperatorsType1 | Unset, data)

        height_operator = _parse_height_operator(d.pop("height_operator", UNSET))

        def _parse_other_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_details = _parse_other_details(d.pop("other_details", UNSET))

        def _parse_fire_prevention_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fire_prevention_area = _parse_fire_prevention_area(d.pop("fire_prevention_area", UNSET))

        def _parse_other_areas(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_areas = _parse_other_areas(d.pop("other_areas", UNSET))

        def _parse_area_of_use(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_of_use = _parse_area_of_use(d.pop("area_of_use", UNSET))

        def _parse_construction_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        construction_type = _parse_construction_type(d.pop("construction_type", UNSET))

        def _parse_fire_resistance_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fire_resistance_type = _parse_fire_resistance_type(d.pop("fire_resistance_type", UNSET))

        def _parse_fire_use_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fire_use_type = _parse_fire_use_type(d.pop("fire_use_type", UNSET))

        def _parse_total_floor_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_floor_area = _parse_total_floor_area(d.pop("total_floor_area", UNSET))

        def _parse_total_floor_area_operator(data: object) -> None | OperatorsType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_operators_type_1 = OperatorsType1(data)

                return componentsschemas_operators_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OperatorsType1 | Unset, data)

        total_floor_area_operator = _parse_total_floor_area_operator(d.pop("total_floor_area_operator", UNSET))

        def _parse_specified_area_ratio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        specified_area_ratio = _parse_specified_area_ratio(d.pop("specified_area_ratio", UNSET))

        def _parse_specified_area_ratio_operator(data: object) -> None | OperatorsType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_operators_type_1 = OperatorsType1(data)

                return componentsschemas_operators_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OperatorsType1 | Unset, data)

        specified_area_ratio_operator = _parse_specified_area_ratio_operator(
            d.pop("specified_area_ratio_operator", UNSET)
        )

        def _parse_designated_building_coverage_ratio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        designated_building_coverage_ratio = _parse_designated_building_coverage_ratio(
            d.pop("designated_building_coverage_ratio", UNSET)
        )

        def _parse_designated_building_coverage_ratio_operator(data: object) -> None | OperatorsType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_operators_type_1 = OperatorsType1(data)

                return componentsschemas_operators_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OperatorsType1 | Unset, data)

        designated_building_coverage_ratio_operator = _parse_designated_building_coverage_ratio_operator(
            d.pop("designated_building_coverage_ratio_operator", UNSET)
        )

        def _parse_building_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        building_area = _parse_building_area(d.pop("building_area", UNSET))

        def _parse_building_area_operator(data: object) -> None | OperatorsType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_operators_type_1 = OperatorsType1(data)

                return componentsschemas_operators_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OperatorsType1 | Unset, data)

        building_area_operator = _parse_building_area_operator(d.pop("building_area_operator", UNSET))

        def _parse_floor_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        floor_area = _parse_floor_area(d.pop("floor_area", UNSET))

        def _parse_floor_area_operator(data: object) -> None | OperatorsType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_operators_type_1 = OperatorsType1(data)

                return componentsschemas_operators_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OperatorsType1 | Unset, data)

        floor_area_operator = _parse_floor_area_operator(d.pop("floor_area_operator", UNSET))

        def _parse_building_uses(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                building_uses_type_0 = cast(list[str], data)

                return building_uses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        building_uses = _parse_building_uses(d.pop("building_uses", UNSET))

        def _parse_partial_structures(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                partial_structures_type_0 = cast(list[str], data)

                return partial_structures_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        partial_structures = _parse_partial_structures(d.pop("partial_structures", UNSET))

        japan_project_attributes = cls(
            name=name,
            planned_construction_start_date=planned_construction_start_date,
            street_address=street_address,
            coordinates=coordinates,
            state=state,
            country=country,
            structures=structures,
            site_area=site_area,
            site_area_operator=site_area_operator,
            floors_above_ground=floors_above_ground,
            floors_above_ground_operator=floors_above_ground_operator,
            floors_below_ground=floors_below_ground,
            floors_below_ground_operator=floors_below_ground_operator,
            height=height,
            height_operator=height_operator,
            other_details=other_details,
            fire_prevention_area=fire_prevention_area,
            other_areas=other_areas,
            area_of_use=area_of_use,
            construction_type=construction_type,
            fire_resistance_type=fire_resistance_type,
            fire_use_type=fire_use_type,
            total_floor_area=total_floor_area,
            total_floor_area_operator=total_floor_area_operator,
            specified_area_ratio=specified_area_ratio,
            specified_area_ratio_operator=specified_area_ratio_operator,
            designated_building_coverage_ratio=designated_building_coverage_ratio,
            designated_building_coverage_ratio_operator=designated_building_coverage_ratio_operator,
            building_area=building_area,
            building_area_operator=building_area_operator,
            floor_area=floor_area,
            floor_area_operator=floor_area_operator,
            building_uses=building_uses,
            partial_structures=partial_structures,
        )

        japan_project_attributes.additional_properties = d
        return japan_project_attributes

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
