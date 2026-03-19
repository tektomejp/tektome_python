from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlobUploadCompleteIn")


@_attrs_define
class BlobUploadCompleteIn:
    """Request to complete a blob upload.

    Attributes:
        upload_id (str): Upload ID from blob upload request
        initialize (bool | Unset): Whether to start OCR extraction after upload Default: False.
    """

    upload_id: str
    initialize: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

        initialize = self.initialize

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upload_id": upload_id,
            }
        )
        if initialize is not UNSET:
            field_dict["initialize"] = initialize

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload_id = d.pop("upload_id")

        initialize = d.pop("initialize", UNSET)

        blob_upload_complete_in = cls(
            upload_id=upload_id,
            initialize=initialize,
        )

        blob_upload_complete_in.additional_properties = d
        return blob_upload_complete_in

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
