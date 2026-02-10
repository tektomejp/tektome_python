from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlobUploadCompleteOut")


@_attrs_define
class BlobUploadCompleteOut:
    """Response for completed blob upload.

    Attributes:
        resource_id (UUID): Resource ID
        bim_project_id (None | Unset | UUID): BIM Project ID
    """

    resource_id: UUID
    bim_project_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = str(self.resource_id)

        bim_project_id: None | str | Unset
        if isinstance(self.bim_project_id, Unset):
            bim_project_id = UNSET
        elif isinstance(self.bim_project_id, UUID):
            bim_project_id = str(self.bim_project_id)
        else:
            bim_project_id = self.bim_project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_id": resource_id,
            }
        )
        if bim_project_id is not UNSET:
            field_dict["bim_project_id"] = bim_project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_id = UUID(d.pop("resource_id"))

        def _parse_bim_project_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bim_project_id_type_0 = UUID(data)

                return bim_project_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bim_project_id = _parse_bim_project_id(d.pop("bim_project_id", UNSET))

        blob_upload_complete_out = cls(
            resource_id=resource_id,
            bim_project_id=bim_project_id,
        )

        blob_upload_complete_out.additional_properties = d
        return blob_upload_complete_out

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
