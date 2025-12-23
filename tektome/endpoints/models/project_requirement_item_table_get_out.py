from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_requirement_item_table_get_out_value_item import ProjectRequirementItemTableGetOutValueItem


T = TypeVar("T", bound="ProjectRequirementItemTableGetOut")


@_attrs_define
class ProjectRequirementItemTableGetOut:
    """
    Attributes:
        value (list[ProjectRequirementItemTableGetOutValueItem] | Unset):
        id (None | Unset | UUID):
        nonce (int | Unset):  Default: 0.
        extraction_status (None | str | Unset):  Default: 'pending'.
    """

    value: list[ProjectRequirementItemTableGetOutValueItem] | Unset = UNSET
    id: None | Unset | UUID = UNSET
    nonce: int | Unset = 0
    extraction_status: None | str | Unset = "pending"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = []
            for value_item_data in self.value:
                value_item = value_item_data.to_dict()
                value.append(value_item)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        nonce = self.nonce

        extraction_status: None | str | Unset
        if isinstance(self.extraction_status, Unset):
            extraction_status = UNSET
        else:
            extraction_status = self.extraction_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if id is not UNSET:
            field_dict["id"] = id
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if extraction_status is not UNSET:
            field_dict["extraction_status"] = extraction_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_requirement_item_table_get_out_value_item import (
            ProjectRequirementItemTableGetOutValueItem,
        )

        d = dict(src_dict)
        _value = d.pop("value", UNSET)
        value: list[ProjectRequirementItemTableGetOutValueItem] | Unset = UNSET
        if _value is not UNSET:
            value = []
            for value_item_data in _value:
                value_item = ProjectRequirementItemTableGetOutValueItem.from_dict(value_item_data)

                value.append(value_item)

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        nonce = d.pop("nonce", UNSET)

        def _parse_extraction_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extraction_status = _parse_extraction_status(d.pop("extraction_status", UNSET))

        project_requirement_item_table_get_out = cls(
            value=value,
            id=id,
            nonce=nonce,
            extraction_status=extraction_status,
        )

        project_requirement_item_table_get_out.additional_properties = d
        return project_requirement_item_table_get_out

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
