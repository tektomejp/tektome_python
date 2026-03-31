from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WrapCoreResourcePostIn")


@_attrs_define
class WrapCoreResourcePostIn:
    """Input for wrapping a core resource with a LawtalkResource.

    Attributes:
        rvc_id (UUID):
    """

    rvc_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rvc_id = str(self.rvc_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rvc_id": rvc_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rvc_id = UUID(d.pop("rvc_id"))

        wrap_core_resource_post_in = cls(
            rvc_id=rvc_id,
        )

        wrap_core_resource_post_in.additional_properties = d
        return wrap_core_resource_post_in

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
