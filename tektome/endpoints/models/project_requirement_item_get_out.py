from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_requirement_item_get_out_value_type_0 import ProjectRequirementItemGetOutValueType0


T = TypeVar("T", bound="ProjectRequirementItemGetOut")


@_attrs_define
class ProjectRequirementItemGetOut:
    """
    Attributes:
        value (None | ProjectRequirementItemGetOutValueType0 | Unset):
        id (None | Unset | UUID):
        nonce (int | Unset):  Default: 0.
    """

    value: None | ProjectRequirementItemGetOutValueType0 | Unset = UNSET
    id: None | Unset | UUID = UNSET
    nonce: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.project_requirement_item_get_out_value_type_0 import ProjectRequirementItemGetOutValueType0

        value: dict[str, Any] | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, ProjectRequirementItemGetOutValueType0):
            value = self.value.to_dict()
        else:
            value = self.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        nonce = self.nonce

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if id is not UNSET:
            field_dict["id"] = id
        if nonce is not UNSET:
            field_dict["nonce"] = nonce

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_requirement_item_get_out_value_type_0 import ProjectRequirementItemGetOutValueType0

        d = dict(src_dict)

        def _parse_value(data: object) -> None | ProjectRequirementItemGetOutValueType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = ProjectRequirementItemGetOutValueType0.from_dict(data)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProjectRequirementItemGetOutValueType0 | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

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

        project_requirement_item_get_out = cls(
            value=value,
            id=id,
            nonce=nonce,
        )

        project_requirement_item_get_out.additional_properties = d
        return project_requirement_item_get_out

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
