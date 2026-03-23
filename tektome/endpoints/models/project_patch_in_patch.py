from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coordinate import Coordinate


T = TypeVar("T", bound="ProjectPatchInPatch")


@_attrs_define
class ProjectPatchInPatch:
    """
    Attributes:
        name (None | str | Unset):
        planned_construction_start_date (datetime.date | None | Unset):
        state (None | str | Unset):
        region (None | str | Unset):
        street_address (None | str | Unset):
        coordinates (Coordinate | None | Unset):
        other_details (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    planned_construction_start_date: datetime.date | None | Unset = UNSET
    state: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    street_address: None | str | Unset = UNSET
    coordinates: Coordinate | None | Unset = UNSET
    other_details: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.coordinate import Coordinate

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        planned_construction_start_date: None | str | Unset
        if isinstance(self.planned_construction_start_date, Unset):
            planned_construction_start_date = UNSET
        elif isinstance(self.planned_construction_start_date, datetime.date):
            planned_construction_start_date = self.planned_construction_start_date.isoformat()
        else:
            planned_construction_start_date = self.planned_construction_start_date

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        street_address: None | str | Unset
        if isinstance(self.street_address, Unset):
            street_address = UNSET
        else:
            street_address = self.street_address

        coordinates: dict[str, Any] | None | Unset
        if isinstance(self.coordinates, Unset):
            coordinates = UNSET
        elif isinstance(self.coordinates, Coordinate):
            coordinates = self.coordinates.to_dict()
        else:
            coordinates = self.coordinates

        other_details: None | str | Unset
        if isinstance(self.other_details, Unset):
            other_details = UNSET
        else:
            other_details = self.other_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if planned_construction_start_date is not UNSET:
            field_dict["planned_construction_start_date"] = planned_construction_start_date
        if state is not UNSET:
            field_dict["state"] = state
        if region is not UNSET:
            field_dict["region"] = region
        if street_address is not UNSET:
            field_dict["street_address"] = street_address
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if other_details is not UNSET:
            field_dict["other_details"] = other_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coordinate import Coordinate

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_planned_construction_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                planned_construction_start_date_type_0 = isoparse(data).date()

                return planned_construction_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        planned_construction_start_date = _parse_planned_construction_start_date(
            d.pop("planned_construction_start_date", UNSET)
        )

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_street_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_address = _parse_street_address(d.pop("street_address", UNSET))

        def _parse_coordinates(data: object) -> Coordinate | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coordinates_type_0 = Coordinate.from_dict(data)

                return coordinates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Coordinate | None | Unset, data)

        coordinates = _parse_coordinates(d.pop("coordinates", UNSET))

        def _parse_other_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_details = _parse_other_details(d.pop("other_details", UNSET))

        project_patch_in_patch = cls(
            name=name,
            planned_construction_start_date=planned_construction_start_date,
            state=state,
            region=region,
            street_address=street_address,
            coordinates=coordinates,
            other_details=other_details,
        )

        project_patch_in_patch.additional_properties = d
        return project_patch_in_patch

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
