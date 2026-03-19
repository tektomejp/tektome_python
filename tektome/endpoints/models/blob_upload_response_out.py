from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="BlobUploadResponseOut")


@_attrs_define
class BlobUploadResponseOut:
    """Response containing the signed upload URL.

    Attributes:
        upload_id (str): Unique upload session ID
        upload_url (str): Signed URL for direct blob upload
        blob_path (str): Path where file will be stored
        expires_at (datetime.datetime): When the signed URL expires
        expires_in_seconds (int): Seconds until expiration
    """

    upload_id: str
    upload_url: str
    blob_path: str
    expires_at: datetime.datetime
    expires_in_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

        upload_url = self.upload_url

        blob_path = self.blob_path

        expires_at = self.expires_at.isoformat()

        expires_in_seconds = self.expires_in_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upload_id": upload_id,
                "upload_url": upload_url,
                "blob_path": blob_path,
                "expires_at": expires_at,
                "expires_in_seconds": expires_in_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload_id = d.pop("upload_id")

        upload_url = d.pop("upload_url")

        blob_path = d.pop("blob_path")

        expires_at = isoparse(d.pop("expires_at"))

        expires_in_seconds = d.pop("expires_in_seconds")

        blob_upload_response_out = cls(
            upload_id=upload_id,
            upload_url=upload_url,
            blob_path=blob_path,
            expires_at=expires_at,
            expires_in_seconds=expires_in_seconds,
        )

        blob_upload_response_out.additional_properties = d
        return blob_upload_response_out

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
