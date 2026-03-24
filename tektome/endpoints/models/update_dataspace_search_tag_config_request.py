from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_dataspace_search_tag_config_request_default_grouping_option_type_0 import (
    UpdateDataspaceSearchTagConfigRequestDefaultGroupingOptionType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDataspaceSearchTagConfigRequest")


@_attrs_define
class UpdateDataspaceSearchTagConfigRequest:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        is_active (bool | None | Unset):
        default_grouping_option (None | Unset | UpdateDataspaceSearchTagConfigRequestDefaultGroupingOptionType0):
        table_grouping_project_option_ids (list[UUID] | None | Unset):
        table_grouping_resource_option_ids (list[UUID] | None | Unset):
        default_grouping_project_attribute_id (None | Unset | UUID): FK to a project attribute config for the default
            grouping attribute.
        default_grouping_resource_attribute_id (None | Unset | UUID): FK to a resource attribute config for the default
            grouping attribute.
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    default_grouping_option: None | Unset | UpdateDataspaceSearchTagConfigRequestDefaultGroupingOptionType0 = UNSET
    table_grouping_project_option_ids: list[UUID] | None | Unset = UNSET
    table_grouping_resource_option_ids: list[UUID] | None | Unset = UNSET
    default_grouping_project_attribute_id: None | Unset | UUID = UNSET
    default_grouping_resource_attribute_id: None | Unset | UUID = UNSET
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
        elif isinstance(self.default_grouping_option, UpdateDataspaceSearchTagConfigRequestDefaultGroupingOptionType0):
            default_grouping_option = self.default_grouping_option.value
        else:
            default_grouping_option = self.default_grouping_option

        table_grouping_project_option_ids: list[str] | None | Unset
        if isinstance(self.table_grouping_project_option_ids, Unset):
            table_grouping_project_option_ids = UNSET
        elif isinstance(self.table_grouping_project_option_ids, list):
            table_grouping_project_option_ids = []
            for table_grouping_project_option_ids_type_0_item_data in self.table_grouping_project_option_ids:
                table_grouping_project_option_ids_type_0_item = str(table_grouping_project_option_ids_type_0_item_data)
                table_grouping_project_option_ids.append(table_grouping_project_option_ids_type_0_item)

        else:
            table_grouping_project_option_ids = self.table_grouping_project_option_ids

        table_grouping_resource_option_ids: list[str] | None | Unset
        if isinstance(self.table_grouping_resource_option_ids, Unset):
            table_grouping_resource_option_ids = UNSET
        elif isinstance(self.table_grouping_resource_option_ids, list):
            table_grouping_resource_option_ids = []
            for table_grouping_resource_option_ids_type_0_item_data in self.table_grouping_resource_option_ids:
                table_grouping_resource_option_ids_type_0_item = str(
                    table_grouping_resource_option_ids_type_0_item_data
                )
                table_grouping_resource_option_ids.append(table_grouping_resource_option_ids_type_0_item)

        else:
            table_grouping_resource_option_ids = self.table_grouping_resource_option_ids

        default_grouping_project_attribute_id: None | str | Unset
        if isinstance(self.default_grouping_project_attribute_id, Unset):
            default_grouping_project_attribute_id = UNSET
        elif isinstance(self.default_grouping_project_attribute_id, UUID):
            default_grouping_project_attribute_id = str(self.default_grouping_project_attribute_id)
        else:
            default_grouping_project_attribute_id = self.default_grouping_project_attribute_id

        default_grouping_resource_attribute_id: None | str | Unset
        if isinstance(self.default_grouping_resource_attribute_id, Unset):
            default_grouping_resource_attribute_id = UNSET
        elif isinstance(self.default_grouping_resource_attribute_id, UUID):
            default_grouping_resource_attribute_id = str(self.default_grouping_resource_attribute_id)
        else:
            default_grouping_resource_attribute_id = self.default_grouping_resource_attribute_id

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
        if table_grouping_project_option_ids is not UNSET:
            field_dict["table_grouping_project_option_ids"] = table_grouping_project_option_ids
        if table_grouping_resource_option_ids is not UNSET:
            field_dict["table_grouping_resource_option_ids"] = table_grouping_resource_option_ids
        if default_grouping_project_attribute_id is not UNSET:
            field_dict["default_grouping_project_attribute_id"] = default_grouping_project_attribute_id
        if default_grouping_resource_attribute_id is not UNSET:
            field_dict["default_grouping_resource_attribute_id"] = default_grouping_resource_attribute_id

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
        ) -> None | Unset | UpdateDataspaceSearchTagConfigRequestDefaultGroupingOptionType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_grouping_option_type_0 = UpdateDataspaceSearchTagConfigRequestDefaultGroupingOptionType0(data)

                return default_grouping_option_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateDataspaceSearchTagConfigRequestDefaultGroupingOptionType0, data)

        default_grouping_option = _parse_default_grouping_option(d.pop("default_grouping_option", UNSET))

        def _parse_table_grouping_project_option_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                table_grouping_project_option_ids_type_0 = []
                _table_grouping_project_option_ids_type_0 = data
                for table_grouping_project_option_ids_type_0_item_data in _table_grouping_project_option_ids_type_0:
                    table_grouping_project_option_ids_type_0_item = UUID(
                        table_grouping_project_option_ids_type_0_item_data
                    )

                    table_grouping_project_option_ids_type_0.append(table_grouping_project_option_ids_type_0_item)

                return table_grouping_project_option_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        table_grouping_project_option_ids = _parse_table_grouping_project_option_ids(
            d.pop("table_grouping_project_option_ids", UNSET)
        )

        def _parse_table_grouping_resource_option_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                table_grouping_resource_option_ids_type_0 = []
                _table_grouping_resource_option_ids_type_0 = data
                for table_grouping_resource_option_ids_type_0_item_data in _table_grouping_resource_option_ids_type_0:
                    table_grouping_resource_option_ids_type_0_item = UUID(
                        table_grouping_resource_option_ids_type_0_item_data
                    )

                    table_grouping_resource_option_ids_type_0.append(table_grouping_resource_option_ids_type_0_item)

                return table_grouping_resource_option_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        table_grouping_resource_option_ids = _parse_table_grouping_resource_option_ids(
            d.pop("table_grouping_resource_option_ids", UNSET)
        )

        def _parse_default_grouping_project_attribute_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_grouping_project_attribute_id_type_0 = UUID(data)

                return default_grouping_project_attribute_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_grouping_project_attribute_id = _parse_default_grouping_project_attribute_id(
            d.pop("default_grouping_project_attribute_id", UNSET)
        )

        def _parse_default_grouping_resource_attribute_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_grouping_resource_attribute_id_type_0 = UUID(data)

                return default_grouping_resource_attribute_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_grouping_resource_attribute_id = _parse_default_grouping_resource_attribute_id(
            d.pop("default_grouping_resource_attribute_id", UNSET)
        )

        update_dataspace_search_tag_config_request = cls(
            name=name,
            description=description,
            is_active=is_active,
            default_grouping_option=default_grouping_option,
            table_grouping_project_option_ids=table_grouping_project_option_ids,
            table_grouping_resource_option_ids=table_grouping_resource_option_ids,
            default_grouping_project_attribute_id=default_grouping_project_attribute_id,
            default_grouping_resource_attribute_id=default_grouping_resource_attribute_id,
        )

        update_dataspace_search_tag_config_request.additional_properties = d
        return update_dataspace_search_tag_config_request

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
