from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResourceVCWithVersionSchemaPathIn")


@_attrs_define
class ResourceVCWithVersionSchemaPathIn:
    """Input Schema for resource with specific version

    Attributes:
        resource_group_id (UUID):
        resource_vc_id (UUID):
        version_num (int):
    """

    resource_group_id: UUID
    resource_vc_id: UUID
    version_num: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_group_id = str(self.resource_group_id)

        resource_vc_id = str(self.resource_vc_id)

        version_num = self.version_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_group_id": resource_group_id,
                "resource_vc_id": resource_vc_id,
                "version_num": version_num,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_group_id = UUID(d.pop("resource_group_id"))

        resource_vc_id = UUID(d.pop("resource_vc_id"))

        version_num = d.pop("version_num")

        resource_vc_with_version_schema_path_in = cls(
            resource_group_id=resource_group_id,
            resource_vc_id=resource_vc_id,
            version_num=version_num,
        )

        resource_vc_with_version_schema_path_in.additional_properties = d
        return resource_vc_with_version_schema_path_in

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
