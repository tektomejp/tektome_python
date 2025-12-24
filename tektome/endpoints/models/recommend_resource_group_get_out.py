from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.recommend_resource_group_get_out_parsed_location import RecommendResourceGroupGetOutParsedLocation
    from ..models.recommend_resource_group_schema import RecommendResourceGroupSchema


T = TypeVar("T", bound="RecommendResourceGroupGetOut")


@_attrs_define
class RecommendResourceGroupGetOut:
    """
    Attributes:
        resource_groups (list[RecommendResourceGroupSchema]):
        parsed_location (RecommendResourceGroupGetOutParsedLocation):
        count (int):
    """

    resource_groups: list[RecommendResourceGroupSchema]
    parsed_location: RecommendResourceGroupGetOutParsedLocation
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_groups = []
        for resource_groups_item_data in self.resource_groups:
            resource_groups_item = resource_groups_item_data.to_dict()
            resource_groups.append(resource_groups_item)

        parsed_location = self.parsed_location.to_dict()

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_groups": resource_groups,
                "parsed_location": parsed_location,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recommend_resource_group_get_out_parsed_location import RecommendResourceGroupGetOutParsedLocation
        from ..models.recommend_resource_group_schema import RecommendResourceGroupSchema

        d = dict(src_dict)
        resource_groups = []
        _resource_groups = d.pop("resource_groups")
        for resource_groups_item_data in _resource_groups:
            resource_groups_item = RecommendResourceGroupSchema.from_dict(resource_groups_item_data)

            resource_groups.append(resource_groups_item)

        parsed_location = RecommendResourceGroupGetOutParsedLocation.from_dict(d.pop("parsed_location"))

        count = d.pop("count")

        recommend_resource_group_get_out = cls(
            resource_groups=resource_groups,
            parsed_location=parsed_location,
            count=count,
        )

        recommend_resource_group_get_out.additional_properties = d
        return recommend_resource_group_get_out

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
