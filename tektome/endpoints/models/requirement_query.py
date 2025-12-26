from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequirementQuery")


@_attrs_define
class RequirementQuery:
    """
    Attributes:
        project_id (UUID):
        recent (bool | Unset):  Default: False.
        filter_name (None | str | Unset):
    """

    project_id: UUID
    recent: bool | Unset = False
    filter_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = str(self.project_id)

        recent = self.recent

        filter_name: None | str | Unset
        if isinstance(self.filter_name, Unset):
            filter_name = UNSET
        else:
            filter_name = self.filter_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
            }
        )
        if recent is not UNSET:
            field_dict["recent"] = recent
        if filter_name is not UNSET:
            field_dict["filter_name"] = filter_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = UUID(d.pop("project_id"))

        recent = d.pop("recent", UNSET)

        def _parse_filter_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_name = _parse_filter_name(d.pop("filter_name", UNSET))

        requirement_query = cls(
            project_id=project_id,
            recent=recent,
            filter_name=filter_name,
        )

        requirement_query.additional_properties = d
        return requirement_query

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
