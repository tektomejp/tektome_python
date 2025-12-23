from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

if TYPE_CHECKING:
    from ..models.organizations_patch_in import OrganizationsPatchIn


T = TypeVar("T", bound="AppaccountRoutesOrganizationsPatchOrganizationMultiPartBodyParams")


@_attrs_define
class AppaccountRoutesOrganizationsPatchOrganizationMultiPartBodyParams:
    """
    Attributes:
        payload (OrganizationsPatchIn):
        logo_file (File | Unset):
    """

    payload: OrganizationsPatchIn
    logo_file: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload = self.payload.to_dict()

        logo_file: FileTypes | Unset = UNSET
        if not isinstance(self.logo_file, Unset):
            logo_file = self.logo_file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payload": payload,
            }
        )
        if logo_file is not UNSET:
            field_dict["logo_file"] = logo_file

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("payload", (None, json.dumps(self.payload.to_dict()).encode(), "application/json")))

        if not isinstance(self.logo_file, Unset):
            files.append(("logo_file", self.logo_file.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organizations_patch_in import OrganizationsPatchIn

        d = dict(src_dict)
        payload = OrganizationsPatchIn.from_dict(d.pop("payload"))

        _logo_file = d.pop("logo_file", UNSET)
        logo_file: File | Unset
        if isinstance(_logo_file, Unset):
            logo_file = UNSET
        else:
            logo_file = File(payload=BytesIO(_logo_file))

        appaccount_routes_organizations_patch_organization_multi_part_body_params = cls(
            payload=payload,
            logo_file=logo_file,
        )

        appaccount_routes_organizations_patch_organization_multi_part_body_params.additional_properties = d
        return appaccount_routes_organizations_patch_organization_multi_part_body_params

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
