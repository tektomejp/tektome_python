from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coordinate import Coordinate


T = TypeVar("T", bound="LawtalkProjectRequiredSchema")


@_attrs_define
class LawtalkProjectRequiredSchema:
    """
    Attributes:
        name (str | Unset):  Default: ''.
        description (str | Unset):  Default: ''.
        planned_construction_start_date (datetime.date | Unset):  Default: isoparse('1970-01-01').date().
        country (str | Unset):  Default: ''.
        street_address (str | Unset):  Default: ''.
        coordinates (Coordinate | Unset):
        state (str | Unset):  Default: ''.
        region (str | Unset):  Default: ''.
        other_details (str | Unset):  Default: ''.
    """

    name: str | Unset = ""
    description: str | Unset = ""
    planned_construction_start_date: datetime.date | Unset = isoparse("1970-01-01").date()
    country: str | Unset = ""
    street_address: str | Unset = ""
    coordinates: Coordinate | Unset = UNSET
    state: str | Unset = ""
    region: str | Unset = ""
    other_details: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        planned_construction_start_date: str | Unset = UNSET
        if not isinstance(self.planned_construction_start_date, Unset):
            planned_construction_start_date = self.planned_construction_start_date.isoformat()

        country = self.country

        street_address = self.street_address

        coordinates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates.to_dict()

        state = self.state

        region = self.region

        other_details = self.other_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if planned_construction_start_date is not UNSET:
            field_dict["planned_construction_start_date"] = planned_construction_start_date
        if country is not UNSET:
            field_dict["country"] = country
        if street_address is not UNSET:
            field_dict["street_address"] = street_address
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if state is not UNSET:
            field_dict["state"] = state
        if region is not UNSET:
            field_dict["region"] = region
        if other_details is not UNSET:
            field_dict["other_details"] = other_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coordinate import Coordinate

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _planned_construction_start_date = d.pop("planned_construction_start_date", UNSET)
        planned_construction_start_date: datetime.date | Unset
        if isinstance(_planned_construction_start_date, Unset):
            planned_construction_start_date = UNSET
        else:
            planned_construction_start_date = isoparse(_planned_construction_start_date).date()

        country = d.pop("country", UNSET)

        street_address = d.pop("street_address", UNSET)

        _coordinates = d.pop("coordinates", UNSET)
        coordinates: Coordinate | Unset
        if isinstance(_coordinates, Unset):
            coordinates = UNSET
        else:
            coordinates = Coordinate.from_dict(_coordinates)

        state = d.pop("state", UNSET)

        region = d.pop("region", UNSET)

        other_details = d.pop("other_details", UNSET)

        lawtalk_project_required_schema = cls(
            name=name,
            description=description,
            planned_construction_start_date=planned_construction_start_date,
            country=country,
            street_address=street_address,
            coordinates=coordinates,
            state=state,
            region=region,
            other_details=other_details,
        )

        lawtalk_project_required_schema.additional_properties = d
        return lawtalk_project_required_schema

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
