from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataspace_project_attribute_post_in_attribute_metadata_type_0 import (
        DataspaceProjectAttributePostInAttributeMetadataType0,
    )


T = TypeVar("T", bound="DataspaceProjectAttributePostIn")


@_attrs_define
class DataspaceProjectAttributePostIn:
    """Schema for posting attributes to a project in a dataspace.

    Attributes:
        attribute_label (str):
        attribute_type (str):
        attribute_metadata (DataspaceProjectAttributePostInAttributeMetadataType0 | None | Unset):
        enabled (bool | Unset):  Default: True.
    """

    attribute_label: str
    attribute_type: str
    attribute_metadata: DataspaceProjectAttributePostInAttributeMetadataType0 | None | Unset = UNSET
    enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dataspace_project_attribute_post_in_attribute_metadata_type_0 import (
            DataspaceProjectAttributePostInAttributeMetadataType0,
        )

        attribute_label = self.attribute_label

        attribute_type = self.attribute_type

        attribute_metadata: dict[str, Any] | None | Unset
        if isinstance(self.attribute_metadata, Unset):
            attribute_metadata = UNSET
        elif isinstance(self.attribute_metadata, DataspaceProjectAttributePostInAttributeMetadataType0):
            attribute_metadata = self.attribute_metadata.to_dict()
        else:
            attribute_metadata = self.attribute_metadata

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_label": attribute_label,
                "attribute_type": attribute_type,
            }
        )
        if attribute_metadata is not UNSET:
            field_dict["attribute_metadata"] = attribute_metadata
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_project_attribute_post_in_attribute_metadata_type_0 import (
            DataspaceProjectAttributePostInAttributeMetadataType0,
        )

        d = dict(src_dict)
        attribute_label = d.pop("attribute_label")

        attribute_type = d.pop("attribute_type")

        def _parse_attribute_metadata(
            data: object,
        ) -> DataspaceProjectAttributePostInAttributeMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attribute_metadata_type_0 = DataspaceProjectAttributePostInAttributeMetadataType0.from_dict(data)

                return attribute_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataspaceProjectAttributePostInAttributeMetadataType0 | None | Unset, data)

        attribute_metadata = _parse_attribute_metadata(d.pop("attribute_metadata", UNSET))

        enabled = d.pop("enabled", UNSET)

        dataspace_project_attribute_post_in = cls(
            attribute_label=attribute_label,
            attribute_type=attribute_type,
            attribute_metadata=attribute_metadata,
            enabled=enabled,
        )

        dataspace_project_attribute_post_in.additional_properties = d
        return dataspace_project_attribute_post_in

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
