from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.japan_project_attributes import JapanProjectAttributes
    from ..models.united_kingdom_project_attributes import UnitedKingdomProjectAttributes
    from ..models.united_states_project_attributes import UnitedStatesProjectAttributes


T = TypeVar("T", bound="LawtalkProjectPostIn")


@_attrs_define
class LawtalkProjectPostIn:
    """
    Attributes:
        attributes (JapanProjectAttributes | UnitedKingdomProjectAttributes | UnitedStatesProjectAttributes):
    """

    attributes: JapanProjectAttributes | UnitedKingdomProjectAttributes | UnitedStatesProjectAttributes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.japan_project_attributes import JapanProjectAttributes
        from ..models.united_kingdom_project_attributes import UnitedKingdomProjectAttributes

        attributes: dict[str, Any]
        if isinstance(self.attributes, JapanProjectAttributes):
            attributes = self.attributes.to_dict()
        elif isinstance(self.attributes, UnitedKingdomProjectAttributes):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.japan_project_attributes import JapanProjectAttributes
        from ..models.united_kingdom_project_attributes import UnitedKingdomProjectAttributes
        from ..models.united_states_project_attributes import UnitedStatesProjectAttributes

        d = dict(src_dict)

        def _parse_attributes(
            data: object,
        ) -> JapanProjectAttributes | UnitedKingdomProjectAttributes | UnitedStatesProjectAttributes:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_country_attributes_type_0 = JapanProjectAttributes.from_dict(data)

                return componentsschemas_country_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_country_attributes_type_1 = UnitedKingdomProjectAttributes.from_dict(data)

                return componentsschemas_country_attributes_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_country_attributes_type_2 = UnitedStatesProjectAttributes.from_dict(data)

            return componentsschemas_country_attributes_type_2

        attributes = _parse_attributes(d.pop("attributes"))

        lawtalk_project_post_in = cls(
            attributes=attributes,
        )

        lawtalk_project_post_in.additional_properties = d
        return lawtalk_project_post_in

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
