from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.choice_schema import ChoiceSchema


T = TypeVar("T", bound="ProjectChoicesGetOut")


@_attrs_define
class ProjectChoicesGetOut:
    """
    Attributes:
        building_types (list[ChoiceSchema]):
        structures (list[ChoiceSchema]):
    """

    building_types: list[ChoiceSchema]
    structures: list[ChoiceSchema]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        building_types = []
        for building_types_item_data in self.building_types:
            building_types_item = building_types_item_data.to_dict()
            building_types.append(building_types_item)

        structures = []
        for structures_item_data in self.structures:
            structures_item = structures_item_data.to_dict()
            structures.append(structures_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "building_types": building_types,
                "structures": structures,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.choice_schema import ChoiceSchema

        d = dict(src_dict)
        building_types = []
        _building_types = d.pop("building_types")
        for building_types_item_data in _building_types:
            building_types_item = ChoiceSchema.from_dict(building_types_item_data)

            building_types.append(building_types_item)

        structures = []
        _structures = d.pop("structures")
        for structures_item_data in _structures:
            structures_item = ChoiceSchema.from_dict(structures_item_data)

            structures.append(structures_item)

        project_choices_get_out = cls(
            building_types=building_types,
            structures=structures,
        )

        project_choices_get_out.additional_properties = d
        return project_choices_get_out

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
