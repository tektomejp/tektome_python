from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BimProjectV2IndexStatusResponse")


@_attrs_define
class BimProjectV2IndexStatusResponse:
    """Response schema for BIM project V2 index status from Elasticsearch.

    Attributes:
        bim_project_id (UUID): BIM project ID
        objects_count (int): Number of BIM objects (parent documents) indexed in Elasticsearch V2
        views_count (int): Number of BIM views (parent documents) indexed in Elasticsearch V2
        sheets_count (int): Number of BIM sheets (parent documents) indexed in Elasticsearch V2
    """

    bim_project_id: UUID
    objects_count: int
    views_count: int
    sheets_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bim_project_id = str(self.bim_project_id)

        objects_count = self.objects_count

        views_count = self.views_count

        sheets_count = self.sheets_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bim_project_id": bim_project_id,
                "objects_count": objects_count,
                "views_count": views_count,
                "sheets_count": sheets_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bim_project_id = UUID(d.pop("bim_project_id"))

        objects_count = d.pop("objects_count")

        views_count = d.pop("views_count")

        sheets_count = d.pop("sheets_count")

        bim_project_v2_index_status_response = cls(
            bim_project_id=bim_project_id,
            objects_count=objects_count,
            views_count=views_count,
            sheets_count=sheets_count,
        )

        bim_project_v2_index_status_response.additional_properties = d
        return bim_project_v2_index_status_response

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
