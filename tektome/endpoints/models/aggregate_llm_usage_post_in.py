from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AggregateLLMUsagePostIn")


@_attrs_define
class AggregateLLMUsagePostIn:
    """
    Attributes:
        start_date (str): ISO 8601 date
        end_date (str): ISO 8601 date
        organization_id (None | str | Unset):
        dataspace_id (None | str | Unset):
        project_id (None | str | Unset):
        user_id (None | str | Unset):
    """

    start_date: str
    end_date: str
    organization_id: None | str | Unset = UNSET
    dataspace_id: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date

        end_date = self.end_date

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        dataspace_id: None | str | Unset
        if isinstance(self.dataspace_id, Unset):
            dataspace_id = UNSET
        else:
            dataspace_id = self.dataspace_id

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_date": start_date,
                "end_date": end_date,
            }
        )
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if dataspace_id is not UNSET:
            field_dict["dataspace_id"] = dataspace_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        def _parse_organization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        def _parse_dataspace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataspace_id = _parse_dataspace_id(d.pop("dataspace_id", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        aggregate_llm_usage_post_in = cls(
            start_date=start_date,
            end_date=end_date,
            organization_id=organization_id,
            dataspace_id=dataspace_id,
            project_id=project_id,
            user_id=user_id,
        )

        aggregate_llm_usage_post_in.additional_properties = d
        return aggregate_llm_usage_post_in

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
