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


T = TypeVar("T", bound="UnitedStatesProjectAttributes")


@_attrs_define
class UnitedStatesProjectAttributes:
    """United States project attributes

    Attributes:
        name (str):
        planned_construction_start_date (datetime.date):
        street_address (str):
        coordinates (Coordinate):
        state (str):
        country (Literal['united_states'] | Unset):  Default: 'united_states'.
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
        building_types (list[str] | None | Unset):
        gross_external_area (float | None | Unset):
        gross_external_area_operator (None | OperatorsType1 | Unset):
        gross_internal_area (float | None | Unset):
        gross_internal_area_operator (None | OperatorsType1 | Unset):
        net_internal_area (float | None | Unset):
        net_internal_area_operator (None | OperatorsType1 | Unset):
        proposed_development (None | str | Unset):
        other_restrictions (None | str | Unset):
    """

    name: str
    planned_construction_start_date: datetime.date
    street_address: str
    coordinates: Coordinate
    state: str
    country: Literal["united_states"] | Unset = "united_states"
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
    building_types: list[str] | None | Unset = UNSET
    gross_external_area: float | None | Unset = UNSET
    gross_external_area_operator: None | OperatorsType1 | Unset = UNSET
    gross_internal_area: float | None | Unset = UNSET
    gross_internal_area_operator: None | OperatorsType1 | Unset = UNSET
    net_internal_area: float | None | Unset = UNSET
    net_internal_area_operator: None | OperatorsType1 | Unset = UNSET
    proposed_development: None | str | Unset = UNSET
    other_restrictions: None | str | Unset = UNSET
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

        building_types: list[str] | None | Unset
        if isinstance(self.building_types, Unset):
            building_types = UNSET
        elif isinstance(self.building_types, list):
            building_types = self.building_types

        else:
            building_types = self.building_types

        gross_external_area: float | None | Unset
        if isinstance(self.gross_external_area, Unset):
            gross_external_area = UNSET
        else:
            gross_external_area = self.gross_external_area

        gross_external_area_operator: None | str | Unset
        if isinstance(self.gross_external_area_operator, Unset):
            gross_external_area_operator = UNSET
        elif isinstance(self.gross_external_area_operator, OperatorsType1):
            gross_external_area_operator = self.gross_external_area_operator.value
        else:
            gross_external_area_operator = self.gross_external_area_operator

        gross_internal_area: float | None | Unset
        if isinstance(self.gross_internal_area, Unset):
            gross_internal_area = UNSET
        else:
            gross_internal_area = self.gross_internal_area

        gross_internal_area_operator: None | str | Unset
        if isinstance(self.gross_internal_area_operator, Unset):
            gross_internal_area_operator = UNSET
        elif isinstance(self.gross_internal_area_operator, OperatorsType1):
            gross_internal_area_operator = self.gross_internal_area_operator.value
        else:
            gross_internal_area_operator = self.gross_internal_area_operator

        net_internal_area: float | None | Unset
        if isinstance(self.net_internal_area, Unset):
            net_internal_area = UNSET
        else:
            net_internal_area = self.net_internal_area

        net_internal_area_operator: None | str | Unset
        if isinstance(self.net_internal_area_operator, Unset):
            net_internal_area_operator = UNSET
        elif isinstance(self.net_internal_area_operator, OperatorsType1):
            net_internal_area_operator = self.net_internal_area_operator.value
        else:
            net_internal_area_operator = self.net_internal_area_operator

        proposed_development: None | str | Unset
        if isinstance(self.proposed_development, Unset):
            proposed_development = UNSET
        else:
            proposed_development = self.proposed_development

        other_restrictions: None | str | Unset
        if isinstance(self.other_restrictions, Unset):
            other_restrictions = UNSET
        else:
            other_restrictions = self.other_restrictions

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
        if building_types is not UNSET:
            field_dict["building_types"] = building_types
        if gross_external_area is not UNSET:
            field_dict["gross_external_area"] = gross_external_area
        if gross_external_area_operator is not UNSET:
            field_dict["gross_external_area_operator"] = gross_external_area_operator
        if gross_internal_area is not UNSET:
            field_dict["gross_internal_area"] = gross_internal_area
        if gross_internal_area_operator is not UNSET:
            field_dict["gross_internal_area_operator"] = gross_internal_area_operator
        if net_internal_area is not UNSET:
            field_dict["net_internal_area"] = net_internal_area
        if net_internal_area_operator is not UNSET:
            field_dict["net_internal_area_operator"] = net_internal_area_operator
        if proposed_development is not UNSET:
            field_dict["proposed_development"] = proposed_development
        if other_restrictions is not UNSET:
            field_dict["other_restrictions"] = other_restrictions

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

        country = cast(Literal["united_states"] | Unset, d.pop("country", UNSET))
        if country != "united_states" and not isinstance(country, Unset):
            raise ValueError(f"country must match const 'united_states', got '{country}'")

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

        def _parse_gross_external_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gross_external_area = _parse_gross_external_area(d.pop("gross_external_area", UNSET))

        def _parse_gross_external_area_operator(data: object) -> None | OperatorsType1 | Unset:
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

        gross_external_area_operator = _parse_gross_external_area_operator(d.pop("gross_external_area_operator", UNSET))

        def _parse_gross_internal_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gross_internal_area = _parse_gross_internal_area(d.pop("gross_internal_area", UNSET))

        def _parse_gross_internal_area_operator(data: object) -> None | OperatorsType1 | Unset:
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

        gross_internal_area_operator = _parse_gross_internal_area_operator(d.pop("gross_internal_area_operator", UNSET))

        def _parse_net_internal_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        net_internal_area = _parse_net_internal_area(d.pop("net_internal_area", UNSET))

        def _parse_net_internal_area_operator(data: object) -> None | OperatorsType1 | Unset:
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

        net_internal_area_operator = _parse_net_internal_area_operator(d.pop("net_internal_area_operator", UNSET))

        def _parse_proposed_development(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proposed_development = _parse_proposed_development(d.pop("proposed_development", UNSET))

        def _parse_other_restrictions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_restrictions = _parse_other_restrictions(d.pop("other_restrictions", UNSET))

        united_states_project_attributes = cls(
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
            building_types=building_types,
            gross_external_area=gross_external_area,
            gross_external_area_operator=gross_external_area_operator,
            gross_internal_area=gross_internal_area,
            gross_internal_area_operator=gross_internal_area_operator,
            net_internal_area=net_internal_area,
            net_internal_area_operator=net_internal_area_operator,
            proposed_development=proposed_development,
            other_restrictions=other_restrictions,
        )

        united_states_project_attributes.additional_properties = d
        return united_states_project_attributes

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
