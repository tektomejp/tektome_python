from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataspace_search_filter_configuration_out import DataspaceSearchFilterConfigurationOut
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="DataspaceSearchTagConfigOut")


@_attrs_define
class DataspaceSearchTagConfigOut:
    """Schema for the response of a dataspace tag configuration.

    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        name (str):
        filters (list[DataspaceSearchFilterConfigurationOut] | Unset):
        id (None | Unset | UUID):
        description (None | str | Unset):
        is_active (bool | Unset):  Default: False.
        default_filter (None | Unset | UUID):
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    name: str
    filters: list[DataspaceSearchFilterConfigurationOut] | Unset = UNSET
    id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    is_active: bool | Unset = False
    default_filter: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        name = self.name

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_active = self.is_active

        default_filter: None | str | Unset
        if isinstance(self.default_filter, Unset):
            default_filter = UNSET
        elif isinstance(self.default_filter, UUID):
            default_filter = str(self.default_filter)
        else:
            default_filter = self.default_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "name": name,
            }
        )
        if filters is not UNSET:
            field_dict["filters"] = filters
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if default_filter is not UNSET:
            field_dict["default_filter"] = default_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_search_filter_configuration_out import DataspaceSearchFilterConfigurationOut
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        name = d.pop("name")

        _filters = d.pop("filters", UNSET)
        filters: list[DataspaceSearchFilterConfigurationOut] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = DataspaceSearchFilterConfigurationOut.from_dict(filters_item_data)

                filters.append(filters_item)

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        is_active = d.pop("is_active", UNSET)

        def _parse_default_filter(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_filter_type_0 = UUID(data)

                return default_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_filter = _parse_default_filter(d.pop("default_filter", UNSET))

        dataspace_search_tag_config_out = cls(
            created_by=created_by,
            updated_by=updated_by,
            name=name,
            filters=filters,
            id=id,
            description=description,
            is_active=is_active,
            default_filter=default_filter,
        )

        dataspace_search_tag_config_out.additional_properties = d
        return dataspace_search_tag_config_out

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
