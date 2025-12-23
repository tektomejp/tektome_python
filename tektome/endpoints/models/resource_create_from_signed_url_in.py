from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceCreateFromSignedUrlIn")


@_attrs_define
class ResourceCreateFromSignedUrlIn:
    """
    Attributes:
        url (str):
        resource_id (UUID):
        bim_project_name (None | str | Unset):
    """

    url: str
    resource_id: UUID
    bim_project_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        resource_id = str(self.resource_id)

        bim_project_name: None | str | Unset
        if isinstance(self.bim_project_name, Unset):
            bim_project_name = UNSET
        else:
            bim_project_name = self.bim_project_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "resource_id": resource_id,
            }
        )
        if bim_project_name is not UNSET:
            field_dict["bim_project_name"] = bim_project_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        resource_id = UUID(d.pop("resource_id"))

        def _parse_bim_project_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bim_project_name = _parse_bim_project_name(d.pop("bim_project_name", UNSET))

        resource_create_from_signed_url_in = cls(
            url=url,
            resource_id=resource_id,
            bim_project_name=bim_project_name,
        )

        resource_create_from_signed_url_in.additional_properties = d
        return resource_create_from_signed_url_in

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
