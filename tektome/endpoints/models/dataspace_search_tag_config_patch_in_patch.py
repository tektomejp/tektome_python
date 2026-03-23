from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataspace_search_tag_config_patch_in_patch_default_grouping_option_type_0 import (
    DataspaceSearchTagConfigPatchInPatchDefaultGroupingOptionType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataspaceSearchTagConfigPatchInPatch")


@_attrs_define
class DataspaceSearchTagConfigPatchInPatch:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        is_active (bool | None | Unset):
        default_grouping_option (DataspaceSearchTagConfigPatchInPatchDefaultGroupingOptionType0 | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    default_grouping_option: DataspaceSearchTagConfigPatchInPatchDefaultGroupingOptionType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        default_grouping_option: None | str | Unset
        if isinstance(self.default_grouping_option, Unset):
            default_grouping_option = UNSET
        elif isinstance(self.default_grouping_option, DataspaceSearchTagConfigPatchInPatchDefaultGroupingOptionType0):
            default_grouping_option = self.default_grouping_option.value
        else:
            default_grouping_option = self.default_grouping_option

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if default_grouping_option is not UNSET:
            field_dict["default_grouping_option"] = default_grouping_option

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_default_grouping_option(
            data: object,
        ) -> DataspaceSearchTagConfigPatchInPatchDefaultGroupingOptionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_grouping_option_type_0 = DataspaceSearchTagConfigPatchInPatchDefaultGroupingOptionType0(data)

                return default_grouping_option_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataspaceSearchTagConfigPatchInPatchDefaultGroupingOptionType0 | None | Unset, data)

        default_grouping_option = _parse_default_grouping_option(d.pop("default_grouping_option", UNSET))

        dataspace_search_tag_config_patch_in_patch = cls(
            name=name,
            description=description,
            is_active=is_active,
            default_grouping_option=default_grouping_option,
        )

        dataspace_search_tag_config_patch_in_patch.additional_properties = d
        return dataspace_search_tag_config_patch_in_patch

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
