from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataspace_resource_attribute_patch_in_patch_attribute_metadata_type_0 import (
        DataspaceResourceAttributePatchInPatchAttributeMetadataType0,
    )
    from ..models.table_metadata_update_request import TableMetadataUpdateRequest


T = TypeVar("T", bound="DataspaceResourceAttributePatchInPatch")


@_attrs_define
class DataspaceResourceAttributePatchInPatch:
    """
    Attributes:
        attribute_label (None | str | Unset):
        description (None | str | Unset):
        enabled (bool | None | Unset):
        hidden (bool | None | Unset):
        attribute_metadata (DataspaceResourceAttributePatchInPatchAttributeMetadataType0 | None | Unset):
        table_attribute_config (None | TableMetadataUpdateRequest | Unset):
    """

    attribute_label: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    hidden: bool | None | Unset = UNSET
    attribute_metadata: DataspaceResourceAttributePatchInPatchAttributeMetadataType0 | None | Unset = UNSET
    table_attribute_config: None | TableMetadataUpdateRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dataspace_resource_attribute_patch_in_patch_attribute_metadata_type_0 import (
            DataspaceResourceAttributePatchInPatchAttributeMetadataType0,
        )
        from ..models.table_metadata_update_request import TableMetadataUpdateRequest

        attribute_label: None | str | Unset
        if isinstance(self.attribute_label, Unset):
            attribute_label = UNSET
        else:
            attribute_label = self.attribute_label

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        hidden: bool | None | Unset
        if isinstance(self.hidden, Unset):
            hidden = UNSET
        else:
            hidden = self.hidden

        attribute_metadata: dict[str, Any] | None | Unset
        if isinstance(self.attribute_metadata, Unset):
            attribute_metadata = UNSET
        elif isinstance(self.attribute_metadata, DataspaceResourceAttributePatchInPatchAttributeMetadataType0):
            attribute_metadata = self.attribute_metadata.to_dict()
        else:
            attribute_metadata = self.attribute_metadata

        table_attribute_config: dict[str, Any] | None | Unset
        if isinstance(self.table_attribute_config, Unset):
            table_attribute_config = UNSET
        elif isinstance(self.table_attribute_config, TableMetadataUpdateRequest):
            table_attribute_config = self.table_attribute_config.to_dict()
        else:
            table_attribute_config = self.table_attribute_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_label is not UNSET:
            field_dict["attribute_label"] = attribute_label
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if attribute_metadata is not UNSET:
            field_dict["attribute_metadata"] = attribute_metadata
        if table_attribute_config is not UNSET:
            field_dict["table_attribute_config"] = table_attribute_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_resource_attribute_patch_in_patch_attribute_metadata_type_0 import (
            DataspaceResourceAttributePatchInPatchAttributeMetadataType0,
        )
        from ..models.table_metadata_update_request import TableMetadataUpdateRequest

        d = dict(src_dict)

        def _parse_attribute_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        attribute_label = _parse_attribute_label(d.pop("attribute_label", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_hidden(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hidden = _parse_hidden(d.pop("hidden", UNSET))

        def _parse_attribute_metadata(
            data: object,
        ) -> DataspaceResourceAttributePatchInPatchAttributeMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attribute_metadata_type_0 = DataspaceResourceAttributePatchInPatchAttributeMetadataType0.from_dict(data)

                return attribute_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataspaceResourceAttributePatchInPatchAttributeMetadataType0 | None | Unset, data)

        attribute_metadata = _parse_attribute_metadata(d.pop("attribute_metadata", UNSET))

        def _parse_table_attribute_config(data: object) -> None | TableMetadataUpdateRequest | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                table_attribute_config_type_0 = TableMetadataUpdateRequest.from_dict(data)

                return table_attribute_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TableMetadataUpdateRequest | Unset, data)

        table_attribute_config = _parse_table_attribute_config(d.pop("table_attribute_config", UNSET))

        dataspace_resource_attribute_patch_in_patch = cls(
            attribute_label=attribute_label,
            description=description,
            enabled=enabled,
            hidden=hidden,
            attribute_metadata=attribute_metadata,
            table_attribute_config=table_attribute_config,
        )

        dataspace_resource_attribute_patch_in_patch.additional_properties = d
        return dataspace_resource_attribute_patch_in_patch

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
